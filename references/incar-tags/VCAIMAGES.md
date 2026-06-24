<!-- Source: https://vasp.at/wiki/index.php/VCAIMAGES | revid: 36724 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VCAIMAGES
VCAIMAGES = \[real\]  
Default: **VCAIMAGES** = -1 

Description: The tag VCAIMAGES allows to perform thermodynamic
integrations (TI); it defines the coupling parameter λ.

------------------------------------------------------------------------

VCAIMAGES allows two molecular dynamics (MD) simulations to be performed
with e.g. different [POTCAR](../input-files/POTCAR.md) or
[KPOINTS](../input-files/KPOINTS.md) files or different
exchange-correlation functionals, and averages the energies and forces
between the two calculations. This is known as thermodynamic integration
(TI) ^([\[1\]](#cite_note-dorner:PRL:2018-1)).

The tag VCAIMAGES internally splits the available nodes into two groups,
and each group then performs an independent VASP calculation (this
implies VCAIMAGES only works in the MPI version). This behavior is
implemented in the same way as the [nudged elastic band
method](../tutorials/Nudged_elastic_bands.md) (NEB)
described under the tag [IMAGES](IMAGES.md). As opposed to
NEB, only two images are created ([IMAGES](IMAGES.md)=2 is
set internally). The two calculations are performed in subdirectories
`01` and `02` (`00` and `03` are not required, in contrast to NEB).

## Contents

- [1 Description of reading a writing during the
  calculation](#Description_of_reading_a_writing_during_the_calculation)
- [2 Finding the energies](#Finding_the_energies)
- [3 Related tags and articles](#Related_tags_and_articles)
- [4 References](#References)

### Description of reading a writing during the calculation
The two calculations are performed essentially independently in
subdirectories `01` and `02`. The forces, energies, and the stress
tensor of the two calculations are averaged according to the coupling
parameter supplied by VCAIMAGES. Specifically, the value supplied in the
tag VCAIMAGES determines the weight of the calculations performed in
subdirectory `01`. The weight of the second image is 1-VCAIMAGES. After
self-consistency has been reach for both calculations, the energies and
forces are averaged, affecting the final total energy as well as the
forces. This ensures that the trajectories for the two MD simulations
are identical.

|  |
|----|
| **Important:** Make sure that the initial [POSCAR](../input-files/POSCAR.md) is identical in both subdirectories. |

### Finding the energies
The averaged energies can be found in the
[OUTCAR](../output-files/OUTCAR.md) file after the lines
`ENERGY OF THE ELECTRON-ION-THERMOSTAT SYSTEM (eV)`, as well as in the
file [OSZICAR](../output-files/OSZICAR.md) (in the lines writing the free
energy `F=`). This can make looking for the energies of the individual
calculation awkward. You can find these under
`FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)` in the
[OUTCAR](../output-files/OUTCAR.md) file for a DFT calculation (They are
under `ML FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)` for a
machine-learned force field (MLFF)).

[TABLE]

The usage of this tag is also explained in the supplementary information
of reference ^([\[1\]](#cite_note-dorner:PRL:2018-1)).

## Related tags and articles
[NCORE_IN_IMAGE1](NCORE_IN_IMAGE1.md),
[SCALEE](SCALEE.md), [IMAGES](IMAGES.md),
[Thermodynamic integration
calculations](../tutorials/Thermodynamic_integration_calculations.md)

## References
1.  ↑ ^([a](#cite_ref-dorner:PRL:2018_1-0))
    ^([b](#cite_ref-dorner:PRL:2018_1-1)) [F. Dorner, Z. Sukurma, C.
    Dellago, and G. Kresse, Phys. Rev. Lett. **121**, 195701
    (2018).](https://doi.org/10.1103/PhysRevLett.121.195701)
