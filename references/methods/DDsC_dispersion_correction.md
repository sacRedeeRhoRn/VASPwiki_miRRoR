<!-- Source: https://vasp.at/wiki/index.php/DDsC_dispersion_correction | revid: 29772 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DDsC dispersion correction


The expression for the density-dependent energy correction
dDsC[^steinmann:jcp:11-1][^steinmann:jctc:11-2]
is very similar to that of the [DFT-D2](DFT-D2.md) method
(see the equation for $E_{disp}$
for the [DFT-D2](DFT-D2.md) method). The important
difference is, however, that the dispersion coefficients and damping
function are charge-density dependent. The dDsC method is therefore able
to take into account variations in the vdW contributions of atoms due to
their local chemical environment. In this method, polarizability,
dispersion coefficients, charge and charge-overlap of an atom in a
molecule or solid are computed in the basis of a simplified
exchange-hole dipole moment
formalism[^steinmann:jcp:11-1]
pioneered by Becke and
Johnson[^becke:jcp:05-3].

The dDsC dispersion energy is expressed as follows:

${{E}_{\mathrm{disp}}}=-\sum\limits_{i=2}^{{{N}_\mathrm{at}}}{\sum\limits_{j=1}^{i-1}\sum\limits_{n=3}^{n=5}{{{f}_{2n}}(b{{R}_{ij}})\frac{C_{2n}^{ij}}{R_{ij}^{2n}}}}
{{E}_{\mathrm{disp}}}=-\sum\limits_{i=2}^{{{N}_{\mathrm{at}}}}{\sum\limits_{j=1}^{i-1}
{{{f}_{6}}(b{{R}_{ij}})\frac{C_{6,ij}}{R_{ij}^{6}}}}$

where $N_{\mathrm{at}}$ is the number of atoms in the system and
$b$ is the Tang and Toennies (TT) damping factor. The
damping function $f_{6}(bR_{ij})$ is defined as follows:

$f_{6}(x)=1-\exp(-x)\sum^{6}_{k=0}\frac{x^k}{k!}$

and its role is to attenuate the correction at short internuclear
distances. A key component of the dDsC method is the damping factor
$b$:

$b(x)=\frac{2 b_{ij,\mathrm{asym}}}{{{e}^{{{a}_{0}}\cdot x}}+1}$

where the fitted parameter $a_{0}$
controls the short-range behaviour and $x$ is the
damping argument for the TT-damping factor associated with two separated
atoms ($b_{ij,\mathrm{asym}}$). The term $b_{ij,\mathrm{asym}}$ is computed according to the combination rule:

$b_{ij,\mathrm{asym}}=2\frac{b_{ii,\mathrm{asym}}\cdot
b_{jj,\mathrm{asym}}}{b_{ii,\mathrm{asym}} + b_{jj,\mathrm{asym}}}$

with $b_{ii,\mathrm{asym}}$ being estimated from effective atomic
polarizabilities:

${b}_{ii,\mathrm{asym}}={b}_{0}\cdot \sqrt\[3\]{\frac{1}{\alpha_{i}}}$

The effective atom-in-molecule polarizabilities
$\alpha_{i}$ are computed from the tabulated
free-atomic polarizabilities (available for the elements of the first
six rows of the periodic table except of lanthanides) in the same way as
in the [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)
and [Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
but the Hirshfeld-dominant instead of the conventional Hirshfeld
partitioning is used. The last element of the correction is the damping
argument $x$:

$x=\left( 2{{q}_{ij}}+\frac{|({{Z}_{i}}-N_{i}^{D})\cdot
({{Z}_{j}}-N_{j}^{D})|}{{{r}_{ij}}}
\right)\frac{N_{i}^{D}+N_{j}^{D}}{N_{i}^{D}\cdot N_{j}^{D}}$

where $Z_i$ and
$N_i^D$ are the nuclear charge and Hirshfeld dominant
population of atom $i$,
respectively. The term $2q_{ij} = q_{ij} + q_{ji}$ is a covalent bond index based on the overlap of
conventional Hirshfeld populations $q_{ij}=\int
w_i({\mathbf{r}})w_j({\mathbf{r}})n({\mathbf{r}})d{\mathbf{r}}$, and the fractional term in the parentheses is a
distance-dependent ionic bond index.

The Performance of PBE-dDsC in the description of the adsorption of
hydrocarbons on Pt(111) has been examined in reference
[^gautier:pccp:15-4].

## Usage\[<a
href="/wiki/index.php?title=DDsC_dispersion_correction&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

The dDsC correction is invoked by setting [IVDW](../incar-tags/IVDW.md)=4.
The default values for damping function parameters are available for the
functionals PBE ([GGA](../incar-tags/GGA.md)=*PE*}) and revPBE
([GGA](../incar-tags/GGA.md)=*RE*). If another functional is used, the user
has to define these parameters via corresponding tags in the
[INCAR](../input-files/INCAR.md) file (parameters for common DFT functionals
can be found in reference
[^steinmann:jctc:11-2].
The following parameters can be optionally defined in the
[INCAR](../input-files/INCAR.md) file (the given values are the default
ones):

- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=50.0 : cutoff radius (in
  $\AA$) for pair interactions
- [VDW_S6](../incar-tags/VDW_S6.md)=13.96 : scaling factor
  ${a}_{0}$
- [VDW_SR](../incar-tags/VDW_SR.md)=1.32 : scaling factor
  ${b}_{0}$

  

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The dDsC method has been implemented into VASP by Stephan N.
Steinmann.</li>
<li>This method requires the use of <a href="/wiki/POTCAR"
title="POTCAR">POTCAR</a> files from the PAW dataset version 52 or
later.</li>
<li>The input reference polarizabilities for non-interacting atoms are
available only for elements of the first six rows of periodic table
except of the lanthanides.</li>
<li>It is essential that a sufficiently dense FFT grid (controlled via
<a href="/wiki/NGXF" title="NGXF">NGXF</a>, <a href="/wiki/NGYF"
title="NGYF">NGYF</a> and <a href="/wiki/NGZF" title="NGZF">NGZF</a>) is
used when using dDsC, especially for accurate gradients. We strongly
recommend to use <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Accurate</em> for this type of calculations
(in any case, avoid using <a href="/wiki/PREC"
title="PREC">PREC</a>=<em>Low</em>).</li>
<li>The charge-density dependence of gradients is neglected. This
approximation has been thoroughly investigated and validated in
reference [^bremond:jcp:14-5].</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=DDsC_dispersion_correction&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_SR](../incar-tags/VDW_SR.md),
[IVDW](../incar-tags/IVDW.md)

## References\[<a
href="/wiki/index.php?title=DDsC_dispersion_correction&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^steinmann:jcp:11-1]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Phys. **134**, 044117 (2011).](https://doi.org/10.1063/1.3545985)
[^steinmann:jctc:11-2]: [S. N. Steinmann and C. Corminboeuf, J. Chem. Theory Comput. **7**, 3567 (2011).](https://doi.org/10.1021/ct200602x)
[^becke:jcp:05-3]: [A. D. Becke and E. R. Johnson, J. Chem. Phys. **122**, 154104 (2005).](https://doi.org/10.1063/1.2795701)
[^gautier:pccp:15-4]: [S. Gautier, S. N. Steinmann, C. Michel, P. Fleurat-Lessard, and P. Sautet, Phys. Chem. Chem. Phys. **17**, 28921 (2015).](https://doi.org/10.1039/C5CP04534G)
[^bremond:jcp:14-5]: [E. Bremond, N. Golubev, S. N. Steinmann, and C. Corminboeuf, J. Chem. Phys. **140**, 18A516 (2014).](https://doi.org/10.1063/1.4867195)
