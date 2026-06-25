<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni_DOS_with_hybrid_functional | revid: 14725 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni DOS with hybrid functional



[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum
mixing](MgO_optimum_mixing.md) \>
fcc Ni DOS with hybrid
functional \> [Si
bandstructure](Si_bandstructure.md)
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
- [3
  Calculation](#Calculation)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculate fcc Ni DOS using HSE and PBE0 (comparison with PBE).

## Input\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc Ni
     3.53
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    ## Plot the spin-polarized DOS of fcc Ni 
    ## at HSE and PBE0 level, and compare with
    ## standard PBE.
    ## Better preconverge with PBE first!
        
     SYSTEM = fcc Ni
     ISMEAR = -5
     LORBIT = 11
         
     ISPIN = 2
     MAGMOM = 1
         
    ## Selects the HSE06 hybrid functional
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ;
    #ALGO = D ; TIME = 0.4 ; LSUBROT = .TRUE.
         
    ## Selects the PBE0  hybrid functional
    #LHFCALC = .TRUE. ;
    #ALGO = D ; TIME = 0.4 ; LSUBROT = .TRUE.

  

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
    0
    Gamma
      5  5  5
      0  0  0

## Calculation\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

## Download\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS_with_hybrid_functional&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/2/2b/FccNi_hybrid_DOS.tgz" class="internal"
title="FccNi hybrid DOS.tgz">fccNi_hybrid_DOS.tgz</a>


[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum
mixing](MgO_optimum_mixing.md) \>
fcc Ni DOS with hybrid
functional \> [Si
bandstructure](Si_bandstructure.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


