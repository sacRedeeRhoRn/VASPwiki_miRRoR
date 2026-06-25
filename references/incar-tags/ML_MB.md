<!-- Source: https://vasp.at/wiki/index.php/ML_MB | revid: 32824 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MB


ML_MB = \[integer\]  
Default: **ML_MB** = see below 

Description: This tag sets the maximum number of local reference
configurations (i.e. basis functions in the kernel) in the machine
learning force field method.

------------------------------------------------------------------------

The defaults for ML_MB are
different for each different [ML_MODE](ML_MODE.md) setting.
Here are the defaults for each mode:

- [`ML_MODE`](ML_MODE.md)` = train`:
  - No [ML_AB](../input-files/ML_AB.md) present (learning from scratch):
    `min(1500 , max(`[`NSW`](NSW.md)` , 2*`[`ML_MCONF_NEW`](ML_MCONF_NEW.md)` * MAXAT_SP)`
  - [ML_AB](../input-files/ML_AB.md) present (continuation of learning):
    `MB_AB + min(1500, max(`[`NSW`](NSW.md)` , 2*`[`ML_MCONF_NEW`](ML_MCONF_NEW.md)` * MAXAT_SP)`
- [`ML_MODE`](ML_MODE.md)` = select`:
  `MB_AB + `[`ML_MCONF_NEW`](ML_MCONF_NEW.md)` * MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = refit`: `MB_AB + MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = refitbayesian`:
  `MB_AB + MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = run`: `MB_AB`

using the following definitions:

- `MAXAT_SP` = greatest number of atoms within all species among the
  current structures and the structures in the
  [ML_AB](../input-files/ML_AB.md) file (if present).
- `MB_AB` = greatest number of local reference configurations within all
  species in the [ML_AB](../input-files/ML_AB.md) file.

The default value for [`ML_MODE`](ML_MODE.md)` = train` and
[`ML_MODE`](ML_MODE.md)` = select` is a relatively safe
value for most materials. However one might need to increase it to a
greater value for liquids, polymers and amorphous systems, or when a
MLFF for many different polytypes is trained. By default
([`ML_LBASIS_DISCARD`](ML_LBASIS_DISCARD.md)` = .TRUE.`),
if the number of local reference configurations would exceed
ML_MB, VASP would continue the
calculation and disposes of these, but one should make extensive tests
whether the generated MLFF is sufficiently accurate.

If VASP stops, subsequent training can be restarted from the existing
ML_AB file. This avoids loss of already acquired training data.

Depending on the calculation mode VASP adds a little overhead in the
allocation of ML_MB arrays to
buffer for new candidate structures. Here are the buffer sizes for each
mode:

- [`ML_MODE`](ML_MODE.md)` = train`:
  - No [ML_AB](../input-files/ML_AB.md) present (learning from scratch):
    `min(`[`NSW`](NSW.md)` , `[`ML_MCONF_NEW`](ML_MCONF_NEW.md)`) * MAXAT_SP`
  - [ML_AB](../input-files/ML_AB.md) present (continuation of learning):
    `min(`[`NSW`](NSW.md)` , `[`ML_MCONF_NEW`](ML_MCONF_NEW.md)`) * MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = select`:
  [`ML_MCONF_NEW`](ML_MCONF_NEW.md)` * MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = refit`: `MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = refitbayesian`: `MAXAT_SP`
- [`ML_MODE`](ML_MODE.md)` = run`: `0`

The flag ML_MB also determines
the maximum number of rows of the design matrix. This is usually a huge
matrix. The design matrix is allocated statically at the beginning of
the run, since several parts of the code use MPI shared memory and
dynamic reallocation of these arrays can cause issues on many operating
systems. An estimate of the size of the design matrix and all other
large arrays is printed out to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md) before allocation. The
design matrix is fully distributed in a block-cyclic fashion for
scaLAPACK, and thus the memory requirement for each core scales
inversely proportional to the number of used cores.

## Related tags and articles\[<a href="/wiki/index.php?title=ML_MB&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_MCONF](ML_MCONF.md),
[ML_LBASIS_DISCARD](ML_LBASIS_DISCARD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MB-_incategory-Examples)

------------------------------------------------------------------------


