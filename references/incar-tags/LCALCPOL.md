<!-- Source: https://vasp.at/wiki/index.php/LCALCPOL | revid: 31524 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCALCPOL
LCALCPOL = .TRUE. \| .FALSE.  
Default: **LCALCPOL** = .FALSE. 

Description: LCALCPOL=.TRUE. switches on the evaluation of the Berry
phase expressions for the macroscopic electronic polarization in
accordance with the so-called [Modern Theory of
Polarization](../theory/Berry_phases_and_finite_electric_fields.md).

------------------------------------------------------------------------

For LCALCPOL=.TRUE., VASP calculates the electronic contribution to the
polarization, along the three reciprocal lattice vectors **G**_(i),
i=1,2,3, (i.e. Σ_(i) **P**·**G**_(i)) in a single run (unlike
[LBERRY](LBERRY.md)=.TRUE.).

### An example: The fluorine displacement dipole (Born effective charge) in NaF
- With [INCAR](../input-files/INCAR.md) file:

&nbsp;

    PREC = Med
    EDIFF= 1E-6

    ISMEAR = 0
    DIPOL  = 0.25 0.25 0.25

    LCALCPOL = .TRUE.

- [KPOINTS](../input-files/KPOINTS.md) file:

&nbsp;

    6x6x6
     0
    Gamma
     6 6 6
     0 0 0

- [POSCAR](../input-files/POSCAR.md) file:

&nbsp;

    NaF
     4.5102
     0.0 0.5 0.5
     0.5 0.0 0.5
     0.5 0.5 0.0
    1 1
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000
      0.5000000000000000  0.5000000000000000  0.5000000000000000

- and LDA Na_sv and F PAW datasets.

The [OUTCAR](../output-files/OUTCAR.md) file should now contain the
following lines:

                Ionic dipole moment: p[ion]=(     2.25510     2.25510     2.25510 ) electrons Angst

     Total electronic dipole moment: p[elc]=(     0.00000     0.00000     0.00000 ) electrons Angst

Here the units "electrons Angst" denote $e\AA=-1.602 10^{-19}C\AA$.

To calculate the change in the electronic polarization of NaF due to the
displacement of the fluorine sublattice we repeat the previous
calculation with the following [POSCAR](../input-files/POSCAR.md) file:

    NaF
     4.5102
     0.0 0.5 0.5
     0.5 0.0 0.5
     0.5 0.5 0.0
    1 1
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000
      0.5100000000000000  0.5100000000000000  0.4900000000000000

The [OUTCAR](../output-files/OUTCAR.md) should now contain something very
similar to the following lines:

                Ionic dipole moment: p[ion]=(     2.25510     2.25510     1.93939 ) electrons Angst

     Total electronic dipole moment: p[elc]=(     0.00000     0.00000     0.36061 ) electrons Angst

From the above one easily recognizes that the change in the electronic
dipole moment due to the F-sublattice displacement is:

$\Delta\mathrm{p\[elc\]}=0.3606\hat{z}\\e\AA$

and the corresponding change in the ionic dipole moment:

$\Delta\mathrm{p\[ion\]}=1.93939-2.25510=-0.31571\hat{z}\\e\AA$

Thus the total change is found to be:

$\Delta\mathrm{p\[tot\]}=0.36061-0.31571=0.0449\hat{z}\\e\AA$

and considering that the F-sublattice was displaced by 0.045102 Å these
calculations yield a Born effective charge for fluorine of

$Z^\*=0.0449/0.045102=-0.995|e|\\$.

The socalled parallel or $\mathbf{G}_{\parallel}$ direction in the integration over the reciprocal space unit
cell is set in [IGPAR](IGPAR.md).

## Related tags and articles
[LCALCEPS](LCALCEPS.md),
[EFIELD_PEAD](EFIELD_PEAD.md),
[LPEAD](LPEAD.md), [IPEAD](IPEAD.md),
[LBERRY](LBERRY.md), [IGPAR](IGPAR.md),
[NPPSTR](NPPSTR.md), [DIPOL](DIPOL.md), [Berry
phases and finite electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCALCPOL-_incategory-Examples)

------------------------------------------------------------------------
