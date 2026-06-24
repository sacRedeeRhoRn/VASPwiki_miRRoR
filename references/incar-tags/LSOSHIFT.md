<!-- Source: https://vasp.at/wiki/index.php/LSOSHIFT | revid: 34271 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSOSHIFT
LSOSHIFT  = \[logical\]  
Default: **LSOSHIFT** = LSORBIT 

Description: `LSOSHIFT`` = .True.` activates spin–orbit coupling (SOC)
contributions to the calculated chemical shielding tensor in
[NMR](../categories/Category-NMR.md).

------------------------------------------------------------------------

`LSOSHIFT`` = .True.` allows accounting for spin-orbit coupling (SOC)
for the computation of [nuclear magnetic
resonance](../categories/Category-NMR.md) (NMR) chemical shielding
tensors within linear response theory
([LCHIMAG](LCHIMAG.md)). SOC contributions are essential
for accurate shielding predictions for heavy elements where spin–orbit
effects influence the induced magnetic responses.

The relativistic effects are included on the level of the spin-orbit
zeroth-order regular approximation (ZORA)
^([\[1\]](#cite_note-lenthe:jcp:1993-1)) employing the gauge-including
projector augmented waves (GIPAW) approach. The implementation and
benchmarks are presented by Speelman et
al.^([\[2\]](#cite_note-speelman:jcp:2025-2)). These calculations
require the executable `vasp_ncl`.

|  |
|----|
| **Warning:** We do **not** recommend using [`LZORA`](LZORA.md)` = T` and `LSOSHIFT`` = T` together, since it gives worse results, although being formally correct.^([\[2\]](#cite_note-speelman:jcp:2025-2)) |

|                                                        |
|--------------------------------------------------------|
| **Mind:** This tag is only supported as of VASP.6.6.0. |

## Related tags and articles
[LSORBIT](LSORBIT.md), [LCHIMAG](LCHIMAG.md),
[LZORA](LZORA.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-_LSOSHIFT_-_incategory-Howto)

## References
1.  [↑](#cite_ref-lenthe:jcp:1993_1-0) [E. van Lenthe, E. J. Baerends,
    and J. G. Snijders, *Relativistic regular two-component
    Hamiltonians*, J. Chem. Phys. **99**, 4597
    (1993).](https://doi.org/10.1063/1.466059)
2.  ↑ ^([a](#cite_ref-speelman:jcp:2025_2-0))
    ^([b](#cite_ref-speelman:jcp:2025_2-1)) [T. Speelman, M.-T. Huebsch,
    R.W.A. Havenith, M. Marsman, G.A. de Wijs, *NMR chemical shielding
    for solid-state systems using spin-orbit coupled ZORA GIPAW*, J.
    Chem. Phys. **163**, 104115
    (2025).](https://doi.org/10.1063/5.0278794)
