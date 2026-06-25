<!-- Source: https://vasp.at/wiki/index.php/Coulomb_singularity | revid: 21754 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Coulomb singularity


The bare Coulomb operator

$V(\vert\mathbf{r}-\mathbf{r}'\vert)=\frac{1}{\vert\mathbf{r}-\mathbf{r}'\vert}$

in the [unscreened HF
exchange](Hybrid_functionals-_formalism.md)
has a representation in the reciprocal space that is given by

$V(q)=\frac{4\pi}{q^2}$

It has an (integrable) singularity at $q=\vert\mathbf{k}'-\mathbf{k}+\mathbf{G}\vert=0$ that
leads to a very slow convergence of the results with respect to the cell
size or number of **k** points. In order to alleviate this issue
different methods have been proposed: the auxiliary function
[^gygi:prb:86-1],
probe-charge Ewald
[^massidda:prb:93-2]
([HFALPHA](../incar-tags/HFALPHA.md)), and Coulomb
truncation[^spenceralavi:prb:08-3]
methods (selected with [HFRCUT](../incar-tags/HFRCUT.md)). These mostly
involve modifying the Coulomb Kernel in a way that yields the same
result as the unmodified kernel in the limit of large supercell sizes.
These methods can also be applied to the
[Thomas-Fermi](Hybrid_functionals-_formalism.md)
and [error
function](Hybrid_functionals-_formalism.md)
screened Coulomb operators given by

$V(\vert\mathbf{r}-\mathbf{r}'\vert)=\frac{e^{-\lambda\left\vert\mathbf{r}-\mathbf{r}'\right\vert}}{\left\vert\mathbf{r}-\mathbf{r}'\right\vert}$

and

$V(\vert\mathbf{r}-\mathbf{r}'\vert)=\frac{\text{erfc}\left({-\lambda\left\vert\mathbf{r}-\mathbf{r}'\right\vert}\right)}{\left\vert\mathbf{r}-\mathbf{r}'\right\vert}$

respectively, whose representations in the reciprocal space are given by

$V(q)=\frac{4\pi}{q^{2}+\lambda^{2}}$

and

$V(q)=\frac{4\pi}{q^{2}}\left(1-e^{-q^{2}/\left(4\lambda^2\right)}\right)$

respectively.


## Contents


- [1 Auxiliary
  function](#auxiliary-function)
- [2 Probe-charge
  Ewald](#probe-charge-ewald)
- [3 Spherical
  truncation](#spherical-truncation)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


### Auxiliary function\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Auxiliary function">edit</a> \| (./index.php.md)\]

In this approach an auxiliary periodic function
$F(q)$ with the same $1/q^2$
divergence as the Coulomb potential in reciprocal space is subtracted in
the **k** points used to integrate the Hartree-Fock energy, thus
regularizing the
integral[^gygi:prb:86-1].
This function is chosen such that it has a closed analytical expression
for its
integral[^gygi:prb:86-1]
or the integral is evaluated
numerically[^carrier:prb:2007-4].
This approach is currently not implemented in VASP, instead, the
probe-charge Ewald method is used.

### Probe-charge Ewald\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Probe-charge Ewald">edit</a> \| (./index.php.md)\]

A similar approach to the auxiliary function method described above is
the probe-charge Ewald method
[^massidda:prb:93-2].
In this case, the auxiliary function $F(q)$ is
chosen to have the form of the Coulomb kernel times a Gaussian function
$e^{-\alpha q^2}$ with a width
$\alpha$ ([HFALPHA](../incar-tags/HFALPHA.md)) comparable
to the Brillouin zone diameter. This function is used to regularize the
Coulomb integral that is evaluated in the regular **k** point grid with
the divergent part being evaluated by analytical integration of the
Coulomb kernel (see eq. 29 in ref.
[^massidda:prb:93-2]).
The value of the integral of the bare Coulomb potential is (see eq. 31
in ref.
[^massidda:prb:93-2])

$\begin{aligned} \frac{1}{2\pi^2} \int \frac{4\pi}{\mathbf{|q|}^2}
e^{-\alpha\mathbf{|q|}^2} d\mathbf{q}= \frac{2}{\pi} \int
\frac{1}{q^2} e^{-\alpha q^2} q^2 dq = \frac{2}{\pi} \int e^{-\alpha
q^2} dq= \frac{1}{\sqrt{\pi \alpha}} \end{aligned}$

for the Thomas-Fermi and error function screened Coulomb kernels we have

$\begin{aligned} \frac{1}{2\pi^2} \int
\frac{4\pi}{\mathbf{|q|}^2+\lambda^2} e^{-\alpha\mathbf{|q|}^2}
d\mathbf{q}= \frac{2} {\pi} \int \frac{q^2}{q^2+\lambda^2} e^{-\alpha
q^2} q^2 dq = -\lambda e^{\alpha \lambda^2} \text{erfc}({\lambda
\sqrt{\alpha}}) + \frac{1}{\sqrt{\pi \alpha}} \end{aligned}$

and

$\begin{aligned} \frac{1}{2\pi^2} \int \frac{4\pi}{\mathbf{q}^2} \left(
1-e^{-\mathbf{|q|}^2/(4\lambda^2)} \right) e^{-
\alpha\mathbf{|q|}^2} d\mathbf{q}= \frac{2}{\pi} \int \frac{1}{q^2}
\left( 1-e^{-q^2/(4\lambda^2)} \right) e^{-\alpha q^2} q^2 dq =
\frac{1}{\sqrt{\pi \alpha}} - \frac{1}{\sqrt{\pi
\left(\alpha+\frac{1}{4\lambda^2}\right)}} \end{aligned}$

respectively.

### Spherical truncation\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Spherical truncation">edit</a> \| (./index.php.md)\]

In this
method[^spenceralavi:prb:08-3]
the bare Coulomb operator $V(\vert\mathbf{r}-\mathbf{r}'\vert)$ is spherically
truncated by multiplying it by the step function
$\theta(R_{\text{c}}-\left\vert\mathbf{r}-\mathbf{r}'\right\vert)$, and in the reciprocal this leads to

$V(q)=\frac{4\pi}{q^{2}}\left(1-\cos(q R_{\text{c}})\right)$

whose value at $q=0$ is
finite and is given by $V(q=0)=2\pi R_{\text{c}}^{2}$, where the truncation radius
$R_{\text{c}}$ ([HFRCUT](../incar-tags/HFRCUT.md)) is by
default chosen as $R_{\text{c}}=\left(3/\left(4\pi\right)N_{\mathbf{k}}\Omega\right)^{1/3}$ with $N_{\mathbf{k}}$ being the number of $k$-points in
the full Brillouin zone.

The screened potentials have no singularity at
$q=0$. Nevertheless, it is still beneficial for
accelerating the convergence with respect to the number of **k** points
to multiply these screened operators by $\theta(R_{\text{c}}-\left\vert\mathbf{r}-\mathbf{r}'\right\vert)$, which in the reciprocal space gives

$V(q)=\frac{4\pi}{q^{2}+\lambda^{2}} \left( 1-e^{-\lambda
R_{\text{c}}}\left(\frac{\lambda}{q} \sin\left(qR_{\text{c}}\right) +
\cos\left(qR_{\text{c}}\right)\right)\right)$

and

$V(q)=\frac{4\pi}{q^{2}} \left(
1-\cos(qR_{\text{c}})\text{erfc}\left(\lambda R_{\text{c}}\right) -
e^{-q^{2}/\left(4\lambda^2\right)} \Re\left({\text{erf}\left(\lambda
R_{\text{c}} + \text{i}\frac{q}{2\lambda}\right)}\right)\right)$

respectively, with the following values at $q=0$:

$V(q=0)=\frac{4\pi}{\lambda^{2}}\left(1-e^{-\lambda
R_{\text{c}}}\left(\lambda R_{\text{c}} + 1\right)\right)$

and

$V(q=0)=2\pi\left(R_{\text{c}}^{2}\text{erfc}(\lambda R_{\text{c}}) -
\frac{R_{\text{c}}e^{-\lambda^{2}R_{\text{c}}^{2}}}{\sqrt{\pi}\lambda} +
\frac{\text{erf}(\lambda R_{\text{c}})}{2\lambda^{2}}\right)$

Note that the spherical truncation method described above works very
well in the case of 3D systems. However, it is not recommended for
systems with a lower
dimensionality[^sundararamanarias:prb:13-5].
For such systems, the approach proposed in ref.
[^sundararamanarias:prb:13-5]
(not implemented in VASP) is more adapted since the truncation is done
according to the Wigner-Seitz cell and therefore more general.

## Related tags and articles\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[HFRCUT](../incar-tags/HFRCUT.md), [FOCKCORR](../incar-tags/FOCKCORR.md),
[Hybrid functionals:
formalism](Hybrid_functionals-_formalism.md),
[Downsampling of the Hartree-Fock
operator](Downsampling_of_the_Hartree-Fock_operator.md)

## References\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^gygi:prb:86-1]: [F. Gygi and A. Baldereschi, Phys. Rev. B **34**, 4405(R) (1986).](https://doi.org/10.1103/PhysRevB.34.4405)
[^massidda:prb:93-2]: [S. Massidda, M. Posternak, and A. Baldereschi, Phys. Rev. B **48**, 5058 (1993).](https://doi.org/10.1103/PhysRevB.48.5058)
[^spenceralavi:prb:08-3]: [J. Spencer and A. Alavi, Phys. Phys. Rev. B **77**, 193110 (2008).](https://doi.org/10.1103/PhysRevB.77.193110)
[^carrier:prb:2007-4]: [P. Carrier, S. Rohra, and A. Görling, Phys. Rev. B **75**, 205126 (2007).](https://doi.org/10.1103/PhysRevB.86.165105)
[^sundararamanarias:prb:13-5]: [R. Sundararaman and T. A. Arias, Phys. Rev. B **87**, 165122 (2013).](https://doi.org/10.1103/PhysRevB.87.165122)
