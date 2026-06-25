<!-- Source: https://vasp.at/wiki/index.php/LVDW_ONECELL | revid: 16913 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVDW_ONECELL


LVDW_ONECELL =
\[logical\]\[logical\]\[logical\]  
Default: **LVDW_ONECELL** = .FALSE. .FALSE. .FALSE. 

Description: LVDW_ONECELL  can
be used to disable vdW interaction with mirror image in X Y Z direction.
This is advisable for molecular calculations in the gas phase. In all
other cases, use the default.

Note: There is some confusing documentation on the ASE pages, which
states that ".TRUE. .TRUE. .TRUE." enables the interaction with
neighboring cells. However, the opposite is the case and *.TRUE.*
disables the interaction (".FALSE. .FALSE. .FALSE." = interactions
switched on, ".TRUE. .TRUE. .TRUE." = interactions switched off).

------------------------------------------------------------------------

## Related tags and articles\[<a
href="/wiki/index.php?title=LVDW_ONECELL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md), [Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md),

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LVD_ONECELL-_incategory-Examples)

------------------------------------------------------------------------


