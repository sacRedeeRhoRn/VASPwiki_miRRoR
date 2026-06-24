<!-- Source: https://vasp.at/wiki/index.php/LNMRLEG | revid: 34241 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNMRLEG
LNMRLEG = .TRUE.\| .FALSE. 

|                      |           |     |
|----------------------|-----------|-----|
| Default: **LNMRLEG** | = .FALSE. |     |

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

Description: LNMRLEG controls whether VASP prints NMR properties to
[OUTCAR](../output-files/OUTCAR.md) according to the old format (pre-version
6.6.0).

------------------------------------------------------------------------

In version 6.6.0, the output format for NMR properties was updated. The
legacy format is as presented below (see
[LCHIMAG](LCHIMAG.md) for the current version). The
chemical shielding tensors, `UNSYMMETRIZED TENSORS` and
`SYMMETRIZED TENSORS` are printed. From the three diagonal values of the
symmetrized tensor, the isotropic chemical "shift"
$\delta_{\mathrm{iso}}\mathrm{\[VASP\]}$, span $\Omega$, and skew
$\kappa$ are calculated and printed, see
Ref. ^([\[1\]](#cite_note-mason:ssn:1993-1)) for unambiguous
definitions. Note that $\kappa$ is
ill-defined if $\Omega = 0$. Units are
ppm, except for the skew. A typical output is given below:

                                                                                                              
       ---------------------------------------------------------------------------------
        CSA tensor (J. Mason, Solid State Nucl. Magn. Reson. 2, 285 (1993))
       ---------------------------------------------------------------------------------
                   EXCLUDING G=0 CONTRIBUTION             INCLUDING G=0 CONTRIBUTION
               -----------------------------------   -----------------------------------
        ATOM    ISO_SHIFT        SPAN        SKEW     ISO_SHIFT        SPAN        SKEW
       ---------------------------------------------------------------------------------
        (absolute, valence only)
           1    4598.8125      0.0000      0.0000     4589.9696      0.0000      0.0000
           2     291.5486      0.0000      0.0000      282.7058      0.0000      0.0000
           3     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
           4     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
           5     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
       ---------------------------------------------------------------------------------
        (absolute, valence and core)
           1   -6536.1417      0.0000      0.0000    -6547.9848      0.0000      0.0000
           2   -5706.3864      0.0000      0.0000    -5718.2296      0.0000      0.0000
           3   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
           4   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
           5   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
       ---------------------------------------------------------------------------------
        IF SPAN.EQ.0, THEN SKEW IS ILL-DEFINED
       ---------------------------------------------------------------------------------

The isotropic chemical shielding for each atom, excluding and including
G=0 contributions, as well as the span and skew (descriptions of
asymmetry), follow. Finally, core contributions are taken into account
for the `ISO_SHIFT`, `SPAN`, and `SKEW`.

[TABLE]

|  |
|----|
| **Mind:** In legacy mode, the chemical shift (the negative of the chemical shielding) is always printed, even if [LNMRSHIELD](LNMRSHIELD.md) = .TRUE.. |

## Related tags and articles
[LCHIMAG](LCHIMAG.md),
[INMRPRINT](INMRPRINT.md)

## References
1.  [↑](#cite_ref-mason:ssn:1993_1-0) [J. Mason, *Conventions for the
    reporting of nuclear magnetic shielding (or shift) tensors suggested
    by participants in the NATO ARW on NMR shielding constants at the
    University of Maryland, College Park, July 1992*, Solid State Nucl.
    Magn. Reson. **2**, 285
    (1993).](https://doi.org/10.1016/0926-2040(93)90010-K)
2.  [↑](#cite_ref-gregor:jcp:1999_2-0) [T. Gregor, F. Mauri, and R. Car,
    *A comparison of methods for the calculation of NMR chemical
    shifts*, J. Chem. Phys. **111**, 1815
    (1999).](https://doi.org/10.1063/1.479451)
