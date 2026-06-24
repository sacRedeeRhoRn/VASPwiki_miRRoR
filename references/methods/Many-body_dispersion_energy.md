<!-- Source: https://vasp.at/wiki/index.php/Many-body_dispersion_energy | revid: 29774 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Many-body dispersion energy
The many-body dispersion energy method (MBD@rsSCS) of Tkatchenko et
al.,^([\[1\]](#cite_note-tkatchenko:prl:12-1)[\[2\]](#cite_note-ambrosetti:jcp:14-2))
invoked by setting [IVDW](../incar-tags/IVDW.md)=202, is based on the
random-phase expression for the correlation energy

$E_c = \int_{0}^{\infty} \frac{d\omega}{2\pi}
\mathrm{Tr}\left\\\mathrm{ln} (1-v\chi_0(i\omega))+v\chi_0(i\omega)
\right\\$

whereby the response function $\chi_0$
is approximated by a sum of atomic contributions represented by quantum
harmonic oscillators. The expression for the dispersion energy used in
the VASP k-space implementation of the MBD@rsSCS method (see reference
^([\[3\]](#cite_note-bucko:jpcm:16-3)) for details) is as follows:

$E_{\mathrm{disp}} =
-\int_{\mathrm{FBZ}}\frac{d{\mathbf{k}}}{v_{\mathrm{FBZ}}}
\int_0^{\infty} {\frac{d\omega}{2\pi}} \\ {\mathrm{Tr}}\left \\
\mathrm{ln} \left ({\mathbf{1}}-{\mathbf{A}}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}}) \right ) \right \\$

where ${\mathbf{A}}_{LR}$ is the
frequency-dependent polarizability matrix and $\mathbf{T}_{LR}$ is the long-range interaction tensor, which
describes the interaction of the screened polarizabilities embedded in
the system in a given geometrical arrangement. The components of
$\mathbf{A}_{LR}$ are obtained using an
atoms-in-molecule approach as employed in the pairwise
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)
(see references
^([\[2\]](#cite_note-ambrosetti:jcp:14-2)[\[3\]](#cite_note-bucko:jpcm:16-3))
for details).

Details of the implementation of the MBD@rsSCS method in VASP are
presented in reference ^([\[3\]](#cite_note-bucko:jpcm:16-3)).

## Usage
The input reference data for non-interacting atoms can be optionally
defined via the parameters [VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md), and [VDW_R0](../incar-tags/VDW_R0.md)
(described by the [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)).
This method has one free parameter ($\beta$) that must be adjusted for each exchange-correlation
functional. The default value of $\beta$=0.83 corresponds to the PBE functional
([GGA](../incar-tags/GGA.md)=PE). If another functional is used, the value of
$\beta$ must be specified via
[VDW_SR](../incar-tags/VDW_SR.md) in the [INCAR](../input-files/INCAR.md)
file.

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
- [ITIM](https://vasp.at/wiki/index.php/index.php)")=-1:
  if set to +1, apply eigenvalue remapping to avoid unphysical cases
  where the eigenvalues of the matrix

$\left(1-\mathbf{A}^{(0)}_{LR}(\omega)
{\mathbf{T}}_{LR}({\mathbf{k}})\right)$are non-positive, see
reference^([\[4\]](#cite_note-4)) for details

  

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
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References
1.  [↑](#cite_ref-tkatchenko:prl:12_1-0) [A. Tkatchenko, R. A. DiStasio,
    Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**, 236402
    (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
2.  ↑ ^([a](#cite_ref-ambrosetti:jcp:14_2-0))
    ^([b](#cite_ref-ambrosetti:jcp:14_2-1)) [A. Ambrosetti, A. M.
    Reilly, and R. A. DiStasio Jr., J. Chem. Phys. **140**, 018A508
    (2014).](https://doi.org/10.1063/1.4865104)
3.  ↑ ^([a](#cite_ref-bucko:jpcm:16_3-0))
    ^([b](#cite_ref-bucko:jpcm:16_3-1))
    ^([c](#cite_ref-bucko:jpcm:16_3-2))
    ^([d](#cite_ref-bucko:jpcm:16_3-3)) [T. Bučko, S. Lebègue, T. Gould,
    and J. G. Ángyán, J. Phys.: Condens. Matter **28**, 045201
    (2016).](https://doi.org/10.1088/0953-8984/28/4/045201)
4.  [↑](#cite_ref-4) [T. Gould, S. Lebègue, J. G. Ángyán, and T.
    Bučko, J. Chem. Theory Comput. 12, 5920
    (2016).](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.6b00925)

------------------------------------------------------------------------
