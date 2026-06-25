<!-- Source: https://vasp.at/wiki/index.php/FBIAS_A | revid: 29881 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FBIAS_A


FBIAS_A = \[real (array)\] 

Description: Defines the step height for the bias potential in
$eV$.

------------------------------------------------------------------------

FBIAS_A defines the height of
the step ($A_{\mu}$) in
the Fermi-like step-shaped bias potential of the following form:

$\tilde{V}(\xi_1,\dots,\xi_{M_4}) =
\sum_{\mu=1}^{M_4}\frac{A_{\mu}}{1+\text{exp}\left
\[-D_{\mu}(\frac{\xi(q)}{\xi_{0\mu}} -1) \right \]}, \\$

where the sum runs over all ($M_4$)
coordinates the potential acts upon, which are defined in the
[ICONST](../input-files/ICONST.md) file by setting the `status` to 4. The
units of $A_{\mu}$ are
$eV$. The number of items defined via
FBIAS_A must be equal to
$M_4$, otherwise the calculation terminates with an
error message.

## Related tags and articles\[<a href="/wiki/index.php?title=FBIAS_A&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[FBIAS_R0](FBIAS_R0.md),
[FBIAS_D](FBIAS_D.md), [ICONST](../input-files/ICONST.md),
[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)

------------------------------------------------------------------------


