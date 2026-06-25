<!-- Source: https://vasp.at/wiki/index.php/LMAXTAU | revid: 29387 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMAXTAU


LMAXTAU = \[integer\] 

|                      |     |                                        |
|----------------------|-----|----------------------------------------|
| Default: **LMAXTAU** | = 6 | if [LASPH](LASPH.md)=.TRUE. |
|                      | = 0 | else                                   |

Description: LMAXTAU is the
maximum *l*-quantum number included in the PAW one-center expansion of
the kinetic energy density.

------------------------------------------------------------------------

The PAW one-center expansion of the density has component up to and
including *L*=2\**l*<sub>max</sub>, where *l*<sub>max</sub> is the
*l*-quantum number of the partial waves on the
[POTCAR](../input-files/POTCAR.md) file, with the highest angular moment.
If the PAW one-center expansion of the density has component up to *L*,
then the one-center expansion of the kinetic energy density has
components up to *L*+2.

This means that as a rule of thumb, for *s*-elements:
LMAXTAU=2, for *p*:
LMAXTAU=4, and for *d*:
LMAXTAU=6. If you are willing
to live with the computational costs, the default for
LMAXTAU should be safe in all
cases, except those involving *f*-elements.

## Related tags and articles\[<a href="/wiki/index.php?title=LMAXTAU&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[METAGGA](METAGGA.md), [CMBJ](CMBJ.md),
[CMBJA](CMBJA.md), [CMBJB](CMBJB.md),
[LASPH](LASPH.md), [LMIXTAU](LMIXTAU.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMAXTAU-_incategory-Examples)

------------------------------------------------------------------------


