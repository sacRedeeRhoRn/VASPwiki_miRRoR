<!-- Source: https://vasp.at/wiki/index.php/CLNT | revid: 28291 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CLNT
CLNT = \[integer\] 

|                   |     |     |
|-------------------|-----|-----|
| Default: **CLNT** | = 1 |     |

Description: CLNT selects the type of the excited atoms in XAS
calculations with [ICORELEVEL](ICORELEVEL.md)\>0.

------------------------------------------------------------------------

All atoms of the selected type are excited in the XAS calculation with
[ICORELEVEL](ICORELEVEL.md)=2. Hence, it is recommended
that the excited atom is separated into a dedicated type with a single
atom. Exciting multiple atoms in the supercell core-hole approach causes
the interaction between core holes in neighboring atoms and should be
avoided. Exciting multiple atoms in BSE proportionately increases the
number of core states included in the BSE Hamiltonian and, hence,
increases the computational cost of the calculation.

See a detailed description on how to set this tag in the
[SCH](../tutorials/Supercell_core-hole_calculations.md)
and
[BSE](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)
calculations.

## Related tags and articles
[ICORELEVEL](ICORELEVEL.md), [CLN](CLN.md),
[CLL](CLL.md), [CLZ](CLZ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CLNT-_incategory-Examples)

------------------------------------------------------------------------
