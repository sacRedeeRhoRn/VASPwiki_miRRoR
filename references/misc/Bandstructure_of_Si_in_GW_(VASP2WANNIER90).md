<!-- Source: https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_%28VASP2WANNIER90%29 | revid: 24635 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandstructure of Si in GW (VASP2WANNIER90)
[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> bandstructure of
Si in GW (VASP2WANNIER90) \> [bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of SrVO3](CRPA_of_SrVO3.md)  \>
[Equilibrium volume of Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Step 1: a DFT groundstate
  calculation](#Step_1:_a_DFT_groundstate_calculation)
- [3 Step 2: obtain DFT virtual
  orbitals](#Step_2:_obtain_DFT_virtual_orbitals)
- [4 Step 3: GW calculation including LWANNIER90
  TAG](#Step_3:_GW_calculation_including_LWANNIER90_TAG)
- [5 Step 4: WANNIER90](#Step_4:_WANNIER90)
  - [5.1 Compute Wannier functions](#Compute_Wannier_functions)
  - [5.2 Obtain bandstructure (Wannier
    interpolation)](#Obtain_bandstructure_(Wannier_interpolation))
- [6 Download](#Download)

## Task
Calculation of the bandstructure of Si in GW using the VASP2WANNIER90
interface.

------------------------------------------------------------------------

**Mind**: The procedure to compute bandstructure in GW using V2W is
almost identical to the corresponding HSE one described in [Si
bandstructure](Si_bandstructure.md).

**Mind**: The standard procedure for GW calculations is described in
[Bandgap of Si in GW](Bandgap_of_Si_in_GW.md).

------------------------------------------------------------------------

## Step 1: a DFT groundstate calculation
Everything starts with a standard DFT groundstate calculation (in this
case PBE).

- [INCAR](../input-files/INCAR.md)

&nbsp;

    ISMEAR =  0
    SIGMA  =  0.05
    GGA    = PE

  

- [KPOINTS](../input-files/KPOINTS.md)

&nbsp;

    4x4x4
     0
    G
     4 4 4
     0 0 0

- [POSCAR](../input-files/POSCAR.md)

&nbsp;

    system Si
    5.430
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00
    0.25 0.25 0.25

## Step 2: obtain DFT virtual orbitals
To obtain a [WAVECAR](../input-files/WAVECAR.md) file with a reasonable
number of virtual orbitals (50-100 per atom) we need to restart from the
previous groundstate calculation with [ALGO](../incar-tags/ALGO.md)=Exact,
and manually set the number of bands by means of the
[NBANDS](../incar-tags/NBANDS.md)-tag. To obtain the corresponding
[WAVEDER](../input-files/WAVEDER.md) file we additionally specify
[LOPTICS](../incar-tags/LOPTICS.md)=.TRUE.

- [INCAR](../input-files/INCAR.md)

&nbsp;

    ALGO = Exact
    NBANDS  = 64
    LOPTICS = .TRUE.
    NEDOS = 2000
        
    ISMEAR =  0
    SIGMA  =  0.05
    GGA    = PE

## Step 3: GW calculation including LWANNIER90 TAG
Restart from the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files of the previous calculation,
with

- [INCAR](../input-files/INCAR.md)

&nbsp;

    ## Frequency dependent dielectric tensor including
    ## local field effects within the RPA (default) or
    ## including changes in the DFT xc-potential (LRPA=.FALSE.).
    ## N.B.: beware one first has to have done a
    ## calculation with ALGO=Exact and LOPTICS=.TRUE.
    ## and a reasonable number of virtual states (see above)
    ALGO = GW0 ; LSPECTRAL = .TRUE. ; NOMEGA = 50
    #LRPA = .FALSE. 
    ## be sure to take the same number of bands as for
    ## the LOPTICS=.TRUE. calculation, otherwise the
    ## WAVEDER file is not read correctly
    NBANDS = 64
    ##VASP2WANNIER90
    LWANNIER90=.TRUE.

Use the wannier90.win file given below which contains all instructions
needed to generate the necessary input files for the WANNIER90 runs
(wannier90.amn, wannier90.mmn, wannier90.eig).

- wannier90.win

&nbsp;

    num_wann=8
    num_bands=8

    exclude_bands = 9-64

    Begin Projections
    Si:sp3
    End Projections

    dis_froz_max=9
    dis_num_iter=1000

    guiding_centres=true

    # Bandstructure plot 
    #restart         =  plot
    #bands_plot      =  true
    #begin kpoint_path
    #L 0.50000  0.50000 0.5000 G 0.00000  0.00000 0.0000
    #G 0.00000  0.00000 0.0000 X 0.50000  0.00000 0.5000
    #X 0.50000  0.00000 0.5000 K 0.37500 -0.37500 0.0000
    #K 0.37500 -0.37500 0.0000 G 0.00000  0.00000 0.0000
    #end kpoint_path
    #bands_num_points 40
    #bands_plot_format gnuplot xmgrace

    begin unit_cell_cart
         2.7150000     2.7150000     0.0000000
         0.0000000     2.7150000     2.7150000
         2.7150000     0.0000000     2.7150000
    end unit_cell_cart

    begin atoms_cart
    Si       0.0000000     0.0000000     0.0000000
    Si       1.3575000     1.3575000     1.3575000
    end atoms_cart

    mp_grid =     4     4     4

    begin kpoints
         0.0000000     0.0000000     0.0000000
         0.2500000     0.0000000     0.0000000
         0.5000000     0.0000000     0.0000000
         0.2500000     0.2500000     0.0000000
         0.5000000     0.2500000     0.0000000
        -0.2500000     0.2500000     0.0000000
         0.5000000     0.5000000     0.0000000
        -0.2500000     0.5000000     0.2500000
         0.0000000     0.2500000     0.0000000
         0.0000000     0.0000000     0.2500000
        -0.2500000    -0.2500000    -0.2500000
        -0.2500000     0.0000000     0.0000000
         0.0000000    -0.2500000     0.0000000
         0.0000000     0.0000000    -0.2500000
         0.2500000     0.2500000     0.2500000
         0.0000000     0.5000000     0.0000000
         0.0000000     0.0000000     0.5000000
        -0.5000000    -0.5000000    -0.5000000
         0.0000000     0.2500000     0.2500000
         0.2500000     0.0000000     0.2500000
        -0.2500000    -0.2500000     0.0000000
        -0.2500000     0.0000000    -0.2500000
         0.0000000    -0.2500000    -0.2500000
         0.0000000     0.5000000     0.2500000
         0.2500000     0.0000000     0.5000000
        -0.2500000    -0.2500000     0.2500000
        -0.5000000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.0000000
         0.2500000    -0.2500000    -0.2500000
        -0.5000000    -0.5000000    -0.2500000
         0.0000000     0.2500000     0.5000000
        -0.2500000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.5000000
         0.5000000     0.0000000     0.2500000
        -0.5000000    -0.2500000     0.0000000
         0.0000000    -0.5000000    -0.2500000
        -0.2500000     0.0000000    -0.5000000
         0.2500000     0.2500000    -0.2500000
         0.5000000     0.2500000     0.5000000
        -0.2500000    -0.5000000     0.0000000
        -0.2500000     0.2500000     0.2500000
         0.5000000     0.5000000     0.2500000
         0.0000000    -0.2500000    -0.5000000
         0.2500000    -0.2500000     0.2500000
         0.2500000     0.5000000     0.5000000
        -0.5000000     0.0000000    -0.2500000
         0.0000000    -0.2500000     0.2500000
         0.2500000     0.0000000    -0.2500000
        -0.2500000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.2500000
         0.2500000    -0.2500000     0.0000000
        -0.5000000    -0.2500000    -0.2500000
         0.2500000     0.2500000     0.5000000
         0.0000000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.2500000
         0.5000000     0.2500000     0.2500000
        -0.2500000     0.0000000     0.2500000
         0.0000000     0.5000000     0.5000000
         0.5000000     0.0000000     0.5000000
         0.2500000    -0.2500000     0.5000000
         0.5000000     0.2500000    -0.2500000
        -0.5000000    -0.2500000    -0.7500000
         0.2500000    -0.5000000    -0.2500000
        -0.2500000     0.2500000    -0.5000000
    end kpoints

## Step 4: WANNIER90
### Compute Wannier functions
run wannier90:

wannier90.x wannier90

This run generates the wannier90 standard output (wannier90.wout) and
the file wannier90.chk needed for the wannier interpolation (next step)

### Obtain bandstructure (Wannier interpolation)
Uncomment the bandstructure plot flags in wannier90.win and rerun
(restart) wannier90:

wannier90.x wannier90

This run generates the following bandstructure files which can be
visualized using xmgrace or gnuplot:

wannier90_band.agr

wannier90_band.dat

wannier90_band.gnu

to plot the band structure using gnuplot:
`gnuplot -persist wannier90_band.gnu`

## Download
[Si_bandstructure_GW.tgz](https://vasp.at/wiki/images/e/ea/Si_bandstructure_GW.tgz "Si bandstructure GW.tgz")

[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> bandstructure of
Si in GW (VASP2WANNIER90) \> [bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of SrVO3](CRPA_of_SrVO3.md)  \>
[Equilibrium volume of Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).
