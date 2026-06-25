<!-- Source: https://vasp.at/wiki/index.php/Dielectric_properties_of_Si | revid: 10416 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Dielectric properties of Si



[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
[dielectric properties of
SiC](Dielectric_properties_of_SiC.md) \>
dielectric properties of Si
 \> [Ionic contributions to
the frequency dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
- [3
  Calculation](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the static and frequency dependent dielectric properties
of Si. Please have a look at the example on [calculation of the static
and frequency dependent dielectric properties of
SiC](Dielectric_properties_of_SiC.md)
first. The same procedures apply to this example.

## Input\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    system Si
    5.430
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00
    0.25 0.25 0.25

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md) file for the static calculation:

<!-- -->

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

<!-- -->

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

## Calculation\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

## Download\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/0/08/Si_dielectric.tgz" class="internal"
title="Si dielectric.tgz">Si_dielectric.tgz</a>


[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
[dielectric properties of
SiC](Dielectric_properties_of_SiC.md) \>
dielectric properties of Si
 \> [Ionic contributions to
the frequency dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


