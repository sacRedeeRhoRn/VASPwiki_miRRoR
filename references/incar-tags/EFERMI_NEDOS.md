<!-- Source: https://vasp.at/wiki/index.php/EFERMI_NEDOS | revid: 35851 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EFERMI_NEDOS
EFERMI_NEDOS = \[integer\]  
Default: **EFERMI_NEDOS** = 21 

Description: Number of Gauss–Legendre integration points used to
evaluate the Fermi–Dirac distribution and determine the Fermi level at
finite temperature using the tetrahedron method only with
[ISMEAR](ISMEAR.md) = −14 or -15 .

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

**EFERMI_NEDOS** sets the number of points in the Gauss–Legendre grid
used to integrate the Fermi–Dirac distribution for determining the Fermi
level within the [tetrahedron
method](../tutorials/Smearing_technique.md)
when [ISMEAR](ISMEAR.md) = −14 or -15 . Larger values
improve accuracy, especially at low temperatures or with sharp features
in the [electronic
DOS](../categories/Category-Density_of_states.md), but
also increase computational cost. A brief convergence test is
recommended in case very accurate occupancies are required, e.g., in the
context of [transport
calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md).

|  |
|----|
| **Mind:** **ELPH_FERMI_NEDOS** is a valid alternative way of writing this tag. |

## Implementation details
At $T=0$, the integrated and
differential densities of states are \$\$
n(\epsilon)=\sum\_{n\mathbf{k}}\theta(\epsilon-\epsilon\_{n\mathbf{k}}),
\qquad
g(\epsilon)=\sum\_{n\mathbf{k}}\delta(\epsilon-\epsilon\_{n\mathbf{k}}).
\$\$

At finite temperature, \$\$ N_e(\epsilon_F,T)=
\sum\_{n\mathbf{k}}f(\epsilon\_{n\mathbf{k}}-\epsilon_F,T) =\int
g(\epsilon)f(\epsilon-\epsilon_F,T)\\d\epsilon. \tag{1} \$\$

With the substitution $x = 1 -
2f(\epsilon-\epsilon_F,T)$, \$\$ \epsilon =
k_BT\ln\\\frac{1+x}{1-x}+\epsilon_F, \qquad d\epsilon =
-k_BT\\\frac{2}{x^2-1}\\dx, \$\$ Eq. (1) becomes \$\$ N_e(\epsilon_F,T)=
\frac{1}{2}\int\_{-1}^{1}
n\\\left(k_BT\ln\\\frac{1+x}{1-x}+\epsilon_F\right)\\dx. \$\$

In practice, this integral is discretized as \$\$
N_e(\epsilon_F,T)\simeq \frac{1}{2}\sum\_{i=1}^{N}w_i\\
n\\\left(k_BT\ln\\\frac{1+x_i}{1-x_i}+\epsilon_F\right), \$\$ where
$w_i$ and $x_i$ are Gauss–Legendre weights and abscissas. The step functions
\\\theta(\epsilon-\epsilon\_{n\mathbf{k}})\\ entering \\n(\epsilon)\\
are evaluated using the tetrahedron method, with the number of energy
points $N$ given by EFERMI_NEDOS.

## Related tags and articles
[ISMEAR](ISMEAR.md), [SIGMA](SIGMA.md), [Smearing
technique](../tutorials/Smearing_technique.md), [K-point
integration](../redirects/K-point_integration.md)
