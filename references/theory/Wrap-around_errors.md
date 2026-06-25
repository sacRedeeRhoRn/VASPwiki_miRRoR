<!-- Source: https://vasp.at/wiki/index.php/Wrap-around_errors | revid: 32949 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Wrap-around errors


**Wrap-around errors** arise if the
<a href="/wiki/FFT_meshes" class="mw-redirect" title="FFT meshes">Fast
Fourier transformation (FFT) meshes</a> are not sufficiently large. It
can be shown that no errors exist if the
<a href="/wiki/FFT_meshes" class="mw-redirect" title="FFT meshes">FFT
meshes</a> contain all $\mathbf{G}$
vectors up to $2 G_{\rm cut}$.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Wrap_errors_spheres.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/6/61/Wrap_errors_spheres.png/350px-Wrap_errors_spheres.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/6/61/Wrap_errors_spheres.png 1.5x" width="350"
height="452" /></a>
<figcaption>Fig. 1: Sphere intersections for $G_{\mathrm{cut}}$</figcaption>
</figure>

It can be shown that the charge density contains components up to
$2
G_{\mathrm{cut}}$, where $2 G_{\mathrm{cut}}$ is the "longest" plane wave in the basis set:

The wavefunction is defined as

$|
\phi_{n\mathbf{k}} \rangle = \sum_\mathbf{G}
C_{\mathbf{G}n\mathbf{k}} | \mathbf{k}+\mathbf{G}\rangle,$

and in real space it is given by

$\langle \mathbf{r}| \phi_{n\mathbf{k}} \rangle = \sum_\mathbf{G}
\langle \mathbf{r}| \mathbf{k}+\mathbf{G}\rangle \langle
\mathbf{k}+\mathbf{G}|\phi_{n\mathbf{k}} \rangle =
\frac{1}{\Omega^{1/2}} \sum_\mathbf{G}
e^{i(\mathbf{k}+\mathbf{G})\mathbf{r}} C_{\mathbf{G}n\mathbf{k}}.$

Using FFTs one can define

$C_{\mathbf{r}n\mathbf{k}}= \sum_{\mathbf{G}}
C_{\mathbf{G}n\mathbf{k}} e^{i\mathbf{G} \mathbf{r}} \qquad \qquad
\qquad C_{\mathbf{G}n\mathbf{k}}= \frac{1}{N_{\mathrm{FFT}}}
\sum_{\mathbf{r}} C_{\mathbf{r}n\mathbf{k}} e^{-i\mathbf{G}
\mathbf{r}}.$

Therefore the wavefunction can be written in real space as

$\langle\mathbf{r}| \phi_{n\mathbf{k}} \rangle = \phi_{n\mathbf{k}}(r)
= \frac{1}{\Omega^{1/2}} C_{\mathbf{r}n\mathbf{k}}
e^{i\mathbf{k}\mathbf{r}}.$

The charge density is simply given by

$\rho^{\mathrm{ps}}_{\mathbf{r}} \equiv \langle \mathbf{r}
|\rho^{\mathrm{ps}} | \mathbf{r} \rangle = \sum_\mathbf{k}
w_{\mathbf{k}} \sum_n f_{n\mathbf{k}} \phi_{n\mathbf{k}}(r)
\phi^{\*}_{n\mathbf{k}}(r) ,$

and in the reciprocal mesh it can be written as

$\rho^{\mathrm{ps}}_\mathbf{G} \equiv \frac{1}{\Omega} \int
\langle\mathbf{r} | \rho^{\mathrm{ps}}| \mathbf{r}\rangle e^{-i
\mathbf{G}\mathbf{r}}\\ d \mathbf{r} \to \frac{1}{N_{\mathrm{FFT}}}
\sum_{\mathbf{r}} \rho^{\mathrm{ps}}_{\mathbf{r}} e^{-i
\mathbf{G}\mathbf{r}}.$

Using the above equations for $\rho^{\mathrm{ps}}_{\mathbf{r}}$ and
$C_{\mathbf{r}n\mathbf{k}}$ it is very easy to show
that $\rho^{\mathrm{ps}}_{\mathbf{r}}$ contains
Fourier-components up to $2 G_{\mathrm{cut}}$.

Generally it can be shown that a the convolution
$f_r=f^1_r f^2_r$ of two functions
$f^1_r$ with Fourier-components up to
$G_1$ and $f^2_r$ with
Fourier-components up to $G_2$ contains
Fourier-components up to $G_1+G_2$.

The property of the convolution comes once again into play, when the
action of the Hamiltonian onto a wavefunction is calculated. The action
of the local-potential is given by

$a_{\mathbf{r}} = V_{\mathbf{r}} C_{\mathbf{r}n\mathbf{k}}.$

Only the components $a_{\mathbf{G}}$ with $|\mathbf{G}| <
G_{\mathrm{cut}}$ are taken into account (see section
[ALGO](../incar-tags/ALGO.md): $a_{\mathbf{G}}$ is added to the wavefunction during the iterative
refinement of the wavefunctions $C_{\mathbf{G}n\mathbf{k}}$, and $C_{\mathbf{G}n\mathbf{k}}$ contains only components up to
$G_{\mathrm{cut}}$). From the previous theorem we see
that $a_{\mathbf{r}}$ contains components up to $3 G_{\mathrm{cut}}$ ($V_{\mathbf{r}}$ contains components up to $2 G_{\mathrm{cut}}$).

If the FFT mesh contains all components up to
$2
G_{\mathrm cut}$ the resulting wrap-around error is
once again 0. This can be easily seen in Fig. 1. Here we see that the
small sphere contains all plane waves included in the basis set
$G<G_{\mathrm{cut}}$. The charge density contains
components up to $2 G_{\mathrm{cut}}$ (second sphere), and the acceleration
$a$ components up to $3 G_{\mathrm{cut}}$, which are reflected in (third sphere) because of the
finite size of the FFT mesh. Nevertheless the components
$a_{\mathbf{G}}$ with $| \mathbf{G}| <
G_{\mathrm{cut}}$ are correct i.e. the small sphere
does not intersect with the third large sphere}

## Related tags and articles\[<a
href="/wiki/index.php?title=Wrap-around_errors&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PREC](../incar-tags/PREC.md), [ENCUT](../incar-tags/ENCUT.md),
[NGX](../incar-tags/NGX.md), [NGY](../incar-tags/NGY.md), [NGZ](../incar-tags/NGZ.md)

[Energy cutoff and FFT
meshes](../tutorials/Energy_cutoff_and_FFT_meshes.md)


