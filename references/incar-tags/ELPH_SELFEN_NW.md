<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_NW | revid: 32869 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_NW


ELPH_SELFEN_NW = \[integer\]  
Default: **ELPH_SELFEN_NW** = 1 

Description: Number of energies to use when computing the phonon-induced
electron self-energy.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The electron self-energy, $\Sigma_{n \mathbf{k}}(\omega)$, depends on the frequency $\omega$ (or
energy $\hbar \omega$).
ELPH_SELFEN_NW controls the
number and location of frequencies when computing the self-energy in the
following way:

`ELPH_SELFEN_NW`` > 0`  
The self-energy is computed at
ELPH_SELFEN_NW equally spaced
energies between $\varepsilon_{n \mathbf{k}} -
\frac{1}{2} E^{\text{W}}$ and
$\varepsilon_{n \mathbf{k}} + \frac{1}{2} E^{\text{W}}$. The interval is centered around each Kohn-Sham
eigenvalue, $\varepsilon_{n \mathbf{k}}$, and its width, $E^{\text{W}}$, is controlled via
[ELPH_SELFEN_WRANGE](ELPH_SELFEN_WRANGE.md). If
ELPH_SELFEN_NW is an even
number, it is automatically increased by one so that the center-most
energy in each interval always coincides with the corresponding
Kohn-Sham eigenvalue.

`ELPH_SELFEN_NW`` < 0`  
The self-energy is computed at
\|ELPH_SELFEN_NW\| equally
spaced energies between $\varepsilon^{\text{min}}_{\mathbf{k}} - \frac{1}{2} E^{\text{W}}$ and $\varepsilon^{\text{max}}_{\mathbf{k}} + \frac{1}{2} E^{\text{W}}$, where $\varepsilon^{\text{min}}_{\mathbf{k}}$ and
$\varepsilon^{\text{max}}_{\mathbf{k}}$ are the minimum
and maximum Kohn-Sham eigenvalues of the calculation, respectively. Once
again, $E^{\text{W}}$
is controlled via
[ELPH_SELFEN_WRANGE](ELPH_SELFEN_WRANGE.md) and
allows to extend the interval in both directions.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_NW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)
- [ELPH_SELFEN_WRANGE](ELPH_SELFEN_WRANGE.md)


