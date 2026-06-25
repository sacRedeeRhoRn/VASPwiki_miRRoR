<!-- Source: https://vasp.at/wiki/index.php/ELPH_FERMI_NEDOS | revid: 33096 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_FERMI_NEDOS


ELPH_FERMI_NEDOS =
\[integer\]  
Default: **ELPH_FERMI_NEDOS** = 501 

Description: Number of Gauss–Legendre integration points used to
evaluate the Fermi–Dirac distribution and determine the electronic Fermi
level at finite temperature in the context of electron–phonon (el–ph)
coupling calculations.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

**ELPH_FERMI_NEDOS** plays the same role as
[EFERMI_NEDOS](EFERMI_NEDOS.md), but specifically in
the context of electron-phonon coupling calculations. It defines the
number of points in the Gauss–Legendre grid used when integrating the
Fermi–Dirac distribution to determine the Fermi level within the el–ph
workflow.

Larger values yield more accurate Fermi–Dirac occupations and energy
derivatives, particularly at low temperatures or when evaluating sharp
features in the electronic density of states near the Fermi energy. A
short convergence test is recommended for systems with narrow bands or
strong temperature dependence in el–ph properties.

For details of the numerical integration scheme, see
[EFERMI_NEDOS](EFERMI_NEDOS.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_FERMI_NEDOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [EFERMI_NEDOS](EFERMI_NEDOS.md)
- [TRANSPORT_NEDOS](TRANSPORT_NEDOS.md)
- [ISMEAR](ISMEAR.md)
- [Transport coefficients including electron-phonon
  scattering](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Smearing technique](../tutorials/Smearing_technique.md)


