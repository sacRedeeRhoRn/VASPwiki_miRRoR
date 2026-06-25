<!-- Source: https://vasp.at/wiki/index.php/SAXIS | revid: 36604 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SAXIS


SAXIS = \[real array\]  
Default: **SAXIS** = (0, 0, 1) 

Description: Set the global spin-quantization axis w.r.t. Cartesian
coordinates.

------------------------------------------------------------------------

SAXIS specifies the relative
orientation of spinor space spanned by the Pauli matrices
$\\\sigma_1$, $\sigma_2$,
$\mathbf{\sigma}_3\\$ with respect to Cartesian
coordinates $\\\hat x, \hat y, \hat z\\$. The default is $\sigma_1=\hat x$, $\sigma_2 =\hat y$, $\sigma_3 = \hat z$. The direction of the spin-quantization axis
$\sigma_3$ with respect to Cartesian coordinates is set

     SAXIS =   sx sy sz    ! global spin-quantization axis

such that $\sigma_3=\mathbf{s}/|\mathbf{s}|$, i.e.,
$\sigma_3$ points along $\mathbf{s}=(s_x,s_y,s_z)^T$. The directions of $\sigma_1$ and
$\sigma_2$ are a consequence of rotating
$\sigma_3$ to point along $\mathbf{s}$
as described below.

The relative orientation of spinor space with respect to real space
becomes important in case spin-orbit coupling is included
([LSORBIT](LSORBIT.md)=True). All magnetic moments and
spinor-like quantities written or read by VASP are given in the basis of
the spinor space $\\\sigma_1$,
$\sigma_2$, $\mathbf{\sigma}_3\\$. This includes the [MAGMOM](MAGMOM.md) tag
in the [INCAR](../input-files/INCAR.md) file, the total and local
magnetizations in the [OUTCAR](../output-files/OUTCAR.md) and
[PROCAR](../output-files/PROCAR.md) file, the spinor-like orbitals in the
[WAVECAR](../input-files/WAVECAR.md) file, and the magnetization density
in the [CHGCAR](../input-files/CHGCAR.md) file.

|  |
|----|
| **Warning:** **SAXIS** ≠ 0 0 1, is not supported for Hartree-Fock calculations and hybrid functionals (**LHFCALC** = .TRUE.)! These methods set **ISYM** = 3, which only works with the default **SAXIS**. You can still use **SAXIS** with **ISYM** = -1., but in most cases it is computationally more efficient to change **MAGMOM** instead. |

## Coordinate system\[<a href="/wiki/index.php?title=SAXIS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Coordinate system">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Saxis-angles.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/56/Saxis-angles.png/300px-Saxis-angles.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/56/Saxis-angles.png/450px-Saxis-angles.png 1.5x, /wiki/images/thumb/5/56/Saxis-angles.png/600px-Saxis-angles.png 2x"
width="300" height="312" /></a>
<figcaption>Fig 1. Euler angles $\alpha$ and $\beta$ defined by $\mathbf{s}=(s_x,s_y,s_z)^T$.</figcaption>
</figure>

The default orientation is $\sigma_1=\hat x$, $\sigma_2 =\hat y$, $\sigma_3 = \hat z$. To set $\hat{\sigma}_3=s/|s|$, VASP applies two rotations with Euler angles

$\begin{align} \alpha&=\arctan2\left(\frac{s_y}{s_x}\right) \in
\[-\pi,\pi\]\\
\beta&=\arctan2\left(\frac{\sqrt{s_x^2+s_y^2}}{s_z}\right) \in
\[0,\pi\]. \end{align}$

Here, $\alpha$ is
the angle between the projection of
SAXIS onto the *xy* plane
(s<sub>x</sub>,s<sub>y</sub>,0) and the Cartesian vector
$\hat x$, and $\beta$ is the
angle between the vector SAXIS
and the Cartesian vector $\hat z$, see
Fig. 1. Search for \`Euler angles\` in the
[OUTCAR](../output-files/OUTCAR.md) file to see what VASP uses. For the
default $\mathbf{s}=(0,0,1)$, $\alpha=0$ and
$\beta=0$.

The transformation of a vector $\mathbf{m}=(m_1,m_2,m_3)^T$ given in the basis $\\\sigma_1$,
$\sigma_2$, $\mathbf{\sigma}_3\\$ into $\mathbf{m}'=(m_x,m_y,m_z)^T$ in Cartesian coordinates and its inverse
transformation read

$\begin{align} \mathbf{m}&= m_1 \sigma_1 + m_2 \sigma_2 + m_3 \sigma_3 \\
\mathbf{m}'&= m_x \hat x + m_y \hat y + m_z \hat z \\ \mathbf{m}'&=
R_z^\alpha R_y^\beta \mathbf{m} \\ \mathbf{m} &= R_y^{-\beta}
R_z^{-\alpha} \mathbf{m}' \\ \end{align}$

where the rotation matrices are

$R_z^\alpha = \left(\begin{matrix} \cos(\alpha) & -\sin(\alpha) & 0 \\
\sin(\alpha) & \cos(\alpha) & 0 \\ 0 & 0 & 1 \\ \end{matrix}\right),
\quad R_y^\beta = \left(\begin{matrix} \cos(\beta) & 0 & \sin(\beta) \\
0 & 1 & 0 \\ -\sin(\beta) & 0 & \cos(\beta) \\ \end{matrix}\right).$

|  |
|----|
| **Mind:** Apply the proper basis transformation when comparing vector-like quantities and spinor-like quantities. |

For instance, when [LORBMOM](LORBMOM.md)=True the orbital
angular momentum is written to the [OUTCAR](../output-files/OUTCAR.md) file
in Cartesian coordinates. Thus, when comparing the orbital angular
momentum (vector-like quantity) and the magnetization (spinor-like
quantity), one has to perform a basis transformation on one of the
quantities unless the bases agree (default).

## Example\[<a href="/wiki/index.php?title=SAXIS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

- In case the bases have the same orientation, i.e.,
  $\sigma_1=\hat x$, $\sigma_2 =\hat y$, $\sigma_3 = \hat z$ (default)

$\begin{align} m_x & = & m_1, \\ m_y & = & m_2, \\ m_z & = & m_3.
\end{align}$

For a single site this implies setting

    MAGMOM = mx my mz ! magnetic moment in Cartesian coordinates
    SAXIS =  0 0 1   ! default

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Spinor-space-example-saxis.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/e5/Spinor-space-example-saxis.png/300px-Spinor-space-example-saxis.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/e5/Spinor-space-example-saxis.png/450px-Spinor-space-example-saxis.png 1.5x, /wiki/images/thumb/e/e5/Spinor-space-example-saxis.png/600px-Spinor-space-example-saxis.png 2x"
width="300" height="348" /></a>
<figcaption>Fig 2. Example with $\mathbf{s}=(1,1,0)^T$ and Euler angles $\alpha=\pi/4$ and
$\beta=\pi/2$.</figcaption>
</figure>

- Another good choice is setting $\mathbf{s}$
  to point along the direction of the on-site magnetic moment such that

$\begin{align} m_x & = & \sin(\beta)\cos(\alpha) m &= m\\ s_x /
\sqrt{s_x^2+s_y^2+s_z^2} \\ m_y & = & \sin(\beta)\sin(\alpha) m &= m\\
s_y / \sqrt{s_x^2+s_y^2+s_z^2} \\ m_z & = & \cos(\beta) m &= m\\ s_z /
\sqrt{s_x^2+s_y^2+s_z^2}, \end{align}$

where $m$ is the
total on-site magnetic moment.

For a single site, this case implies setting

    MAGMOM = 0 0 m   ! magnetic moment along sigma3
    SAXIS =  sx sy sz ! direction of sigma3

Thus, there are two methods to rotate the initial magnetization in an
arbitrary direction: either by changing the initial magnetic moments
[MAGMOM](MAGMOM.md) or by changing
SAXIS. Both methods should, in
principle, yield exactly the same energy, but for implementation
reasons, the second method might be more precise.

- In case

<!-- -->

    SAXIS =  1 1 0   ! alpha=pi/4, beta=pi/2

the spinor space $\\\sigma_1$,
$\sigma_2$, $\mathbf{\sigma}_3\\$ will be rotated with respect to real space
$\\\hat x, \hat y, \hat z\\$ as shown in Fig. 2.

## Related tags and articles\[<a href="/wiki/index.php?title=SAXIS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LNONCOLLINEAR](LNONCOLLINEAR.md),
[MAGMOM](MAGMOM.md), [LSORBIT](LSORBIT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SAXIS-_incategory-Examples)

------------------------------------------------------------------------


