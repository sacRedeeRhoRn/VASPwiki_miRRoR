<!-- Source: https://vasp.at/wiki/index.php/Alpha-AlF3 | revid: 10405 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Alpha-AlF3
**Exercise :** Determine the ²⁷Al C_(q) value and the Al and F
shieldings.

α-AlF₃ crystallizes in the trigonal R -3c space group.

a = b = 4.9305 Å; c = 12.4462 Å

α = β = 90°; γ = 120°

The unit cell contains two independent atoms (1 Al and 1 F) with 6
formula units (AlF₃) per unit cell (Z=6). AlF₆ octahedron units are
linked together by corner sharing. As the conventional unit cell is
non-primitive, the primitive rhombohedral one is used for the
calculation. It saves a lot of computational time !

We suggest you to use vesta for generation the POSCAR file from the
AlF3.cif file. In the standard export procedure, the POSCAR file is
generated with the conventional unit cell (non primitive R-cell with 24
atoms inside). Ask VESTA to reduce to unit cell to the primitive one.
You will then have only 8 atoms in the POSCAR file.

In this exercise one wants first to calculate the EFG tensor components
of ²⁷Al. This is very fast task calculated at the end of the first SCF
calculation (ground state property). The experimental values for the
C_(q) is 0.21 MHz. The nuclear quadrupolar momentum used to transform
EFG in C_(q) is Q = 14.66 10⁻³⁰ m² (see the paper of Sadoc *et al.*
([http://www.sciencedirect.com/science/article/pii/S0926204014000022](http://www.sciencedirect.com/science/article/pii/S0926204014000022))
(Flurine has a 1/2 nuclear spin, so Q is zero)

In a second step one wants to calculate the shielding parameters for Al
and F. This is done using the linear response using the GIPAW formalism.
As the calculation is quite time consuming, only very few k-points and
small ENCUT are used with standard PAW data sets. The calculated
shielding tensors components can be compared to the ones obtained by
Sadoc *et al.*

  

- [INCAR](../input-files/INCAR.md)

&nbsp;

     SYSTEM       =  Al F3
     GGA          = PE
     ISTART       = 1
     ICHARG       = 0
     INIWAV       = 1
     LREAL        =  AUTO
     ISYM         = 2
     ISPIN        = 1

Ionic minimisation

     NSW          = 0
     ISIF         = 2
     IBRION       = 2

1.  [EDIFFG](../incar-tags/EDIFFG.md) = -2E-2

&nbsp;

     POTIM        = 0.1

Electronic minimisation

     IALGO        = 38
     LWAVE        = .TRUE.
     EMIN         =   -20.0
     EMAX         =   10.0
     NEDOS        = 1601

EFG Calculation

     LEFG         = .TRUE.
     QUAD_EFG     = 146.6 0.0

Chemical Shift

     PREC         = Normal    # nice
     ENCUT        = 400.0      # typically higher cutoffs than usual are needed
     ISMEAR = 0; SIGMA= 0.1 # no fancy smearings, SIGMA sufficiently small
     EDIFF        = 1E-9      # you'd need much smaller EDIFFs.
     LCHIMAG      = .TRUE.   # to switch on linear response for chemical shifts
     DQ           = 0.001         # often the default is sufficient
     ICHIBARE     = 1       # often the default is sufficient
     LNMR_SYM_RED = .TRUE. # be on the safe side
     NLSPLINE     = .TRUE.  # only needed if LREAL is NOT set.
     LREAL        = A          # helps for speed for large systems, not needed
     NBANDS       = 25       # to safe memory, ??? = NELECT/2

  

- [KPOINTS](../input-files/KPOINTS.md)

&nbsp;

    automatic mesh
    0
    Auto
    20

- [POSCAR](../input-files/POSCAR.md)

&nbsp;

    Al1 F3
    1.0
            4.9305000305         0.0000000000         0.0000000000
            2.4652500153         4.2699382798         0.0000000000
            2.4652650832         1.4233214594         4.1486879977
       Al    F
        2    6
    Direct
         0.000000000         0.500000000         0.000000000
         0.500000000         0.000000000         0.500000000
         0.177499995         0.250000000         0.750000000
         0.822499990         0.750000000         0.250000000
         0.677500010         0.322499990         0.250000000
         0.322499990         0.677500010         0.750000000
         0.250000000         0.177499995         0.250000000
         0.750000000         0.822499990         0.750000000

## Download
[AlF3_NMR.tgz](https://vasp.at/wiki/images/f/f7/AlF3_NMR.tgz "AlF3 NMR.tgz")

------------------------------------------------------------------------
