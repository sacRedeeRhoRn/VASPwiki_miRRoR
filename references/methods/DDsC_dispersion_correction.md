<!-- Source: https://vasp.at/wiki/index.php/DDsC_dispersion_correction | revid: 29772 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DDsC dispersion correction
The expression for the density-dependent energy correction
dDsC^([\[1\]](#cite_note-steinmann:jcp:11-1)[\[2\]](#cite_note-steinmann:jctc:11-2))
is very similar to that of the [DFT-D2](DFT-D2.md) method
(see the equation for $E_{disp}$ for
the [DFT-D2](DFT-D2.md) method). The important difference
is, however, that the dispersion coefficients and damping function are
charge-density dependent. The dDsC method is therefore able to take into
account variations in the vdW contributions of atoms due to their local
chemical environment. In this method, polarizability, dispersion
coefficients, charge and charge-overlap of an atom in a molecule or
solid are computed in the basis of a simplified exchange-hole dipole
moment formalism^([\[1\]](#cite_note-steinmann:jcp:11-1)) pioneered by
Becke and Johnson^([\[3\]](#cite_note-becke:jcp:05-3)).

The dDsC dispersion energy is expressed as follows:

${{E}_{\mathrm{disp}}}=-\sum\limits_{i=2}^{{{N}_\mathrm{at}}}{\sum\limits_{j=1}^{i-1}\sum\limits_{n=3}^{n=5}{{{f}_{2n}}(b{{R}_{ij}})\frac{C_{2n}^{ij}}{R_{ij}^{2n}}}}
{{E}_{\mathrm{disp}}}=-\sum\limits_{i=2}^{{{N}_{\mathrm{at}}}}{\sum\limits_{j=1}^{i-1}
{{{f}_{6}}(b{{R}_{ij}})\frac{C_{6,ij}}{R_{ij}^{6}}}}$

where $N_{\mathrm{at}}$ is the number
of atoms in the system and $b$ is the
Tang and Toennies (TT) damping factor. The damping function
$f_{6}(bR_{ij})$ is defined as
follows:

$f_{6}(x)=1-\exp(-x)\sum^{6}_{k=0}\frac{x^k}{k!}$

and its role is to attenuate the correction at short internuclear
distances. A key component of the dDsC method is the damping factor
$b$:

$b(x)=\frac{2
b_{ij,\mathrm{asym}}}{{{e}^{{{a}_{0}}\cdot x}}+1}$

where the fitted parameter $a_{0}$
controls the short-range behaviour and $x$ is the damping argument for the TT-damping factor associated
with two separated atoms ($b_{ij,\mathrm{asym}}$). The term $b_{ij,\mathrm{asym}}$ is computed according to the combination rule:

$b_{ij,\mathrm{asym}}=2\frac{b_{ii,\mathrm{asym}}\cdot
b_{jj,\mathrm{asym}}}{b_{ii,\mathrm{asym}} + b_{jj,\mathrm{asym}}}$

with $b_{ii,\mathrm{asym}}$ being
estimated from effective atomic polarizabilities:

${b}_{ii,\mathrm{asym}}={b}_{0}\cdot
\sqrt\[3\]{\frac{1}{\alpha_{i}}}$

The effective atom-in-molecule polarizabilities $\alpha_{i}$ are computed from the tabulated free-atomic
polarizabilities (available for the elements of the first six rows of
the periodic table except of lanthanides) in the same way as in the
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)
and [Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
but the Hirshfeld-dominant instead of the conventional Hirshfeld
partitioning is used. The last element of the correction is the damping
argument $x$:

$x=\left(
2{{q}_{ij}}+\frac{|({{Z}_{i}}-N_{i}^{D})\cdot
({{Z}_{j}}-N_{j}^{D})|}{{{r}_{ij}}}
\right)\frac{N_{i}^{D}+N_{j}^{D}}{N_{i}^{D}\cdot N_{j}^{D}}$

where $Z_i$ and $N_i^D$ are the nuclear charge and Hirshfeld dominant
population of atom $i$, respectively.
The term $2q_{ij} = q_{ij} + q_{ji}$
is a covalent bond index based on the overlap of conventional Hirshfeld
populations $q_{ij}=\int
w_i({\mathbf{r}})w_j({\mathbf{r}})n({\mathbf{r}})d{\mathbf{r}}$, and the fractional term in the parentheses is a
distance-dependent ionic bond index.

The Performance of PBE-dDsC in the description of the adsorption of
hydrocarbons on Pt(111) has been examined in reference
^([\[4\]](#cite_note-gautier:pccp:15-4)).

## Usage
The dDsC correction is invoked by setting [IVDW](../incar-tags/IVDW.md)=4.
The default values for damping function parameters are available for the
functionals PBE ([GGA](../incar-tags/GGA.md)=*PE*}) and revPBE
([GGA](../incar-tags/GGA.md)=*RE*). If another functional is used, the user
has to define these parameters via corresponding tags in the
[INCAR](../input-files/INCAR.md) file (parameters for common DFT functionals
can be found in reference ^([\[2\]](#cite_note-steinmann:jctc:11-2)).
The following parameters can be optionally defined in the
[INCAR](../input-files/INCAR.md) file (the given values are the default
ones):

- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=50.0 : cutoff radius (in
  $\AA$) for pair interactions
- [VDW_S6](../incar-tags/VDW_S6.md)=13.96 : scaling factor
  ${a}_{0}$
- [VDW_SR](../incar-tags/VDW_SR.md)=1.32 : scaling factor
  ${b}_{0}$

  

[TABLE]

## Related tags and articles
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_SR](../incar-tags/VDW_SR.md),
[IVDW](../incar-tags/IVDW.md)

## References
1.  ↑ ^([a](#cite_ref-steinmann:jcp:11_1-0))
    ^([b](#cite_ref-steinmann:jcp:11_1-1)) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Phys. **134**, 044117
    (2011).](https://doi.org/10.1063/1.3545985)
2.  ↑ ^([a](#cite_ref-steinmann:jctc:11_2-0))
    ^([b](#cite_ref-steinmann:jctc:11_2-1)) [S. N. Steinmann and C.
    Corminboeuf, J. Chem. Theory Comput. **7**, 3567
    (2011).](https://doi.org/10.1021/ct200602x)
3.  [↑](#cite_ref-becke:jcp:05_3-0) [A. D. Becke and E. R. Johnson, J.
    Chem. Phys. **122**, 154104
    (2005).](https://doi.org/10.1063/1.2795701)
4.  [↑](#cite_ref-gautier:pccp:15_4-0) [S. Gautier, S. N. Steinmann, C.
    Michel, P. Fleurat-Lessard, and P. Sautet, Phys. Chem. Chem. Phys.
    **17**, 28921 (2015).](https://doi.org/10.1039/C5CP04534G)
5.  [↑](#cite_ref-bremond:jcp:14_5-0) [E. Bremond, N. Golubev, S. N.
    Steinmann, and C. Corminboeuf, J. Chem. Phys. **140**, 18A516
    (2014).](https://doi.org/10.1063/1.4867195)

------------------------------------------------------------------------
