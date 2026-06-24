<!-- Source: https://vasp.at/wiki/index.php/Bandstructure_and_CRPA_of_SrVO3 | revid: 36493 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandstructure and CRPA of SrVO3
[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> [bandstructure
of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of SrVO3](CRPA_of_SrVO3.md)  \>
[Equilibrium volume of Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 DFT groundstate calculation](#DFT_groundstate_calculation)
- [3 Obtain DFT virtual orbitals and long-wave
  limit](#Obtain_DFT_virtual_orbitals_and_long-wave_limit)
  - [3.1 The dielectric function](#The_dielectric_function)
- [4 GW Step](#GW_Step)
  - [4.1 The dielectric function](#The_dielectric_function_2)
- [5 HSE hybrid functional](#HSE_hybrid_functional)
- [6 Post-processing: Density of states and Bandstructure for PBE, GW
  and
  HSE](#Post-processing:_Density_of_states_and_Bandstructure_for_PBE,_GW_and_HSE)
  - [6.1 Density of States](#Density_of_States)
  - [6.2 Bandstructure with wannier90](#Bandstructure_with_wannier90)
  - [6.3 Alternative way to calculate the PBE
    bandstructure](#Alternative_way_to_calculate_the_PBE_bandstructure)

## Task
Calculation of the GW bandstructure of SrVO₃ using VASP and
[WANNIER90](http://www.wannier.org).

------------------------------------------------------------------------

Performing a GW calculation with VASP is a 3-step procedure: a DFT
groundstate calculation, a calculation to obtain a number of virtual
orbitals, and the actual GW calculation itself. In this example we will
also see how the results of the GW calculation may be postprocessed with
[WANNIER90](http://www.wannier.org) to obtain the dispersion of the
bands along the usual high symmetry directions in reciprocal space.

**N.B.:** This example involves quite a number of individual
calculations. The easiest way to run this example is to execute:

    ./doall.sh

And compare the output of the different steps (DFT, GW, HSE) by:

    ./plotall.sh

In any case, one can consider the `doall.sh` script to be an overview of
the steps described below.

## DFT groundstate calculation
The first step is a conventional DFT (in this case PBE) groundstate
calculation.

- [INCAR](../input-files/INCAR.md) (see INCAR.DFT)

&nbsp;

    SYSTEM  = SrVO3                        # system name
    NBANDS = 36                            # small number  of bands
    ISMEAR = 0                             # Gaussian smearing
    EDIFF = 1E-8                           # high precision for groundstate calculation
    KPAR = 2                               # parallelization of k-points in two groups

Copy the aforementioned file to [INCAR](../input-files/INCAR.md):

    cp INCAR.DFT INCAR

The [POSCAR](../input-files/POSCAR.md) file describes the structure of the
system:

- [POSCAR](../input-files/POSCAR.md)

&nbsp;

    SrVO3
    3.84652  #cubic fit for 6x6x6 k-points
     +1.0000000000  +0.0000000000  +0.0000000000 
     +0.0000000000  +1.0000000000  +0.0000000000 
     +0.0000000000  +0.0000000000  +1.0000000000 
    Sr V O
     1 1 3
    Direct
     +0.0000000000  +0.0000000000  +0.0000000000 
     +0.5000000000  +0.5000000000  +0.5000000000 
     +0.5000000000  +0.5000000000  +0.0000000000 
     +0.5000000000  +0.0000000000  +0.5000000000 
     +0.0000000000  +0.5000000000  +0.5000000000

This file remains unchanged in the following.

The [KPOINTS](../input-files/KPOINTS.md) file describes how the first
Brillouin zone is sampled. In the first step we use a uniform k-point
sampling:

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.BULK)

&nbsp;

    Automatically generated mesh
           0
    Gamma
     4 4 4
     0 0 0

**Mind**: this is definitely not dense enough for a high-quality
description of SrVO₃, but in the interest of speed we will live with it.
Copy the aforementioned file to [KPOINTS](../input-files/KPOINTS.md):

    cp KPOINTS.BULK KPOINTS

and run VASP. If all went well, one should obtain a
[WAVECAR](../input-files/WAVECAR.md) file containing the PBE wavefunction.

## Obtain DFT virtual orbitals and long-wave limit
Use following [INCAR](../input-files/INCAR.md) file to increase the number
of virtual states and to determine the long-wave limit of the
polarizability (stored in [WAVEDER](../input-files/WAVEDER.md)):

- [INCAR](../input-files/INCAR.md) (see INCAR.DIAG)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    KPAR = 2                               # parallelization of k-points in two groups
    ALGO = Exact                           # exact diagonalization
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 96                            # need for a lot of bands in GW
    LOPTICS = .TRUE.                       # we need d phi/ d k  for GW calculations for long-wave limit

Restart VASP. At this stage it is a good idea to make a safety copy of
the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files since we will repeatedly need
them in the calculations that follow:

    cp WAVECAR WAVECAR.DIAG
    cp WAVEDER WAVEDER.DIAG

Also make a backup of the charge density for later:

    cp CHGCAR CHGCAR.DIAG

### The dielectric function
As a bonus, VASP determines the frequency dependent dielectric function
in the independent-particle (IP) picture and writes the result to the
[OUTCAR](../output-files/OUTCAR.md) and
[vasprun.xml](../output-files/Vasprun.xml.md) files. In the
[OUTCAR](../output-files/OUTCAR.md) you should search for

     frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects)

and

     frequency dependent      REAL DIELECTRIC FUNCTION (independent particle, no local field effects)

To visualize the real and imaginary parts of the frequency dependent
dielectric function (from the
[vasprun.xml](../output-files/Vasprun.xml.md)) you may execute

    ./plotoptics2

## GW Step
The actual GW calculation requires a set of one-electron energies and
eigenstates. In this case we use the PBE solution obtained from previous
step:

    cp WAVECAR.DIAG WAVECAR
    cp WAVEDER.DIAG WAVEDER

The following [INCAR](../input-files/INCAR.md) file selects the 'single
shot' GW calculation also known as G₀W₀:

- [INCAR](../input-files/INCAR.md) (see INCAR.GW0)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    KPAR = 2                               # parallelization of k-points in two groups
    ALGO = GW0                             # GW with iteration in G, W kept on DFT level
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 96                            # need for a lot of bands in GW
    PRECFOCK = Fast                        # fast mode for FFTs
    ENCUTGW = 100                          # small energy cutoff for response function suffices for this tutorial
    NOMEGA = 200                           # large number of real frequency points for Hilbert transforms of W and self-energy

Restarting VASP will overwrite the present
[WAVECAR](../input-files/WAVECAR.md) and
[vasprun.xml](../output-files/Vasprun.xml.md) file. Make a copy them
for later.

    cp WAVECAR WAVECAR.GW0
    cp vasprun.xml vasprun.GW0.xml

### The dielectric function
To extract the frequency dependent dielectric constant, both in the
independent-particle picture as well as including local field effects
(either in DFT or in the RPA) and plot the real and imaginary components
using *gnuplot*, execute

    ./plotchi

## HSE hybrid functional
To illustrate the kind of results one would obtain for SrVO₃ using the
[DFT/Hartree-Fock hybrid functional
HSE](../methods/Category-Hybrid_functionals.md),
without actually doing a full self-consistent calculation, we will
recalculate the one-electron energies and DOS
([ALGO](../incar-tags/ALGO.md)=Eigenval) using the HSE functional with DFT
orbitals as input

    cp WAVECAR.DIAG WAVECAR

Use the following [INCAR](../input-files/INCAR.md) file:

- [INCAR](../input-files/INCAR.md) (see INCAR.HSE)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    KPAR = 2                               # parallelization of k-points in two groups
    ALGO = Eigenval                        # calulate eigenvalues
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 48                            # small number of bands suffice
    PRECFOCK = Fast                        # fast mode for FFTs
    LHFCALC = .TRUE.                       # switch on Hartree-Fock routines to calculate exact exchange
    HFSCREEN = 0.2                         # HSE06 screening parameter

Restart VASP and make a copy of the wavefunction for post-processing

    cp WAVECAR WAVECAR.HSE

## Post-processing: Density of states and Bandstructure for PBE, GW and HSE
### Density of States
The DOS of the PBE, GW and HSE solution can be calculated in a
post-processing step with

- [INCAR](../input-files/INCAR.md) (see INCAR.DOS)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = -5                            # Bloechl's tetrahedron method (requires at least 3x3x3 k-points)
    ALGO = NONE                            # no electronic changes required
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 48                            # number of bands used
    EMIN = -20 ; EMAX = 20                 # smallest/largest energy included in calculation
    NEDOS = 1000                           # sampling points for DOS
    LORBIT = 11                            # calculate l-m decomposed DOS
    LWAVE = .FALSE.                        # do not overwrite WAVECAR
    LCHARG = .FALSE.                       # do not overwrite CHGCAR

and requires the apropriate [WAVECAR](../input-files/WAVECAR.md) file from
one of the previous steps. Copy

    cp WAVECAR.DIAG WAVECAR

or

    cp WAVECAR.GW0 WAVECAR

or

    cp WAVECAR.HSE WAVECAR

and restart VASP. The density of states is written to
[DOSCAR](../output-files/DOSCAR.md), make a copy of this file

    cp DOSCAR DOSCAR.XXX

where XXX is either PBE, GW0 or HSE. Visualize the projected DOS for the
V-t2g, V-eg and O-p states with the scriptfile

    ./plotdos.sh DOSCAR.*

This requires gnuplot to be installed.

### Bandstructure with `wannier90`
The bandstructure can be calculated via Wannier interpolation using
`wannier90` in the library mode

- [INCAR](../input-files/INCAR.md) (see INCAR.WAN)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    ALGO = NONE                            # no electronic changes required
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 48                            # number of bands used
    LWAVE = .FALSE.                        # do not overwrite WAVECAR
    LCHARG = .FALSE.                       # do not overwrite CHGCAR
    LWANNIER90_RUN = .TRUE.                # run wannier90 in library mode

Use the corresponding wannier90.win.XXX file as input for `wannier90`

    cp wannier90.win.XXX wannier90.win

where XXX=PBE, GW0 or HSE and looks similar to

    bands_plot = true

    begin kpoint_path
    R  0.50000000  0.50000000  0.50000000  G  0.00000000  0.00000000  0.00000000
    G  0.00000000  0.00000000  0.00000000  X  0.50000000  0.00000000  0.00000000
    X  0.50000000  0.00000000  0.00000000  M  0.50000000  0.50000000  0.00000000
    M  0.50000000  0.50000000  0.00000000  G  0.00000000  0.00000000  0.00000000
    end kpoint_path

    # number of wannier states
    num_wann =    3

    # number of bloch bands
    num_bands=   96

    # GW energy window for t2g states
    dis_win_min = 7.4
    dis_win_max = 9.95

    begin projections
    V:dxy;dxz;dyz
    end projections

Use the corresponding WAVECAR.XXX file as input

    cp WAVECAR.XXX WAVECAR

and restart VASP. If all went well, the Vanadium t2g band dispersion
thus obtained, may conveniently be visualized with gnuplot:

    gnuplot -persist ./wannier90_band.gnu

**N.B.:** Most modern versions of `gnuplot` will respond with an error
message unless you remove the first line of `wannier90_band.gnu` (some
deprecated syntax issue).

### Alternative way to calculate the PBE bandstructure
VASP allows to interpolate the PBE bandstructure from the PBE charge
density

     cp CHGCAR.DIAG CHGCAR
     cp WAVECAR.DIAG WAVECAR

by adapting the [KPOINTS](../input-files/KPOINTS.md) file as follows:

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.BSTR)

&nbsp;

    Auto
    15
    Linemode
    reciprocal
    0.50000000  0.50000000  0.50000000   !R
    0.00000000  0.00000000  0.00000000   !G

    0.00000000  0.00000000  0.00000000   !G
    0.50000000  0.00000000  0.00000000   !X

    0.50000000  0.00000000  0.00000000   !X
    0.50000000  0.50000000  0.00000000   !M 

    0.50000000  0.50000000  0.00000000   !M
    0.00000000  0.00000000  0.00000000   !G

The following [INCAR](../input-files/INCAR.md) file tells VASP to
interpolate the bandstructure:

- [INCAR](../input-files/INCAR.md) (see INCAR.BSTR)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    EDIFF = 1E-7                           # tight convergence criterion
    NBANDS = 36                            # 36 bands are sufficient
    LWAVE = .FALSE.                        # do not overwrite WAVECAR
    LCHARG = .FALSE.                       # do not overwrite CHGCAR
    ICHARG = 11                            # use CHGCAR file for interpolation
    LORBIT = 11                            # compute lm-decomposed states
    EMIN = -20 ; EMAX = 20                 # smallest/largest energy included in calculation
    NEDOS = 1000                           # sampling points for DOS

This PBE bandstructure and the Wannier-interpolated structures of the
PBE, HSE and GW calculation can be compared via

    ./plotbands.sh

**N.B.:** Mind that this approach works only for DFT wavefunctions, like
PBE or LDA.

[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> [bandstructure
of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of SrVO3](CRPA_of_SrVO3.md)  \>
[Equilibrium volume of Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).
