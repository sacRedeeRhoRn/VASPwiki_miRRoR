<!-- Source: https://vasp.at/wiki/index.php/LSYNCH5 | revid: 27700 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSYNCH5


LSYNCH5 = \[logical\]  
Default: **LSYNCH5** = .FALSE. 

Description: LSYNCH5
determines whether the output in
[vaspout.h5](../output-files/Vaspout.h5.md) is always synchronized with
VASP while the calculation is running.

------------------------------------------------------------------------

If you set this flag, VASP will enable single-writer-multiple-reader
mode for the HDF5 file. This allows you to monitor the output using
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> while the calculation
is still running.

|  |
|----|
| **Mind:** Synchronizing the HDF5 file continuously comes with a computational cost. Please do your own testing whether that is a bottleneck for your calculation. |

## Related tags and articles\[<a href="/wiki/index.php?title=LSYNCH5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LH5](LH5.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSYNCH5-_incategory-Examples)


