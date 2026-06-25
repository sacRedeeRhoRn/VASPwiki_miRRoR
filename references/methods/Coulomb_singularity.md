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
<sup>[\[1\]](#cite_note-gygi:prb:86-1)</sup>,
probe-charge Ewald
<sup>[\[2\]](#cite_note-massidda:prb:93-2)</sup>
([HFALPHA](../incar-tags/HFALPHA.md)), and Coulomb
truncation<sup>[\[3\]](#cite_note-spenceralavi:prb:08-3)</sup>
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
integral<sup>[\[1\]](#cite_note-gygi:prb:86-1)</sup>.
This function is chosen such that it has a closed analytical expression
for its
integral<sup>[\[1\]](#cite_note-gygi:prb:86-1)</sup>
or the integral is evaluated
numerically<sup>[\[4\]](#cite_note-carrier:prb:2007-4)</sup>.
This approach is currently not implemented in VASP, instead, the
probe-charge Ewald method is used.

### Probe-charge Ewald\[<a
href="/wiki/index.php?title=Coulomb_singularity&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Probe-charge Ewald">edit</a> \| (./index.php.md)\]

A similar approach to the auxiliary function method described above is
the probe-charge Ewald method
<sup>[\[2\]](#cite_note-massidda:prb:93-2)</sup>.
In this case, the auxiliary function $F(q)$ is
chosen to have the form of the Coulomb kernel times a Gaussian function
$e^{-\alpha q^2}$ with a width
$\alpha$ ([HFALPHA](../incar-tags/HFALPHA.md)) comparable
to the Brillouin zone diameter. This function is used to regularize the
Coulomb integral that is evaluated in the regular **k** point grid with
the divergent part being evaluated by analytical integration of the
Coulomb kernel (see eq. 29 in ref.
<sup>[\[2\]](#cite_note-massidda:prb:93-2)</sup>).
The value of the integral of the bare Coulomb potential is (see eq. 31
in ref.
<sup>[\[2\]](#cite_note-massidda:prb:93-2)</sup>)

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
method<sup>[\[3\]](#cite_note-spenceralavi:prb:08-3)</sup>
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
dimensionality<sup>[\[5\]](#cite_note-sundararamanarias:prb:13-5)</sup>.
For such systems, the approach proposed in ref.
<sup>[\[5\]](#cite_note-sundararamanarias:prb:13-5)</sup>
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


1.  ↑
    <sup>[a](#cite_ref-gygi:prb:86_1-0)</sup>
    <sup>[b](#cite_ref-gygi:prb:86_1-1)</sup>
    <sup>[c](#cite_ref-gygi:prb:86_1-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.34.4405" class="external text"
    rel="nofollow">F. Gygi and A. Baldereschi, Phys. Rev. B
    <strong>34</strong>, 4405(R) (1986).</a>
2.  ↑
    <sup>[a](#cite_ref-massidda:prb:93_2-0)</sup>
    <sup>[b](#cite_ref-massidda:prb:93_2-1)</sup>
    <sup>[c](#cite_ref-massidda:prb:93_2-2)</sup>
    <sup>[d](#cite_ref-massidda:prb:93_2-3)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.48.5058" class="external text"
    rel="nofollow">S. Massidda, M. Posternak, and A. Baldereschi, Phys. Rev.
    B <strong>48</strong>, 5058 (1993).</a>
3.  ↑
    <sup>[a](#cite_ref-spenceralavi:prb:08_3-0)</sup>
    <sup>[b](#cite_ref-spenceralavi:prb:08_3-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.77.193110"
    class="external text" rel="nofollow">J. Spencer and A. Alavi, Phys.
    Phys. Rev. B <strong>77</strong>, 193110 (2008).</a>
4.  [↑](#cite_ref-carrier:prb:2007_4-0)
    <a href="https://doi.org/10.1103/PhysRevB.86.165105"
    class="external text" rel="nofollow">P. Carrier, S. Rohra, and A.
    Görling, Phys. Rev. B <strong>75</strong>, 205126 (2007).</a>
5.  ↑
    <sup>[a](#cite_ref-sundararamanarias:prb:13_5-0)</sup>
    <sup>[b](#cite_ref-sundararamanarias:prb:13_5-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.87.165122"
    class="external text" rel="nofollow">R. Sundararaman and T. A. Arias,
    Phys. Rev. B <strong>87</strong>, 165122 (2013).</a>


------------------------------------------------------------------------


