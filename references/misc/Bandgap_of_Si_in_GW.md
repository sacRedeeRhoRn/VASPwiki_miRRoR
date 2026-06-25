<!-- Source: https://vasp.at/wiki/index.php/Bandgap_of_Si_in_GW | revid: 24917 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandgap of Si in GW



[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
bandgap of Si in
GW \> [bandstructure of
Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of
SrVO3](CRPA_of_SrVO3.md)
 \> [Equilibrium volume of Si
in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2 Step 1: DFT
  groundstate calculation](#step-1-dft-groundstate-calculation)
- [3 Step 2: obtain
  DFT virtual orbitals](#step-2-obtain-dft-virtual-orbitals)
- [4 Step 3: the
  actual GW calculation](#step-3-the-actual-gw-calculation)
  - [4.1 Beyond the
    random-phase-approximation](#beyond-the-random-phase-approximation)
  - [4.2 Beyond
    G<sub>0</sub>W<sub>0</sub>:
    GW<sub>0</sub>](#Beyond_G0W0:_GW0)
- [5
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the bandgap of Si using various flavours of GW.

------------------------------------------------------------------------

**Mind**: before you start doing GW calculations it might be beneficial
to have a look at the examples on the [description of dielectric
properties](Dielectric_properties_of_Si.md).

------------------------------------------------------------------------

To do GW calculations we have to follow a 3-step procedure.

## Step 1: DFT groundstate calculation\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: DFT groundstate calculation">edit</a> \| (./index.php.md)\]

Everything starts with a standard DFT groundstate calculation (in this
case PBE).

- [INCAR](../input-files/INCAR.md) (see INCAR.DFT)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.05
    EDIFF  = 1E-8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.6)

<!-- -->

    6x6x6
     0
    G
     6 6 6
     0 0 0

or to save some time use a "quick-and-dirty" setup (take KPOINTS.4):

    4x4x4
     0
    G
     4 4 4
     0 0 0

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    system Si
    5.430
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00
    0.25 0.25 0.25

## Step 2: obtain DFT virtual orbitals\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: obtain DFT virtual orbitals">edit</a> \| (./index.php.md)\]

To obtain a [WAVECAR](../input-files/WAVECAR.md) file with a reasonable
number of virtual orbitals (50-100 per atom) we need to restart from the
previous groundstate calculation with [ALGO](../incar-tags/ALGO.md)=*Exact*,
and manually set the number of bands by means of the
[NBANDS](../incar-tags/NBANDS.md)-tag. To obtain the corresponding
[WAVEDER](../input-files/WAVEDER.md) file we additionally specify
[LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.*.

- [INCAR](../input-files/INCAR.md) (see INCAR.DIAG)

<!-- -->

    ALGO = Exact
    NBANDS  = 64
    LOPTICS = .TRUE. ; CSHIFT = 0.1
    NEDOS = 2000
    # you might try
    #LPEAD = .TRUE.
       
    ISMEAR =  0
    SIGMA  =  0.05
    EDIFF  = 1E-8

  
**Mind**: make a copy of your [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files, as we will repeatedly need
them in the following. For instance

    cp WAVECAR WAVECAR.DIAG
    cp WAVEDER WAVEDER.DIAG

## Step 3: the actual GW calculation\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: the actual GW calculation">edit</a> \| (./index.php.md)\]

Restart from the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files of the previous calculation,
with

- [INCAR](../input-files/INCAR.md) (see INCAR.GW)

<!-- -->

    # Frequency dependent dielectric tensor including
    # local field effects within the RPA (default) or
    # including changes in the DFT xc-potential (LRPA=.FALSE.).
    # N.B.: beware one first has to have done a
    # calculation with ALGO=Exact, LOPTICS=.TRUE.
    # and a reasonable number of virtual states (see above)
    ALGO = GW0 ; LSPECTRAL = .TRUE. ; NOMEGA = 50
       
    # be sure to take the same number of bands as for
    # the LOPTICS=.TRUE. calculation, otherwise the
    # WAVEDER file is not read correctly
    NBANDS = 64
         
    # Add this to update the quasiparticle energies
    # in the Green's function (GW0)
    #NELM = 4
        
    ISMEAR =  0
    SIGMA  =  0.05
    EDIFF  = 1E-8

  
At the bottom of the [OUTCAR](../output-files/OUTCAR.md) file you will find
the quasi-particle (QP) energies.

     QP shifts <psi_nk| G(iteration)W_0 |psi_nk>: iteration 1
     for sc-GW calculations column KS-energies equals QP-energies in previous step
     and V_xc(KS)=  KS-energies - (<T + V_ion + V_H > + <T+V_H+V_ion>^1  + <V_x>^1)

     k-point   1 :       0.0000    0.0000    0.0000
      band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation

          1      -6.4888      -6.8243     -10.9766     -10.4570     -17.5189       0.6458       2.0000
          2       5.4800       5.1162     -11.8859     -11.4060     -12.7290       0.7580       2.0000
          3       5.4800       5.1162     -11.8859     -11.4060     -12.7290       0.7580       2.0000
          4       5.4800       5.1162     -11.8859     -11.4060     -12.7290       0.7580       2.0000
          5       8.0443       8.3296      -9.7235     -10.1038      -5.7364       0.7502       0.0000
          6       8.0443       8.3296      -9.7235     -10.1038      -5.7364       0.7502       0.0000
          7       8.0443       8.3296      -9.7235     -10.1038      -5.7364       0.7502       0.0000
          8       8.8407       9.2475     -10.5130     -11.0594      -6.0662       0.7445       0.0000

     k-point   2 :       0.1667    0.0000    0.0000
      band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation

          1      -6.1276      -6.4734     -11.0208     -10.4905     -17.3978       0.6521       2.0000
          2       3.0946       2.6991     -11.4452     -10.9063     -13.1354       0.7340       2.0000
          3       5.0279       4.6595     -11.7159     -11.2282     -12.6625       0.7552       2.0000
          4       5.0279       4.6595     -11.7159     -11.2282     -12.6625       0.7552       2.0000
          5       7.8309       8.1065      -9.8441     -10.2097      -5.8680       0.7539       0.0000
          6       8.6943       8.9816      -9.8669     -10.2533      -5.6768       0.7436       0.0000
          7       8.6943       8.9816      -9.8669     -10.2533      -5.6768       0.7436       0.0000
          8      10.9341      11.2678     -10.4716     -10.9278      -5.5632       0.7316       0.0000

         ..         ..           ..           ..           ..           ..           ..           .. 
         ..         ..           ..           ..           ..           ..           ..           .. 
         ..         ..           ..           ..           ..           ..           ..           .. 
         ..         ..           ..           ..           ..           ..           ..           .. 


     k-point  16 :      -0.3333    0.5000    0.1667
      band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation

          1      -2.2240      -2.5911     -11.4857     -10.9550     -16.0663       0.6917       2.0000
          2      -2.2240      -2.5911     -11.4857     -10.9550     -16.0663       0.6917       2.0000
          3       1.8279       1.3698     -10.7735     -10.1380     -12.9637       0.7209       2.0000
          4       1.8279       1.3698     -10.7735     -10.1380     -12.9637       0.7209       2.0000
          5       8.2346       8.4128      -9.3111      -9.5472      -5.1975       0.7546       0.0000
          6       8.2346       8.4128      -9.3111      -9.5472      -5.1975       0.7546       0.0000
          7      12.2605      12.5170      -9.7969     -10.1486      -4.3607       0.7294       0.0000
          8      12.2605      12.5170      -9.7969     -10.1486      -4.3607       0.7294       0.0000

  
To quickly find the QP-energy of the highest lying occupied state, try

    ./gap_GW.sh OUTCAR

### Beyond the random-phase-approximation\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Beyond the random-phase-approximation">edit</a> \| (./index.php.md)\]

To include local field effects beyond the random-phase-approximation in
the description of the frequency dependent dielectric response function
(local field effects in DFT) add the following line to your
[INCAR](../input-files/INCAR.md) file:

    LRPA = .FALSE.

and again restart from the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files from step 2.

### Beyond G<sub>0</sub>W<sub>0</sub>: GW<sub>0</sub>\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Beyond G0W0: GW0">edit</a> \| (./index.php.md)\]

The most usual step beyond single-shot GW (G<sub>0</sub>W<sub>0</sub>)
is to iterate the quasi-particle energies in the Greens functions. This
is the socalled GW<sub>0</sub> approximation. To have VASP do, for
instance, 4 iterations of the QP-energies in G, add the following line
to the [INCAR](../input-files/INCAR.md) file:

    NELM = 4

and again restart from the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files from step 2.

To quickly find the QP-energy of the highest lying occupied state after
4 iterations of the QP energies in G, type:

    ./gap_GW.sh OUTCAR

## Download\[<a
href="/wiki/index.php?title=Bandgap_of_Si_in_GW&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/d/d5/Si_GW_gap.tgz" class="internal"
title="Si GW gap.tgz">Si_GW_gap.tgz</a>


[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
bandgap of Si in
GW \> [bandstructure of
Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \> [CRPA of
SrVO3](CRPA_of_SrVO3.md)
 \> [Equilibrium volume of Si
in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).


