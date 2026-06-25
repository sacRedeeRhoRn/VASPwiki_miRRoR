<!-- Source: https://vasp.at/wiki/index.php/Calculation_of_dimers | revid: 17864 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Calculation of dimers


Reproducing accurate dimer distances is an important difficult benchmark
for a potential. If a potential works accurately for dimers and bulk
calculations, one can be quite confident that the potential possesses
excellent transferability. For the simulation of the dimers, one can use
the $\Gamma$ point
and displace the second atom along the diagonal direction. Generally
bonding length and vibrational frequency have to be compared with
accurate reference data. It is recommended to perform these calculations
using the constant velocity molecular dynamic mode (i.e.
[IBRION](../incar-tags/IBRION.md)=2, [SMASS](../incar-tags/SMASS.md)=-2).
This mode speeds up the calculation because the wave functions are
extrapolated and predicted using information from previous steps. The
[INCAR](../input-files/INCAR.md) file must contain additional lines to
perform the constant velocity MD:

    #ionic relaxation
    NSW = 10     #number of steps for IOM
    SMASS = -2   #constant velocity MD
    POTIM = 1    #time-step for ionic-motion

In addition to the positions the [POSCAR](../input-files/POSCAR.md) file
must also contain velocities:

    dimer
    1
         10.00000    .00000    .00000
           .00000  10.00000    .00000
           .00000    .00000  10.00000
       2
    cart
     0       0       0
     1.47802 1.47802 1.47802
    cart
       0       0       0
     -.02309 -.02309 -.02309

For this [POSCAR](../input-files/POSCAR.md) file the starting distance is
2.56 $\AA$, in each
step the distance is reduced by 0.04 $\AA$, leading
to a final distance of 2.20 $\AA$. The
obtained energies can be fitted to a Morse potential.

Mind: In some rare cases like C<sub>2</sub>, the calculation of the
dimer turns out to be problematic. For this case the LUMO (lowest
unoccupied molecular orbital) and the HOMO (highest occupied molecular
orbital) cross at a certain distance, and are actually degenerate, if
the total energy is used as a variational quantity (i.e.
$\sigma \to 0$). Within the finite temperature LDA these
difficulties are avoided, but interpreting the results is not easy
because of the finite entropy (for C<sub>2</sub> see Ref.
[^pederson:prb:1991-1]).

## References\[<a
href="/wiki/index.php?title=Calculation_of_dimers&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^pederson:prb:1991-1]: [M.R. Pederson and K.A. Jackson, Phys. Rev. B **43**, 7312 (1991).](https://doi.org/10.1103/PhysRevB.43.7312)
