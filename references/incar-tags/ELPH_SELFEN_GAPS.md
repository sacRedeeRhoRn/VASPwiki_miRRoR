<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_GAPS | revid: 33009 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_GAPS


ELPH_SELFEN_GAPS =
\[logical\]  
Default: **ELPH_SELFEN_GAPS** = .FALSE. 

Description: Find the direct and indirect gaps and the valence and
conduction Kohn-Sham states that form it and select to compute their
self-energy due to electron-phonon coupling.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

This tag additionally activates the reporting of the value of the
band-gap renormalization to the standard output, the
[OUTCAR](../output-files/OUTCAR.md) file

     $ grep -A7 'KS-QP gap (meV)' OUTCAR

and the [vaspout.h5](../output-files/Vaspout.h5.md) file under

     $ h5ls -r vaspout.h5 | grep gap_renorm
     /results/electron_phonon/electrons/self_energy_1/direct_gap_renorm
     /results/electron_phonon/electrons/self_energy_1/fundamental_gap_renorm`

This output is reported once for each [electron-phonon
accumulator](../misc/Electron-phonon_accumulators.md).

If instead, the computation of the self-energy for a particular set of
states is desired, those can be manually specified using a combination
of [ELPH_SELFEN_KPTS](ELPH_SELFEN_KPTS.md),
[ELPH_SELFEN_IKPT](ELPH_SELFEN_IKPT.md),
[ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
and
[ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_GAPS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Electron-phonon
  accumulators](../misc/Electron-phonon_accumulators.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_BAND_START](ELPH_SELFEN_BAND_START.md)
- [ELPH_SELFEN_BAND_STOP](ELPH_SELFEN_BAND_STOP.md)


