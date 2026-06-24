<!-- Source: https://vasp.at/wiki/index.php/LWEIGHTED | revid: 35238 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWEIGHTED
LWEIGHTED = \[logical\]  
Default: **LWEIGHTED** = .FALSE. 

Description: LWEIGHTED selects the [weighted-cRPA
method](../theory/Constrained–random-phase–approximation_formalism.md) "Constrained–random-phase–approximation formalism").

------------------------------------------------------------------------

Selects the cRPA method of Sasioglu, Friedrich and
Blügel^([\[1\]](#cite_note-sasioglu:prb:83-1)) where the following
screening contribution is subtracted from the full RPA polarizability:

$\tilde \chi^\sigma_{{\bf G,G}'}({\bf
q},i\omega)\approx \frac 1{N_k}\sum_{nn'{\bf k}} \frac{ f_{n\bf
k}-f_{n'\bf k-q} }{ \epsilon_{n{\bf k}} - \epsilon_{n'\bf k-q} - i
\omega } p_{n\bf k }^{\sigma} p_{n'\bf k-p }^{\sigma'} \langle u_{n
{\bf k }}^{\sigma } |e^{-i \bf (G+q) r}| u_{n'{\bf k-q}}^{ \sigma' }
\rangle \langle u_{n' {\bf k-q}}^{\sigma' } |e^{-i \bf (G'-q)r'} |
u_{n'{\bf k }}^{ \sigma } \rangle$

## Related tags and articles
[LDISENTANGLED](LDISENTANGLED.md),
[LSCRPA](LSCRPA.md), [ALGO](ALGO.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWEIGHTED-_incategory-Howto)

## References
1.  [↑](#cite_ref-sasioglu:prb:83_1-0) [E. Sasioglu, C. Friedrich,
    and S. Blügel, Phys. Rev. B **83**, 121101
    (2011).](https://doi.org/10.1103/PhysRevB.83.121101)
