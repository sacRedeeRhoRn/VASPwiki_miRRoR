<!-- Source: https://vasp.at/wiki/index.php/Tkatchenko-Scheffler_method | revid: 29765 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Tkatchenko-Scheffler method


The expression for the dispersion energy within the method of Tkatchenko
and
Scheffler<sup>[\[1\]](#cite_note-tkatchenko:prl:09-1)</sup>
is formally identical to that of the [DFT-D2](DFT-D2.md)
method. The important difference is, however, that the dispersion
coefficients and damping function are charge-density dependent. The
Tkatchenko-Scheffler method is therefore able to take into account
variations in vdW contributions of atoms due to their local chemical
environment. In this method the polarizability, dispersion coefficients,
and atomic radii of an atom in a molecule or a solid are computed from
their free-atomic values using the following relations:

$\alpha_{i} = \nu_{i}\\ \alpha_{i}^{free},$

$C_{6ii} = \nu_{i}^{2}\\C_{6ii}^{free},$

$R_{0i} = \left(\frac{\alpha_{i}}{\alpha_{i}^{free}}
\right)^{\frac{1}{3}} R_{0i}^{free}.$

The free-atomic quantities $\alpha_{i}^{free},C_{6ii}^{free}$ and
$R_{0i}^{free}$ are tabulated for all elements from the
first six rows of the periodic table except for lanthanides. If a
Tkatchenko-Scheffler calculation is performed for the system containing
an unsupported element, the user has to define the corresponding values
using the tags [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md) and [VDW_R0](../incar-tags/VDW_R0.md) (see
below). The effective atomic volumes $\nu_{i}$ are
determined using the Hirshfeld partitioning of the all-electron density:

$\nu_{i} = \frac{\int r^3 \\w_i({\mathbf{r}})
n({\mathbf{r}})\\d^3{\mathbf{r}}}{\int r^3\\
n_{i}^{free}({\mathbf{r}})\\d^3{\mathbf{r}}}$

where $n({\mathbf{r}})$ is the total electron density and
$n_{i}^{free}({\mathbf{r}})$ is the spherically
averaged electron density of the neutral free atomic species
$i$. The Hirshfeld weight $w_i({\mathbf{r}})$ is defined by free atomic densities as follows:

$w_i({\mathbf{r}}) =
\frac{n_{i}^{free}({\mathbf{r}})}{\sum_{j=1}^{N_{at}}
n_{j}^{free}({\mathbf{r}})}.$

The combination rule to define the strength of the dipole-dipole
dispersion interaction between unlike species is:

$C_{6ij} = \frac{2C_{6ii}\\C_{6jj}}{\[\frac{\alpha_{j}}
{\alpha_{i}}C_{6ii}+\frac{\alpha_{i}}{\alpha_{j}}C_{6jj}\]}.$

The parameter $R_{0ij}$
used in the damping function of the [DFT-D2](DFT-D2.md)
method is obtained from the atom-in-molecule vdW radii as follows:

$R_{0ij} = R_{0i} + R_{0j}.$

The performance of the Tkatchenko-Scheffler method in optimization of
various crystalline systems has been examined in reference
<sup>[\[2\]](#cite_note-bucko:prb:13-2)</sup>.

## Usage\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

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
  $C_6$ parameters (atomic units) for each species
  defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_C6](../incar-tags/VDW_C6.md)=\[real array\] : free-atomic
  $C_6$ parameters ($\mathrm{Jnm}^{6}\mathrm{mol}^{-1}$) for each species
  defined in the [POSCAR](../input-files/POSCAR.md) file (this parameter
  overrides [VDW_C6AU](../incar-tags/VDW_C6AU.md))
- [VDW_R0AU](../incar-tags/VDW_R0AU.md)=\[real array\] : free-atomic
  $R_0$ parameters (atomic units) for each species
  defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_R0](../incar-tags/VDW_R0.md)=\[real array\] :
  $R_0$ parameters (in Å) for each species defined in
  the [POSCAR](../input-files/POSCAR.md) file (this parameter overrides
  [VDW_R0AU](../incar-tags/VDW_R0AU.md))
- [LVDW_EWALD](../incar-tags/LVDW_EWALD.md)=.FALSE. : the lattice
  summation in $E_{\mathrm{disp}}$ expression is computed by means of Ewald's summation
  (*.TRUE.* ) or via a real space summation over all atomic pairs within
  cutoff radius [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) (*.FALSE.*).
  (available in VASP.5.3.4 and later)
- [LTSSURF](../incar-tags/LTSSURF.md)=.FALSE.: if set to .TRUE., the
  standard parametrization of the Tkatchenko-Scheffler method is
  replaced by the one designed to enable reliable modeling of structure
  and stability for a broad class of organic molecules adsorbed on metal
  surfaces is
  activated<sup>[\[3\]](#cite_note-3)</sup>

  

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>This method requires the use of <a href="/wiki/POTCAR"
title="POTCAR">POTCAR</a> files from the PAW dataset version 52 or
later.</li>
<li>The input reference data for non-interacting atoms is available only
for elements of the first six rows of the periodic table except for
lanthanides. If the system contains other elements, the user must
provide the free-atomic parameters for all atoms in the system via <a
href="/wiki/VDW_ALPHA" title="VDW ALPHA">VDW_ALPHA</a>, <a
href="/wiki/VDW_C6" title="VDW C6">VDW_C6</a>, <a href="/wiki/VDW_R0"
title="VDW R0">VDW_R0</a> defined in the <a href="/wiki/INCAR"
title="INCAR">INCAR</a> file.</li>
<li>The charge-density dependence of gradients is neglected.</li>
<li>The DFT-TS method is incompatible with the setting <a
href="/wiki/ADDGRID" title="ADDGRID">ADDGRID</a>=<em>.TRUE.</em>.</li>
<li>It is essential that a sufficiently dense FFT grid (controlled via
<a href="/wiki/NGXF" title="NGXF">NGXF</a>, <a href="/wiki/NGYF"
title="NGYF">NGYF</a> and <a href="/wiki/NGZF" title="NGZF">NGZF</a>) is
used in the DFT-TS calculation - we strongly recommend to use <a
href="/wiki/PREC" title="PREC">PREC</a>=<em>Accurate</em> for this type
of calculations (in any case, avoid using <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Low</em>).</li>
<li>Defaults for the parameters controlling the damping function (<a
href="/wiki/VDW_S6" title="VDW S6">VDW_S6</a>, <a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>, <a href="/wiki/VDW_D"
title="VDW D">VDW_D</a>) are available for the PBE, PBE0, HSE03, HSE06,
TPSS, and M06L functionals. If any other functional is used, the value
of <a href="/wiki/VDW_SR" title="VDW SR">VDW_SR</a> must be specified in
the <a href="/wiki/INCAR" title="INCAR">INCAR</a> file.</li>
<li>Ewald's summation in the calculation of <span class="smj-container"
style="opacity:.5">$E_{disp}$</span>
(controlled via <a href="/wiki/LVDW_EWALD"
title="LVDW EWALD">LVDW_EWALD</a>) implemented according to reference
<sup><a href="#cite_note-kerber:jcc:08-4"><span
class="cite-bracket">[</span>4<span
class="cite-bracket">]</span></a></sup> is available as of
VASP.5.3.4.</li>
<li>Parameters <a href="/wiki/VDW_C6AU" title="VDW C6AU">VDW_C6AU</a>
and <a href="/wiki/VDW_R0AU" title="VDW R0AU">VDW_R0AU</a> are available
as of VASP.5.3.4.</li>
<li>Hirshfeld charges for all configurations generated in a calculation
are written out in the <a href="/wiki/OUTCAR" title="OUTCAR">OUTCAR</a>
file. The corresponding table is introduced by the expression
<em>Hirshfeld charges:</em>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

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

## References\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-tkatchenko:prl:09_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.102.073005"
    class="external text" rel="nofollow">A. Tkatchenko and M. Scheffler,
    Phys. Rev. Lett. <strong>102</strong>, 073005 (2009).</a>
2.  [↑](#cite_ref-bucko:prb:13_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.87.064110"
    class="external text" rel="nofollow">T. Bučko, S. Lebègue, J. Hafner,
    and J. G. Ángyán, Phys. Rev. B <strong>87</strong>, 064110 (2013).</a>
3.  [↑](#cite_ref-3)
    <a
    href="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.035118"
    class="external text" rel="nofollow">V. G. Ruiz, W. Liu, and A.
    Tkatchenko, Phys. Rev. B 93, 035118 (2016).</a>
4.  [↑](#cite_ref-kerber:jcc:08_4-0)
    <a href="https://doi.org/10.1002/jcc.21069" class="external text"
    rel="nofollow">T. Kerber, M. Sierka, and J. Sauer, J. Comput. Chem.
    <strong>29</strong>, 2088 (2008).</a>


------------------------------------------------------------------------


