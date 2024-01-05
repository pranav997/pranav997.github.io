---
layout: distill
title: What is a Synthetic Gauge Field?
description: gauge fields from a condensed matter perspective
img: assets/img/conic1.jpeg
importance: 2
category: work
giscus_comments: true
bibliography: conical.bib
---

Consider a doubly degenerate subspace of a Hamiltonian dependent upon a set of parameters $\mathbf{R}$. We can drive the system adiabatically by varying the parameters $\mathbf{R}$ in time  such that the path ($$\mathcal{C}$$) forms a closed loop. $$\mathcal{C} = \{R(s) | s \in [0, 1]\}$$

Now the wavefunction $$\psi(s)$$ can be written as a linear combination of the eigenstates of the Hamiltonian $$\hat{H}(R(s))$$.

so the wavefunction can be written as:

$$\begin{pmatrix} c_1(s) \\ c_2(s) \end{pmatrix} = \begin{pmatrix} c_1(0) \\ c_2(0) \end{pmatrix}-
\begin{bmatrix} \int_{0}^{s} \bra{1(s')}\ket{2(s')} c_{1} \,ds' + \int_{0}^{s} c_{2} \,ds'   \\   \int_{0}^{s} c_{1} \,ds' + \int_{0}^{s} c_{2} \,ds' \end{bmatrix} $$
