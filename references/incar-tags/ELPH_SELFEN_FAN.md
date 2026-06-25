<!-- Source: https://vasp.at/wiki/index.php/ELPH_SELFEN_FAN | revid: 27936 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_SELFEN_FAN


ELPH_SELFEN_FAN =
\[logical\]  
Default: **ELPH_SELFEN_FAN** = .FALSE. 

Description: Controls whether the Fan-Migdal contribution is included in
the calculation of the phonon-induced electron self-energy.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The phonon-induced electron self-energy has two contributions at second
order in perturbation theory, the Fan-Migdal self-energy and the
real-valued Debye-Waller self-energy.
ELPH_SELFEN_FAN controls the
computation of the former, while the latter can be computed via
[ELPH_SELFEN_DW](ELPH_SELFEN_DW.md).

The result is reported individually for each self-energy accumulator in
the [vaspout.h5](../output-files/Vaspout.h5.md) file as

    /results/electron_phonon/electrons/self_energy_1/selfen_fan

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_SELFEN_FAN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)
- [ELPH_SELFEN_STATIC](ELPH_SELFEN_STATIC.md)


