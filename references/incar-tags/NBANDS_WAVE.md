<!-- Source: https://vasp.at/wiki/index.php/NBANDS_WAVE | revid: 24555 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NBANDS_WAVE
NBANDS_WAVE = \[integer\] 

[TABLE]

Description: NBANDS_WAVE specifies the number of bands written to
[WAVECAR](../input-files/WAVECAR.md) in the all-in-one mode of [many-body
perturbation
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
[NBANDSEXACT](NBANDSEXACT.md) bands. If NBANDS_WAVE is
not set, all orbitals are written to [WAVECAR](../input-files/WAVECAR.md),
which potentially becomes huge in file size.

|  |
|----|
| **Tip:** The NBANDS_WAVE tag can be used to limit the number of bands written to [WAVECAR](../input-files/WAVECAR.md) if [LALL_IN_ONE](LALL_IN_ONE.md)=.TRUE. |

The all-in-one mode is automatically enabled for
[ALGO](ALGO.md)=\[EV\]GW\[0\]R, RPA\[R\],ACFDT\[R\] if
[NBANDS](NBANDS.md) is not set.

## Related tags and articles
[ALGO](ALGO.md), [NBANDS](NBANDS.md)
[NBANDSEXACT](NBANDSEXACT.md)
[IALL_IN_ONE](IALL_IN_ONE.md)
[LALL_IN_ONE](LALL_IN_ONE.md)

------------------------------------------------------------------------
