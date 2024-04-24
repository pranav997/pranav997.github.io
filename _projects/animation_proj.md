---
layout: distill
title: Cool Animations
description: animations and code
img: assets/img/conic1.jpeg
importance: 2
category: fun
giscus_comments: true
---


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="/assets/video/hypersonic.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>
<div class="caption">
    Hypersonic flow around a disk
</div>

One can reproduce this using the following code.
{% raw %}

```python

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig, ax = plt.subplots()
# change size of the figure
fig.set_size_inches(10, 10)


def update(t):

    ax.clear()
    disk = Circle((0, 0), radius=0.21, edgecolor="black", facecolor="blue")
    ax.add_patch(disk)

    # Time steps to add circles
    time_steps = np.arange(0, 100, 2)

    # All the physics is in this loop
    for step in time_steps:
        if t >= step:
            circle = Circle(
                (0.0151 * (step**2 - t**2), 0),
                radius=t - step,
                edgecolor="black",
                facecolor="none",
            )
            ax.add_patch(circle)

    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    # remove the axis
    ax.axis("off")


ani = animation.FuncAnimation(fig, update, frames=range(100), interval=5, blit=False)
# show the animation as a mp4 video
ani.save("hypersonic.mp4", writer="ffmpeg", fps=20)


```

{% endraw %}
