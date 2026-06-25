<!-- Source: https://vasp.at/wiki/index.php/SCISSOR | revid: 25097 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SCISSOR


SCISSOR = \[real\] 

|                      |     |     |
|----------------------|-----|-----|
| Default: **SCISSOR** | = 0 |     |

Description: SCISSOR specifies
the shift for the scissor operator in eV.

------------------------------------------------------------------------

The scissor operator in
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE</a> and
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW</a> calculations shifts the unoccupied states
relative to the valence
states<sup>[\[1\]](#cite_note-vincenzo:prb:1995-1)</sup>.
For example, the scissor operator can be used in the BSE calculations to
match the band gap to the known experimental value, thus achieving the
right offset in the calculated spectrum. Notably, unlike the self-energy
operator in GW, the scissor operator applies a universal shift to all
conduction states, i.e., the shift is independent of energy or momentum
and leaves the valence states unchanged. The scissor operator only
shifts empty states, thus partially occupied orbitals are not affected
by it.

## Related tags and articles\[<a href="/wiki/index.php?title=SCISSOR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>

## References\[<a href="/wiki/index.php?title=SCISSOR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-vincenzo:prb:1995_1-0)
    <a href="http://doi.org/10.1103/PhysRevB.51.17196" class="external text"
    rel="nofollow">V. Fiorentini and A. Baldereschi, <em>Dielectric scaling
    of the self-energy scissor operator in semiconductors and
    insulators</em>, Phys. Rev. B <em>51</em>, 17196-17198 (1995)</a>


------------------------------------------------------------------------


