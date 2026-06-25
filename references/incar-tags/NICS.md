<!-- Source: https://vasp.at/wiki/index.php/NICS | revid: 34570 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NICS


The NICS file contains the NMR
nucleus-independent chemical shielding (NICS) in ppm. It is written if
[NUCIND](NUCIND.md) = .TRUE. is set and no
[POSNICS](POSNICS.md) is present. The format is the same as
[CHGCAR](../input-files/CHGCAR.md) with a header to define the grid and
then 9 blocks that correspond to the indices of the chemical shielding
tensor $\sigma_{ij}$: $\sigma_{xx}$, $\sigma_{xy}$, $\sigma_{xz}$, $\sigma_{yx}$, $\sigma_{yy}$, $\sigma_{yz}$, $\sigma_{zx}$, $\sigma_{zy}$, and $\sigma_{zz}$.

## Related tags and articles\[<a href="/wiki/index.php?title=NICS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [NUCIND](NUCIND.md),
[LNICSALL](LNICSALL.md)


