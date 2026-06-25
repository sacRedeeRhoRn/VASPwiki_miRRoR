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
(ZORA)[^lenthe:jcp:1993-1]
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
| **Warning:** We do **not** recommend using `LZORA`` = T` and [`LSOSHIFT`](LSOSHIFT.md)` = T` together, since it gives worse results, although being formally correct.[^speelman:jcp:2025-2] |

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

[^lenthe:jcp:1993-1]: [E. van Lenthe, E. J. Baerends, and J. G. Snijders, *Relativistic regular two-component Hamiltonians*, J. Chem. Phys. **99**, 4597 (1993).](https://doi.org/10.1063/1.466059)
[^speelman:jcp:2025-2]: [T. Speelman, M.-T. Huebsch, R.W.A. Havenith, M. Marsman, G.A. de Wijs, *NMR chemical shielding for solid-state systems using spin-orbit coupled ZORA GIPAW*, J. Chem. Phys. **163**, 104115 (2025).](https://doi.org/10.1063/5.0278794)
