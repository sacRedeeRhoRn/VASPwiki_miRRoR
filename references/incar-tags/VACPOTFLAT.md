<!-- Source: https://vasp.at/wiki/index.php/VACPOTFLAT | revid: 23548 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VACPOTFLAT
VACPOTFLAT = \[real\]  
Default: **VACPOTFLAT** = 0.1 

Description: Maximum permissible 2D-averaged electric field for a region
considered to be field-free in eV/Å.

------------------------------------------------------------------------

A region of space is considered to be field-free if the 2D-averaged
electric field ([LVACPOTAV](LVACPOTAV.md)=True) is
smaller than VACPOTFLAT.

|  |
|----|
| **Tip:** Increase VACPOTFLAT for a quick estimation of the vacuum potential and decrease for a precise value. If the cell is large and [EDIFF](EDIFF.md) small, the final result of [LVACPOTAV](LVACPOTAV.md) should be independent of VACPOTFLAT. |

## Related tags and articles
[LVACPOTAV](LVACPOTAV.md), [LVTOT](LVTOT.md),
[LVHAR](LVHAR.md),
[WRT_POTENTIAL](WRT_POTENTIAL.md),
[DIPOL](DIPOL.md), [LDIPOL](LDIPOL.md),
[IDIPOL](IDIPOL.md)
