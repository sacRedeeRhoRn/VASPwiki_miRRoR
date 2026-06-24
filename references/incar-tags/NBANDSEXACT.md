<!-- Source: https://vasp.at/wiki/index.php/NBANDSEXACT | revid: 24272 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDSEXACT
NBANDSEXACT = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **NBANDSEXACT** | = -1 | for [LALL_IN_ONE](LALL_IN_ONE.md)=.FALSE. |
|  | = maximum number of plane waves | for [LALL_IN_ONE](LALL_IN_ONE.md)=.TRUE. |

Description: NBANDSEXACT specifies the number of bands used in the
all-in-one mode of [many-body perturbation
theory](../redirects/Many-body_perturbation_theory.md)
calculations.

|                                      |
|--------------------------------------|
| **Mind:** available as of VASP.6.4.0 |

------------------------------------------------------------------------

In the all-in-one mode, VASP automatically performs the necessary DFT
steps prior to the many-body perturbation theory (MBPT) calculation,
i.e. a DFT calculation with [NBANDS](NBANDS.md), followed by
an exact diagonalization of the Kohn-Sham Hamiltonian with NBANDSEXACT
bands. Note, NBANDSEXACT is set by default to the maximum number of
plane-waves given by the chosen energy cutoff for the orbitals
[ENCUT](ENCUT.md). In the all-in-one mode, the actual GW/RPA
calculation is also performed with NBANDSEXACT bands. If
[NBANDS_WAVE](NBANDS_WAVE.md) is not set, all orbitals
are written to [WAVECAR](../input-files/WAVECAR.md), which potentially
becomes huge in file size.

|  |
|----|
| **Tip:** The [NBANDS_WAVE](NBANDS_WAVE.md) tag can be used to limit the number of bands written to [WAVECAR](../input-files/WAVECAR.md) if [LALL_IN_ONE](LALL_IN_ONE.md)=.TRUE. |

The all-in-one mode is automatically enabled for
[ALGO](ALGO.md)=\[EV\]GW\[0\]R, RPA\[R\],ACFDT\[R\] if
[NBANDS](NBANDS.md) is not set.

## Related tags and articles
[ALGO](ALGO.md), [NBANDS](NBANDS.md)
[NBANDS_WAVE](NBANDS_WAVE.md)
[LALL_IN_ONE](LALL_IN_ONE.md)
[IALL_IN_ONE](IALL_IN_ONE.md)

------------------------------------------------------------------------
