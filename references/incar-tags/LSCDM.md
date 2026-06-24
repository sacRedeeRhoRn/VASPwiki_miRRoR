<!-- Source: https://vasp.at/wiki/index.php/LSCDM | revid: 23559 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCDM
LSCDM = .TRUE. \| .FALSE. 

|                    |           |     |
|--------------------|-----------|-----|
| Default: **LSCDM** | = .FALSE. |     |

Description: LSCDM switches on the selected columns of the density
matrix (SCDM) method.

------------------------------------------------------------------------

The selected columns of the density matrix (SCDM) method works by
fitting a unitary matrix $U_{mn\mathbf{k}}$ that transforms the basis from Bloch states
$|\psi_{n\mathbf{k}}\rangle$ obtained
by VASP to a [Wannier
basis](https://vasp.at/wiki/index.php/Wannier_functions)
$|w_{m\mathbf{R}}\rangle$.

$|w_{m\mathbf{R}}\rangle = \sum_{n\mathbf{k}}
e^{-i\mathbf{k}\cdot\mathbf{R}} U_{mn\mathbf{k}}
|\psi_{n\mathbf{k}}\rangle.$

This is done using a [one-shot
method](../redirects/Wannier_Functions.md) "Wannier Functions")
through a singular-value decomposition as proposed by A. Damle and L.
Lin ^([\[1\]](#cite_note-damle:mms:2018-1)).

In order to obtain a good Wannierization, a certain level of freedom
should be given to the localized orbitals to adequately accommodate the
Bloch states. This is controlled by the cutoff function specified by the
[CUTOFF_TYPE](CUTOFF_TYPE.md) tag and related
parameters $\mu$
([CUTOFF_MU](CUTOFF_MU.md)) and $\sigma$ ([CUTOFF_SIGMA](CUTOFF_SIGMA.md)).

## Related tags and articles
[CUTOFF_TYPE](CUTOFF_TYPE.md),
[CUTOFF_MU](CUTOFF_MU.md),
[CUTOFF_SIGMA](CUTOFF_SIGMA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCDM-_incategory-Examples)

## References
1.  [↑](#cite_ref-damle:mms:2018_1-0) [A. Damle and L. Lin, Multiscale
    Model. Simul., **16(3)**, 1392–1410
    (2018).](https://doi.org/10.1137/17M1129696)
