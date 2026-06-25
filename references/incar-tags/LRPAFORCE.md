<!-- Source: https://vasp.at/wiki/index.php/LRPAFORCE | revid: 34943 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LRPAFORCE


LRPAFORCE = .TRUE. \|
.FALSE.  
Default: **LRPAFORCE** = .FALSE. 

Description: LRPAFORCE=.TRUE.
calculates forces in the random-phase approximation (RPA).

------------------------------------------------------------------------

Available as of VASP.6.1.

This tag can be optionally set in low-scaling [RPA
calculations](../methods/ACFDT__RPA_calculations.md)
or <a href="/wiki/GW_calculations#RPAFORCES" class="mw-redirect"
title="GW calculations">GW calculations</a>. It allows computing the
<a href="/wiki/Forces#RPA-forces" class="mw-redirect" title="Forces">RPA
forces</a><sup>[\[1\]](#cite_note-ramberger:prl:118-1)</sup>
on each ion. Setting

    ALGO = RPAR ;  LRPAFORCE = .TRUE. 

or equivalently

    ALGO = G0W0R ; LRPAFORCE = .TRUE. 

determines the RPA total energy with corresponding forces and the
quasiparticle energies within the GW approximation.

The LRPAFORCE tag can be used
in combination with the standard relaxation options
[IBRION](IBRION.md) and [NSW](NSW.md) as explained
in the corresponding [RPA calculations
guide](../methods/ACFDT__RPA_calculations.md).

Generally, the energy calculated by the RPA can be quite noisy as a
function of the ionic positions, in particular, if
[PRECFOCK](PRECFOCK.md) = FAST and
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a> = 1 is set (these are the default
values for RPA calculations). Most of the noise is related to the exact
exchange energy, and we are working on methods to improve this issue.
Currently, to reduce the noise in the energy and forces, it is sensible
to set [PRECFOCK](PRECFOCK.md) = Normal (typically
doubling the execution time and memory requirement). It is also possible
to set <a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a> = -1 (which implicitly sets
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a> = 0). This makes the correlation
energies and the related forces less noisy, but technically less
accurate (i.e. part of the correlation energy will be missing at high
transition energies). Overall, RPA forces must be used carefully and
only after extensive testing of all relevant parameters.

|  |
|----|
| **Mind:** The RPA stress tensor is not available. |

|  |
|----|
| **Warning:** Only [ISIF](ISIF.md)=0 is supported. |

|  |
|----|
| **Warning:** Using [`LDAU`](LDAU.md)` = .TRUE.` with LRPAFORCE introduces double counting errors prior to version 6.6.0. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LRPAFORCE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](IBRION.md), [NSW](NSW.md),
[ALGO](ALGO.md), [NBANDS](NBANDS.md),
<a href="/wiki/NMAXFOCKAE" class="mw-redirect"
title="NMAXFOCKAE">NMAXFOCKAE</a>, [RPA
calculations](../methods/ACFDT__RPA_calculations.md),
<a href="/wiki/GW_calculations#RPAFORCES" class="mw-redirect"
title="GW calculations">GW calculations</a> [Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LRPAFORCE-_incategory-Examples)

------------------------------------------------------------------------

## References\[<a
href="/wiki/index.php?title=LRPAFORCE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-ramberger:prl:118_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.118.106403"
    class="external text" rel="nofollow">B. Ramberger, T. Schäfer and G.
    Kresse, Phys. Rev. Lett <strong>118</strong>, 106403 (2017).</a>


