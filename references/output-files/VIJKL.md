<!-- Source: https://vasp.at/wiki/index.php/VIJKL | revid: 35265 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VIJKL


The VIJKL file stores the bare
Coulomb integrals at the unit-cell origin (**R** = 0):

$V_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
\frac{ w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r})
w_{k}^{\*\sigma'}({\bf r}') w_{l}^{\sigma'}({\bf r}')}{|{\bf r}-{\bf
r}'|}$

The columns I, J, K, L are the Wannier function indices; RE and IM are
the real and imaginary parts. The format is as follows:

     # V_ijkl = [ij,R|kl,0] 
     #  I   J   K   L          RE(V_IJKL)          IM(V_IJKL)
        1   1   1   1       14.4576272582        0.0000000000
        2   1   1   1        0.0000010313        0.0000031049
      ...

## Related tags and articles\[<a href="/wiki/index.php?title=VIJKL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Constrained–random-phase–approximation
formalism](../theory/Constrained–random-phase–approximation_formalism.md)

Files: [UIJKL](UIJKL.md), [URijkl](URijkl.md),
[VRijkl](VRijkl.md)

Tags: [LOCALIZED_BASIS](../theory/LOCALIZED_BASIS.md),
[ALGO](../incar-tags/ALGO.md)


