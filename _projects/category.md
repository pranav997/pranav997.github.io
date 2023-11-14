---
layout: distill
title: Dequantization of quantum algorithms
description: sometimes classical algorithms are better
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

Quantum machine learning is a rapidly growing field of research. The promise of quantum machine learning is that quantum computers can be used to speed up classical machine learning algorithms. However, it is not clear that quantum machine learning algorithms are always better than classical machine learning algorithms. A series of works that come
under the category of dequantization of quantum algorithms show that the 
apparent exponential speedup can be replicated in a classical setting
provided we relax a few assumptions. In this post, we will discuss this in detail.

It's not straightforward to compare quantum and classical algorithms. The reason is that quantum algorithms take quantum states as inputs such 
as $$ \ket{x} = \sum_{i=1}^n x_i \ket{i} $$ and classical algorithms take classical states as inputs such as $$ \vec{x} = (x_1, \ldots, x_n) $$. To compare the two, Ewin Twang proposed _sample and query access_ (SQ access) model. Concretely it is defined as follows:

{% details SQ access definition %}
SQ access is an oracle which enables querying a vector $$ x \in \mathbb{C}^n $$ such that:
* The orcale outputs $$i \in \{1, \ldots, 2^n\}$$ with probability $$|x_i|^2$$ upon sampling.
* The oracle outputs $$x_i$$ upon querying.
* The oracle outputs $$||x||_2$$ upon querying N times.
{% enddetails %}
