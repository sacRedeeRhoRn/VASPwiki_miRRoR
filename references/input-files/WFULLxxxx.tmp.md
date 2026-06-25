<!-- Source: https://vasp.at/wiki/index.php/WFULLxxxx.tmp | revid: 30528 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WFULLxxxx.tmp


These files store the full-screened exchange $W$, needed
for BSE calculations. The *xxxx* in the name corresponds to integer
values labeling the k-point index. During the BSE calculations, VASP
will first try to read the
WFULLxxxx.tmp files, and then,
if these are missing, the [Wxxxx.tmp](Wxxxx.tmp.md)
files. In the low-scaling *GW* algorithm use
[NOMEGA_DUMP](../incar-tags/NOMEGA_DUMP.md) to produce the
WFULLxxxx.tmp files. For small
isotropic (jellium-like) bulk systems, results with the
[Wxxxx.tmp](Wxxxx.tmp.md) might be similar to the results
obtained using the
WFULLxxxx.tmp files. However,
for molecules and atoms as well as surfaces it is strictly required to
use the full-screened Coulomb kernel.

------------------------------------------------------------------------


