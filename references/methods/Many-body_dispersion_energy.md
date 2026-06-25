<!-- Source: https://vasp.at/wiki/index.php/Many-body_dispersion_energy | revid: 29774 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Many-body dispersion energy


The many-body dispersion energy method (MBD@rsSCS) of Tkatchenko et
al.,<sup>[\[1\]](#cite_note-tkatchenko:prl:12-1)[\[2\]](#cite_note-ambrosetti:jcp:14-2)</sup>
invoked by setting [IVDW](../incar-tags/IVDW.md)=202, is based on the
random-phase expression for the correlation energy

$E_c = \int_{0}^{\infty} \frac{d\omega}{2\pi}
\mathrm{Tr}\left\\\mathrm{ln} (1-v\chi_0(i\omega))+v\chi_0(i\omega)
\right\\$

whereby the response function $\chi_0$ is
approximated by a sum of atomic contributions represented by quantum
harmonic oscillators. The expression for the dispersion energy used in
the VASP k-space implementation of the MBD@rsSCS method (see reference
<sup>[\[3\]](#cite_note-bucko:jpcm:16-3)</sup>
for details) is as follows:

$E_{\mathrm{disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\$

where ${\mathbf{A}}_{LR}$ is the frequency-dependent polarizability matrix and
$\mathbf{T}_{LR}$ is the long-range interaction tensor,
which describes the interaction of the screened polarizabilities
embedded in the system in a given geometrical arrangement. The
components of $\mathbf{A}_{LR}$ are obtained using an atoms-in-molecule approach as
employed in the pairwise [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)
(see references
<sup>[\[2\]](#cite_note-ambrosetti:jcp:14-2)[\[3\]](#cite_note-bucko:jpcm:16-3)</sup>
for details).

Details of the implementation of the MBD@rsSCS method in VASP are
presented in reference
<sup>[\[3\]](#cite_note-bucko:jpcm:16-3)</sup>.

## Usage\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

The input reference data for non-interacting atoms can be optionally
defined via the parameters [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md), and [VDW_R0](../incar-tags/VDW_R0.md)
(described by the [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)).
This method has one free parameter ($\beta$) that
must be adjusted for each exchange-correlation functional. The default
value of $\beta$=0.83
corresponds to the PBE functional ([GGA](../incar-tags/GGA.md)=PE). If
another functional is used, the value of $\beta$ must
be specified via [VDW_SR](../incar-tags/VDW_SR.md) in the
[INCAR](../input-files/INCAR.md) file.

The following optional parameters can be user-defined (the given values
are the default ones):

- [VDW_SR](../incar-tags/VDW_SR.md)=0.83 : scaling parameter
  $\beta$
- [LVDWEXPANSION](../incar-tags/LVDWEXPANSION.md)=.FALSE. : writes
  the two- to six-body contributions to the MBD dispersion energy in the
  [OUTCAR](../output-files/OUTCAR.md)
  ([LVDWEXPANSION](../incar-tags/LVDWEXPANSION.md)=*.TRUE.*)
- [LSCSGRAD](../incar-tags/LSCSGRAD.md)=.TRUE. : compute gradients (or
  not)
- [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
  [VDW_C6](../incar-tags/VDW_C6.md), [VDW_R0](../incar-tags/VDW_R0.md) :
  atomic reference (see also [Tkatchenko-Scheffler
  method](Tkatchenko-Scheffler_method.md))
- <a href="/wiki/index.php?title=ITIM&amp;action=edit&amp;redlink=1"
  class="new" title="ITIM (page does not exist)">ITIM</a>=-1: if set to
  +1, apply eigenvalue remapping to avoid unphysical cases where the
  eigenvalues of the matrix

$\left(1-\mathbf{A}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}})\right)$are
non-positive, see
reference<sup>[\[4\]](#cite_note-4)</sup>
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
<li>The input reference data for non-interacting atoms are available
only for elements of the first six rows of the periodic table except of
the lanthanides. If the system contains other elements, the user has to
provide the free-atomic parameters for all atoms in the system via <a
href="/wiki/VDW_ALPHA" title="VDW ALPHA">VDW_ALPHA</a>, <a
href="/wiki/VDW_C6" title="VDW C6">VDW_C6</a> and <a href="/wiki/VDW_R0"
title="VDW R0">VDW_R0</a> (described by the <a
href="/wiki/Tkatchenko-Scheffler_method"
title="Tkatchenko-Scheffler method">Tkatchenko-Scheffler method</a>)
defined in the <a href="/wiki/INCAR" title="INCAR">INCAR</a> file.</li>
<li>The charge-density dependence of gradients is neglected.</li>
<li>This method is incompatible with the setting <a href="/wiki/ADDGRID"
title="ADDGRID">ADDGRID</a>=<em>.TRUE.</em>.</li>
<li>It is essential that a sufficiently dense FFT grid (controlled via
<a href="/wiki/NGXF" title="NGXF">NGXF</a>, <a href="/wiki/NGYF"
title="NGYF">NGYF</a> and <a href="/wiki/NGZF" title="NGZF">NGZF</a> )
is used in the <a href="/wiki/Tkatchenko-Scheffler_method"
title="Tkatchenko-Scheffler method">Tkatchenko-Scheffler method</a>
calculation. We strongly recommend to use <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Accurate</em> for this type of calculations
(in any case, avoid using <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Low</em>).</li>
<li>The method sometimes has numerical problems if highly polarizable
atoms are located at short distances. In such a case the calculation
terminates with an error message
<em>Error(vdw\_tsscs\_range\_separated\_k): d\_lr(pp)&lt;=0</em>. Note
that this problem is not caused by a bug, but rather it is due to a
limitation of the underlying physical model.</li>
<li>Analytical gradients of the energy are implemented (fore details see
reference <sup><a href="#cite_note-bucko:jpcm:16-3"><span
class="cite-bracket">[</span>3<span
class="cite-bracket">]</span></a></sup>) and hence the atomic and
lattice relaxations can be performed.</li>
<li>Due to the long-range nature of dispersion interactions, the
convergence of energy with respect to the number of k-points should be
carefully examined.</li>
<li>A default value for the free-parameter of this method is available
only for the PBE (<a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>=0.83), PBE0 (<a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>=0.85), HSE06 (<a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>=0.85), B3LYP (<a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>=0.64), and SCAN (<a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>=1.12) functionals. If any other functional is
used, the value of <a href="/wiki/VDW_SR" title="VDW SR">VDW_SR</a> must
be specified in the <a href="/wiki/INCAR" title="INCAR">INCAR</a>
file.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy&amp;veaction=edit&amp;section=2"
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
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References\[<a
href="/wiki/index.php?title=Many-body_dispersion_energy&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-tkatchenko:prl:12_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.108.236402"
    class="external text" rel="nofollow">A. Tkatchenko, R. A. DiStasio, Jr.,
    R. Car, and M. Scheffler, Phys. Rev. Lett. <strong>108</strong>, 236402
    (2012).</a>
2.  ↑
    <sup>[a](#cite_ref-ambrosetti:jcp:14_2-0)</sup>
    <sup>[b](#cite_ref-ambrosetti:jcp:14_2-1)</sup>
    <a href="https://doi.org/10.1063/1.4865104" class="external text"
    rel="nofollow">A. Ambrosetti, A. M. Reilly, and R. A. DiStasio Jr., J.
    Chem. Phys. <strong>140</strong>, 018A508 (2014).</a>
3.  ↑
    <sup>[a](#cite_ref-bucko:jpcm:16_3-0)</sup>
    <sup>[b](#cite_ref-bucko:jpcm:16_3-1)</sup>
    <sup>[c](#cite_ref-bucko:jpcm:16_3-2)</sup>
    <sup>[d](#cite_ref-bucko:jpcm:16_3-3)</sup>
    <a href="https://doi.org/10.1088/0953-8984/28/4/045201"
    class="external text" rel="nofollow">T. Bučko, S. Lebègue, T. Gould, and
    J. G. Ángyán, J. Phys.: Condens. Matter <strong>28</strong>, 045201
    (2016).</a>
4.  [↑](#cite_ref-4)
    <a href="https://pubs.acs.org/doi/abs/10.1021/acs.jctc.6b00925"
    class="external text" rel="nofollow">T. Gould, S. Lebègue, J. G. Ángyán,
    and T. Bučko, J. Chem. Theory Comput. 12, 5920 (2016).</a>


------------------------------------------------------------------------


