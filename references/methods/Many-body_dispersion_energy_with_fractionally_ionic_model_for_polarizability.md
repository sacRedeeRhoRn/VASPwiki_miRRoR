<!-- Source: https://vasp.at/wiki/index.php/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability | revid: 29773 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Many-body dispersion energy with fractionally ionic model for polarizability


A variant of [Many-body dispersion
energy](Many-body_dispersion_energy.md)
method based on fractionally ionic model for polarizability of
Gould[^gould:jctc:2016_a-1],
hereafter dubbed MBD@rsSCS/FI, has been introduced in
Ref.[^gould:jctc:2016_b-2]
Just like in the original MBD@rsSCS, dispersion energy in MBD@rsSCS/FI
is computed using

$E_{\mathrm{disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\$.

However, the two methods differ in the model used to approximate the
atomic polarizabilities ($\alpha_p^{\text{AIM}}$) needed to define tensor$\mathbf{A}^{(0)}(\omega)({\mathbf{k}})$. The MBD@rsSCS
makes use of the pre-computed static polarizabilities of neutral atoms
($\alpha_p^{\text{atom}}$)

$\alpha_p^{\text{AIM}} = \alpha_p^{\text{atom}}
\frac{V^{\text{eff}}_p}{V^{\text{atom}}_p}$,

whereby the volume ratios between interacting and non-interacting atoms
($\frac{V^{\text{eff}}_p}{V^{\text{atom}}_p}$) is
obtained using conventional Hirshfeld
partitioning[^hirshfeld:tca:1977-3].
Although the MBD@rsSCS/FI employs a similar scaling relation:

$\alpha_p^{\text{AIM}}(\omega) = \alpha_p^{\text{FI}}(\omega)
\frac{V^{\text{eff}}_p}{V^{\text{FI}}_p}$,

it relies on Gould's
model[^gould:jctc:2016_a-1]
of frequency-dependent polarizabilities ($\alpha_p^{\text{FI}}(\omega)$) and charge densities of non-interacting fractional
ions combined with iterative Hirshfeld
partitioning[^bultinck:jcp:07-4].
Obviously, the MBD@rsSCS and the MBD@rsSCS/FI are equivalent for
non-polar systems, such as graphite, but typically yield distinctly
different results for polar and ionic
materials[^gould:jctc:2016_b-2].

## Usage\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

The MBD@rsSCS/FI method is invoked by setting
[IVDW](../incar-tags/IVDW.md)=263. Optionally, the following parameters can
be user-defined (the given values are the default ones):

- [VDW_SR](../incar-tags/VDW_SR.md)=0.83 : scaling parameter
  $\beta$
- [LVDWEXPANSION](../incar-tags/LVDWEXPANSION.md)=.FALSE. : writes
  the two- to six- body contributions to the MBD dispersion energy in
  the [OUTCAR](../output-files/OUTCAR.md)
  ([LVDWEXPANSION](../incar-tags/LVDWEXPANSION.md)=*.TRUE.*)
- [LSCSGRAD](../incar-tags/LSCSGRAD.md)=.TRUE. : compute gradients (or
  not)
- [VDW_R0](../incar-tags/VDW_R0.md) : radii for atomic reference (see also
  [Tkatchenko-Scheffler
  method](Tkatchenko-Scheffler_method.md))
- <a href="/wiki/index.php?title=ITIM&amp;action=edit&amp;redlink=1"
  class="new" title="ITIM (page does not exist)">ITIM</a>=1: if set to
  +1, apply eigenvalue remapping to avoid unphysical cases where the
  eigenvalues of the matrix $\left(1-\mathbf{A}^{(0)}_{LR}(\omega)
  {\mathbf{T}}_{LR}({\mathbf{k}})\right)$ are
  non-positive, see
  reference[^gould:jctc:2016_b-2]
  for details

  

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
<li>The parametrization of reference data is available only for elements
of the first six rows of the periodic table except of the
lanthanides.</li>
<li>The charge-density dependence of gradients is neglected.</li>
<li>This method is incompatible with the setting <a href="/wiki/ADDGRID"
title="ADDGRID">ADDGRID</a>=<em>.TRUE.</em>.</li>
<li>It is essential that a sufficiently dense FFT grid (controlled via
<a href="/wiki/NGXF" title="NGXF">NGXF</a>, <a href="/wiki/NGYF"
title="NGYF">NGYF</a> and <a href="/wiki/NGZF" title="NGZF">NGZF</a> )
is used. We strongly recommend to use <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Accurate</em> for this type of calculations
(in any case, avoid using <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Low</em>}).</li>
<li>The method has sometimes numerical problems if highly polarizable
atoms are located at short distances. In such a case the calculation
terminates with an error message
<em>Error(vdw\_tsscs\_range\_separated\_k): d\_lr(pp)&lt;=0</em>. Note
that this problem is not caused by a bug, but rather it is due to a
limitation of the underlying physical model.</li>
<li>Analytical gradients of the energy are implemented (fore details see
reference [^bucko:jpcm:16-5]) and hence the atomic and
lattice relaxations can be performed.</li>
<li>Due to the long-range nature of dispersion interactions, the
convergence of energy with respect to the number of k-points should be
carefully examined.</li>
<li>A default value for the free-parameter of this method is available
only for the PBE (<a href="/wiki/VDW_SR" title="VDW SR">VDW_SR</a>=0.83)
and SCAN (<a href="/wiki/VDW_SR" title="VDW SR">VDW_SR</a>=1.12)
functionals. If any other functional is used, the value of <a
href="/wiki/VDW_SR" title="VDW SR">VDW_SR</a> must be specified in the
<a href="/wiki/INCAR" title="INCAR">INCAR</a> file.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md), [VDW_R0](../incar-tags/VDW_R0.md),
[VDW_SR](../incar-tags/VDW_SR.md),
[LVDWEXPANSION](../incar-tags/LVDWEXPANSION.md),
[LSCSGRAD](../incar-tags/LSCSGRAD.md), [IVDW](../incar-tags/IVDW.md),
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
[Self-consistent screening in Tkatchenko-Scheffler
method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[Many-body dispersion
energy](Many-body_dispersion_energy.md)

## References\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^gould:jctc:2016_a-1]: [T. Gould and T. Bučko, *C6 Coefficients and Dipole Polarizabilities for All Atoms and Many Ions in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**, 3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
[^gould:jctc:2016_b-2]: [T. Gould, S. Lebègue, J. G. Ángyán, and T. Bučko, *A Fractionally Ionic Approach to Polarizability and van der Waals Many-Body Dispersion Calculations*, J. Chem. Theory Comput. **12**, 5920 (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
[^hirshfeld:tca:1977-3]: [F. Hirshfeld, *Bonded-atom fragments for describing molecular charge densities*, Theor. Chim. Acta **44**, 129 (1977).](https://doi.org/10.1007/BF00549096)
[^bultinck:jcp:07-4]: [P. Bultinck, C. Van Alsenoy, P. W. Ayers, and R. Carbó Dorca, J. Chem. Phys. **126**, 144111 (2007).](https://doi.org/10.1063/1.2715563)
[^bucko:jpcm:16-5]: [T. Bučko, S. Lebègue, T. Gould, and J. G. Ángyán, J. Phys.: Condens. Matter **28**, 045201 (2016).](https://doi.org/10.1088/0953-8984/28/4/045201)
