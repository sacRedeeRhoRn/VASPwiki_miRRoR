<!-- Source: https://vasp.at/wiki/index.php/IFC_ASR | revid: 32876 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IFC_ASR
IFC_ASR = \[integer\]  
Default: **IFC_ASR** = 1 

Description: If positive, enforces the acoustic sum rule on the
interatomic force constants during an electron-phonon calculation.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The matrix of interatomic force constants (IFC) should obey the
so-called acoustic sum rule (ASR). However, due to numerical
inaccuracies, it is possible that the ASR is slightly broken in
practice. In such cases, the phonons obtained from the [Fourier
interpolation of the IFC
matrix](../tutorials/Computing_the_phonon_dispersion_and_DOS.md)
can become imaginary.

By setting `IFC_ASR`` > 0`, the ASR is explicitly enforced on the IFC
matrix via an iterative scheme. The number of iterations is also given
by IFC_ASR.

|  |
|----|
| **Mind:** `IFC_ASR`` = -2` has a special meaning. Usually, the IFC matrix is forced to be symmetric. However, if `IFC_ASR`` = -2`, then the IFC matrix is neither forced to be symmetric nor is the ASR applied. We do not recommend to use this setting. |

## Related tags and articles
- [ELPH_RUN](ELPH_RUN.md)
- [ELPH_IGNORE_IMAG_PHONONS](ELPH_IGNORE_IMAG_PHONONS.md)
