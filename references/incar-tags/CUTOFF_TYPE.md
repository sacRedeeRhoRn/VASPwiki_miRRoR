<!-- Source: https://vasp.at/wiki/index.php/CUTOFF_TYPE | revid: 32843 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CUTOFF_TYPE


CUTOFF_TYPE = erfc \| gaussian
\| fermi \| num_wann 

|                          |        |     |
|--------------------------|--------|-----|
| Default: **CUTOFF_TYPE** | = erfc |     |

Description: CUTOFF_TYPE
chooses the type of cutoff function to be used before performing the
singular-value decomposition (SVD) of the initial projections matrix.

------------------------------------------------------------------------

This tag governs how much weight should be given in the SVD during the
<a
href="/wiki/Wannier_functions#One-shot_single_value_decomposition_(SVD)"
class="mw-redirect" title="Wannier functions">one-shot
Wannierization</a> to a certain orbital with energy
$\epsilon_{n\mathbf{k}}$. If the weight is zero the
orbital is not included in the fitting while if it is one it is included
with the maximum importance. This behavior is similar to the wannier90
disentanglement window.

In order to obtain a good Wannierization, a certain level of freedom
should be given to the localized orbitals to adequately accommodate the
Bloch states. Applying a smooth cutoff function from the following table
can help achieve this goal by including more states beyond the relevant
energy range. This is particularly important for systems with entangled
states.

|  |  |
|----|----|
| CUTOFF_TYPE | Function |
| erfc | $\frac{1}{2}\text{erfc}\left\[(\epsilon_{n\mathbf{k}}-\mu)/\sigma\right\]$ |
| gaussian | $e^{-(\epsilon_{n\mathbf{k}}-\mu)^2/\sigma}$ |
| fermi | $\frac{1}{e^{(\epsilon_{n\mathbf{k}}-\mu)/\sigma}+1}$ |

with $\sigma$
specified by the [CUTOFF_SIGMA](CUTOFF_SIGMA.md) tag
and $\mu$ by
[CUTOFF_MU](CUTOFF_MU.md).

In addition to the aforementioned cutoff functions, it is also possible
to select
`CUTOFF_TYPE`` = num_wann`.
This mode is identical to
`CUTOFF_TYPE`` = erfc` with
the exception that $\mu$ is set
to $\epsilon_{N \mathbf{k}}$ at each individual k-point,
where $N$ is the
number of Wannier orbitals specified via
[NUM_WANN](NUM_WANN.md). In this case,
[CUTOFF_MU](CUTOFF_MU.md) is ignored.

## Related tags and articles\[<a
href="/wiki/index.php?title=CUTOFF_TYPE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CUTOFF_MU](CUTOFF_MU.md),
[CUTOFF_SIGMA](CUTOFF_SIGMA.md),
[LSCDM](LSCDM.md), [LOCPROJ](LOCPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CUTOFF_TYPE-_incategory-Examples)


