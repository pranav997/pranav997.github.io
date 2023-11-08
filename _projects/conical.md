---
layout: distill
title: Conical Intersections and Jahn Teller Effect
description: a side grad project
img: assets/img/conic1.jpeg
importance: 2
category: work
giscus_comments: true
bibliography: conical.bib
---

 The Jahn-Teller effect is a phenomenon in molecular and solid-state physics where distortions in the molecular geometry occur due to degenerate electronic states. The effect is often associated with the geometric aspects and the Berry phase. In the gauge formalism of Jahn-Teller models, we can visualize the introduction of a magnetic flux into the Conical Intersection (CI). This has led to discussions about a "molecular Aharonov-Bohm effect.

In their work  <d-cite key="schon1995geometric"></d-cite> Schön and Köppel explored a scenario of 'self-interference.' They considered an initial Gaussian wave-packet located at the minima of the lower potential energy surface. As the wave-packet expands, it predominantly follows the minima's path. After a certain time, the initial wave-packet has propagated around the entire minimum and interferes with itself. This interference pattern captures the π-magnetic flux through the CI.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.html path="/assets/video/111.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>
<div class="caption">
    Gaussian wavepacket evolving and self interfering as it goes around a CI
</div>

One can reproduce this using the following code.
<d-code block language="python">

# Set seaborn style
sns.set_style("darkgrid")
sns.set_context("talk")

c = 4
w = 2  # 2*np.pi*f_Rabi
num_time_steps = 100
pop = np.zeros((num_time_steps, 2))
time = np.zeros(num_time_steps)

psi = pt.Wavefunction(["exp(-(x+1)**2-(y)**2)*exp(1j*2*x)", "0"], number_of_grid_points=(128*3, 128*3), spatial_ext=[(-4, 4), (-4, 4)])

V = ["1/2*w**2*((x+1)**2 + y**2)", "c*y", "1/2*w**2*((x-1)**2 + y**2)"]


def init():
    data=np.abs(psi.amp[:,:,0].T)**2
    sns.heatmap(data, cmap='jet',cbar=False)


def animate(i):
    psi.propagate(V, num_time_steps=1, delta_t=0.05, variables={'w': w, 'c': c})
    data=np.abs(psi.amp[:,:,0].T)**2

    fig.clear()
    sns.heatmap(data, cmap='jet',cbar=False)
    #remove ticks in seaborn plot
    plt.xticks([])
    plt.yticks([])
    plt.ylabel('$Q_y$')
    plt.xlabel('$Q_x$')
    plt.title('Time evolution of the wavefunction')
    

fig = plt.figure(figsize=(8, 8))


anim=animation.FuncAnimation(fig, animate, init_func=init, frames=num_time_steps, repeat=False)
HTML(anim.to_html5_video())
</d-code>

