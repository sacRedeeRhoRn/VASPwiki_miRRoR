<!-- Source: https://vasp.at/wiki/index.php/Estimation_of_J_magnetic_coupling | revid: 20170 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Estimation of J magnetic coupling
Description: Estimation of the J magnetic exchange coupling using the
GGA+U method.

Switching off the symmetry ([ISYM](../incar-tags/ISYM.md) = 0) is often
necessary to generate different magnetic configurations.

  
**Exercise :** Study the change of the 180° superexchange coupling J₂
between the next nearest neighbors (d_(Ni-Ni) = 4.17 A) by varying the
U_(eff) value. The following equation J₂ = (E_(FM) - E_(AFM)) / 12
expresses the super exchange Ni-O-Ni coupling as a function of the
energy difference of the ferromagnetic (FM) and antiferromagnetic (AFM)
configurations. In this case, the superexchange coupling J₁ between the
nearest neighbors is neglected. The theoretical results can be compared
to the experimental one : J₂ = 19.01 meV (Hutchings M. T., Samuelsen E.
J., *Phys. Rev. B 6*, 9, **1972**, 3447)

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

&nbsp;

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

&nbsp;

    k-points
     0
    gamma
     4  4  4 
     0  0  0

- [POSCAR](../input-files/POSCAR.md)

&nbsp;

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
the U_(eff) value. To assess the obtained value, similar calculations
could be done using a [hybrid functional](NiO_HSE06.md).

## Download
[nio_Jcoupl.tgz](https://vasp.at/wiki/images/b/bb/Nio_Jcoupl.tgz "Nio Jcoupl.tgz")

------------------------------------------------------------------------
