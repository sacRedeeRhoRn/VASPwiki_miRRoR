<!-- Source: https://vasp.at/wiki/index.php/MSDGW_SEED | revid: 33475 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MSDGW SEED


MSDGW_SEED = \[integer\]  
Default: **MSDGW_SEED** = 2 

Description: Seed for pseudo orbitals used by mixed
stochastic-deterministic compression
algorithm.<sup>[\[1\]](#cite_note-altman:prl:2024-1)</sup>

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

When set in combination with [MSDGW_F](../incar-tags/MSDGW_F.md),
MSDGW_SEED changes the random
phases of the stochastic orbitals determined by the compression
algorithm. [MSDGW_NXI](MSDGW_NXI.md) stochastic orbitals
$\lbrace |\xi_1\rangle, \cdots,|\xi_{N_\xi}\rangle \rbrace$ are determined from the original orbitals
$\lbrace|\phi_1\rangle,\cdots,|\phi_N\rangle\rbrace$
by drawing $N_\xi \times N$ pseudo numbers $0\le \alpha_{i n}< 1$ and forming the linear combinations
$|\xi_i \rangle = \sum_{n=1}^{N} e^{i 2\pi \alpha_{in}}|\phi_n\rangle$.

## Related tags and articles\[<a
href="/wiki/index.php?title=MSDGW_SEED&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[MSDGW_NXI](MSDGW_NXI.md),
[MSDGW_F](../incar-tags/MSDGW_F.md),
[MSDGW_NP](MSDGW_NP.md)

## References\[<a
href="/wiki/index.php?title=MSDGW_SEED&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-altman:prl:2024_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.132.086401"
    class="external text" rel="nofollow">Altman, A. R. and Kundu, S. and da
    Jornada, F. H., <em>Mixed Stochastic-Deterministic Approach for
    Many-Body Perturbation Theory Calculations</em>, Phys. Rev. Lett.
    <strong>132</strong>, 086401 (2024).</a>


------------------------------------------------------------------------


