<!-- Source: https://vasp.at/wiki/index.php/Best_practices_for_Bethe-Salpeter_calculations | revid: 28660 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Best practices for Bethe-Salpeter calculations



## Contents


- [1 Optimizing
  performance](#Optimizing_performance)
  - [1.1 Small
    cells](#Small_cells)
  - [1.2 Large
    cells](#Large_cells)
- [2 Related
  articles](#Related_articles)


## Optimizing performance\[<a
href="/wiki/index.php?title=Best_practices_for_Bethe-Salpeter_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Optimizing performance">edit</a> \| (./index.php.md)\]

Due to the steep scaling of the BSE method with the system size, it is
important to optimize the parameters of the calculation. Here we provide
recommendations that can significantly speed up the BSE calculations in
VASP. Below we consider two limiting cases: small cells and large cells.

### Small cells\[<a
href="/wiki/index.php?title=Best_practices_for_Bethe-Salpeter_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Small cells">edit</a> \| (./index.php.md)\]

We consider that small cells are the cells where the number of atoms
doesn't exceed *eight*. For such cells, it is typical that a large
number of k-points is required to obtain a converged spectrum. Hence,
the following optimizations should be considered.

- **Use the Lanczos algorithm**. Diagonalizing large matrices can be too
  time-consuming. Thus, for large matrices (e.g. rank \> 1000) we
  recommend using the Lanczos ([IBSE](../incar-tags/IBSE.md)=3) or
  time-evolution ([IBSE](../incar-tags/IBSE.md)=1) algorithms.
- **Set [KPAR](../incar-tags/KPAR.md) to the number of MPI ranks**.
  [KPAR](../incar-tags/KPAR.md) in BSE divides all MPI ranks into KPAR
  groups, which will share the wavefunctions. Thus, if
  [KPAR](../incar-tags/KPAR.md)=`number of MPI ranks` all wavefunctions are
  stored on every MPI rank, which eliminates the need to send/receive
  the orbitals during the calculation of the matrix elements. For small
  cells, it can be greatly beneficial to distribute all wavefunctions
  within a small group of MPI ranks or ideally store all orbitals on
  every rank.
- **Use [OMEGAMAX](../incar-tags/OMEGAMAX.md) to limit the energy
  range**. The [OMEGAMAX](../incar-tags/OMEGAMAX.md) can be used to
  exclude transitions with higher energy from the BSE calculation. This
  largely reduces both the memory requirement and the computational
  time. It is especially beneficial for systems with a strong band
  dispersion, where energies can strongly vary at different k-points.
  This, however, requires some caution as it is not guaranteed that the
  spectrum up to [OMEGAMAX](../incar-tags/OMEGAMAX.md) is fully
  converged and the convergence of the spectrum with
  [OMEGAMAX](../incar-tags/OMEGAMAX.md) must be carefully investigated.
- **Compile VASP with `-Dsingle_prec_bse`**. By default, VASP stores and
  solves the BSE in double precision. However, if VASP is compiled with
  the flag `-Dsingle_prec_bse` the matrix is stored and solved in single
  precision, which gives a factor of two in performance and halves the
  memory required to store the matrix.

### Large cells\[<a
href="/wiki/index.php?title=Best_practices_for_Bethe-Salpeter_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Large cells">edit</a> \| (./index.php.md)\]

The following optimizations should be relevant for cells where the
number of atoms is larger than *eight*.

- **Use the Lanczos algorithm**. Diagonalizing large matrices can be
  very time-consuming. Thus, for large matrices, e.g. rank \> 1000, we
  recommend using the Lanczos ([IBSE](../incar-tags/IBSE.md)=3) or
  time-evolution ([IBSE](../incar-tags/IBSE.md)=1) algorithms.
- **Use [NBSEBLOCKV](../incar-tags/NBSEBLOCKV.md) and/or
  [NBSEBLOCKO](../incar-tags/NBSEBLOCKO.md)**. For large cells, it is
  typical that the number of k-points is small and the number of bands
  is large. By default in VASP, the matrix elements calculation in BSE
  is parallelized over k-points, which might not allow for the optimal
  load balancing of the computational load. By using parallelization
  over bands, we can subdivide large blocks of data each MPI rank
  computes into smaller blocks thus improving the load balance.
- **Compile VASP with `-Dsingle_prec_bse`**. By default, VASP stores and
  solves the BSE in double precision. However, if VASP is compiled with
  the flag `-Dsingle_prec_bse` the matrix is stored and solved in single
  precision, which gives a factor of two in performance and halves the
  memory required to store the matrix.
- **Use vasp_gam**. If possible use the gamma version of VASP as it
  substantially reduces the required memory and computational time.
- **Use [OMEGAMAX](../incar-tags/OMEGAMAX.md) to limit the energy
  range**. The [OMEGAMAX](../incar-tags/OMEGAMAX.md) can be used to
  exclude transitions with higher energy from the BSE calculation. This
  largely reduces both the memory requirement and the computational
  time. It is especially beneficial for systems with a strong band
  dispersion, where energies can strongly vary at different k-points.
  This, however, requires some caution as it is not guaranteed that the
  spectrum up to [OMEGAMAX](../incar-tags/OMEGAMAX.md) is fully
  converged and the convergence of the spectrum with
  [OMEGAMAX](../incar-tags/OMEGAMAX.md) must be carefully investigated.
- **Use lower [PRECFOCK](../incar-tags/PRECFOCK.md)**. In large cells,
  the FFTs may take up the majority of the time in the calculation of
  the matrix elements, and reducing the FFT grid can largely speed up
  the calculation. For the large cells, even low precision can be found
  sufficiently accurate, but the convergence with
  [PRECFOCK](../incar-tags/PRECFOCK.md) must be investigated for each
  system.

## Related articles\[<a
href="/wiki/index.php?title=Best_practices_for_Bethe-Salpeter_calculations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[ALGO](../incar-tags/ALGO.md), [LADDER](../incar-tags/LADDER.md),
[LHARTREE](../incar-tags/LHARTREE.md),
[NBANDSV](../incar-tags/NBANDSV.md), [NBANDSO](../incar-tags/NBANDSO.md),
[NBSEBLOCKV](../incar-tags/NBSEBLOCKV.md),
[NBSEBLOCKO](../incar-tags/NBSEBLOCKO.md),
[OMEGAMAX](../incar-tags/OMEGAMAX.md)


