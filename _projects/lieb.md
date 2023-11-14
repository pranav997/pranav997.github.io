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
in case people find them helpful [PDF](/assets/pdf/LB_Bounds.pdf).However, in this post I will talk about what I understand/find interesting about LB bound.

So we consider a local Hamiltonian of the form $$\mathcal{H}=\sum h_x$$ defined on $$n$$ qubits. We have a Hilbert space with $$2^n$$ dimensions such that time evolution of an
initial state $$|\psi(0)\rangle$$ is given by $$|\psi(t)\rangle=e^{-i\mathcal{H}t}|\psi(0)\rangle$$. We are interested in the spread of information in the system. The implementation of such unitaries on a quantum computer is considered efficient if, Unitary $$U$$ can be implemented in time $$t$$ with a number of gates $$g$$ such that $$g\leq poly(n)$$ and $$t\leq poly(n)$$. The trick is to decompose continuos time evolutions into discrete steps such that discrete steps commute, this is known as Trotterization.

{% details Trotterization example %}
Let's say we want to evolve a Hamiltonian given by $$\mathcal{H}=\sum_{i} J(X_{i}X_{i+1} + Y_{i}Y_{i+1}+ Z_{i}Z_{i+1})$$ for time $$t$$. We can decompose the time evolution into $$N$$ steps of size $$\delta t=t/N$$ where $$N$$ is the number of steps. We can write $$U=e^{-i\mathcal{H}t}$$ as $$U=[e^{-i\sum_{i}J\delta t(X_{i}X_{i+1})}e^{-i\sum_{i}J\delta t(Y_{i}Y_{i+1})}e^{-i\sum_{i}J\delta t(Z_{i}Z_{i+1})}]^N$$
{% enddetails %}
***
## Simple example of a Lieb Robinson bound

Consider a simpler example of a electron hopping on a tight binding lattice with
 nearest neighbour interactions, $$ \mathcal{H}=\sum_{n} J(|n\rangle \langle
 n+1|+|n+1\rangle \langle n|)$$. The dispersion relation is given by
 $$\epsilon_k=-2t\cos{ka} $$ where $$k$$ is the electron momentum. Hence, the
 maxmimum group velocity can be derived as $$v_g= \frac{dw}{dk} \leq 2ta $$. If
 we have a 1D lattice, then the maximum speed with which information can spread
 is $$2ta$$. An interesting question to ask is how does a perturbation at one
 site spread through the lattice. This can be measured by observing the difference between 
 the unperturbed time evolved state $$|\psi(t)\rangle=e^{-i\mathcal{H}t}|\psi(0)\rangle $$ with the perturbed state
 $$|\psi(t)\rangle=e^{-i\mathcal{H}t}e^{-iX_0}|\psi(0)\rangle $$.
