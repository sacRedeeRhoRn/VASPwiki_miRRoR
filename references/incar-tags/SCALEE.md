<!-- Source: https://vasp.at/wiki/index.php/SCALEE | revid: 26796 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SCALEE


SCALEE = \[real\]  
Default: **SCALEE** = 1 

Description: This tag specifies the coupling parameter of the energies
and forces between a fully interacting system and a reference system.

------------------------------------------------------------------------

The tag SCALEE sets the
coupling parameter $\lambda$ and
hence controls the Hamiltonian of the calculation. By default
SCALEE=1 and the scaling of
the energies and forces via the coupling constant is internally skipped
in the code. To enable the scaling
SCALEE$\ne$1 has to
be specified.

More information using this tag is given
[here](../tutorials/Thermodynamic_integration_calculations.md).

## Related tags and articles\[<a href="/wiki/index.php?title=SCALEE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VCAIMAGES](VCAIMAGES.md),
[IMAGES](IMAGES.md), [NCORE IN
IMAGE1](NCORE_IN_IMAGE1.md),
[PHON_NSTRUCT](PHON_NSTRUCT.md),
[IBRION](IBRION.md)

------------------------------------------------------------------------


