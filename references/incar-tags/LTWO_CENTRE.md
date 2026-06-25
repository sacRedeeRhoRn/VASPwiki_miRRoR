<!-- Source: https://vasp.at/wiki/index.php/LTWO_CENTRE | revid: 36302 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTWO_CENTRE


LTWO_CENTRE = \[logical\]  
Default: **LTWO_CENTRE** = .FALSE. 

Description: LTWO_CENTRE
calculates off-center [Coulomb
integrals](../theory/Constrained–random-phase–approximation_formalism.md).

------------------------------------------------------------------------

When chosen, the system calculates two types of integrals:

- Bare integrals (stored in [VRijkl](../output-files/VRijkl.md))

$V_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
\frac{w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r})
w_{k}^{\*\sigma'}({\bf r}'+{\bf R}) w_{l}^{\sigma'}({\bf r}'+{\bf
R})}{|{\bf r}-{\bf r}'|}$

- Effectively screened integrals (stored in
  [URijkl](../output-files/URijkl.md))

$U_{ijkl}^{\sigma\sigma'} = \int {\rm d}{\bf r}\int {\rm d}{\bf r}'
w_{i}^{\*\sigma}({\bf r}) w_{j}^{\sigma}({\bf r}) U({\bf r},{\bf
r}',\omega) w_{k}^{\*\sigma'}({\bf r}'+{\bf R}) w_{l}^{\sigma'}({\bf
r}'+{\bf R})$

When chosen, cRPA matrix elements in
[vaspout.h5](../output-files/Vaspout.h5.md) can be used with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> to analyze the spatial
decay of the Coulomb interaction using the Ohno
potential[^kaltak:prb:2025-1]

$U(R) = \frac{U(R=0)}{\sqrt{\frac{R}\delta + 1}}$


    import py4vasp as pv

    calc = pv.Calculation.from_path(".")
    calc.effective_coulomb.plot(selection="U V", radius=...)


The above plots the spatial decay of the Coulomb interaction and fits
the Ohno potential to the off-center integrals. Using `radius=...`
passes the radial grid directly from the VASP output.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

## Related tags and articles\[<a
href="/wiki/index.php?title=LTWO_CENTRE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VRijkl](../output-files/VRijkl.md), [URijkl](../output-files/URijkl.md),
[LDISENTANGLED](LDISENTANGLED.md),
[LWEIGHTED](LWEIGHTED.md),
[LSCRPA](LSCRPA.md), [ALGO](ALGO.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LTWO_CENTRE-_incategory-Howto)

## References\[<a
href="/wiki/index.php?title=LTWO_CENTRE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^kaltak:prb:2025-1]: [M. Kaltak, A. Hampel, M. Schlipf, I. R. Reddy, B. Kim and G. Kresse, Phys. Rev. B **112**, 245102 (2025).](https://doi.org/10.1103/m3gh-g6r6)
