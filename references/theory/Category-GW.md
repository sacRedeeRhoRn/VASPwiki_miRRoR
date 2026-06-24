<!-- Source: https://vasp.at/wiki/index.php/Category:GW | revid: 35522 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:GW
## Contents

- [1 Theory](#Theory)
- [2 Practical guides](#Practical_guides)
- [3 Additional resources](#Additional_resources)
  - [3.1 Lectures](#Lectures)
  - [3.2 Tutorials](#Tutorials)
  - [3.3 How to](#How_to)

## Theory
The GW approximation goes hand in hand with the RPA, since the very same
diagrammatic contributions are taken into account in the screened
Coulomb interaction of a system often denoted as W. However, in contrast
to the RPA/ACFDT, the GW method provides access to the spectral
properties of the system by means of determining the energies of the
quasi-particles of a system using a screened exchange-like contribution
to the self-energy. The GW approximation is currently one of the most
accurate many-body methods to calculate band-gaps.

More information about the GW method can be found on the following page:
[GW approximation of Hedin's
equations](../methods/GW_approximation_of_Hedin's_equations.md)

## Practical guides
While more recent versions of VASP (6.0 and newer) support GW
calculations in one go, older versions require two steps. First, a
groundstate DFT calculation is performed, followed by the actual GW
step.

More detailed guides for the GW method are bound below.

## Additional resources
### Lectures
- Lecture on [GW approximation](https://youtu.be/zGPqDxsD80o).
- Lecture on the [optical bandgap, including in
  GW](https://youtu.be/6F_WNIh6V7I).

### Tutorials
- Tutorial for [GW
  calculations](https://www.vasp.at/tutorials/latest/gw/).

### How to
- [Practical guide to GW
  calculations](../methods/Practical_guide_to_GW_calculations.md).
- [Practical guide to GW calculations for large
  systems](../methods/Practical_guide_to_GW_calculations.md).
- Using the GW routines for the determination of frequency-dependent
  dielectric matrix: [GW and dielectric
  matrix](../methods/GW_and_dielectric_matrix.md).
