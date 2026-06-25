<!-- Source: https://vasp.at/wiki/index.php/LZORA | revid: 36619 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LZORA


LZORA = \[logical\]  
Default: **LZORA** = .False. 

Description:
`LZORA`` = .True.` yields ZORA
scalar-relativistic chemical shieldings in
[NMR](../categories/Category-NMR.md).

------------------------------------------------------------------------

The zeroth-order regular approximation
(ZORA)<sup>[\[1\]](#cite_note-lenthe:jcp:1993-1)</sup>
is a way to approximate the fully relativistic Dirac equation while
keeping a two-component formalism. It captures relativistic effects
without solving the full four-component Dirac equation. ZORA can be used
in two flavors: scalar-relativistic ZORA (no spin dependence) and
spin–orbit ZORA (includes spin-orbit coupling explicitly).

`LZORA`` = .True.` allows
accounting for the ZORA K factor in the computation of [nuclear magnetic
resonance](../categories/Category-NMR.md) (NMR) chemical shielding
tensors within linear response theory
([LCHIMAG](LCHIMAG.md)) on the level of the
scalar-relativistic ZORA. Scalar ZORA calculations can be executed using
`vasp_std`.

|  |
|----|
| **Warning:** We do **not** recommend using `LZORA`` = T` and [`LSOSHIFT`](LSOSHIFT.md)` = T` together, since it gives worse results, although being formally correct.<sup>[\[2\]](#cite_note-speelman:jcp:2025-2)</sup> |

|  |
|----|
| **Mind:** This tag is only supported as of VASP.6.6.0. |

## Related tags and articles\[<a href="/wiki/index.php?title=LZORA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md),
[LSOSHIFT](LSOSHIFT.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LZORA-_incategory-Howto)

## References\[<a href="/wiki/index.php?title=LZORA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-lenthe:jcp:1993_1-0)
    <a href="https://doi.org/10.1063/1.466059" class="external text"
    rel="nofollow">E. van Lenthe, E. J. Baerends, and J. G. Snijders,
    <em>Relativistic regular two-component Hamiltonians</em>, J. Chem. Phys.
    <strong>99</strong>, 4597 (1993).</a>
2.  [↑](#cite_ref-speelman:jcp:2025_2-0)
    <a href="https://doi.org/10.1063/5.0278794" class="external text"
    rel="nofollow">T. Speelman, M.-T. Huebsch, R.W.A. Havenith, M. Marsman,
    G.A. de Wijs, <em>NMR chemical shielding for solid-state systems using
    spin-orbit coupled ZORA GIPAW</em>, J. Chem. Phys. <strong>163</strong>,
    104115 (2025).</a>


