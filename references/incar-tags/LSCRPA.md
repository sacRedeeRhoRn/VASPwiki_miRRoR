<!-- Source: https://vasp.at/wiki/index.php/LSCRPA | revid: 35660 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCRPA


LSCRPA = \[logical\]  
Default: **LSCRPA** = .FALSE. 

Description: LSCRPA selects
the [spectral-cRPA
method](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism").

------------------------------------------------------------------------

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

In constrained random-phase approximation (cRPA) calculations, the
target polarizability $\tilde\chi$
is computed from the eigenspectrum of the target-space projectors as
follows

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)\approx \frac
1{N_k}\sum_{nn'{\bf k}} \frac{ f_{n\bf k}-f_{n'\bf k-q} }{
\epsilon_{n{\bf k}} - \epsilon_{n'\bf k-q} - i \omega } \theta_{n\bf
k }^{\sigma} \theta_{n'\bf k-p }^{\sigma'} \langle u_{n {\bf k
}}^{\sigma } |e^{-i \bf (G+q) r}| u_{n'{\bf k-q}}^{ \sigma' } \rangle
\langle u_{n' {\bf k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} | u_{n'{\bf
k }}^{ \sigma } \rangle$

Here $\theta_{n{\bf k}}^\sigma$ are the eigenvalues of the [correlated
projectors](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism")

$P_{mn}^{\sigma({\bf k})} = \sum_{i\in \cal T} T_{i m}^{\*\sigma({\bf
k})} T_{i n}^{\sigma({\bf k})}$

ordered according to their leverage scores. The s-cRPA method results in
larger effective interactions compared to
[w-cRPA](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism")
or the [projector-cRPA
method](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism")
and conserves the number of
electrons.[^kaltak:prb:2025-1]

## Related tags and articles\[<a href="/wiki/index.php?title=LSCRPA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LDISENTANGLED](LDISENTANGLED.md),
[LWEIGHTED](LWEIGHTED.md), [ALGO](ALGO.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCRPA-_incategory-Howto)

## References\[<a href="/wiki/index.php?title=LSCRPA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^kaltak:prb:2025-1]: [M. Kaltak, A. Hampel, M. Schlipf, I. R. Reddy, B. Kim and G. Kresse, Phys. Rev. B **112**, 245102 (2025).](https://doi.org/10.1103/m3gh-g6r6)
