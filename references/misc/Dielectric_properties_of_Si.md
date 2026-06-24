<!-- Source: https://vasp.at/wiki/index.php/Dielectric_properties_of_Si | revid: 10416 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Dielectric properties of Si
[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
[dielectric properties of
SiC](Dielectric_properties_of_SiC.md) \>
dielectric properties of Si  \> [Ionic contributions to the frequency
dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
- [3 Calculation](#Calculation)
- [4 Download](#Download)

## Task
Calculation of the static and frequency dependent dielectric properties
of Si. Please have a look at the example on [calculation of the static
and frequency dependent dielectric properties of
SiC](Dielectric_properties_of_SiC.md)
first. The same procedures apply to this example.

## Input
### [POSCAR](../input-files/POSCAR.md)
    system Si
    5.430
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00
    0.25 0.25 0.25

### [INCAR](../input-files/INCAR.md)
- [INCAR](../input-files/INCAR.md) file for the static calculation:

&nbsp;

    ## Static dielectric properties by means of DFPT
    #NBANDS = 4
    #EDIFF = 1E-6
    #LEPSILON = .TRUE.
    ## try to add this to the DFPT calculation
    #LPEAD = .TRUE.
    ## to get the ionic contributions to the
    ## static dielectric properties from
    ## perturbation theory
    #IBRION = 8
            
    ## Static dielectric properties by means of PEAD
    #EDIFF = 1E-8      # finite field requires very tight convergence
    #LCALCEPS = .TRUE.
    #NELM = 100
            
    ## Leave this in
    ISMEAR = 0
    SIGMA = 0.01
    GGA = PE

  

- [INCAR](../input-files/INCAR.md) for the frequency dependent calculation:

&nbsp;

    ## Frequency dependent dielectric tensor without
    ## local field effects
    #ALGO = Exact
    #NBANDS  = 64
    #LOPTICS = .TRUE. ; CSHIFT = 0.1
    #NEDOS = 2000
    ## and you might try with the following
    #LPEAD = .TRUE.
        
    ## Frequency dependent dielectric tensor with and
    ## without local field effects in RPA and due to
    ## changes in the DFT xc-potential
    ## N.B.: beware one first has to have done a
    ## calculation with LOPTICS = .TRUE. (see above)
    #ALGO = CHI ; LSPECTRAL = .FALSE.
    #LRPA = .FALSE.
    ## be sure to take the same number of bands as for
    ## the LOPTICS = .TRUE. calculation, otherwise the
    ## WAVEDER file is not read correctly
    # NBANDS = 64
        
    ## Leave this in
    ISMEAR = 0
    SIGMA = 0.01
    GGA = PE

## Calculation
## Download
[Si_dielectric.tgz](https://vasp.at/wiki/images/0/08/Si_dielectric.tgz "Si dielectric.tgz")

[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
[dielectric properties of
SiC](Dielectric_properties_of_SiC.md) \>
dielectric properties of Si  \> [Ionic contributions to the frequency
dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)
