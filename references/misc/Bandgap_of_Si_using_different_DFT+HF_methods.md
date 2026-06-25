<!-- Source: https://vasp.at/wiki/index.php/Bandgap_of_Si_using_different_DFT%2BHF_methods | revid: 15054 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Bandgap of Si using different DFT+HF methods



[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
bandgap of Si using different DFT+HF
methods \> [MgO optimum
mixing](MgO_optimum_mixing.md) \>
[fcc Ni DOS with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
[Si bandstructure](Si_bandstructure.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2
  Input](#Input)
  - [2.1
    POSCAR](#POSCAR)
  - [2.2
    INCAR](#INCAR)
  - [2.3
    KPOINTS](#KPOINTS)
  - [2.4
    Calculation](#Calculation)
- [3
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the band gap in Si using different DFT+HF schemes [(PBE,
B3LYP, PBE0, HSE06, and
HF)](../methods/List_of_hybrid_functionals.md).

## Input\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    System: Si                             
     5.430 
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1  
    Cartesian
    0    0    0
    0.25 0.25 0.25

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    ## Better preconverge with PBE first
    ## and use the WAVECAR file as inout for the DFT+HF calculation
       
    ## Selects the B3LYP hybrid functional
    #LHFCALC = .TRUE. ; GGA = B3 ; AEXX = 0.2 ; AGGAX = 0.72 
    #AGGAC = 0.81 ; ALDAC = 0.19
    #ALGO = D ; TIME = 0.4 
       
    ## Selects the PBE0  hybrid functional
    #LHFCALC = .TRUE. ; 
    #ALGO = D ; TIME = 0.4 
       
    ## Selects the HSE06 hybrid functional
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; 
    #ALGO = D ; TIME = 0.4 
       
    ## Selects HF 
    #LHFCALC = .TRUE. ; AEXX = 1.0 ; ALDAC = 0.0 ; AGGAC = 0
    #ALGO = D ; TIME = 0.4 
       
    ## Leave this in
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Gamma
      6  6  6
      0  0  0

### Calculation\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- script to extract eigenvalues and calculate the bandgap

<!-- -->

    homo=`awk '/NELECT/ {print $3/2}' $1`
    lumo=`awk '/NELECT/ {print $3/2+1}' $1`
    nkpt=`awk '/NKPTS/ {print $4}' $1`

    e1=`grep "     $homo     " $1 | head -$nkpt | sort -n -k 2 | tail -1 | awk '{print $2}'`
    e2=`grep "     $lumo     " $1 | head -$nkpt | sort -n -k 2 | head -1 | awk '{print $2}'`

    echo "HOMO: band:" $homo " E=" $e1
    echo "LUMO: band:" $lumo " E=" $e2

type

    ./gap.sh OUTCAR

  

- README.txt

<!-- -->

    For each HF+DFT method (B3LYP, PBE0, HSE06, and HF) compute the bandgap of Si
    adopting the following procedure:

    i) Perform a standard PBE calculation
    ii) Perform a HF+DFT run (VASP reads in the WAVECAR from run (i)
    iii) Calculate the value of the bandgap by running the script 'gap': 
         bandgap = min(cband) - max(vband) 

## Download\[<a
href="/wiki/index.php?title=Bandgap_of_Si_using_different_DFT%2BHF_methods&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/2/2f/Si_hybrids_gap.tgz" class="internal"
title="Si hybrids gap.tgz">Si_hybrids_gap.tgz</a>


[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
bandgap of Si using different DFT+HF
methods \> [MgO optimum
mixing](MgO_optimum_mixing.md) \>
[fcc Ni DOS with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
[Si bandstructure](Si_bandstructure.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).


