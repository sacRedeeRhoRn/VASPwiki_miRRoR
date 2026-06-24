<!-- Source: https://vasp.at/wiki/index.php/Self-consistent_screening_in_Tkatchenko-Scheffler_method | revid: 29771 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Self-consistent screening in Tkatchenko-Scheffler method
A computationally efficient way to account for electrodynamic response
effects, in particular the interaction of atoms with the dynamic
electric field due to the surrounding polarizable atoms, was proposed by
Tkatchenko et al^([\[1\]](#cite_note-tkatchenko:prl:12-1)). In this
method, termed TS+SCS, the frequency-dependent screened polarizabilities
$\alpha^{SCS}(\omega)$ are obtained by
solving the self-consistent screening equation:

$\alpha_{i}^{SCS}(\omega) = \alpha_{i}(\omega) -
\alpha_{i}(\omega) \sum_{i \neq j} \tau_{ij}
\alpha_{j}^{SCS}(\omega)$

where $\tau_{ij}$ is the dipole-dipole
interaction tensor and $\alpha_{i}(\omega)$ is the effective frequency-dependent polarizability,
approximated by

$\alpha_{i}(\omega) = \frac{\alpha_{i}}{1+\left
( \omega / \omega_i \right )^2}$

with the characteristic mean excitation frequency $\omega_i = \frac{4}{3} \frac{C_{6ii}}{(\alpha_{i})^2}$. The
dispersion coefficients are computed from the Casimir-Polder integral:

$C_{6ii} = \frac{3}{\pi} \int_0^{\infty}
\alpha_{i}^{SCS}(\omega) \alpha_{i}^{SCS}(\omega) \\d\omega.$

The van der Waals radii of atoms are obtained by rescaling the radii:

$R_{0i}^{SCS} = \left (
\frac{\alpha_{i}^{SCS}}{\alpha_{i}} \right )^{1/3} R_{0i}.$

The dispersion energy is computed using the same equation as in the
original [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)
but with corrected parameters $C_{6ii}^{SCS}$, $\alpha_{i}^{SCS}$, and
$R_{0i}^{SCS}$.

Details of the implementation of the TS+SCS method in VASP and the
performance tests made on various crystalline systems are presented in
reference ^([\[2\]](#cite_note-bucko:prb:13-2)).

## Usage
The TS+SCS method is invoked by setting [IVDW](../incar-tags/IVDW.md)=2\|20
and [LVDWSCS](../incar-tags/LVDWSCS.md)=*.TRUE.*. In addition to
parameters controlling the [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
the following optional parameters can set by the user:

- [VDW_SR](../incar-tags/VDW_SR.md)=0.97 scaling factor
  $s_{R}$
- [SCSRAD](../incar-tags/SCSRAD.md)=120 cutoff radius (in
  $\AA$) used in the calculation of
  $\tau_{ij}$
- [LSCSGRAD](../incar-tags/LSCSGRAD.md)=.TRUE. decides whether to
  compute SCS contribution to gradients
  ([LSCSGRAD](../incar-tags/LSCSGRAD.md)=*.TRUE.*) or not
- [LSCALER0](../incar-tags/LSCALER0.md)=.TRUE. decides whether to use
  the equation above for $R_{0i}^{SCS}$
  to re-scale the parameter $R_{0}$
  ([LSCALER0](../incar-tags/LSCALER0.md)=*.TRUE.*) or not

  

[TABLE]

## Related tags and articles
[LVDWSCS](../incar-tags/LVDWSCS.md), [VDW_SR](../incar-tags/VDW_SR.md),
[SCSRAD](../incar-tags/SCSRAD.md), [LSCSGRAD](../incar-tags/LSCSGRAD.md),
[LSCALER0](../incar-tags/LSCALER0.md), [IVDW](../incar-tags/IVDW.md),
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
[Tkatchenko-Scheffler method with iterative Hirshfeld
partitioning](Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning.md),
[Many-body dispersion
energy](Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References
1.  [↑](#cite_ref-tkatchenko:prl:12_1-0) [A. Tkatchenko, R. A. DiStasio,
    Jr., R. Car, and M. Scheffler, Phys. Rev. Lett. **108**, 236402
    (2012).](https://doi.org/10.1103/PhysRevLett.108.236402)
2.  [↑](#cite_ref-bucko:prb:13_2-0) [T. Bučko, S. Lebègue, J. Hafner,
    and J. G. Ángyán, Phys. Rev. B **87**, 064110
    (2013).](https://doi.org/10.1103/PhysRevB.87.064110)

------------------------------------------------------------------------
