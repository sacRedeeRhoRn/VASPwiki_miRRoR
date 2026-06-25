<!-- Source: https://vasp.at/wiki/index.php/PROJCAR | revid: 18105 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PROJCAR


The PROJCAR file contains
information about the projections of the Kohn-Sham orbitals onto the
localized orbitals specified with the [LOCPROJ](LOCPROJ.md)
tag. This file is built specifically to be human-readable but contains
the same information as the [LOCPROJ](LOCPROJ.md) file.

For every localized orbital that is generated, a line is written with
the following information:

- ISITE: the index of the site in the [POSCAR](../input-files/POSCAR.md)
  file.
- R: the position in fractional coordinates.
- Radial type: can be one of "PAW projector","PS partial wave",
  "Hydrogen-like" depending on the choice of **Pr**, **Ps** or **Hy**,
  respectively.

Then, for each Kohn-Sham orbital, the k point and spin indexes are
reported. For each band, VASP writes the value of the projection
$\langle \beta_{lm}^{\alpha}|S|\psi_{n\mathbf{k}}\rangle$ onto the different angular characters of the radial
function. To find a list of the possible angular character, go to
[LOCPROJ](LOCPROJ.md) and see the table in
**\<functions-Ylm-specs\>**.

## Related Tags and Sections\[<a href="/wiki/index.php?title=PROJCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[LOCPROJ](LOCPROJ.md)

------------------------------------------------------------------------


