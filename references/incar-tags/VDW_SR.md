<!-- Source: https://vasp.at/wiki/index.php/VDW_SR | revid: 34374 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_SR
VDW_SR = \[real\] 

Description: VDW_SR sets a parameter in the damping function of van der
Waals methods.

------------------------------------------------------------------------

VDW_SR allows to set the value of a parameter in the following methods:

- Radii scaling $s_{r,6}$ in the
  dipole-dipole zero-damping function of DFT-D3. VDW_SR can be used for
  both implementations of DFT-D3: [DFT-D3](../methods/DFT-D3.md)
  ([IVDW](IVDW.md)=11) and
  [simple-DFT-D3](../methods/Simple-DFT-D3.md)
  ([IVDW](IVDW.md)=15 with
  [SDFTD3_DAMPING](SDFTD3_DAMPING.md)=zero or
  mzero).
- Radii scaling $s_{R}$ in the damping
  function of the Tkatchenko-Scheffler methods
  ([IVDW](IVDW.md)=2 and 21).
- Radii scaling $\beta$ in the damping
  function of the many-body dispersion energy methods
  ([IVDW](IVDW.md)=202 and 263).
- TT-damping factor $b_0$ in
  [DDsC](../methods/DDsC_dispersion_correction.md)
  ([IVDW](IVDW.md)=4).

## Related tags and articles
[IVDW](IVDW.md), VDW_SR, [DFT-D3](../methods/DFT-D3.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md),
[Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](../methods/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](../methods/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md),
[DDsC](../methods/DDsC_dispersion_correction.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_SR-_incategory-Examples)

------------------------------------------------------------------------
