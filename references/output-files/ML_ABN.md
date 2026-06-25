<!-- Source: https://vasp.at/wiki/index.php/ML_ABN | revid: 32827 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_ABN


In context of the machine-learned force fields method this file serves
as an output for the collected training data set. When running VASP with
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select` it is
automatically written out whenever a learning step is performed. The
file format is shared with the [ML_AB](../input-files/ML_AB.md) input file,
for further details please have a look at the
[ML_AB](../input-files/ML_AB.md) Wiki entry. An
ML_ABN file can be reused as a
starting point for continuation runs
([`ML_MODE`](../incar-tags/ML_MODE.md)` = train`) and local reference
configuration re-selection runs
([`ML_MODE`](../incar-tags/ML_MODE.md)` = select`) simply by renaming (or
copying) it to [ML_AB](../input-files/ML_AB.md).

------------------------------------------------------------------------


