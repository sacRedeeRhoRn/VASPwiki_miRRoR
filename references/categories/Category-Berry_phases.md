<!-- Source: https://vasp.at/wiki/index.php/Category:Berry_phases | revid: 32921 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Berry phases
The polarization in a periodic system can be computed using the [berry
phase formulation of the
polarization](../theory/Berry_phases_and_finite_electric_fields.md)
(often referred to as the modern theory of polarization). The
calculation of the polarization is activated using
[LBERRY](../incar-tags/LBERRY.md). To compute the three components of the
polarization vector, we recommend using
[LCALCPOL](../incar-tags/LCALCPOL.md).

With a method to compute the polarization, one can compute the ground
state with a [finite electric
field](../theory/Berry_phases_and_finite_electric_fields.md)
applied to the system.

Finally, by applying a small electric field
[EFIELD_PEAD](../incar-tags/EFIELD_PEAD.md) along the three cartesian
directions and computing the polarization, forces, and stress tensor it
is possible to obtain [dielectric tensor, Born-effective charges, and
piezoelectric
tensor](../theory/Berry_phases_and_finite_electric_fields.md)
respectively. These calculations can be automated inside VASP using
[LCALCEPS](../incar-tags/LCALCEPS.md).
