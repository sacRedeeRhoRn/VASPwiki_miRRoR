<!-- Source: https://vasp.at/wiki/index.php/UIJKL | revid: 35637 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# UIJKL


The UIJKL file stores the
effectively screened Coulomb integrals at the unit-cell origin (**R** =
0):

$U_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r}) U({\bf r},{\bf
r}',\omega) w_{k}^{\*\sigma'}({\bf r}') w_{l}^{\sigma'}({\bf r}')$

evaluated at zero frequency ($\omega=0$).
The columns I, J, K, L are the Wannier function indices; RE and IM are
the real and imaginary parts. The format is as follows:

     # U_ijkl = [ij,R|kl,0] 
     #  I   J   K   L          RE(V_IJKL)          IM(V_IJKL)
        1   1   1   1        4.3457689208        0.0000000000
        2   1   1   1        0.0000021313        0.0000001349
      ...

## Related tags and articles\[<a href="/wiki/index.php?title=UIJKL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Constrained–random-phase–approximation
formalism](../theory/Constrained–random-phase–approximation_formalism.md)

[VIJKL](VIJKL.md), [URijkl](URijkl.md),
[VRijkl](VRijkl.md),
[LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md),
[ALGO](../incar-tags/ALGO.md)


