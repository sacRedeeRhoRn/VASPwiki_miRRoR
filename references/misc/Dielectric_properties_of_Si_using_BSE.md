<!-- Source: https://vasp.at/wiki/index.php/Dielectric_properties_of_Si_using_BSE | revid: 10417 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Dielectric properties of Si using BSE
[Overview](../tutorials/BSE_-_Tutorial.md) \> Dielectric
properties of Si using BSE \> [Improving the dielectric
function](Improving_the_dielectric_function.md)
 \> [Plotting the BSE fatband structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
  - [3.1 Step 1: DFT groundstate
    calculation](#Step_1:_DFT_groundstate_calculation)
  - [3.2 Step 2: Obtain DFT "virtual" orbitals (empty
    states)](#Step_2:_Obtain_DFT_%22virtual%22_orbitals_(empty_states))
  - [3.3 Step 3: RPA quasiparticles with single-shot GW
    (G0W0)](#Step_3:_RPA_quasiparticles_with_single-shot_GW_(G0W0))
  - [3.4 Step 4 (optional): Plot IPA dielectric function using GW0
    quasiparticle
    energies](#Step_4_(optional):_Plot_IPA_dielectric_function_using_GW0_quasiparticle_energies)
  - [3.5 Step 5: The BSE calculation](#Step_5:_The_BSE_calculation)
- [4 Download](#Download)

## Task
Description: Calculate the dielectric function of Si including excitonic
effects by solving the Bethe-Salpeter equation (BSE) on top of GW0.

## Input
### [POSCAR](../input-files/POSCAR.md)
    Si
     5.4300
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00 
    0.25 0.25 0.25 

### [INCAR](../input-files/INCAR.md)
- This is the [INCAR](../input-files/INCAR.md) file for the basic DFT
  calculation:

&nbsp;

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2
    EDIFF = 1.E-8

### [KPOINTS](../input-files/KPOINTS.md)
    Automatic
     0
    Gamma
     6 6 6 
     0 0 0

## Calculation
- The workflow of GW0+BSE calculations is given in doall.sh and consists
  of the following consecutive steps:

1.  "Standard" DFT groundstate calculation.
2.  Obtain virtual orbitals: needs [WAVECAR](../input-files/WAVECAR.md)
    file from step 1.
3.  The GW0 calculation: need [WAVECAR](../input-files/WAVECAR.md) and
    [WAVEDER](../input-files/WAVEDER.md) from step 2.
4.  Optional step: use [LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* to
    plot dielectric function in the independent particle approximation
    (IPA) using GW0 quasiparticle energies instead of DFT energies.
5.  The BSE calculation: needs [WAVECAR](../input-files/WAVECAR.md) from
    step 3 and [WAVEDER](../input-files/WAVEDER.md) from step 2.

### Step 1: DFT groundstate calculation
- We perform standard DFT calculation using the INCAR.DFT file.

### Step 2: Obtain DFT "virtual" orbitals (empty states)
- This step uses the INCAR.DIAG file:

&nbsp;

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ALGO = EXACT ; NELM = 1
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2
    NBANDS = 128
    LOPTICS = .TRUE. ; LPEAD = .TRUE.
    OMEGAMAX = 40

- We use exact diagonalization for this step
  ([ALGO](../incar-tags/ALGO.md)=*EXACT*) and keep 128 bands after
  diagonalization ([NBANDS](../incar-tags/NBANDS.md)=128).
- With [LPEAD](../incar-tags/LPEAD.md)=*.TRUE.* we use an alternative way
  of computing the derivates of the orbitals with respect to the Bloch
  wave vectors.
- It is important that this calculations needs the orbitals
  ([WAVECAR](../input-files/WAVECAR.md) file) written in step 1.

### Step 3: RPA quasiparticles with single-shot GW (G0W0)
- This step uses the INCAR.GW0 file:

&nbsp;

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ALGO = GW0  
    ISMEAR = 0 ; SIGMA = 0.01 
    ENCUTGW = 150 ; NELM = 1 ;  NOMEGA =  50 ;  OMEGATL = 280
    KPAR = 2
    #NBANDSO=4 ; NBANDSV=8 ; LADDER=.TRUE. ; LUSEW=.TRUE.
    NBANDS = 128
    NBANDSGW = 12
    LWAVE = .TRUE.
    PRECFOCK = Normal

- We select the G0W0 method by specifying
  [ALGO](../incar-tags/ALGO.md)=*GW0* and [NELM](../incar-tags/NELM.md)=1.
- The energy cut off for the response function is select by
  [ENCUTGW](../incar-tags/ENCUTGW.md).
- The number of point used in the frequency integration is given by
  [NOMEGA](../incar-tags/NOMEGA.md).
- Use the same number of bands ([NBANDS](../incar-tags/NBANDS.md)) as in
  step 2, otherwise the [WAVEDER](../input-files/WAVEDER.md) file is not
  read correctly.
- The quasiparticle energies are calculated for the first few bands
  given by [NBANDSGW](../incar-tags/NBANDSGW.md).
- It is important that this calculation needs the orbitals
  ([WAVECAR](../input-files/WAVECAR.md) file) and the derivatives of the
  orbitals with respect to the Bloch vectors
  ([WAVEDER](../input-files/WAVEDER.md) file).
- The quasiparticle energies can be found in the
  [OUTCAR](../output-files/OUTCAR.md) file (saved as OUTCAR.GW0 in this
  example):

&nbsp;

      QP shifts <psi_nk| G(iteration)W_0 |psi_nk>: iteration 1
    for sc-GW calculations column KS-energies equals QP-energies in previous step
    and V_xc(KS)=  KS-energies - (<T + V_ion + V_H > + <T+V_H+V_ion>^1  + <V_x>^1)
     
    k-point   1 :       0.0000    0.0000    0.0000
     band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation

### Step 4 (optional): Plot IPA dielectric function using GW0 quasiparticle energies
- This step uses the INCAR.NONE file:

&nbsp;

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ALGO = Nothing ; NELM = 1
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2
    NBANDS = 128
    LWAVE = .FALSE.
    LOPTICS = .TRUE. ; LPEAD = .TRUE.
    OMEGAMAX = 40  

- By specyfing [ALGO](../incar-tags/ALGO.md)=*Nothing* we do nothing except
  reading the [WAVECAR](../input-files/WAVECAR.md) file.
- Using [LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* and
  [LPEAD](../incar-tags/LPEAD.md)=*.TRUE.* we compute the dielectric
  function in the IPA.

### Step 5: The BSE calculation
- This step uses the INCAR.BSE file:

&nbsp;

    PREC = Normal ; ENCUT = 250.0
    ALGO = BSE 
    ANTIRES = 0
    ISMEAR = 0 ; SIGMA = 0.01
    ENCUTGW = 150
    EDIFF = 1.E-8
    NBANDS = 128
    NBANDSO = 4
    NBANDSV = 8
    OMEGAMAX = 20
    PRECFOCK = Normal

- By specifying [ANTIRES](../incar-tags/ANTIRES.md)=0 we use the
  Tamm-Dancoff approximation.
- [ENCUTGW](../incar-tags/ENCUTGW.md)=150 specifies the energy cut-off of
  the response function.
- [NBANDSO](../incar-tags/NBANDSO.md) and
  [NBANDSV](../incar-tags/NBANDSV.md) define the number of valence and
  conduction bands in the calculations.
- This calculation needs the orbitals
  ([WAVECAR](../input-files/WAVECAR.md) file) from step 3 and the
  derivative of the orbitals with respect to the Bloch vectors
  ([WAVEDER](../input-files/WAVEDER.md) file) written in step 2.
- By using the script ./plotall.sh we get the absorption spectra within
  the independent particle picture and with BSE:

[![](https://vasp.at/wiki/images/thumb/f/ff/Fig_BSE_example1_2.png/600px-Fig_BSE_example1_2.png)](https://vasp.at/wiki/File:Fig_BSE_example1_2.png)

- The calculated dielectric function of Si is at this point (GW+BSE)
  already in much better agreement with experiment. However we can do
  even better as shown in the following figure:

[![](https://vasp.at/wiki/images/thumb/9/98/Fig_BSE_example1_4.png/400px-Fig_BSE_example1_4.png)](https://vasp.at/wiki/File:Fig_BSE_example1_4.png)

- The problem comes from the coarse k-point grid that we have used. A
  denser grid samples more (direct) transitions between the bands.

[![](https://vasp.at/wiki/images/thumb/5/50/Fig_BSE_example1_3.png/200px-Fig_BSE_example1_3.png)](https://vasp.at/wiki/File:Fig_BSE_example1_3.png)

- Simply using a denser grid is mostly not an option because of the
  computational expense.

------------------------------------------------------------------------

## Download
[Si_BSE.tgz](https://vasp.at/wiki/images/a/a4/Si_BSE.tgz "Si BSE.tgz")

[Overview](../tutorials/BSE_-_Tutorial.md) \> Dielectric
properties of Si using BSE \> [Improving the dielectric
function](Improving_the_dielectric_function.md)
 \> [Plotting the BSE fatband structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)
