<!-- Source: https://vasp.at/wiki/index.php/SCISSOR | revid: 25097 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SCISSOR
SCISSOR = \[real\] 

|                      |     |     |
|----------------------|-----|-----|
| Default: **SCISSOR** | = 0 |     |

Description: SCISSOR specifies the shift for the scissor operator in eV.

------------------------------------------------------------------------

The scissor operator in [BSE](../redirects/BSE_calculations.md)
and [GW](../redirects/GW_calculations.md) calculations shifts
the unoccupied states relative to the valence
states^([\[1\]](#cite_note-vincenzo:prb:1995-1)). For example, the
scissor operator can be used in the BSE calculations to match the band
gap to the known experimental value, thus achieving the right offset in
the calculated spectrum. Notably, unlike the self-energy operator in GW,
the scissor operator applies a universal shift to all conduction states,
i.e., the shift is independent of energy or momentum and leaves the
valence states unchanged. The scissor operator only shifts empty states,
thus partially occupied orbitals are not affected by it.

## Related tags and articles
[BSE calculations](../redirects/BSE_calculations.md)

## References
1.  [↑](#cite_ref-vincenzo:prb:1995_1-0) [V. Fiorentini and A.
    Baldereschi, *Dielectric scaling of the self-energy scissor operator
    in semiconductors and insulators*, Phys. Rev. B *51*, 17196-17198
    (1995)](http://doi.org/10.1103/PhysRevB.51.17196)

------------------------------------------------------------------------
