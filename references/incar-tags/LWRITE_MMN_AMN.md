<!-- Source: https://vasp.at/wiki/index.php/LWRITE_MMN_AMN | revid: 18095 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWRITE_MMN_AMN


LWRITE_MMN_AMN = .TRUE. \|
.FALSE. 

|  |  |  |
|----|----|----|
| Default: **LWRITE_MMN_AMN** | = .TRUE. | if [LWANNIER90](LWANNIER90.md)=.TRUE. |
|  | = .FALSE. | otherwise |

Description:
LWRITE_MMN_AMN=.TRUE. tells
the VASP2WANNIER90 interface to write the **wannier90.mmn** and
**wannier90.amn** files.

------------------------------------------------------------------------

When running WANNIER90 in library mode
([LWANNIER90_RUN](LWANNIER90_RUN.md)=.TRUE.), the
**wannier90.mmn** and **wannier90.amn** files are not written. The
information these files normally contain is passed on to `wannier_run`
internally. If you want these files to be written anyway, for instance,
to be able to run WANNIER90 standalone later on, set
LWRITE_MMN_AMN=.TRUE. in the
[INCAR](../input-files/INCAR.md) file.

## Related tags and articles\[<a
href="/wiki/index.php?title=LWRITE_MMN_AMN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWANNIER90](LWANNIER90.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWRITE_MMN_AMN-_incategory-Examples)

------------------------------------------------------------------------


