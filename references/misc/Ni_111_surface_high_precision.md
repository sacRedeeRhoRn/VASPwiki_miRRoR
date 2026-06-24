<!-- Source: https://vasp.at/wiki/index.php/Ni_111_surface_high_precision | revid: 10443 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ni 111 surface high precision
[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \> Ni 111
surface high precision \> [partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> [STM of
graphene](STM_of_graphene.md) \> [collective jumps
of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
  - [3.1 Adsorption energies](#Adsorption_energies)
  - [3.2 Work function](#Work_function)
- [4 Download](#Download)

## Task
Calculation of the adsorption energies and the work function of a Ni
(111) surface with high precision.

## Input
### [POSCAR](../input-files/POSCAR.md)
     fcc (111) surface                      
       3.53000000000000     
         0.7071067800000000    0.0000000000000000    0.0000000000000000
        -0.3535533900000000    0.6123724000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    5.1961523999999999
       Ni
         5
    Selective dynamics
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000   F   F   F
      0.3333333300000021  0.6666666699999979  0.1111111100000031   F   F   F
      0.6666666699999979  0.3333333300000021  0.2222222199999990   F   F   F
     -0.0000000000000000 -0.0000000000000000  0.3320935940210170   T   T   T
      0.3333333300000021  0.6666666699999979  0.4413539967541983   T   T   T
     
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00
      0.00000000E+00  0.00000000E+00  0.00000000E+00

  

### [INCAR](../input-files/INCAR.md)
     ENMAX = 400
        
    general:
      SYSTEM = clean nickel (111) surface
      ISTART = 0
      ICHARG = 2
      ISMEAR = 2 ; SIGMA = 0.2
      ALGO = Fast
      EDIFF = 1E-6
        
    special:
      LVHAR = .TRUE.
    #  LVTOT = .TRUE.

- Run a single point calculation for the Ni(111) clean surface at a
  higher cutoff (400eV), which is needed to compute the adsorption
  energy.
- Potentials for O and C require an energy cut-off of 400eV:
  - Previous calculation for clean cannot be used as reference.
  - Recalculate with same energy cut-off.

### [KPOINTS](../input-files/KPOINTS.md)
    K-Points
    0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation
### Adsorption energies
- Change of cut-off lowers total energy:
  - -25.732 eV (270 eV); -25.737 eV (400 eV).
  - Becomes more important for larger cells.

&nbsp;

- The adsorption energy is calculated in the following way:
  - $E_{\mathrm{ads}} = E_{\mathrm{total}} -
    E_{\mathrm{clean}} - E_{\mathrm{CO}}$.
  - $E_{\mathrm{ads}} = -40.829 + 25.737 + 14.835
    = -0.257$ eV.

### Work function
- We use this run also to calculate the work-function of Ni(111).

&nbsp;

- Use p4vasp to show the planar average of the potential:

[![](https://vasp.at/wiki/images/thumb/d/d0/Fig_Ni_111_high_prec_1.png/700px-Fig_Ni_111_high_prec_1.png)](https://vasp.at/wiki/File:Fig_Ni_111_high_prec_1.png)

- Vacuum potential $E^{\mathrm{vac}} = 5.45$ eV.
- Fermi level $\epsilon_{\mathrm{F}} = 0.224$ eV. (from [OUTCAR](../output-files/OUTCAR.md) file).
- Work function $\Phi = E^{\mathrm{vac}} -
  \epsilon_{\mathrm{F}} = 5.23$ eV.

## Download
[Ni111clean_400eV.tgz](https://vasp.at/wiki/images/4/43/Ni111clean_400eV.tgz "Ni111clean 400eV.tgz")

[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \> Ni 111
surface high precision \> [partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of graphite](STM_of_graphite.md) \> [STM of
graphene](STM_of_graphene.md) \> [collective jumps
of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")
 \> [List of tutorials](../categories/Category-Tutorials.md)
