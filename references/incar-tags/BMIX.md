<!-- Source: https://vasp.at/wiki/index.php/BMIX | revid: 28223 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BMIX
BMIX = \[real\]  
Default: **BMIX** = 1.0 

Description: BMIX sets the cutoff wave vector for Kerker mixing scheme
([IMIX](IMIX.md)=1 and/or [INIMIX](INIMIX.md)=1).

------------------------------------------------------------------------

The mixed density is given by

$\rho_{\rm mix}\left(G\right)=\rho_{\rm
in}\left(G\right)+A \frac{G^2}{G^2+B^2}\Bigl(\rho_{\rm
out}\left(G\right)-\rho_{\rm in}\left(G\right)\Bigr)$

with $A$=[AMIX](AMIX.md) and
$B$=BMIX

In VASP the eigenvalue spectrum of the charge dielectric matrix is
calculated and written to the [OUTCAR](../output-files/OUTCAR.md) file at
each electronic step. This allows a rather easy optimization of the
mixing parameters, if required. Search in the
[OUTCAR](../output-files/OUTCAR.md) file for

    eigenvalues of (default mixing * dielectric matrix)

The parameters for the mixing are optimal if the mean eigenvalue
Γ_(mean)=1, and if the width of the eigenvalue spectrum is minimal. For
an initial linear mixing (BMIX≈0) an optimal setting for
[AMIX](AMIX.md) can be found easily by setting
[AMIX](AMIX.md)_(optimal)=[AMIX](AMIX.md)_(current)\*Γ_(mean).
For the Kerker scheme ([IMIX](IMIX.md)=1) either
[AMIX](AMIX.md) or BMIX can be optimized, but we recommend to
change only BMIX and keep [AMIX](AMIX.md) fixed (you must
decrease BMIX if the mean eigenvalue is larger than one, and increase
BMIX if the mean eigenvalue Γ_(mean)\<1).

## Related tags and articles
[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md), [WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-BMIX-_incategory-Examples)

## References