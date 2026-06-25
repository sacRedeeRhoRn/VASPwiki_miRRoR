<!-- Source: https://vasp.at/wiki/index.php/NiO_HSE06 | revid: 14726 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NiO HSE06


Description: Hybrid functional calculation using the HSE06 functional.

It is strongly recommended to start from a converged PBE calculation
([ISTART](../incar-tags/ISTART.md) = 1) before beginning with a DFT+HF
method. For other [hybrid
functionals](../methods/List_of_hybrid_functionals.md)

*<u>Exercise :</u>* Check the values presented
[here](NiO_GGA+U.md).

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    NiO HSE06 AFM
      SYSTEM   = "NiO"
        
    Electronic minimization
      ENCUT    = 450
      EDIFF    = 1E-5
      LORBIT   = 11
      LREAL    = .False.
      ISTART   = 0
      NELMIN   = 6
        
    DOS
      ISMEAR   = -5
        
    Magnetism
      ISPIN    = 2
      MAGMOM   = 2.0 -2.0 2*0.0
        
    Mixer
      AMIX     = 0.2
      BMIX     = 0.00001
      AMIX_MAG = 0.8
      BMIX_MAG = 0.00001 
        
    Hybrid functional
      #LHFCALC  = .TRUE.
      #HFSCREEN = 0.2 
      #ALGO     = D
      #TIME     = 0.4

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    k-points
     0
    gamma
     4  4  4 
     0  0  0

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    NiO
     4.17
     1.0 0.5 0.5
     0.5 1.0 0.5
     0.5 0.5 1.0
     2 2
    Cartesian
     0.0 0.0 0.0
     1.0 1.0 1.0
     0.5 0.5 0.5
     1.5 1.5 1.5

## Download\[<a
href="/wiki/index.php?title=NiO_HSE06&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/7/7b/Nio_hse06.tgz" class="internal"
title="Nio hse06.tgz">nio_hse06.tgz</a>

------------------------------------------------------------------------


