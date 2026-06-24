<!-- Source: https://vasp.at/wiki/index.php/ENCUT | revid: 26956 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUT
ENCUT = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ENCUT** | = largest [ENMAX](../redirects/ENMAX.md) in the [POTCAR](../input-files/POTCAR.md) file |  |

Description: ENCUT specifies the energy cutoff for the plane-wave basis
set in eV.

------------------------------------------------------------------------

All plane waves with a kinetic energy smaller than
$E_{\mathrm{cut}}$ are included in the
basis set, i.e.,

$| \mathbf{G} + \mathbf{k} | <
G_{\mathrm{cut}}$ with $E_{\mathrm{cut}} = \frac{\hbar^2}{2m} G^2_{\mathrm{cut}}$

With this energy cutoff, the number of plane waves included in the basis
set depends on the **k**-point, leading to a superior behavior. For
instance, for energy-volume calculations the total number of plane waves
changes fairly smoothly according to the volume, while the criterion
$| \mathbf{G} | < G_{\mathrm{cut}}$
(i.e. same number of plane waves for all **k**-points) would lead to a
very rough energy-volume curve and, generally, to a slower energy
convergence with respect to the basis set size.

The [POTCAR](../input-files/POTCAR.md) files contain a default
[ENMAX](../redirects/ENMAX.md) (and [ENMIN](ENMIN.md)).
Therefore, it is, in principle, not necessary to specify ENCUT in the
[INCAR](../input-files/INCAR.md) file. For calculations with more than one
species, the maximum cutoff [ENMAX](../redirects/ENMAX.md) (or
[ENMIN](ENMIN.md)) value is used for the calculation (see
[PREC](PREC.md)).

[TABLE]

## Related tags and articles
[ENMAX](../redirects/ENMAX.md), [ENMIN](ENMIN.md),
[ENINI](ENINI.md), [ENAUG](ENAUG.md),
[PREC](PREC.md), [NGX](NGX.md),
[NGY](NGY.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [POTCAR](../input-files/POTCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENCUT-_incategory-Examples)
