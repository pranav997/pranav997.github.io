---
layout: distill
title: Lieb Robinson Bounds
description: limits on the spread of information in quantum systems
img: assets/img/lieb1.png
importance: 2
category: work
giscus_comments: true
bibliography: 2018-12-22-distill.bib
date: 2023-11-09
authors:
  - name: Pranav

_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }
---

I had known about Lieb Robinson bounds previously because of the HHKL algorithm <d-cite key="haah2021quantum"></d-cite>. But I never thought of going into 
depth, until I attended a talk by Prof. Mari Carmen Bañuls, where she talked about one of her papers titled "Light cone tensor network and time evolution" <d-cite key="mari_light"></d-cite> . This sort of reintroduced me to the idea, of how there are bounds on the speed with which information spreads in a quantum system. There are great reviews/notes available for a graduate level introduction to this topic <d-cite key="chen2023speed,hastings2010locality"></d-cite>. Andy Lucas does
a nice job of summarizing it in this Boulder summer school [lecture](https://www.youtube.com/watch?v=2gktIZpPhSM). I have prepared some handwritten notes for the lecture
in case people find them helpful. However, in this post I will talk about what I understand/find interesting about LB bound. [PDF](/assets/pdf/LB_Bounds.pdf)

So we consider a local Hamiltonian of the form $$\mathcal{H}=\sum h_x$$ defined on $$n$$ qubits. We have a Hilbert space with $$2^n$$ dimensions such that time evolution of an
initial state $$|\psi(0)\rangle$$ is given by $$|\psi(t)\rangle=e^{-i\mathcal{H}t}|\psi(0)\rangle$$. We are interested in the spread of information in the system. The implementation of such unitaries on a quantum computer is considered efficient if, Unitary $$U$$ can be implemented in time $$t$$ with a number of gates $g$ such that $$g\leq poly(n)$$ and $$t\leq poly(n)$$. The trick is to decompose continuos time evolutions into discrete steps such that discrete steps commute, this is known as Trotterization. The idea is to decompose the Hamiltonian into $$\mathcal{H}=\sum h_x$$ and then approximate $$e^{-i\mathcal{H}t}\approx \prod e^{-ih_xt}$$ where $$h_x$$ are the local terms. This is known as the Trotter-Suzuki decomposition. The error in this approximation is $$O(t^2)$$. Even if the Hamiltonian is sparse, we still have $$\epsilon\sim O(n^2)$$ . This is where LB bounds come in. They tell us that the error in the approximation is $$O(t^2)$$ but the error in the spread of information is $$O(t)$$.

In relativity, we have absolute light cones, where the events inside the cone cannot influence the outside and they are separated by a strict line, which is the speed of light.
In quantum mechanics, we have a similar concept, where we have a light cone, but the events inside the cone can influence the outside, but the influence is exponentially suppressed. This is known as the Lieb Robinson bound. The idea is that the spread of information is bounded by the Lieb Robinson velocity $$v_{LR}$$ which is $$v_{LR}\sim O(1)$$. The best intuition for this comes from the qubits picture. Consider an intial state $$|......0000.....\rangle$$ where operator $$X$$ acts at time $$t=0$$ at one site. 
