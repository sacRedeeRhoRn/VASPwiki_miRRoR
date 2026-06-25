<!-- Source: https://vasp.at/wiki/index.php/INIMIX | revid: 27012 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# INIMIX


INIMIX = 0 \| 1 \| 2  
Default: **INIMIX** = 1 

Description: Determines the functional form of the initial mixing matrix
in the Broyden scheme ([IMIX](IMIX.md)=4).

------------------------------------------------------------------------

The initial mixing matrix might influence the convergence speed for
complex situations (especially surfaces and magnetic systems),
nevertheless INIMIX must not
be changed from the default setting: anything which can be done with
INIMIX can also be done with
[AMIX](AMIX.md) and [BMIX](BMIX.md), and changing
[AMIX](AMIX.md) and [BMIX](BMIX.md) is definitely
preferable.

Possible choices for INIMIX are:

- INIMIX=0

Linear mixing according to the setting of [AMIX](AMIX.md)

- INIMIX=1

Kerker mixing (see [IMIX](IMIX.md)=1) according to the
settings of [AMIX](AMIX.md) and [BMIX](BMIX.md).

The mixed density is given by

$\rho_{\rm mix}\left(G\right)=\rho_{\rm in}\left(G\right)+A
\frac{G^2}{G^2+B^2}\Bigl(\rho_{\rm out}\left(G\right)-\rho_{\rm
in}\left(G\right)\Bigr)$

with $A$=[AMIX](AMIX.md) and
$B$=[BMIX](BMIX.md)

- INIMIX=2

No mixing (equal to INIMIX=0
and [AMIX](AMIX.md)=1, not recommended)

## Related tags and articles\[<a href="/wiki/index.php?title=INIMIX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMIX](IMIX.md), [MAXMIX](MAXMIX.md),
[AMIX](AMIX.md), [BMIX](BMIX.md),
[AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md), [WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-INIMIX-_incategory-Examples)


