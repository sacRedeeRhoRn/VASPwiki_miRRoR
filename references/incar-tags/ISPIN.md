<!-- Source: https://vasp.at/wiki/index.php/ISPIN | revid: 36282 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ISPIN
ISPIN = 1 \| 2  
Default: **ISPIN** = 1 

Description: ISPIN specifies whether a calculation is performed with or
without spin polarization.

------------------------------------------------------------------------

In spin-polarized calculations, VASP treats spin-up and spin-down
electrons separately, allowing each spin channel to develop a different
charge density and occupation. This is essential for magnetic systems;
for nonmagnetic systems it is generally unnecessary and increases
computational cost.

- ISPIN=1: VASP performs a non-spin-polarized calculation. Spin-up and
  spin-down electrons share a single charge density.

&nbsp;

- ISPIN=2: VASP performs a spin-polarized collinear calculation. Spin-up
  and spin-down electrons are treated separately.

Spin-polarized calculations are commonly used for magnetic materials
such as Fe, Co, Ni, and magnetic oxides. To initialize magnetic moments
on atoms, combine ISPIN=2 with [MAGMOM](MAGMOM.md).

    ISPIN = 2
    MAGMOM = 2*5.0 2*-5.0

This example initializes two atoms with positive magnetic moments and
two atoms with negative magnetic moments, which may be useful for
antiferromagnetic calculations.

  

|  |
|----|
| **Mind:** For noncollinear calculations, ISPIN is ignored; use [LNONCOLLINEAR](LNONCOLLINEAR.md)=.TRUE. instead. |

  

|  |
|----|
| **Mind:** Since VASP 6.5.0, the calculation exits with an error if ISPIN=2 and [MAGMOM](MAGMOM.md) are used together with [LNONCOLLINEAR](LNONCOLLINEAR.md)=.TRUE. |

## Related tags and articles
[MAGMOM](MAGMOM.md)
[LNONCOLLINEAR](LNONCOLLINEAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ISPIN-_incategory-Howto)
