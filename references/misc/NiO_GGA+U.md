<!-- Source: https://vasp.at/wiki/index.php/NiO_GGA%2BU | revid: 36494 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NiO GGA+U


Description: Antiferromagnetic (AFM) configuration for NiO in the
GGA+U<sub>eff</sub> (Dudarev's) approach ; PBE functional

In the Dudarev method, a Hubbard effective parameter U<sub>eff</sub> =
U - J is used. Concretely, the J value is considered equal to 0, and
U<sub>eff</sub> = U. For more details read the page on the
[LDAUTYPE](../incar-tags/LDAUTYPE.md)-tag .

  
*<u>Exercise :</u>* Study the change of the magnetic moment of Ni atoms
and the DOS by varying the U<sub>eff</sub> value.

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    NiO GGA+U AFM
      SYSTEM    = "NiO"
        
    Electronic minimization
      ENCUT     = 450
      EDIFF     = 1E-5
      LORBIT    = 11
      LREAL     = .False.
      ISTART    = 0
      NELMIN    = 6
        
    DOS
      ISMEAR    = -5
        
    Magnetism
      ISPIN     = 2
      MAGMOM    = 2.0 -2.0 2*0.0 
         
    Mixer
      AMIX      = 0.2
      BMIX      = 0.00001
      AMIX_MAG  = 0.8
      BMIX_MAG  = 0.00001
         
    GGA+U
      LDAU      = .TRUE.
      LDAUTYPE  = 2
      LDAUL     = 2 -1
      LDAUU     = 5.00 0.00
      LDAUJ     = 0.00 0.00
      LDAUPRINT = 1
      LMAXMIX   = 4 

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

------------------------------------------------------------------------

To check the results obtained with this approach, they can be compared
to those determined with a [hybrid](NiO_HSE06.md)
approach. The magnetic moment for the Ni atoms and the E<sub>g</sub>
calculated using this approach are 1.67 μ<sub>B</sub> and 3.97 eV
respectively.

## Download\[<a
href="/wiki/index.php?title=NiO_GGA%2BU&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/e/e9/Nio_gga%2Bu.tgz" class="internal"
title="Nio gga+u.tgz">nio_gga+u.tgz</a>

------------------------------------------------------------------------


