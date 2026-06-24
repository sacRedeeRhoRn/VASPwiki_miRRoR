<!-- Source: https://vasp.at/wiki/index.php/Bandstructure_of_SrVO3_in_GW | revid: 25105 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandstructure of SrVO3 in GW
[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> [bandstructure
of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
bandstructure of SrVO3 in GW  \> [CRPA of
SrVO3](CRPA_of_SrVO3.md)  \> [Equilibrium volume of
Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 DFT groundstate calculation](#DFT_groundstate_calculation)
- [3 Obtain DFT virtual orbitals and long-wave
  limit](#Obtain_DFT_virtual_orbitals_and_long-wave_limit)
  - [3.1 The dielectric function](#The_dielectric_function)
- [4 GW Step](#GW_Step)
- [5 HSE hybrid functional](#HSE_hybrid_functional)
- [6 Post-processing: Density of states and Bandstructure for PBE, GW
  and
  HSE](#Post-processing:_Density_of_states_and_Bandstructure_for_PBE,_GW_and_HSE)
  - [6.1 Density of States](#Density_of_States)
  - [6.2 Bandstructure with wannier90](#Bandstructure_with_wannier90)
  - [6.3 The preferred way to calculate the PBE
    bandstructure](#The_preferred_way_to_calculate_the_PBE_bandstructure)
- [7 Download](#Download)

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

The [POSCAR](../input-files/POSCAR.md) can be visualized with
[p4v](http://p4vasp.at) or
[VESTA](http://www.jp-minerals.org/vesta/en/download.html) and remains
unchanged in the following.

[![](https://vasp.at/wiki/images/thumb/0/0a/SrVO3_structure.png/340px-SrVO3_structure.png)](https://vasp.at/wiki/File:SrVO3_structure.png)

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

- [INCAR](../input-files/INCAR.md) (see INCAR.PBE)

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

    cp WAVECAR WAVECAR.PBE
    cp WAVEDER WAVEDER.PBE

Also make a backup of the charge density for later:

    cp CHGCAR CHGCAR.PBE

### The dielectric function
As a bonus, VASP determines the frequency dependent dielectric function
in the independent-particle (IP) picture and writes the result to the
[OUTCAR](../output-files/OUTCAR.md) and
[vasprun.xml](../output-files/Vasprun.xml.md) files. In the
[OUTCAR](../output-files/OUTCAR.md) you should search for

     frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects)

and

     frequency dependent      REAL DIELECTRIC FUNCTION (independent particle, no local field effects)

## GW Step
The actual GW calculation requires a set of one-electron energies and
eigenstates. In this case we use the PBE solution obtained from previous
step:

    cp WAVECAR.PBE WAVECAR
    cp WAVEDER.PBE WAVEDER

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

## HSE hybrid functional
To illustrate the kind of results one would obtain for SrVO₃ using the
[DFT/Hartree-Fock hybrid
functional](../methods/Category-Hybrid_functionals.md)
HSE, without actually doing a full self-consistent calculation, we will
recalculate the one-electron energies and DOS
([ALGO](../incar-tags/ALGO.md)=Eigenval) using the HSE functional with DFT
orbitals as input

    cp WAVECAR.PBE WAVECAR

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

    cp WAVECAR.PBE WAVECAR

or

    cp WAVECAR.GW0 WAVECAR

or

    cp WAVECAR.HSE WAVECAR

and restart VASP. The density of states is written to
[DOSCAR](../output-files/DOSCAR.md), make a copy of this file

    cp DOSCAR DOSCAR.XXX

where XXX is either PBE, GW0 or HSE. Visualize the projected DOS for the
V-t2g, V-eg and O-p states with the scriptfile

    ./plotdos_comp.sh DOSCAR.???

This requires gnuplot to be installed.

[![](https://vasp.at/wiki/images/thumb/3/3a/DOS_SrVO3_comparison.png/480px-DOS_SrVO3_comparison.png)](https://vasp.at/wiki/File:DOS_SrVO3_comparison.png)

### Bandstructure with `wannier90`
The bandstructure can be calculated via Wannier interpolation using
`wannier90` in the library mode

- [INCAR](../input-files/INCAR.md) (see INCAR.WAN.XXX)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    ALGO = NONE                            # no electronic changes required
    NELM = 1                               # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 48                            # number of bands used
    LWAVE = .FALSE.                        # do not overwrite WAVECAR
    LCHARG = .FALSE.                       # do not overwrite CHGCAR
    LWANNIER90_RUN = .TRUE.                # run wannier90 in library mode

    # As of vasp-6.4.3 define wannier90 interpolation from INCAR as follows:
    # For older versions copy wannier90.win.XXX to wannier90.win and use INCAR.WAN as input for vasp
    NUM_WANN = 3
    WANNIER90_WIN = "

    # use this energy window for t2g states for GW
    dis_win_min = 7.4
    dis_win_max = 9.95

    begin projections
    V:dxy;dxz;dyz
    end projections

    # plot bands
    bands_plot = true

    begin kpoint_path
    R  0.50000000  0.50000000  0.50000000  G  0.00000000  0.00000000  0.00000000
    G  0.00000000  0.00000000  0.00000000  X  0.50000000  0.00000000  0.00000000
    X  0.50000000  0.00000000  0.00000000  M  0.50000000  0.50000000  0.00000000
    M  0.50000000  0.50000000  0.00000000  G  0.00000000  0.00000000  0.00000000
    end kpoint_path
    "

  

|  |
|----|
| **Mind:** Prior VASP.6.4.3 a proper wannier90.win.XXX file should be used instead. |

Use the corresponding INCAR.WAN.XXX file as input for `wannier90`

    cp INCAR.WAN.XXX INCAR

where XXX=PBE, GW0 or HSE.

Use the corresponding WAVECAR.XXX file as input

    cp WAVECAR.XXX WAVECAR

and restart VASP. If all went well, the Vanadium t2g band dispersion
thus obtained, may conveniently be visualized with gnuplot:

    gnuplot -persist ./wannier90_band.gnu

**N.B.:** Most modern versions of `gnuplot` will respond with an error
message unless you remove the first line of `wannier90_band.gnu` (some
deprecated syntax issue).

### The preferred way to calculate the PBE bandstructure
Provided one has a self-consistent charge density
([CHGCAR](../input-files/CHGCAR.md)) file of sufficient quality (generated
using a regular grid of k-points of sufficient density) one may read
this charge density and keep it fixed
([ICHARG](../incar-tags/ICHARG.md)=11). For density functional
calculations this charge density completely defines the Hamiltonian and
using this Hamiltonian one may non-selfconsistently determine the
orbitals and corresponding eigenenergies at arbitrary k-points. This is
a very convenient way to calculate the bandstructure.

First we copy the self-consistent charge density of one of our previous
calculations:

     cp CHGCAR.PBE CHGCAR
     cp WAVECAR.PBE WAVECAR

The bandstructure is conventionally plotted along lines of high symmetry
in the 1st Brillouin zone. The easiest way to specify these is by means
of the so-called *linemode*:

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

**N.B.:** using these *k*-points for a *self-consistent* calculation
([ICHARG](../incar-tags/ICHARG.md)\<10) would be a very bad idea since
such and irregular sampling of the 1st Brillouin zone will not yield
sensible charge densities.

Use the following [INCAR](../input-files/INCAR.md) file:

- [INCAR](../input-files/INCAR.md) (see INCAR.BSTR)

&nbsp;

    SYSTEM = SrVO3                         # system name
    ISMEAR = 0                             # Gaussian smearing
    EDIFF = 1E-7                           # tight convergence criterion
    NBANDS = 36                            # 36 bands are sufficient
    LWAVE = .FALSE.                        # do not overwrite WAVECAR
    LCHARG = .FALSE.                       # do not overwrite CHGCAR
    ICHARG = 11                            # read the charge density from the CHGCAR file and keep it fixed
    LORBIT = 11                            # compute lm-decomposed states
    EMIN = -20 ; EMAX = 20                 # smallest/largest energy included in calculation
    NEDOS = 1000                           # sampling points for DOS

**N.B.:** Mind that this approach works only for density functional
calculations (*e.g.* PBE or LDA) and is not applicable to orbital
dependent functionals (like hybrid functionals) or in case of GW
calculations.

This PBE bandstructure and the Wannier-interpolated structures of the
PBE, HSE and GW calculation can be compared via

    ./plotbands.sh

[![](https://vasp.at/wiki/images/thumb/0/01/SrVO3_bandstructure.png/600px-SrVO3_bandstructure.png)](https://vasp.at/wiki/File:SrVO3_bandstructure.png)

## Download
[SrVO3_GW_band.zip](https://vasp.at/wiki/images/9/91/SrVO3_GW_band.zip "SrVO3 GW band.zip")

[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \> [bandstructure
of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
bandstructure of SrVO3 in GW  \> [CRPA of
SrVO3](CRPA_of_SrVO3.md)  \> [Equilibrium volume of
Si in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

Back to the [main page](The_VASP_Manual.md).
