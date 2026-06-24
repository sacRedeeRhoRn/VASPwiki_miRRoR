<!-- Source: https://vasp.at/wiki/index.php/BEXT | revid: 35038 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BEXT
BEXT = \[real\] ( \[real\] \[real\] ) 

|  |  |  |
|----|----|----|
| Default: **BEXT** | = 0.0 | if [ISPIN](ISPIN.md)=2 |
|  | = 3\*0.0 | if [LNONCOLLINEAR](LNONCOLLINEAR.md)=.TRUE. |
|  | = N/A | else |

Description: Specifies an external magnetic field in eV.

------------------------------------------------------------------------

BEXT tag sets an external magnetic field that acts on the electrons in a
Zeeman-like manner. An additional potential of the following form
carries this interaction:

- For spin-polarized calculations ([ISPIN](ISPIN.md) = 2):

$V^{\uparrow} = V^{\uparrow} + B_{\rm ext}$

$V^{\downarrow} = V^{\downarrow} - B_{\rm ext}$

and $B_{\rm ext}$ = BEXT (in eV).

- For noncollinear calculations
  ([LNONCOLLINEAR](LNONCOLLINEAR.md) = .TRUE.):

$V_{\alpha\beta} = V_{\alpha\beta} +
\mathbf{B}_{\rm ext} \cdot \mathbf{\sigma}_{\alpha \beta}$

where $\mathbf{B}_{\rm ext}=({B}^1_{\rm ext},
{B}^2_{\rm ext}, {B}^3_{\rm ext})^T$ is given by

[TABLE]

and $\mathbf{\sigma}$ is the vector of
Pauli matrices ([SAXIS](SAXIS.md), default:
$\sigma_1=\hat x$,
$\sigma_2 =\hat y$,
$\sigma_3 = \hat z$).

The effect of the above is most easily understood for the collinear case
([ISPIN](ISPIN.md)=2): The eigenenergies of spin-up states
are raised by $B_{\rm ext}$ eV, whereas
the eigenenergies of spin-down states are lowered by the same amount.
The total energy changes by:

$\Delta E = (n^{\uparrow} - n^{\downarrow})
B_{\rm ext}$ eV

where $n^{\uparrow}$ and
$n^{\downarrow}$ are the number of up-
and down-spin electrons in the system.

BEXT is applied during the self-consistent [electronic
minimization](../redirects/Electronic_minimization.md)
and effectively shifts the eigenenergies of the spin-up and spin-down
states w.r.t. each other at each step. Consequently, the electrons
redistribute (changing the occupancies) *and* the density changes. The
change in the density (,e.g., charge density and magnetization) also
affects the scf potential and KS orbitals. For a rigid-band Zeeman
splitting, converge the charge density with BEXT=0 and restart with
BEXT$\neq$0 and fixed charge density
([ICHARG](ICHARG.md)=11).

## Units
For an applied magnetic field $B_0$, the
energy difference between two Zeeman-splitted electronic states is given
by:

$\hbar \omega = g_e \mu_B B_0,$

where $\mu_B$ is the Bohr magneton and
$g_e$ is the electron spin *g*-factor.

For [ISPIN](ISPIN.md)=2, rigid-band Zeeman-splitted states
imply:

$V^{\uparrow} - V^{\downarrow} = 2 B_{\rm ext}$

This leads to the following relationship between our definition of
$B_{\rm ext}$ (in eV) and the magnetic
field $B_0$ (in T):

$B_0 = \frac{2 B_{\rm ext}}{g_e \mu_B}$

where $\mu_B$= 5.788 381 8060 x 10⁻⁵ eV
T⁻¹, and $g_e$= 2.002 319 304 362 56.

## Related tags and articles
[ISPIN](ISPIN.md),
[LNONCOLLINEAR](LNONCOLLINEAR.md),
[SAXIS](SAXIS.md)

------------------------------------------------------------------------
