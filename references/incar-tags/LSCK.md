<!-- Source: https://vasp.at/wiki/index.php/LSCK | revid: 35875 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCK


LSCK = \[logical\]  
Default: **LSCK** = .FALSE. 

|  |
|----|
| **Important:** Up to vasp.6.2, the default was LSCK= .TRUE. |

------------------------------------------------------------------------

Description: LSCK=.True.
switches on the squeezed Coulomb kernel.

If LSCK is set to .TRUE., the
squeezed Coulomb kernel is used instead of the [cosine
window](ENCUTGWSOFT.md)
<sup>[\[1\]](#cite_note-riemelmoser:jcp:2020-1)</sup>:

$v_{G} = 4 \pi e^2 \frac{ (G_{max}-G_{min})(G_{max}-G) }{
(G_{min}^2 - G(2G_{min}-G_{max}))^2 } \qquad \mbox{for} \quad
\mathrm{ENCUTGWSOFT}=\frac{\hbar^2G_{min}^2}{2m_e}<\frac{\hbar^2
G^2}{2m_e}<\frac{\hbar^2G_{max}^2}{2m_e}=\mathrm{ENCUTGW}$

This kernel 'squeezes' the contributions from large wave vectors
$G>G_{max}$ into the window given by
[ENCUTGWSOFT](ENCUTGWSOFT.md). Effectively, this
extrapolates the random-phase-approximation–correlation energy to the
[ENCUTGW](ENCUTGW.md) $\to \infty$
limit, assuming that the basis-set-incompleteness error falls off as
$1/$[ENCUTGW](ENCUTGW.md)$^{3/2}$.

## Related tags and articles\[<a href="/wiki/index.php?title=LSCK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ENCUTGW](ENCUTGW.md),
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a> [ACFDT/RPA
calculations](../methods/ACFDT__RPA_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCK-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-riemelmoser:jcp:2020_1-0)
    <a href="https://doi.org/10.1063/5.0002246" class="external text"
    rel="nofollow">S. Riemelmoser, M. Kaltak, and G. Kresse, J. Chem. Phys.
    <strong>152(13)</strong>, 134103 (2020).</a>


