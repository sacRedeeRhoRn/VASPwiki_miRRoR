<!-- Source: https://vasp.at/wiki/index.php/Estimation_of_J_magnetic_coupling | revid: 20170 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Estimation of J magnetic coupling


Description: Estimation of the J magnetic exchange coupling using the
GGA+U method.

Switching off the symmetry ([ISYM](../incar-tags/ISYM.md) = 0) is often
necessary to generate different magnetic configurations.

  
*<u>Exercise :</u>* Study the change of the 180° superexchange coupling
J<sub>2</sub> between the next nearest neighbors (d<sub>Ni-Ni</sub> =
4.17 A) by varying the U<sub>eff</sub> value. The following equation
J<sub>2</sub> = (E<sub>FM</sub> - E<sub>AFM</sub>) / 12 expresses the
super exchange Ni-O-Ni coupling as a function of the energy difference
of the ferromagnetic (FM) and antiferromagnetic (AFM) configurations. In
this case, the superexchange coupling J<sub>1</sub> between the nearest
neighbors is neglected. The theoretical results can be compared to the
experimental one : J<sub>2</sub> = 19.01 meV (Hutchings M. T., Samuelsen
E. J., *Phys. Rev. B 6*, 9, **1972**, 3447)

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    NiO GGA+U AFM
      SYSTEM    = "NiO"
        
    Electronic minimization
      ENCUT     = 450
      EDIFF     = 1E-4
      LORBIT    = 11
      LREAL     = .False.
      ISTART    = 0
      ISYM      = 0
      NELMIN    = 6
        
    DOS
      ISMEAR    = -5
        
    Magnetism
      ISPIN     = 2
      MAGMOM    = 2.0 -2.0 2*0  # AFM conf.
      # MAGMOM    = 2*2.0 2*0  # FM conf.

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

Necessarely, the J magnetic coupling decreases with the increasing of
the U<sub>eff</sub> value. To assess the obtained value, similar
calculations could be done using a [hybrid
functional](NiO_HSE06.md).

## Download\[<a
href="/wiki/index.php?title=Estimation_of_J_magnetic_coupling&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/b/bb/Nio_Jcoupl.tgz" class="internal"
title="Nio Jcoupl.tgz">nio_Jcoupl.tgz</a>

------------------------------------------------------------------------


