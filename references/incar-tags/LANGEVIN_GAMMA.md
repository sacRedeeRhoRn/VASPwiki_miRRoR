<!-- Source: https://vasp.at/wiki/index.php/LANGEVIN_GAMMA | revid: 36570 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LANGEVIN_GAMMA


LANGEVIN_GAMMA = \[Real
array\]  
Default: **LANGEVIN_GAMMA** = NTYP×0 

Description: LANGEVIN_GAMMA
specifies the friction coefficients (in ps<sup>-1</sup>) for atomic
degrees-of-freedom when using a Langevin thermostat (in case VASP was
compiled with <a href="/wiki/Precompiler_flags" class="mw-redirect"
title="Precompiler flags">-Dtbdyn</a>).

------------------------------------------------------------------------

When using a [Langevin
thermostat](../tutorials/Langevin_thermostat.md)<sup>[\[1\]](#cite_note-allen:book:1991-1)</sup>
([MDALGO](MDALGO.md)=3), the friction coefficients γ for the
atomic degrees-of-freedom are specified (in ps<sup>-1</sup>) using the
LANGEVIN_GAMMA-tag.

One has to specify a separate friction coefficient for each of the NTYP
atomic species found on the [POTCAR](../input-files/POTCAR.md)-file.

#### Practical example\[<a
href="/wiki/index.php?title=LANGEVIN_GAMMA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Practical example">edit</a> \| (./index.php.md)\]

Consider a system consisting of 16 hydrogen and 48 silicon atoms.
Suppose that eight silicon atoms are considered to be Langevin atoms and
the remaining 32 Si atoms are either fixed or Newtonian atoms. The
Langevin and Newtonian (or fixed) atoms should be considered as
different species, *i.e.*, the [POSCAR](../input-files/POSCAR.md)-file
should contain the line like this:

    Si H Si
    40 16 8

As only the final eight Si atoms are considered to be Langevin atoms,
the [INCAR](../input-files/INCAR.md)-file should contain the following line
defining the friction coefficients:

    LANGEVIN_GAMMA = 0.0   0.0   10.0

*i.e.*, for all non-Langevin atoms, γ should be set to zero.

## Related tags and articles\[<a
href="/wiki/index.php?title=LANGEVIN_GAMMA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LANGEVIN_GAMMA_L](LANGEVIN_GAMMA_L.md),
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LANGEVIN_GAMMA-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LANGEVIN_GAMMA&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------


1.  [↑](#cite_ref-allen:book:1991_1-0)
    <a
    href="https://books.google.co.jp/books?id=WFExDwAAQBAJ&amp;lpg=PP1&amp;hl=ja&amp;pg=PP1#v=onepage&amp;q&amp;f=false"
    class="external text" rel="nofollow">M. P. Allen and D. J. Tildesley,
    <em>Computer simulation of liquids</em> (Oxford university press: New
    York, 1991).</a>


