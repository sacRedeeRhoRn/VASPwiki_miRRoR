<!-- Source: https://vasp.at/wiki/index.php/Tkatchenko-Scheffler_method | revid: 29765 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Tkatchenko-Scheffler method
The expression for the dispersion energy within the method of Tkatchenko
and Scheffler^([\[1\]](#cite_note-tkatchenko:prl:09-1)) is formally
identical to that of the [DFT-D2](DFT-D2.md) method. The
important difference is, however, that the dispersion coefficients and
damping function are charge-density dependent. The Tkatchenko-Scheffler
method is therefore able to take into account variations in vdW
contributions of atoms due to their local chemical environment. In this
method the polarizability, dispersion coefficients, and atomic radii of
an atom in a molecule or a solid are computed from their free-atomic
values using the following relations:

$\alpha_{i} = \nu_{i}\\ \alpha_{i}^{free},$

$C_{6ii} = \nu_{i}^{2}\\C_{6ii}^{free},$

$R_{0i} =
\left(\frac{\alpha_{i}}{\alpha_{i}^{free}} \right)^{\frac{1}{3}}
R_{0i}^{free}.$

The free-atomic quantities $\alpha_{i}^{free},C_{6ii}^{free}$ and $R_{0i}^{free}$ are tabulated for all elements from the first
six rows of the periodic table except for lanthanides. If a
Tkatchenko-Scheffler calculation is performed for the system containing
an unsupported element, the user has to define the corresponding values
using the tags [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md) and [VDW_R0](../incar-tags/VDW_R0.md) (see
below). The effective atomic volumes $\nu_{i}$ are determined using the Hirshfeld partitioning of the
all-electron density:

$\nu_{i} = \frac{\int r^3 \\w_i({\mathbf{r}})
n({\mathbf{r}})\\d^3{\mathbf{r}}}{\int r^3\\
n_{i}^{free}({\mathbf{r}})\\d^3{\mathbf{r}}}$

where $n({\mathbf{r}})$ is the total
electron density and $n_{i}^{free}({\mathbf{r}})$ is the spherically averaged electron density of the neutral
free atomic species $i$. The Hirshfeld
weight $w_i({\mathbf{r}})$ is defined by
free atomic densities as follows:

$w_i({\mathbf{r}}) =
\frac{n_{i}^{free}({\mathbf{r}})}{\sum_{j=1}^{N_{at}}
n_{j}^{free}({\mathbf{r}})}.$

The combination rule to define the strength of the dipole-dipole
dispersion interaction between unlike species is:

$C_{6ij} =
\frac{2C_{6ii}\\C_{6jj}}{\[\frac{\alpha_{j}}
{\alpha_{i}}C_{6ii}+\frac{\alpha_{i}}{\alpha_{j}}C_{6jj}\]}.$

The parameter $R_{0ij}$ used in the
damping function of the [DFT-D2](DFT-D2.md) method is
obtained from the atom-in-molecule vdW radii as follows:

$R_{0ij} = R_{0i} + R_{0j}.$

The performance of the Tkatchenko-Scheffler method in optimization of
various crystalline systems has been examined in reference
^([\[2\]](#cite_note-bucko:prb:13-2)).

## Usage
The Tkatchenko-Scheffler method is invoked by setting
[IVDW](../incar-tags/IVDW.md)=2\|20. The following parameters can be
optionally defined in [INCAR](../input-files/INCAR.md) (the given values are
the default ones):

- [LVDWSCS](../incar-tags/LVDWSCS.md)=.FALSE. : activates the
  [self-consistent screening in Tkatchenko-Scheffler
  method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md)
- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=50.0 : cutoff radius (in
  Å) for pair interactions
- [VDW_S6](../incar-tags/VDW_S6.md)=1.00 : global scaling factor
  $s_6$
- [VDW_SR](../incar-tags/VDW_SR.md)=0.94 : scaling factor
  $s_R$
- [VDW_D](../incar-tags/VDW_D.md)=20.0 : damping parameter
  $d$
- [VDW_ALPHA](../incar-tags/VDW_ALPHA.md)=\[real array\] : free-atomic
  polarizabilities (atomic units) for each species defined in the
  [POSCAR](../input-files/POSCAR.md) file
- [VDW_C6AU](../incar-tags/VDW_C6AU.md)=\[real array\] : free-atomic
  $C_6$ parameters (atomic units) for
  each species defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_C6](../incar-tags/VDW_C6.md)=\[real array\] : free-atomic
  $C_6$ parameters
  ($\mathrm{Jnm}^{6}\mathrm{mol}^{-1}$)
  for each species defined in the [POSCAR](../input-files/POSCAR.md) file
  (this parameter overrides [VDW_C6AU](../incar-tags/VDW_C6AU.md))
- [VDW_R0AU](../incar-tags/VDW_R0AU.md)=\[real array\] : free-atomic
  $R_0$ parameters (atomic units) for
  each species defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_R0](../incar-tags/VDW_R0.md)=\[real array\] :
  $R_0$ parameters (in Å) for each
  species defined in the [POSCAR](../input-files/POSCAR.md) file (this
  parameter overrides [VDW_R0AU](../incar-tags/VDW_R0AU.md))
- [LVDW_EWALD](../incar-tags/LVDW_EWALD.md)=.FALSE. : the lattice
  summation in $E_{\mathrm{disp}}$
  expression is computed by means of Ewald's summation (*.TRUE.* ) or
  via a real space summation over all atomic pairs within cutoff radius
  [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) (*.FALSE.*). (available in
  VASP.5.3.4 and later)
- [LTSSURF](../incar-tags/LTSSURF.md)=.FALSE.: if set to .TRUE., the
  standard parametrization of the Tkatchenko-Scheffler method is
  replaced by the one designed to enable reliable modeling of structure
  and stability for a broad class of organic molecules adsorbed on metal
  surfaces is activated^([\[3\]](#cite_note-3))

  

[TABLE]

## Related tags and articles
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_SR](../incar-tags/VDW_SR.md),
[VDW_D](../incar-tags/VDW_D.md), [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6AU](../incar-tags/VDW_C6AU.md), [VDW_C6](../incar-tags/VDW_C6.md),
[VDW_R0AU](../incar-tags/VDW_R0AU.md), [VDW_R0](../incar-tags/VDW_R0.md),
[LVDW_EWALD](../incar-tags/LVDW_EWALD.md), [IVDW](../incar-tags/IVDW.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[Self-consistent screening in Tkatchenko-Scheffler
method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References
1.  [↑](#cite_ref-tkatchenko:prl:09_1-0) [A. Tkatchenko and M.
    Scheffler, Phys. Rev. Lett. **102**, 073005
    (2009).](https://doi.org/10.1103/PhysRevLett.102.073005)
2.  [↑](#cite_ref-bucko:prb:13_2-0) [T. Bučko, S. Lebègue, J. Hafner,
    and J. G. Ángyán, Phys. Rev. B **87**, 064110
    (2013).](https://doi.org/10.1103/PhysRevB.87.064110)
3.  [↑](#cite_ref-3) [V. G. Ruiz, W. Liu, and A. Tkatchenko, Phys. Rev.
    B 93, 035118
    (2016).](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.035118)
4.  [↑](#cite_ref-kerber:jcc:08_4-0) [T. Kerber, M. Sierka, and J.
    Sauer, J. Comput. Chem. **29**, 2088
    (2008).](https://doi.org/10.1002/jcc.21069)

------------------------------------------------------------------------
