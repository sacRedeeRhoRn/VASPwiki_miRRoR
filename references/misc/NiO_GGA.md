<!-- Source: https://vasp.at/wiki/index.php/NiO_GGA | revid: 10447 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NiO GGA
**Exercise :** Determine the most stable magnetic order between the
antiferromagnetic (AFM) and ferromagnetic (FM) configurations. Compare
the both DOS.

- [INCAR](../input-files/INCAR.md)

&nbsp;

    NiO GGA AFM
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
      MAGMOM   = 2.0 -2.0 2*0  # AFM order
      # MAGMOM   = 2.0 2.0 2*0 # FM order
        
    Mixer
      AMIX     = 0.2
      BMIX     = 0.00001
      AMIX_MAG = 0.8
      BMIX_MAG = 0.00001 

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

## Download
[nio_gga.tgz](https://vasp.at/wiki/images/e/e6/Nio_gga.tgz "Nio gga.tgz")

------------------------------------------------------------------------
