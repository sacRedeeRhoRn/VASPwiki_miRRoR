<!-- Source: https://vasp.at/wiki/index.php/EDIFFG | revid: 32794 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EDIFFG
EDIFFG = \[real\]  
Default: **EDIFFG** = [EDIFF](EDIFF.md)×10 

Description: EDIFFG defines the break condition for the ionic relaxation
loop.

------------------------------------------------------------------------

When EDIFFG is positive, the relaxation is stopped when the change of
the total energy is smaller than EDIFFG between two ionic steps.

When EDIFFG is negative, the relaxation is stopped when the norms of all
the forces are smaller than \|EDIFFG\|. This is usually a more
convenient setting.

If EDIFFG = 0, the ionic relaxation is stopped after
[NSW](NSW.md) steps.

|  |
|----|
| **Warning:** EDIFFG does not apply to [molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics) simulations. |

|  |
|----|
| **Tip:** You can get information at each electronic step using [`NWRITE`](NWRITE.md)` = 2,3`. |

## Related tags and articles
[EDIFF](EDIFF.md), [NWRITE](NWRITE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EDIFFG-_incategory-Examples)

------------------------------------------------------------------------
