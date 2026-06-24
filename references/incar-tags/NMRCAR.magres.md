<!-- Source: https://vasp.at/wiki/index.php/NMRCAR.magres | revid: 34765 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NMRCAR.magres
The NMRCAR.magres file is writte when [calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md)
or [calculating the electric field
gradient](../tutorials/Calculating_the_electric_field_gradient.md)
if [`LNMRCAR`](LNMRCAR.md)` = T` (default). The file format
followes the [Magres format](https://www.ccpnc.ac.uk/docs/magres) in
order to allow easy analysis using e.g.
[magresview](https://ccp-nc.github.io/magresview-2/) or the Python
package [Soprano](https://ccp-nc.github.io/soprano/intro.html)
^([\[1\]](#cite_note-liborio:jcp:2018-1)). Mind that, while the Magres
format does not clearly state if the [macroscopic
susceptibility](../categories/Category-NMR.md)
should be included, here it is included in the chemical shielding.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

## Related tags and articles
[LCHIMAG](LCHIMAG.md), [LEFG](LEFG.md) ,
[LNMRCAR](LNMRCAR.md)

[Calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md),
[Calculating the electric field
gradient](../tutorials/Calculating_the_electric_field_gradient.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNMRCAR-_incategory-HowTo)

## References
1.  [↑](#cite_ref-liborio:jcp:2018_1-0) [L. Liborio, S. Sturniolo,
    and D. Jochym, *Computational prediction of muon stopping sites
    using ab initio random structure searching (AIRSS)*, J. Chem. Phys.
    **148**, 134114 (2018).](https://doi.org/10.1063/1.5024450)
