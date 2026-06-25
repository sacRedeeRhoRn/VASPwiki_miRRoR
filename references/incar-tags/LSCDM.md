<!-- Source: https://vasp.at/wiki/index.php/LSCDM | revid: 23559 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSCDM


LSCDM = .TRUE. \| .FALSE. 

|                    |           |     |
|--------------------|-----------|-----|
| Default: **LSCDM** | = .FALSE. |     |

Description: LSCDM switches on
the selected columns of the density matrix (SCDM) method.

------------------------------------------------------------------------

The selected columns of the density matrix (SCDM) method works by
fitting a unitary matrix $U_{mn\mathbf{k}}$ that transforms the basis from Bloch states
$|\psi_{n\mathbf{k}}\rangle$ obtained by VASP to a
<a href="/wiki/Wannier_functions" class="mw-redirect"
title="Wannier functions">Wannier basis</a> $|w_{m\mathbf{R}}\rangle$.

$|w_{m\mathbf{R}}\rangle = \sum_{n\mathbf{k}}
e^{-i\mathbf{k}\cdot\mathbf{R}} U_{mn\mathbf{k}}
|\psi_{n\mathbf{k}}\rangle.$

This is done using a <a
href="/wiki/Wannier_Functions#One-shot_single_value_decomposition_(SVD)"
class="mw-redirect" title="Wannier Functions">one-shot method</a>
through a singular-value decomposition as proposed by A. Damle and L.
Lin
<sup>[\[1\]](#cite_note-damle:mms:2018-1)</sup>.

In order to obtain a good Wannierization, a certain level of freedom
should be given to the localized orbitals to adequately accommodate the
Bloch states. This is controlled by the cutoff function specified by the
[CUTOFF_TYPE](CUTOFF_TYPE.md) tag and related
parameters $\mu$
([CUTOFF_MU](CUTOFF_MU.md)) and
$\sigma$
([CUTOFF_SIGMA](CUTOFF_SIGMA.md)).

## Related tags and articles\[<a href="/wiki/index.php?title=LSCDM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CUTOFF_TYPE](CUTOFF_TYPE.md),
[CUTOFF_MU](CUTOFF_MU.md),
[CUTOFF_SIGMA](CUTOFF_SIGMA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSCDM-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LSCDM&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-damle:mms:2018_1-0)
    <a href="https://doi.org/10.1137/17M1129696" class="external text"
    rel="nofollow">A. Damle and L. Lin, Multiscale Model. Simul.,
    <strong>16(3)</strong>, 1392–1410 (2018).</a>


