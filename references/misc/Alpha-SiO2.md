<!-- Source: https://vasp.at/wiki/index.php/Alpha-SiO2 | revid: 10407 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Alpha-SiO2


*<u>Exercise :</u>* Determine the <sup>17</sup>O C<sub>q</sub> value and
the Si and O schieldings.

α-SiO<sub>2</sub> crystallizes in the trigonal P3<sub>1</sub>2 space
group.

a = b = 4.604 Å; c = 5.207 Å

α = β = 90°; γ = 120°

The unit cell contains two independent atoms (1 Si and 1 O) with 3
formula units (SiO<sub>2</sub>) per unit cell (Z=3). SiO<sub>4</sub>
tetrahedron units are linked together by corner sharing.

In this exercise one wants first to calculate the EFG tensor components
of <sup>17</sup>O. This is very fast task calculated at the end of the
first SCF calculation (ground state property). The experimental values
for the C<sub>q</sub> is 5.19 MHz. The nuclear quadrupolar momentum used
to transform EFG in C<sub>q</sub> is Q = 2.55 10<sup>-30</sup>
m<sup>2</sup> (see the paper of Profeta *et al.*
(<a href="http://pubs.acs.org/doi/abs/10.1021/ja027124r"
class="external free"
rel="nofollow">http://pubs.acs.org/doi/abs/10.1021/ja027124r</a>)
(Silicon has a 1/2 nuclear spin, so Q is zero)

In a second step one wants to calculate the shielding parameters for Si
and O. This is done using the linear response using the GIPAW formalism.
As the calculation is quite time consuming, only very few k-points and
small ENCUT are used with standard PAW data sets. The calculated
shielding tensors components can be compared to the ones obtained by
Profeta *et al.*

- [INCAR](../input-files/INCAR.md)

<!-- -->

     SYSTEM      = Si O2
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

1.  [EDIFFG](../incar-tags/EDIFFG.md)
    = -2E-2

<!-- -->

     POTIM        = 0.1

Electronic minimisation

     IALGO        = 38
     LWAVE        = .TRUE.
     EMIN         =   -20.0
     EMAX         =   10.0
     NEDOS        = 1601

EFG Calculation

     LEFG         = .TRUE.
     QUAD_EFG     = 0.0 25.5

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
     NBANDS       = 30       # to safe memory, ??? = NELECT/2 

  

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    automatic mesh
    0
    Auto
    20

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    O2 Si1
       1.00000000000000
         4.6040000915999997    0.0000000000000000    0.0000000000000000
        -2.3020000457999998    3.9871810383000001    0.0000000000000000
         0.0000000000000000    0.0000000000000000    5.2069997787000002
       Si   O
         3     6
    Direct
      0.4436617824484789 -0.0000000000000000  0.3333333429999996
     -0.0000000000000000  0.4436617824484789  0.6666666870000029
      0.5563382175515210  0.5563382175515210 -0.0000000000000000
      0.3926661416221499  0.3062177364999842  0.2428214976299141
      0.6937822635000156  0.0864484051221655  0.5761548406299137
      0.9135515948778347  0.6073338583778505  0.9094881546299145
      0.3062177364999842  0.3926661416221499  0.7571785323700884
      0.0864484051221655  0.6937822635000156  0.4238451593700863
      0.6073338583778505  0.9135515948778347  0.0905118383700884

## Download\[<a
href="/wiki/index.php?title=Alpha-SiO2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/4/4e/SiO2_NMR.tgz" class="internal"
title="SiO2 NMR.tgz">SiO2_NMR.tgz</a>

------------------------------------------------------------------------


