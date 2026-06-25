<!-- Source: https://vasp.at/wiki/index.php/Wxxxx.tmp | revid: 15070 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Wxxxx.tmp


These files store only the diagonal elements of the screened exchange
$W$ needed for BSE calculations and are therefore fairly
small compared to the
[WFULLxxxx.tmp](WFULLxxxx.tmp.md) files which store
the full matrix. The *xxxx* in the name corresponds to integer values
labeling the k-point index. During the BSE calculations, VASP will first
try to read the [WFULLxxxx.tmp](WFULLxxxx.tmp.md)
files, and then, if these are missing, the
Wxxxx.tmp files. For small
isotropic (jellium-like) bulk systems, results with the
Wxxxx.tmp might be similar to
the results obtained using the
[WFULLxxxx.tmp](WFULLxxxx.tmp.md) files. However, for
molecules and atoms as well as surfaces it is strictly required to use
the full-screened Coulomb kernel $W$.

------------------------------------------------------------------------


