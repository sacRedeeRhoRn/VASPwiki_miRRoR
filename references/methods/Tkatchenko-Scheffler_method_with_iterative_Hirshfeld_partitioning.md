<!-- Source: https://vasp.at/wiki/index.php/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning | revid: 29766 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Tkatchenko-Scheffler method with iterative Hirshfeld partitioning


The [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
which uses fixed neutral atoms as a reference to estimate the effective
volumes of atoms-in-molecule (AIM) and to calibrate their
polarizabilities and dispersion coefficients, fails to describe the
structure and the energetics of ionic solids. As shown in references
<sup>[\[1\]](#cite_note-bucko:jctc:13-1)</sup>
and
<sup>[\[2\]](#cite_note-bucko:jcp:14-2)</sup>,
this problem can be solved by replacing the conventional Hirshfeld
partitioning used to compute properties of interacting atoms by the
iterative scheme proposed by
Bultinck<sup>[\[3\]](#cite_note-bultinck:jcp:07-3)</sup>.
In this iterative Hirshfeld algorithm (HI), the neutral reference atoms
are replaced with ions with fractional charges determined together with
the AIM charge densities in a single iterative procedure. The algorithm
is initialized with a promolecular density defined by non-interacting
neutral atoms. The iterative procedure then runs in the following steps:

- The Hirshfeld weight function for the step $i$ is
  computed as

$w_A^{i}({\mathbf{r}}) = {n^{i}_A({\mathbf{r}})}/\left({\sum_B
n^{i}_B({\mathbf{r}})}\right)$

where the sum extends over all atoms in the system.

- The number of electrons per atom is determined using

$N_{A}^{i+1} = N_{A}^{i} + \int \left\[ n_{A}^{i}(\mathbf{r}) -
w_{A}^i(\mathbf{r})\\n(\mathbf{r}) \right\]\\d^{3}\mathbf{r}.$

- New reference charge densities are computed using

$n^{i+1}_A(\mathbf{r}) = n^{\text{lint}(N^i_A)}(\mathbf{r})\left \[
\text{uint}(N^i_A)-N^i_A\right \] +
n^{\text{uint}(N_A^i)}({\mathbf{r}})\left \[ N^i_A -
\text{lint}(N^i_A)\right \]$

where $\text{lint}(x)$ expresses the integer part of
$x$ and $\text{uint}(x)=\text{lint}(x)+1$.

Steps (1) to (3) are iterated until the difference in the electronic
populations between two subsequent steps ($\Delta_{A}^{i} = \vert
N_{A}^{i}-N_{A}^{i+1}\vert$) is less than a
predefined threshold for all atoms. The converged iterative Hirshfeld
weights ($w_{A}^{i}$)
are then used to define the AIM properties needed to evaluate the
dispersion energy (see [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)).

The TS-HI method is described in detail in reference
<sup>[\[1\]](#cite_note-bucko:jctc:13-1)</sup>
and its performance in optimization of various crystalline systems is
examined in reference
<sup>[\[2\]](#cite_note-bucko:jcp:14-2)</sup>.

## Usage\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

The Tkatchenko-Scheffler method with iterative Hirshfeld partitioning
(TS-HI) is invoked by setting [IVDW](../incar-tags/IVDW.md)=21. The
convergence criterion for iterative Hirshfeld partitioning (in e) can
optionally be defined via the parameter
[HITOLER](../incar-tags/HITOLER.md) (the default value is 5e-5). Other
optional parameters controlling the input for the calculation are as in
the conventional [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md).
The default value of the adjustable parameter
[VDW_SR](../incar-tags/VDW_SR.md) is 0.95 and corresponds to the PBE
functional.

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
the lanthanides. If the system contains other elements, the user must
provide the free-atomic parameters for all atoms in the system via <a
href="/wiki/VDW_ALPHA" title="VDW ALPHA">VDW_ALPHA</a>, <a
href="/wiki/VDW_C6" title="VDW C6">VDW_C6</a>, <a href="/wiki/VDW_R0"
title="VDW R0">VDW_R0</a> (see <a
href="/wiki/Tkatchenko-Scheffler_method"
title="Tkatchenko-Scheffler method">Tkatchenko-Scheffler method</a>
defined in the <a href="/wiki/INCAR" title="INCAR">INCAR</a> file.</li>
<li>The charge-density dependence of gradients is neglected.</li>
<li>The DFT-TS/HI method is incompatible with the setting <a
href="/wiki/ADDGRID" title="ADDGRID">ADDGRID</a>=<em>.TRUE.</em>.</li>
<li>It is essential that a sufficiently dense FFT grid (controlled via
<a href="/wiki/NGXF" title="NGXF">NGXF</a>, <a href="/wiki/NGYF"
title="NGYF">NGYF</a> and <a href="/wiki/NGZF" title="NGZF">NGZF</a>) is
used in the DFT-TS/HI - we strongly recommend to use <a
href="/wiki/PREC" title="PREC">PREC</a>=<em>Accurate</em>} for this type
of calculations (in any case, avoid using <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Low</em>).</li>
<li>Defaults for the parameters controlling the damping function (<a
href="/wiki/VDW_S6" title="VDW S6">VDW_S6</a>, <a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a>, <a href="/wiki/VDW_D"
title="VDW D">VDW_D</a>) are available only for the PBE functional. If a
functional other than PBE is used, the value of <a href="/wiki/VDW_SR"
title="VDW SR">VDW_SR</a> must be specified in the <a href="/wiki/INCAR"
title="INCAR">INCAR</a> file.</li>
<li>Ewald's summation in the calculation of <span class="smj-container"
style="opacity:.5">$E_{disp}$</span>
(controlled via <a href="/wiki/LVDW_EWALD"
title="LVDW EWALD">LVDW_EWALD</a>) implemented according to reference
<sup><a href="#cite_note-kerber:jcc:08-4"><span
class="cite-bracket">[</span>4<span
class="cite-bracket">]</span></a></sup> is available as of
VASP.5.3.4.</li>
<li>Hirshfeld charges for all configurations generated in a calculation
are written out in the <a href="/wiki/OUTCAR" title="OUTCAR">OUTCAR</a>
file. The corresponding table is introduced by the expression
<em>Hirshfeld charges:</em>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[HITOLER](../incar-tags/HITOLER.md), [VDW_SR](../incar-tags/VDW_SR.md),
[VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md), [VDW_R0](../incar-tags/VDW_R0.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_D](../incar-tags/VDW_D.md),
[LVDW_EWALD](../incar-tags/LVDW_EWALD.md), [IVDW](../incar-tags/IVDW.md),
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
[Self-consistent screening in Tkatchenko-Scheffler
method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References\[<a
href="/wiki/index.php?title=Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-bucko:jctc:13_1-0)</sup>
    <sup>[b](#cite_ref-bucko:jctc:13_1-1)</sup>
    <a href="https://doi.org/10.1021/ct400694h" class="external text"
    rel="nofollow">T. Bučko, S. Lebègue, J. Hafner, and J. G. Ángyán, J.
    Chem. Theory Comput. <strong>9</strong>, 4293 (2013)</a>
2.  ↑
    <sup>[a](#cite_ref-bucko:jcp:14_2-0)</sup>
    <sup>[b](#cite_ref-bucko:jcp:14_2-1)</sup>
    <a href="https://doi.org/10.1063/1.4890003" class="external text"
    rel="nofollow">T. Bučko, S. Lebègue, J. G. Ángyán, and J. Hafner, J.
    Chem. Phys. <strong>141</strong>, 034114 (2014).</a>
3.  [↑](#cite_ref-bultinck:jcp:07_3-0)
    <a href="https://doi.org/10.1063/1.2715563" class="external text"
    rel="nofollow">P. Bultinck, C. Van Alsenoy, P. W. Ayers, and R. Carbó
    Dorca, J. Chem. Phys. <strong>126</strong>, 144111 (2007).</a>
4.  [↑](#cite_ref-kerber:jcc:08_4-0)
    <a href="https://doi.org/10.1002/jcc.21069" class="external text"
    rel="nofollow">T. Kerber, M. Sierka, and J. Sauer, J. Comput. Chem.
    <strong>29</strong>, 2088 (2008).</a>


------------------------------------------------------------------------


