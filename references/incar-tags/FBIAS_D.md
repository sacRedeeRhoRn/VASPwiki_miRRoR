<!-- Source: https://vasp.at/wiki/index.php/FBIAS_D | revid: 29882 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FBIAS_D
FBIAS_D = \[real (array)\] 

Description: Sets the slope of the bias potential.

------------------------------------------------------------------------

FBIAS_D defines the parameter $D_{\mu}$, which controls the slope of the central part of the
Fermi-like step-shaped bias potential of the following form:

$\tilde{V}(\xi_1,\dots,\xi_{M_4}) =
\sum_{\mu=1}^{M_4}\frac{A_{\mu}}{1+\text{exp}\left
\[-D_{\mu}(\frac{\xi(q)}{\xi_{0\mu}} -1) \right \]}, \\$

where the sum runs over all ($M_4$)
coordinates the potential acts upon, which are defined in the
[ICONST](../input-files/ICONST.md)-file by setting the `status` to 4. The
parameters $D_{\mu}$ are dimensionless.
The number of items defined via FBIAS_D must equal to
$M_4$, otherwise the calculation
terminates with an error message.

## Related tags and articles
[FBIAS_R0](FBIAS_R0.md),
[FBIAS_A](FBIAS_A.md), [ICONST](../input-files/ICONST.md),
[Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)

------------------------------------------------------------------------
