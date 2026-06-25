<!-- Source: https://vasp.at/wiki/index.php/SPRING_V0 | revid: 29887 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SPRING_V0


SPRING_V0 = \[real (array)\] 

|  |  |  |
|----|----|----|
| Default: **SPRING_V0** | = 0 | for all coordinates with `status=8` in [ICONST](../input-files/ICONST.md). |

Description: Rate at which the bias potential is shifted in
$uc/fs$.

------------------------------------------------------------------------

Consider the bias potential for a
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
(MD) run of the form:

$\tilde{V}(\xi_1,\dots,\xi_{M_8}) =
\sum_{\mu=1}^{M_8}\frac{1}{2}\kappa_{\mu}
(\xi_{\mu}(q)-\xi_{0\mu})^2, \\$

where the sum runs over all ($M_8$)
coordinates the potential acts upon ($\xi_{\mu}(q)$). The coordinates are defined in the
[ICONST](../input-files/ICONST.md) file by setting the `status=8`.
Optionally, the position of minimum ($\xi_{0\mu}$)
can be shifted at a constant rate $\dot{\xi}_{\mu}$ every MD step, i.e.,

$\xi_{0\mu}(t+\Delta t) = \xi_{0\mu}(t) + \dot{\xi}_{\mu}(q)\Delta t,
\\$

where $\Delta t$ is
the time step used in MD ([POTIM](POTIM.md)). The rate
$\dot{\xi}_{\mu}$ can be defined via the parameter
SPRING_V0 and its units are
$uc/fs$, where $uc$
corresponds to the units of the coordinate the potential acts upon
(e.g., ${\AA}$ for
coordinates with `flag` R, $rad.$ for
coordinates with `flag` A, dimensionless for coordinates with `flag` W,
etc...). The number of items defined via
SPRING_V0 must be equal to
$M_8$, otherwise the calculation terminates with an
error message.

## Related tags and articles\[<a
href="/wiki/index.php?title=SPRING_V0&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[SPRING_K](SPRING_K.md),
[SPRING_R0](SPRING_R0.md),
[ICONST](../input-files/ICONST.md), [Biased molecular
dynamics](../theory/Biased_molecular_dynamics.md)

------------------------------------------------------------------------


