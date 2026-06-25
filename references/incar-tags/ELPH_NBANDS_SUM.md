<!-- Source: https://vasp.at/wiki/index.php/ELPH_NBANDS_SUM | revid: 32868 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_NBANDS_SUM


ELPH_NBANDS_SUM = \[integer
array\]  
Default: **ELPH_NBANDS_SUM** =
[ELPH_NBANDS](ELPH_NBANDS.md) 

Description: Number of intermediate states to include in the computation
of the phonon-induced electron self-energy.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The computation of the self-energy is achieved via a sum over
intermediate states $|\Psi_{m \mathbf{k} +
\mathbf{q}}\rangle$.
ELPH_NBANDS_SUM specifies the
maximum number of bands, $N_{\text{b}}$, such that $m$ runs from
$1
\ldots N_{\text{b}}$.

Multiple values can be specified for
ELPH_NBANDS_SUM, in which case
the self-energy is computed once for each value. The results are
reported in separate groups inside the
[vaspout.h5](../output-files/Vaspout.h5.md) file:

    /results/electron_phonon/electrons/self_energy_1
    /results/electron_phonon/electrons/self_energy_2
    /results/electron_phonon/electrons/self_energy_3
    ...

This tag is useful for studying the convergence of the self-energy with
respect to the number of intermediate states. At a certain point,
including more bands in the summation over states should no longer
change the result.

|  |
|----|
| **Mind:** When computing the renormalization of the electronic bandstructure, a large number of intermediate states may be necessary to reach convergence. If the self-energy still changes noticeably around `ELPH_NBANDS_SUM`` = `[`ELPH_NBANDS`](ELPH_NBANDS.md), then you may have to increase [ELPH_NBANDS](ELPH_NBANDS.md). |

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_NBANDS_SUM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Bandstructure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_NBANDS](ELPH_NBANDS.md)
- [ELPH_SELFEN_FAN](ELPH_SELFEN_FAN.md)
- [ELPH_SELFEN_DW](ELPH_SELFEN_DW.md)


