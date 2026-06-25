<!-- Source: https://vasp.at/wiki/index.php/Category:Low-scaling_GW_and_RPA | revid: 24298 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Low-scaling GW and RPA


This category shows all tags and articles concerning low scaling GW and
RPA algorithms available as of VASP.6 and newer.

## Theoretical Background\[<a
href="/wiki/index.php?title=Category:Low-scaling_GW_and_RPA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theoretical Background">edit</a> \| (./index.php.md)\]

The Random Phase Approximation (RPA) is a diagrammatic method to
determine the groundstate energy of interacting electrons. The
computational cost of diagrammatic methods typically exceeds the one of
hybrid DFT calculations, since a frequency dependent Hamiltonian is
diagonalized. Conventional GW and RPA/ACFDT algorithms typically scale
with the forth power of the system size and are, thus, limited to
relatively small system sizes. However, by performing all calculations
on the imaginary time and imaginary frequency axis one can exploit
coarse Fourier transformation compatible grids and obtain a cubic
scaling GW and RPA/ACFDT algorithm. These algorithms can be used to
study relatively large systems with diagrammatic methods.

Please take a look on the
[RPA](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md)
and <a href="/wiki/The_GW_approximation_of_Hedin%27s_equations"
class="mw-redirect"
title="The GW approximation of Hedin&#39;s equations">GW</a> pages for
more information about their theoretical formulation.

## How to\[<a
href="/wiki/index.php?title=Category:Low-scaling_GW_and_RPA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

The following pages contain some general recipes for

- RPA: [RPA-ACFDT
  calculations](../methods/ACFDT__RPA_calculations.md)
- GW: A practical guide to low-scaling GW calculations can be found
  [here](../methods/Practical_guide_to_GW_calculations.md).

------------------------------------------------------------------------


