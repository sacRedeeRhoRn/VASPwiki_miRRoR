<!-- Source: https://vasp.at/wiki/index.php/LALL_IN_ONE | revid: 24254 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LALL IN ONE
LALL_IN_ONE = .FALSE. \| .TRUE. 

[TABLE]

Description: LALL_IN_ONE=.TRUE. enables the all-in-one mode for
[many-body perturbation
theory](../redirects/Many-body_perturbation_theory.md)
calculations, i.e.,
[ALGO](ALGO.md)=[ACFDT\[R\]](/wiki/ACFDT/RPA_calculations "ACFDT/RPA calculations"),
[\[EV\]GW0\[R\]](/wiki/Practical_guide_to_GW_calculations "Practical guide to GW calculations"),
[GWR](../methods/Practical_guide_to_GW_calculations.md).

|                                      |
|--------------------------------------|
| **Mind:** available as of VASP.6.4.0 |

------------------------------------------------------------------------

In the all-in-one mode, VASP automatically performs the necessary DFT
steps prior to the many-body perturbation theory (MBPT) calculation,
i.e. a DFT calculation with [NBANDS](NBANDS.md), followed by
an exact diagonalization of the Kohn-Sham Hamiltonian with
[NBANDSEXACT](NBANDSEXACT.md) bands. Note,
[NBANDSEXACT](NBANDSEXACT.md) is set by default to the
maximum number of plane-waves given by the chosen energy cutoff for the
orbitals [ENCUT](ENCUT.md). In the all-in-one mode, the
actual GW/RPA calculation is also performed with
[NBANDSEXACT](NBANDSEXACT.md) bands. If
[NBANDS_WAVE](NBANDS_WAVE.md) is not set, all orbitals
are written to [WAVECAR](../input-files/WAVECAR.md), which potentially
becomes huge in file size.

|  |
|----|
| **Tip:** The [NBANDS_WAVE](NBANDS_WAVE.md) tag can be used to limit the number of bands written to [WAVECAR](../input-files/WAVECAR.md) if LALL_IN_ONE=.TRUE. |

The all-in-one mode is automatically enabled for
[ALGO](ALGO.md)=\[EV\]GW\[0\]R, RPA\[R\],ACFDT\[R\] if
[NBANDS](NBANDS.md) is not set.

## Related tags and articles
[ALGO](ALGO.md), [NBANDS](NBANDS.md),
[NBANDSEXACT](NBANDSEXACT.md),
[NBANDS_WAVE](NBANDS_WAVE.md),
[IALL_IN_ONE](IALL_IN_ONE.md)

------------------------------------------------------------------------
