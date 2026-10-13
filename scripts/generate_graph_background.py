"""Create a teal graph-network background matching this site's light theme.

Requires: pip install pillow
Run:      python3 scripts/generate_graph_background.py
"""
from math import cos, pi, sin
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw

W, H, SCALE, FRAMES, FPS = 1440, 810, 2, 96, 20
BG, TEAL, INK = "#f7f8f5", "#126466", "#12201f"  # _sass/_themes.scss
OUT = Path("assets/img/growing-dying-graph.gif")
rng = Random(24)
nodes = [(rng.uniform(.08, .92), rng.uniform(.12, .88), rng.uniform(0, 2 * pi)) for _ in range(42)]

# Connect every node to its two closest neighbours: a sparse, organic graph.
edges = {(min(i, j), max(i, j)) for i, (x, y, _) in enumerate(nodes)
         for _, j in sorted(((x - X) ** 2 + (y - Y) ** 2, k)
                            for k, (X, Y, _) in enumerate(nodes) if k != i)[:2]}


def mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


teal = tuple(bytes.fromhex(TEAL[1:]))
bg = tuple(bytes.fromhex(BG[1:]))
frames = []
for frame in range(FRAMES):
    phase = frame / (FRAMES - 1)
    # 0 -> 1 -> 0: the network grows, pauses briefly, then dissolves.
    life = sin(pi * phase) ** 0.72
    image = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    draw = ImageDraw.Draw(image, "RGBA")
    active = []
    for i, (x, y, offset) in enumerate(nodes):
        pulse = .72 + .28 * sin(2 * pi * phase + offset)
        strength = max(0, min(1, (life * 1.35 - i / len(nodes) * .35) * pulse))
        active.append(strength)
    for i, j in edges:
        alpha = int(100 * min(active[i], active[j]))
        if alpha:
            draw.line((nodes[i][0] * W * SCALE, nodes[i][1] * H * SCALE,
                       nodes[j][0] * W * SCALE, nodes[j][1] * H * SCALE),
                      fill=(*teal, alpha), width=2 * SCALE)
    for (x, y, _), strength in zip(nodes, active):
        if strength:
            radius = (2.5 + 4 * strength) * SCALE
            colour = mix(bg, teal, strength)
            draw.ellipse((x * W * SCALE - radius, y * H * SCALE - radius,
                          x * W * SCALE + radius, y * H * SCALE + radius),
                         fill=(*colour, int(225 * strength)))
    frames.append(image.resize((W, H), Image.Resampling.LANCZOS))

OUT.parent.mkdir(parents=True, exist_ok=True)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=1000 // FPS,
               loop=0, optimize=True, disposal=2)
print(f"Wrote {OUT} ({W}x{H}, {FRAMES / FPS:.1f}s)")
