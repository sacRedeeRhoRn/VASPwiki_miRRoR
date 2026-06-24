<!-- Source: https://vasp.at/wiki/index.php/DEG_THRESHOLD | revid: 36280 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DEG_THRESHOLD
DEG_THRESHOLD = \[real\] 

|                            |                        |     |
|----------------------------|------------------------|-----|
| Default: **DEG_THRESHOLD** | = \$2 \times 10^{-3}\$ |     |

Description: DEG_THRESHOLD specifies whether two eigenvalues should be
treated as degenerate during clustering of orbitals in the linear
response code. DEG_THRESHOLD is specified in units of eV.

------------------------------------------------------------------------

This parameter is used to find degenerate clusters of orbitals. It is
used within VASP whenever linear-response calculations are performed
(either with respect to external fields or with respect to ionic
displacements). VASP internally uses an inverse-iteration solver with
imaginary shifting to solve the Sternheimer linear-response equation. If
the value is too large, non-degenerate eigenvalue pairs may be detected
as degenerate pairs. This can lead to very poor convergence or erroneous
results, in particular, for systems with low symmetry and flat semi-core
bands. Conversely, too small a value might not lead to a proper
detection of all degenerate eigenvalues. For insulating systems, this
usually does not lead to substantial errors, since the imaginary shift
can handle degenerate eigenvalue/eigenvector pairs (so VASP implements
two strategies to handle degenerate pairs and combining them yields more
robust results).

It is recommended to use small values for systems without symmetry
(e.g., around \$10^{-5}\$). For highly symmetric insulators, results
should be largely insensitive to the choice of DEG_THRESHOLD. For
metals, degenerate states with partial occupancies must be correctly
resolved to obtain highly accurate results (so DEG_THRESHOLD must be set
to a value that allows safe detection of degenerate states).

  

[TABLE]

## Related tags and articles
[LSUBROT](LSUBROT.md),
[LEPSILON](LEPSILON.md)
