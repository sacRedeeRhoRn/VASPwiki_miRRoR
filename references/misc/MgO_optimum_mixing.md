<!-- Source: https://vasp.at/wiki/index.php/MgO_optimum_mixing | revid: 14728 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MgO optimum mixing



[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
MgO optimum
mixing \> [fcc Ni DOS
with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
[Si bandstructure](Si_bandstructure.md)
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
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Find optimum HSE mixing parameter for MgO.

## Input\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    MgO
    -18.79350000000000000000
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    1 1
    cart
    0.00 0.00 0.00
    0.50 0.0 0.0

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    ##############################################
    ## Optimum HSE mixing parameter (AEXX) for MgO
    ## Expt gap = 7.8 eV
    ## fit gap wrt. 0<AEXX<1
    ## Compute the bandgap using different value of AEXX 
    ## in the range (0,1) and find the value which leads 
    ## to the best agreement with the experimental gap. 
    ## hint: the gap grows lineraly with AEXX
    ## Better preconverge with PBE first!
    ##############################################
        
    ## Selects the HSE06 hybrid functional
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX=0.25  
    #ALGO = D ; TIME = 0.4 
         
    ## Leave this in
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Gamma
      4  4  4
      0  0  0

## Calculation\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- script to extract G-eigenvalues and calculate the bandgap

<!-- -->

    grep "      4     " OUTCAR | head -8 | \
    awk 'BEGIN{i=1}{a[i]=$2 ; i=2} END{for (j=1;j<i;j++) print j,a[j]}' > vband.dat
    grep "      5     " OUTCAR | head -8 | \
    awk 'BEGIN{i=1}{a[i]=$2 ; i=2} END{for (j=1;j<i;j++) print j,a[j]}' > cband.dat

The bandgap is obainted by substracting the eigenvalues written in
cband.dat (conduction band minimum at Gamma) and vband.dat (valence band
maximum at Gamma)

## Download\[<a
href="/wiki/index.php?title=MgO_optimum_mixing&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/6/6b/5_2_MgO_mixing.tgz" class="internal"
title="5 2 MgO mixing.tgz">5_2_MgO_mixing.tgz</a>


[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
MgO optimum
mixing \> [fcc Ni DOS
with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
[Si bandstructure](Si_bandstructure.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


