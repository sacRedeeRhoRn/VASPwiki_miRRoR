<!-- Source: https://vasp.at/wiki/index.php/LORBITALREAL | revid: 31123 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LORBITALREAL
LORBITALREAL = .TRUE. \| .FALSE. 

|                           |           |     |
|---------------------------|-----------|-----|
| Default: **LORBITALREAL** | = .FALSE. |     |

Description: LORBITALREAL forces VASP to make the orbitals
$\phi({\bf r})$ real-valued at the Gamma
point and the Brillouin zone boundary.

------------------------------------------------------------------------

This is done by performing a Fourier transform of the orbitals to real
space. Then the real part of the orbitals is transformed back to
reciprocal space and the resulting orbitals are orthogonalized.

If many degenerate orbitals are present, taking the real part can lead
to linearly dependent orbitals. One can ensure that this problem does
not occur by running the mean-field calculation starting from the
[WAVECAR](../input-files/WAVECAR.md) file with tags
[ALGO](ALGO.md)=SUBROT and LORBITALREAL =.TRUE..

## Related tags and articles
[ALGO](ALGO.md), [IALGO](IALGO.md)
