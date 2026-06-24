<!-- Source: https://vasp.at/wiki/index.php/AMIX | revid: 27038 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMIX
AMIX = \[real\] 

|  |  |  |
|----|----|----|
| Default: **AMIX** | = 0.8 | if [ISPIN](ISPIN.md)=1 and one uses US-PPs |
|  | = 0.4 | if [ISPIN](ISPIN.md)=2 and one uses US-PPs |
|  | = 0.4 | if one uses PAW datasets |

Description: AMIX specifies the linear mixing parameter.

------------------------------------------------------------------------

In VASP the eigenvalue spectrum of the charge dielectric matrix is
calculated and written to the [OUTCAR](../output-files/OUTCAR.md) file at
each electronic step. This allows a rather easy optimization of the
mixing parameters, if required. Search in the
[OUTCAR](../output-files/OUTCAR.md) file for

    eigenvalues of (default mixing * dielectric matrix)

The parameters for the mixing are optimal if the mean eigenvalue
Γ_(mean)=1, and if the width of the eigenvalue spectrum is minimal. For
an initial linear mixing ([BMIX](BMIX.md)≈0) an optimal
setting for AMIX can be found easily by setting
AMIX_(optimal)=AMIX_(current)\*Γ_(mean). For the Kerker scheme
([IMIX](IMIX.md)=1) either AMIX or [BMIX](BMIX.md)
can be optimized, but we recommend to change only
[BMIX](BMIX.md) and keep AMIX fixed (you must decrease
[BMIX](BMIX.md) if the mean eigenvalue is larger than one, and
increase [BMIX](BMIX.md) if the mean eigenvalue Γ_(mean)\<1).
However, the optimal AMIX depends very much on the system, for metals
this parameter usually has to be rather small, e.g. AMIX= 0.02.

## Related tags and articles
[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [BMIX](BMIX.md),
[AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md), [WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMIX-_incategory-Examples)
