<!-- Source: https://vasp.at/wiki/index.php/Spin-orbit_coupling_in_a_Ni_monolayer | revid: 36615 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Spin-orbit coupling in a Ni monolayer
[Overview](../tutorials/Magnetism_-_Tutorial.md) \> [fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
[NiO](NiO.md) \> [NiO
LSDA+U](NiO_LSDA+U.md) \> Spin-orbit coupling in a Ni
monolayer \> [Spin-orbit coupling in a Fe
monolayer](Spin-orbit_coupling_in_a_Fe_monolayer.md) \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
- [4 Download](#Download)

## Task
Spin-orbit coupling (SOC) in a freestanding Ni monolayer.

## Input
### [POSCAR](../input-files/POSCAR.md)
    fcc Ni 100 surface
     3.53
       .50000   .50000   .00000
      -.50000   .50000   .00000
       .00000   .00000  5.00000
      1
    Cartesian
       .00000   .00000   .00000

### [INCAR](../input-files/INCAR.md)
    SYSTEM        = Ni (100) monolayer
    ISTART        = 0
    ENCUT         = 270.00
    LNONCOLLINEAR = .TRUE.
    MAGMOM        = 0.0 0.0 1.0
    VOSKOWN       = 1
    LSORBIT       = .TRUE.
        
    LMAXMIX       = 4

- Initialization of moment along z-direction (out of plane)
  ([MAGMOM](../incar-tags/MAGMOM.md) = 0.0 0.0 1.0).
- Spin-orbit interaction switched on
  ([LSORBIT](../incar-tags/LSORBIT.md)=*.TRUE.*).
- For the second calculation, switch to in-plane magnetization by
  setting [MAGMOM](../incar-tags/MAGMOM.md) = 1.0 0.0 0.0 in the
  [INCAR](../input-files/INCAR.md) file.

### [KPOINTS](../input-files/KPOINTS.md)
    k-points
     0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation
- The sample output for the total energy using out of plane
  magnetization is given in the [OSZICAR](../output-files/OSZICAR.md) file:

&nbsp;

    ...
    DAV:  20    -0.371322930070E+01    0.15852E-03   -0.11632E-03   636   0.235E-01    0.225E-02
    DAV:  21    -0.371323204989E+01   -0.27492E-05   -0.13047E-05   500   0.184E-02
       1 F= -.37132320E+01 E0= -.37139803E+01  d E =0.224478E-02  mag=  0.0000  0.0000  0.9035

- The sample output for the total energy using in plane magnetization
  looks like the following:

&nbsp;

    ...
    DAV:  19    -0.371443443024E+01   -0.80757E-04   -0.35822E-03  1084   0.323E-01    0.119E-02
    DAV:  20    -0.371446032472E+01   -0.25894E-04   -0.42423E-05   916   0.263E-02
       1 F= -.37144603E+01 E0= -.37150300E+01  d E =0.170900E-02  mag=  0.9049  0.0000  0.0000

- From the energy difference of these calculations we see that the easy
  axis lies in plane:

$E_{\textrm{MAE}}=E(m_{\perp})-E(m_{\parallel})=1.2 \\ \textrm{meV}$

## Download
[4_4_SOI_Ni.tgz](https://vasp.at/wiki/images/9/98/4_4_SOI_Ni.tgz "4 4 SOI Ni.tgz")

[Overview](../tutorials/Magnetism_-_Tutorial.md) \> [fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
[NiO](NiO.md) \> [NiO
LSDA+U](NiO_LSDA+U.md) \> Spin-orbit coupling in a Ni
monolayer \> [Spin-orbit coupling in a Fe
monolayer](Spin-orbit_coupling_in_a_Fe_monolayer.md) \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)
