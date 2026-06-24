<!-- Source: https://vasp.at/wiki/index.php/Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability | revid: 29773 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Many-body dispersion energy with fractionally ionic model for polarizability
A variant of [Many-body dispersion
energy](Many-body_dispersion_energy.md)
method based on fractionally ionic model for polarizability of
Gould^([\[1\]](#cite_note-gould:jctc:2016_a-1)), hereafter dubbed
MBD@rsSCS/FI, has been introduced in
Ref.^([\[2\]](#cite_note-gould:jctc:2016_b-2)) Just like in the original
MBD@rsSCS, dispersion energy in MBD@rsSCS/FI is computed using

$E_{\mathrm{disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\$.

However, the two methods differ in the model used to approximate the
atomic polarizabilities ($\alpha_p^{\text{AIM}}$) needed to define tensor$\mathbf{A}^{(0)}(\omega)({\mathbf{k}})$. The MBD@rsSCS makes
use of the pre-computed static polarizabilities of neutral atoms
($\alpha_p^{\text{atom}}$)

$\alpha_p^{\text{AIM}} = \alpha_p^{\text{atom}}
\frac{V^{\text{eff}}_p}{V^{\text{atom}}_p}$,

whereby the volume ratios between interacting and non-interacting atoms
($\frac{V^{\text{eff}}_p}{V^{\text{atom}}_p}$) is obtained using conventional Hirshfeld
partitioning^([\[3\]](#cite_note-hirshfeld:tca:1977-3)). Although the
MBD@rsSCS/FI employs a similar scaling relation:

$\alpha_p^{\text{AIM}}(\omega) =
\alpha_p^{\text{FI}}(\omega) \frac{V^{\text{eff}}_p}{V^{\text{FI}}_p}$,

it relies on Gould's model^([\[1\]](#cite_note-gould:jctc:2016_a-1)) of
frequency-dependent polarizabilities ($\alpha_p^{\text{FI}}(\omega)$) and charge densities of
non-interacting fractional ions combined with iterative Hirshfeld
partitioning^([\[4\]](#cite_note-bultinck:jcp:07-4)). Obviously, the
MBD@rsSCS and the MBD@rsSCS/FI are equivalent for non-polar systems,
such as graphite, but typically yield distinctly different results for
polar and ionic materials^([\[2\]](#cite_note-gould:jctc:2016_b-2)).

## Usage
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
- [ITIM](https://vasp.at/wiki/index.php/index.php)")=1:
  if set to +1, apply eigenvalue remapping to avoid unphysical cases
  where the eigenvalues of the matrix $\left(1-\mathbf{A}^{(0)}_{LR}(\omega)
  {\mathbf{T}}_{LR}({\mathbf{k}})\right)$ are non-positive,
  see reference^([\[2\]](#cite_note-gould:jctc:2016_b-2)) for details

  

[TABLE]

## Related tags and articles
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

## References
1.  ↑ ^([a](#cite_ref-gould:jctc:2016_a_1-0))
    ^([b](#cite_ref-gould:jctc:2016_a_1-1)) [T. Gould and T. Bučko, *C6
    Coefficients and Dipole Polarizabilities for All Atoms and Many Ions
    in Rows 1–6 of the Periodic Table*, J. Chem. Theory Comput. **12**,
    3603 (2016).](https://doi.org/10.1021/acs.jctc.6b00361)
2.  ↑ ^([a](#cite_ref-gould:jctc:2016_b_2-0))
    ^([b](#cite_ref-gould:jctc:2016_b_2-1))
    ^([c](#cite_ref-gould:jctc:2016_b_2-2)) [T. Gould, S. Lebègue, J. G.
    Ángyán, and T. Bučko, *A Fractionally Ionic Approach to
    Polarizability and van der Waals Many-Body Dispersion
    Calculations*, J. Chem. Theory Comput. **12**, 5920
    (2016).](https://doi.org/10.1021/acs.jctc.6b00925)
3.  [↑](#cite_ref-hirshfeld:tca:1977_3-0) [F. Hirshfeld, *Bonded-atom
    fragments for describing molecular charge densities*, Theor. Chim.
    Acta **44**, 129 (1977).](https://doi.org/10.1007/BF00549096)
4.  [↑](#cite_ref-bultinck:jcp:07_4-0) [P. Bultinck, C. Van
    Alsenoy, P. W. Ayers, and R. Carbó Dorca, J. Chem. Phys. **126**,
    144111 (2007).](https://doi.org/10.1063/1.2715563)
5.  [↑](#cite_ref-bucko:jpcm:16_5-0) [T. Bučko, S. Lebègue, T. Gould,
    and J. G. Ángyán, J. Phys.: Condens. Matter **28**, 045201
    (2016).](https://doi.org/10.1088/0953-8984/28/4/045201)

------------------------------------------------------------------------
