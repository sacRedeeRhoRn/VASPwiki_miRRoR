<!-- Source: https://vasp.at/wiki/index.php/LDISENTANGLED | revid: 35237 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDISENTANGLED


LDISENTANGLED = \[logical\]  
Default: **LDISENTANGLED** = .FALSE. 

Description: Selects the [disentanglement-cRPA
method](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism").

------------------------------------------------------------------------

Selects the cRPA method of Miyake, Aryasetiawan, and
Imada[^miyake:prb:80-1].
Following screening is subtracted from the full RPA polarizability:

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf q},i\omega)= \frac
1{N_k}\sum_{\bf k}\sum_{nn'\in{\cal T}} \frac{ f_{n\bf k}-f_{n'\bf
k-q} }{ \tilde\epsilon_{n{\bf k}} - \tilde\epsilon_{n'\bf k-q} - i
\omega } \langle \tilde u_{n {\bf k }}^{\sigma } |e^{-i \bf (G+q) r}|
\tilde u_{n'{\bf k-q}}^{ \sigma' } \rangle \langle \tilde u_{n' {\bf
k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} | \tilde u_{n{\bf k }}^{ \sigma
} \rangle$,

where $\tilde \epsilon_{n\bf
k}^\sigma$ is the disentangled band structure.

## Related tags and articles\[<a
href="/wiki/index.php?title=LDISENTANGLED&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWEIGHTED](LWEIGHTED.md),
[LSCRPA](LSCRPA.md), [ALGO](ALGO.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDISENTANGLED-_incategory-Howto)

## References\[<a
href="/wiki/index.php?title=LDISENTANGLED&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^miyake:prb:80-1]: [T. Miyake, F. Aryasetiawan, and M. Imada, Phys. Rev. B **80**, 155134 (2009).](https://doi.org/10.1103/PhysRevB.80.155134)
