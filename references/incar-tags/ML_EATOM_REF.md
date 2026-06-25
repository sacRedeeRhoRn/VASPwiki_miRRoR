<!-- Source: https://vasp.at/wiki/index.php/ML_EATOM_REF | revid: 32818 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_EATOM_REF


ML_EATOM_REF = \[real
array\]  
Default: **ML_EATOM_REF** = 0.0 

Description: Reference total energies of isolated atoms used in the
machine learning force field method.

------------------------------------------------------------------------

This tag is only used if
[`ML_ISCALE_TOTEN`](ML_ISCALE_TOTEN.md)` = 1`.

If ML_EATOM_REF is not
provided in the [INCAR](../input-files/INCAR.md) file then 0.0 is assumed
for all species in the system.

By default this tag is not used since all energies are scaled to the
average of the training data
([`ML_ISCALE_TOTEN`](ML_ISCALE_TOTEN.md)` = 2`).

If this tag is used, each reference energy should be obtained from a
VASP calculation of an isolated atoms in a sufficiently large simulation
box. The reference is then simply taken from the Helmholtz free energy
from the [OSZICAR](../output-files/OSZICAR.md) file (value following "1 F="
in that file).

The reference energies are simply set in one line as a list for each
species, i.e. like the following

    ML_EATOM_REF = E_1 E_2 E_3 ...

where E_1, E_2, E_2 etc. are the energies for species 1, 2, 3 etc.
(corresponding to the order they occur in the
[POTCAR](../input-files/POTCAR.md) file).

The unit of the energies is eV/atom.

|  |
|----|
| **Mind:** Reference energies are stored in the [ML_AB](../input-files/ML_AB.md) file and are reused whenever the file is read in, i.e, in case of a continued training ([`ML_MODE`](ML_MODE.md)` = train` with [ML_AB](../input-files/ML_AB.md) present), refitting ([`ML_MODE`](ML_MODE.md)` = refit`) or a re-selection run ([`ML_MODE`](ML_MODE.md)` = select`). However, since VASP 6.4.3 the values in the [INCAR](../input-files/INCAR.md) file take precedence, hence, reference energies from the [ML_AB](../input-files/ML_AB.md) file can be updated by providing new values for the ML_EATOM_REF tag in the [INCAR](../input-files/INCAR.md) file. In case you are unsure, check the [ML_LOGFILE](../output-files/ML_LOGFILE.md) which lists the values actually used. |

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_EATOM_REF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_ISCALE_TOTEN](ML_ISCALE_TOTEN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_EATOM_REF-_incategory-Examples)

------------------------------------------------------------------------


