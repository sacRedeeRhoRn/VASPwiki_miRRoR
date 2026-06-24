<!-- Source: https://vasp.at/wiki/index.php/LFOCKACE | revid: 24256 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LFOCKACE
LFOCKACE = .TRUE. \| .FALSE.  
Default: **LFOCKACE** = .TRUE. 

|                       |          |                        |
|-----------------------|----------|------------------------|
| Default: **LFOCKACE** | = .TRUE. | for VASP.6             |
|                       | = N/A    | for VASP.5.X and older |

Description: LFOCKACE determines whether the Adaptively Compressed
Exchange Operator is used.^([\[1\]](#cite_note-linlin:jctc:2016-1))

- N.B.:Available for CPU and OpenACC version of VASP.6 when compiled
  with [-Dfock_dblbuf](../redirects/Precompiler_flags.md).

------------------------------------------------------------------------

For LFOCKACE=.TRUE. the Cholesky decomposition $X=LL^\dagger$ of the Fock exchange matrix
$X_{ij} = \langle \tilde\psi_i \mid \tilde V_X
\mid \tilde\psi_j \rangle$ is calculated and the adaptively
compressed exchange operator $\tilde V_{ACE} =
-\sum_i \mid \tilde X_i \rangle \langle \tilde X_i \mid$ is
used for the action of the Fock exchange on the pseudo orbitals. This
method can be used for [hybrid
functionals](../methods/Category-Hybrid_functionals.md)
in combination with the Davidson algorithm
([ALGO](ALGO.md)=Normal) to save a factor of
$\approx 3$ in computation time.

For LFOCKACE=.FALSE. the conventional orbital representation is used.

Note: it is good scientific practice to cite the original publication
(Ref. ^([\[1\]](#cite_note-linlin:jctc:2016-1))) if you use this
feature. The feature is used by default, if the Davidson algorithm
([ALGO](ALGO.md) = Normal) is used; ACE is not used for
[ALGO](ALGO.md) = Damped or [ALGO](ALGO.md) = All.

## Related tags and articles
[AEXX](AEXX.md), [AEXX](AEXX.md),
[AGGAX](AGGAX.md), [AGGAC](AGGAC.md),
[LHFCALC](LHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LHFCALC-_incategory-Examples)

## References
1.  ↑ ^([a](#cite_ref-linlin:jctc:2016_1-0))
    ^([b](#cite_ref-linlin:jctc:2016_1-1)) [L. Lin, J. Chem. Theory
    Comput. **12**, 2242-2249
    (2016).](https://doi.org/10.1021/acs.jctc.6b00092)

------------------------------------------------------------------------
