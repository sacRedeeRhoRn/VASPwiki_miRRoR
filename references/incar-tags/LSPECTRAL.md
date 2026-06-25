<!-- Source: https://vasp.at/wiki/index.php/LSPECTRAL | revid: 18018 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSPECTRAL


LSPECTRAL = .FALSE. \| .TRUE. 

|                        |          |                                       |
|------------------------|----------|---------------------------------------|
| Default: **LSPECTRAL** | = .TRUE. | if [NOMEGA](NOMEGA.md)\>2 |

Description: LSPECTRAL
specifies to use the spectral method.

------------------------------------------------------------------------

If LSPECTRAL = .TRUE. is set,
the imaginary part of the independent particle polarizability
$\chi_{\mathbf{q}}^0 (\mathbf{G}, \mathbf{G}', \omega)$
is calculated first, and afterwards the full independent particle
polarizability is determined using a Kramers-Kronig (or Hilbert)
transform. This reduces the computational workload by almost a factor
[NOMEGA](NOMEGA.md)/2. The downside of the coin is that the
response function must be kept in memory for all considered frequencies,
which can cause excessive memory requirements. VASP, therefore,
distributes the dielectric functions among the available compute nodes.

A similar trick is used when the QP-shifts are calculated. In general it
is strongly recommended to set
LSPECTRAL = .TRUE., except if
memory requirements are too excessive.

## Related tags and articles\[<a
href="/wiki/index.php?title=LSPECTRAL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NOMEGA](NOMEGA.md),
[LSPECTRALGW](LSPECTRALGW.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSPECTRAL-_incategory-Examples)

------------------------------------------------------------------------


