<!-- Source: https://vasp.at/wiki/index.php/LSOSHIFT | revid: 34271 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSOSHIFT


LSOSHIFT  = \[logical\]  
Default: **LSOSHIFT** = LSORBIT 

Description:
`LSOSHIFT`` = .True.`
activates spin–orbit coupling (SOC) contributions to the calculated
chemical shielding tensor in [NMR](../categories/Category-NMR.md).

------------------------------------------------------------------------

`LSOSHIFT`` = .True.` allows
accounting for spin-orbit coupling (SOC) for the computation of [nuclear
magnetic resonance](../categories/Category-NMR.md) (NMR) chemical
shielding tensors within linear response theory
([LCHIMAG](LCHIMAG.md)). SOC contributions are essential
for accurate shielding predictions for heavy elements where spin–orbit
effects influence the induced magnetic responses.

The relativistic effects are included on the level of the spin-orbit
zeroth-order regular approximation (ZORA)
<sup>[\[1\]](#cite_note-lenthe:jcp:1993-1)</sup>
employing the gauge-including projector augmented waves (GIPAW)
approach. The implementation and benchmarks are presented by Speelman et
al.<sup>[\[2\]](#cite_note-speelman:jcp:2025-2)</sup>.
These calculations require the executable `vasp_ncl`.

|  |
|----|
| **Warning:** We do **not** recommend using [`LZORA`](LZORA.md)` = T` and `LSOSHIFT`` = T` together, since it gives worse results, although being formally correct.<sup>[\[2\]](#cite_note-speelman:jcp:2025-2)</sup> |

|  |
|----|
| **Mind:** This tag is only supported as of VASP.6.6.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=LSOSHIFT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LSORBIT](LSORBIT.md), [LCHIMAG](LCHIMAG.md),
[LZORA](LZORA.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-_LSOSHIFT_-_incategory-Howto)

## References\[<a href="/wiki/index.php?title=LSOSHIFT&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-lenthe:jcp:1993_1-0)
    <a href="https://doi.org/10.1063/1.466059" class="external text"
    rel="nofollow">E. van Lenthe, E. J. Baerends, and J. G. Snijders,
    <em>Relativistic regular two-component Hamiltonians</em>, J. Chem. Phys.
    <strong>99</strong>, 4597 (1993).</a>
2.  ↑
    <sup>[a](#cite_ref-speelman:jcp:2025_2-0)</sup>
    <sup>[b](#cite_ref-speelman:jcp:2025_2-1)</sup>
    <a href="https://doi.org/10.1063/5.0278794" class="external text"
    rel="nofollow">T. Speelman, M.-T. Huebsch, R.W.A. Havenith, M. Marsman,
    G.A. de Wijs, <em>NMR chemical shielding for solid-state systems using
    spin-orbit coupled ZORA GIPAW</em>, J. Chem. Phys. <strong>163</strong>,
    104115 (2025).</a>


