<!-- Source: https://vasp.at/wiki/index.php/Dielectric_properties_of_Si_using_BSE | revid: 10417 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Dielectric properties of Si using BSE



[Overview](../tutorials/BSE_-_Tutorial.md) \>
Dielectric properties of Si using
BSE \> [Improving the
dielectric
function](Improving_the_dielectric_function.md)
 \> [Plotting the BSE fatband
structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
  - [3.1 Step 1:
    DFT groundstate
    calculation](#step-1-dft-groundstate-calculation)
  - [3.2 Step 2:
    Obtain DFT "virtual" orbitals (empty
    states)](#Step_2:_Obtain_DFT_%22virtual%22_orbitals_(empty_states))
  - [3.3 Step 3:
    RPA quasiparticles with single-shot GW
    (G0W0)](#step-3-rpa-quasiparticles-with-single-shot-gw-g0w0))
  - [3.4 Step 4
    (optional): Plot IPA dielectric function using GW0 quasiparticle
    energies](#Step_4_(optional):_Plot_IPA_dielectric_function_using_GW0_quasiparticle_energies)
  - [3.5 Step 5:
    The BSE calculation](#step-5-the-bse-calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Description: Calculate the dielectric function of Si including excitonic
effects by solving the Bethe-Salpeter equation (BSE) on top of GW0.

## Input\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    Si
     5.4300
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00 
    0.25 0.25 0.25 

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

- This is the [INCAR](../input-files/INCAR.md) file for the basic DFT
  calculation:

<!-- -->

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2
    EDIFF = 1.E-8

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Automatic
     0
    Gamma
     6 6 6 
     0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

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

### Step 1: DFT groundstate calculation\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: DFT groundstate calculation">edit</a> \| (./index.php.md)\]

- We perform standard DFT calculation using the INCAR.DFT file.

### Step 2: Obtain DFT "virtual" orbitals (empty states)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Obtain DFT &quot;virtual&quot; orbitals (empty states)">edit</a> \| (./index.php.md)")\]

- This step uses the INCAR.DIAG file:

<!-- -->

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

### Step 3: RPA quasiparticles with single-shot GW (G0W0)\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: RPA quasiparticles with single-shot GW (G0W0)">edit</a> \| (./index.php.md)")\]

- This step uses the INCAR.GW0 file:

<!-- -->

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

<!-- -->

      QP shifts <psi_nk| G(iteration)W_0 |psi_nk>: iteration 1
    for sc-GW calculations column KS-energies equals QP-energies in previous step
    and V_xc(KS)=  KS-energies - (<T + V_ion + V_H > + <T+V_H+V_ion>^1  + <V_x>^1)
     
    k-point   1 :       0.0000    0.0000    0.0000
     band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation

### Step 4 (optional): Plot IPA dielectric function using GW0 quasiparticle energies\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Step 4 (optional): Plot IPA dielectric function using GW0 quasiparticle energies">edit</a> \| (./index.php.md): Plot IPA dielectric function using GW0 quasiparticle energies")\]

- This step uses the INCAR.NONE file:

<!-- -->

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

### Step 5: The BSE calculation\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: The BSE calculation">edit</a> \| (./index.php.md)\]

- This step uses the INCAR.BSE file:

<!-- -->

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

<a href="/wiki/File:Fig_BSE_example1_2.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/ff/Fig_BSE_example1_2.png/600px-Fig_BSE_example1_2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/f/ff/Fig_BSE_example1_2.png 1.5x" width="600"
height="358" /></a>

- The calculated dielectric function of Si is at this point (GW+BSE)
  already in much better agreement with experiment. However we can do
  even better as shown in the following figure:

<a href="/wiki/File:Fig_BSE_example1_4.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/9/98/Fig_BSE_example1_4.png/400px-Fig_BSE_example1_4.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/9/98/Fig_BSE_example1_4.png 1.5x" width="400"
height="290" /></a>

- The problem comes from the coarse k-point grid that we have used. A
  denser grid samples more (direct) transitions between the bands.

<a href="/wiki/File:Fig_BSE_example1_3.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/50/Fig_BSE_example1_3.png/200px-Fig_BSE_example1_3.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/50/Fig_BSE_example1_3.png/300px-Fig_BSE_example1_3.png 1.5x, /wiki/images/5/50/Fig_BSE_example1_3.png 2x"
width="200" height="277" /></a>

- Simply using a denser grid is mostly not an option because of the
  computational expense.

------------------------------------------------------------------------

## Download\[<a
href="/wiki/index.php?title=Dielectric_properties_of_Si_using_BSE&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/a/a4/Si_BSE.tgz" class="internal"
title="Si BSE.tgz">Si_BSE.tgz</a>


[Overview](../tutorials/BSE_-_Tutorial.md) \>
Dielectric properties of Si using
BSE \> [Improving the
dielectric
function](Improving_the_dielectric_function.md)
 \> [Plotting the BSE fatband
structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


