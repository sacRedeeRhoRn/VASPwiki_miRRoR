<!-- Source: https://vasp.at/wiki/index.php/Hybrid_functionals:_formalism | revid: 36553 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Hybrid functionals: formalism


The exchange energy in hybrid functionals is a mixture of semilocal (SL)
and nonlocal Hartree-Fock (HF) types. They can be categorized into
different families according to the type of semilocal approximation
(LDA, GGA, or MGGA) or the treatment of the short- and long-range parts
of the exchange. A rather general formula that encompasses the different
families of hybrid functionals is given by

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

where

- $a_{\mathrm{SR}}$ and $a_{\mathrm{LR}}$ are the **mixing parameters (fraction of HF
  exchange) at short and long range**, respectively.
- $\mu$ is the **screening parameter** that determines
  the separation between short range (SR) and long range (LR).

The SR and LR components of the full-range $E_{\mathrm{x}}^{\mathrm{SL}}$ and $E_{\mathrm{x}}^{\mathrm{HF}}$ exchange energies are constructed such that at all
values of $\mu$

- $E_{\mathrm{x}}^{\mathrm{HF}}=E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu)+E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu)$
- $E_{\mathrm{x}}^{\mathrm{SL}}=E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu)+E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu)$

The HF exchange energy (full-range, SR, or LR) is given by
 

$E_{\mathrm{x,(SR/LR)}}^{\rm HF}(\mu)=
-\frac{1}{2}\sum_{n\mathbf{k},m\mathbf{q}} f_{n\mathbf{k}}
f_{m\mathbf{q}} \int \int d^3\mathbf{r} d^3\mathbf{r}'
v(\mu,|\mathbf{r}-\mathbf{r}'|)
\psi_{n\mathbf{k}}^{\*}(\mathbf{r})\psi_{m\mathbf{q}}^{\*}(\mathbf{r}')
\psi_{n\mathbf{k}}(\mathbf{r}')\psi_{m\mathbf{q}}(\mathbf{r})$

with $\\\psi_{n\mathbf{k}}(\mathbf{r})\\$ being the set of
one-electron Bloch states of the system, and $\\f_{n\mathbf{k}}\\$ the corresponding set of (possibly fractional)
occupational numbers. The sums over ${\bf k}$ and
${\bf q}$ run over all k-points chosen to sample the
Brillouin zone, whereas the sums over $m$ and
$n$ run over all bands at these k-points. The
corresponding nonlocal HF exchange potential is given by
 

$V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}}\left(\mu,\mathbf{r},\mathbf{r}'\right)=
-\sum_{m\mathbf{q}}f_{m\mathbf{q}}v(\mu,|\mathbf{r}-\mathbf{r}'|)\psi_{m\mathbf{q}}^{\*}(\mathbf{r}')\psi_{m\mathbf{q}}(\mathbf{r})$

The orbital-dependent form of the HF exchange energy is such that hybrid
functionals are implemented within the generalized KS
scheme[^seidl:prb:96-1].
Thus, the total energy is minimized with respect to the orbitals instead
of the electron density as in LDA and GGA, which means that the HF
potential is a nonlocal operator as in the Hartree-Fock-Roothaan theory.


## Contents


- [1 Expressions of
  the Hartree-Fock potential for the plane-wave basis
  set](#expressions-of-the-hartree-fock-potential-for-the-plane-wave-basis-set)
- [2 Types of
  potentials](#types-of-potentials)
- [3 Families of
  hybrid functionals](#families-of-hybrid-functionals)
  - [3.1 HF
    exchange at full range](#hf-exchange-at-full-range)
  - [3.2 HF
    exchange at short range (error-function
    screening)](#hf-exchange-at-short-range-error-function-screening))
  - [3.3 HF
    exchange at short range and long range with different mixings
    (error-function
    screening)](#hf-exchange-at-short-range-and-long-range-with-different-mixings-error-function-screening))
  - [3.4 HF
    exchange at long range (error-function
    screening)](#hf-exchange-at-long-range-error-function-screening))
  - [3.5 HF
    exchange at short range (exponential
    screening)](#hf-exchange-at-short-range-exponential-screening))
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


### Expressions of the Hartree-Fock potential for the plane-wave basis set\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Expressions of the Hartree-Fock potential for the plane-wave basis set">edit</a> \| (./index.php.md)\]

Using the decomposition of the Bloch states $\psi_{m\mathbf{q}}$ in plane waves,

$\psi_{m\mathbf{q}}(\mathbf{r})= \frac{1}{\sqrt{\Omega}}
\sum_\mathbf{G}C_{m\mathbf{q}}(\mathbf{G})e^{i(\mathbf{q}+\mathbf{G})
\cdot \mathbf{r}}$

the HF exchange potential can be written as

$V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}}\left(\mu,\mathbf{r},\mathbf{r}'\right)=
\sum_{\mathbf{k}}\sum_{\mathbf{G}\mathbf{G}'}
e^{i(\mathbf{k}+\mathbf{G})\cdot\mathbf{r}} V_{\mathbf{k}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)
e^{-i(\mathbf{k}+\mathbf{G}')\cdot\mathbf{r}'}$

where

$V_{\mathbf{k}}\left(\mu, \mathbf{G},\mathbf{G}'\right)= \langle
\mathbf{k}+\mathbf{G} | V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}} |
\mathbf{k}+\mathbf{G}'\rangle$

## Types of potentials\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Types of potentials">edit</a> \| (./index.php.md)\]

For most hybrid functionals proposed in the literature, the
interelectronic Coulomb potential $v(\mu,|\mathbf{r}-\mathbf{r}'|)$ is one of these
types ($r=|\mathbf{r}-\mathbf{r}'|$):

- Full range (bare Coulomb potential):

$v^{\mathrm{bare}}(r)=\frac{1}{r}$

 

$V_{\mathbf{k}}^{\mathrm{bare}}\left( \mathbf{G},\mathbf{G}'\right)=
-\frac{4\pi}{\Omega}
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
\frac{C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')}
{|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2}$

- Short-range with error function:

$v_{\mathrm{SR}}^{\mathrm{erf}}(\mu,r)=\frac{\mathrm{erfc}(\mu r)}{r}$

 

$\begin{align} V_{\mathbf{k},\mathrm{SR}}^{\mathrm{erf}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)= -\frac{4\pi}{\Omega}
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
\frac{C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')}
{|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2} \left(
1-e^{-|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2 /(4\mu^2)} \right)
\end{align}$

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Screened_operator.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/0/07/Screened_operator.png/340px-Screened_operator.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/0/07/Screened_operator.png/510px-Screened_operator.png 1.5x, /wiki/images/thumb/0/07/Screened_operator.png/680px-Screened_operator.png 2x"
width="340" height="340" /></a>
<figcaption>Short- and long-range potentials using the error or
exponential screening compared to the bare potential. $\mu=1$ is used.</figcaption>
</figure>

- Short-range with exponential function:

$v_{\mathrm{SR}}^{\mathrm{exp}}(\mu,r)=\frac{e^{-\mu r}}{r}$

 

$V_{\mathbf{k},\mathrm{SR}}^{\mathrm{exp}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)= -\frac{4\pi}{\Omega}
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
\frac{C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')}
{|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2 + \mu^2}$

The corresponding long-range potentials are given by
$v_{\mathrm{LR}}^{\mathrm{erf/exp}}=v^{\mathrm{bare}}-v_{\mathrm{SR}}^{\mathrm{erf/exp}}$.

In VASP, these expressions are implemented within the [PAW
formalism](Projector-augmented-wave_formalism.md).[^paier:jcp:05-2][^angyan:jpa:2006-3]

The families of hybrid functionals implemented in VASP are listed below
along with examples, whose corresponding [INCAR](../input-files/INCAR.md)
files can be found at the page [list of hybrid
functionals](List_of_hybrid_functionals.md).

|  |
|----|
| **Important:** The screening $\mu$ ([HFSCREEN](../incar-tags/HFSCREEN.md) tag) can be used only when the semilocal functional is PBE, PBEsol, or LDA ([GGA](../incar-tags/GGA.md)=PE, PS, or CA, respectively). The other [GGA](../incar-tags/GGA.md) and [METAGGA](../incar-tags/METAGGA.md) functionals have no screened version available in VASP. |

## Families of hybrid functionals\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Families of hybrid functionals">edit</a> \| (./index.php.md)\]

### HF exchange at full range\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: HF exchange at full range">edit</a> \| (./index.php.md)\]

There is no range separation, i.e. the same fraction of HF exchange is
applied at full range, $a_{\mathrm{SR}}=a_{\mathrm{LR}}=a$
([AEXX](../incar-tags/AEXX.md) tag):

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a E_{\mathrm{x}}^{\mathrm{HF}} +
(1-a)E_{\mathrm{x}}^{\mathrm{SL}} + E_{\mathrm{c}}^{\mathrm{SL}}$

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>These functionals are set with <a href="/wiki/LHFCALC"
title="LHFCALC">LHFCALC</a>=.TRUE. By default <a href="/wiki/AEXX"
title="AEXX">AEXX</a>=0.25, but can be set to another value.</li>
<li>The semilocal part can be of the LDA, GGA or MGGA type.</li>
</ul></td>
</tr>
</tbody>
</table>

These are the original and most simple forms of hybrid functionals. Two
examples, PBE0 and B3LYP, are given below.

- [PBE0](List_of_hybrid_functionals.md):[^perdew:jcp:1996-4]

$E_{\mathrm{xc}}^{\mathrm{PBE0}}=\frac{1}{4}
E_{\mathrm{x}}^{\mathrm{HF}} + \frac{3}{4}
E_{\mathrm{x}}^{\mathrm{PBE}} + E_{\mathrm{c}}^{\mathrm{PBE}}$

It is based on the PBE GGA
functional[^perdew:prl:1996-5]
and $a=1/4$.

- [B3LYP](List_of_hybrid_functionals.md)[^stephens:jpc:1994-6],
  well known and popular amongst quantum chemists:

 

$\begin{align} E_{\mathrm{x}}^{\mathrm{B3LYP}} &=0.8
E_{\mathrm{x}}^{\mathrm{LDA}}+ 0.2 E_{\mathrm{x}}^{\mathrm{HF}} + 0.72
(E_{\mathrm{x}}^{\mathrm{B88}}-E_{\mathrm{x}}^{\mathrm{LDA}}) + 0.19
E_{\mathrm{c}}^{\mathrm{VWN3}}+ 0.81 E_{\mathrm{c}}^{\mathrm{LYP}}
\end{align}$

The exchange part consists of 80% of LDA exchange plus 20% of HF
exchange, and 72% of the gradient corrections of the B88 GGA
functional.[^becke:pra:1988-7]
The correlation consists of 81% of
LYP[^lee:prb:1988-8]
correlation energy, which contains a LDA and a GGA part, and 19% of the
LDA Vosko-Wilk-Nusair correlation functional
III,[^vosko1980-9]
which was fitted to the correlation energy in the random phase
approximation of the homogeneous electron gas.

### HF exchange at short range (error-function screening)\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: HF exchange at short range (error-function screening)">edit</a> \| (./index.php.md)")\]

The HF exchange is used only at short-range (the long-range part is
fully semilocal, $a_{\mathrm{LR}}=0$) and the screening is done with the error function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) + E_{\mathrm{c}}^{\mathrm{SL}}$

The mixing $a_{\mathrm{SR}}$ and screening $\mu$ are
controlled by the [AEXX](../incar-tags/AEXX.md) and
[HFSCREEN](../incar-tags/HFSCREEN.md) tags, respectively.

The most popular range-separated functional, HSE, is given below.

- [HSE03](List_of_hybrid_functionals.md)[^heyd:jcp:03-10][^heyd:jcp:04-11][^heyd:jcp:06-12]
  and
  [HSE06](List_of_hybrid_functionals.md)[^krukau:jcp:06-13]:

$E_{\mathrm{xc}}^{\mathrm{HSE}}=
\frac{1}{4}E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + \frac{3}{4}
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

They are based on the PBE GGA
functional[^perdew:prl:1996-5]
and $a_{\mathrm{SR}}=1/4$. It has been shown that the optimum
$\mu$, controlling the range separation is approximately
0.2-0.3
Å<sup>-1</sup>.[^heyd:jcp:03-10][^heyd:jcp:04-11][^heyd:jcp:06-12][^krukau:jcp:06-13]
[HSE03](List_of_hybrid_functionals.md)
and
[HSE06](List_of_hybrid_functionals.md)
correspond to [HFSCREEN](../incar-tags/HFSCREEN.md)=0.3 and 0.2,
respectively. Note that the two limit cases of HSE are
[PBE0](List_of_hybrid_functionals.md)
at $\mu=0$ and PBE at $\mu\rightarrow\infty$.

### HF exchange at short range and long range with different mixings (error-function screening)\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: HF exchange at short range and long range with different mixings (error-function screening)">edit</a> \| (./index.php.md)")\]

The fractions of HF exchange at short and long range
($a_{\mathrm{SR}}$ and $a_{\mathrm{LR}}$, respectively) can be different:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

These functionals are selected with
[LMODELHF](../incar-tags/LMODELHF.md)=.TRUE. The mixings
$a_{\mathrm{LR}}$ and $a_{\mathrm{SR}}$ are controlled by the [AEXX](../incar-tags/AEXX.md) and
[BEXX](../incar-tags/BEXX.md) tags, respectively, and the screening
$\mu$ by the [HFSCREEN](../incar-tags/HFSCREEN.md) tag.

|  |
|----|
| **Important:** The possibility to set $a_{\mathrm{SR}}$ with [BEXX](../incar-tags/BEXX.md) within the [LMODELHF](../incar-tags/LMODELHF.md)=.TRUE. method was introduced in VASP.6.6.0. Until VASP.6.5.1 $a_{\mathrm{SR}}$ was fixed to 1 and could not be changed. |

This functional form has been used in the context of
dielectric-dependent hybrids. Examples are provided below.

- [RS-DDH](List_of_hybrid_functionals.md):[^skone:prb:2016-14]

$E_{\mathrm{xc}}^{\mathrm{RS-DDH}}=\frac{1}{4}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
\frac{3}{4}E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{c}}^{\mathrm{PBE}}$

where $a_{\mathrm{SR}}=1/4$ and $a_{\mathrm{LR}}=\varepsilon^{-1}$ is chosen as the
inverse of the dielectric constant $\varepsilon^{-1}$.

- [DD-RSH-CAM](List_of_hybrid_functionals.md),[^chen2018nonempirical-15]
  [DSH](List_of_hybrid_functionals.md):[^cui2018doubly-16]

$E_{\mathrm{xc}}^{\mathrm{DD-RSH-CAM}}=E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
a_{\mathrm{LR}} E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{c}}^{\mathrm{PBE}}$

where $a_{\mathrm{SR}}=1$ and $a_{\mathrm{LR}}=\varepsilon^{-1}$ is chosen as the
inverse of the dielectric constant $\varepsilon^{-1}$.

### HF exchange at long range (error-function screening)\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: HF exchange at long range (error-function screening)">edit</a> \| (./index.php.md)")\]

The HF exchange is used only at long-range (the short-range part is
fully semilocal, $a_{\mathrm{SR}}=0$) and the screening is done with the error function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

These functionals are selected with
[LRHFCALC](../incar-tags/LRHFCALC.md)=.TRUE. The mixing
$a_{\mathrm{LR}}$ and screening
$\mu$ are controlled by the [AEXX](../incar-tags/AEXX.md)
and [HFSCREEN](../incar-tags/HFSCREEN.md) tags, respectively.

|  |
|----|
| **Mind:** [LRHFCALC](../incar-tags/LRHFCALC.md)=.TRUE. automatically sets [AEXX](../incar-tags/AEXX.md)=1. However, [AEXX](../incar-tags/AEXX.md) can be set to another value. |

|  |
|----|
| **Important:** When [AEXX](../incar-tags/AEXX.md)=1 (the default for [LRHFCALC](../incar-tags/LRHFCALC.md)=.TRUE.), the correlation $E_{\mathrm{c}}^{\mathrm{SL}}$ is not included. However, it can be included by setting [ALDAC](../incar-tags/ALDAC.md)=1.0 and [AGGAC](../incar-tags/AGGAC.md)=1.0. |

Long-range hybrid functionals are more popular in molecular chemistry,
where a proper decay of the exchange-correlation potential at long range
far from the nuclei may be important, and thus less useful for bulk
solids. Examples belonging to this class of functionals are:

- [RSHXLDA](List_of_hybrid_functionals.md)
  and
  [RSHXPBE](List_of_hybrid_functionals.md):[^iikura:jcp:2001-17][^gerber:cpl:2005-18][^gerber:jcp:2007-19]

$E_{\mathrm{xc}}^{\mathrm{RSHXLDA}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{LDA}}(\mu) + E_{\mathrm{c}}^{\mathrm{LDA}}$

$E_{\mathrm{xc}}^{\mathrm{RSHXPBE}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

When LDA is chosen, a value of $\mu=0.75$
Å<sup>-1</sup> is recommended for
solids.[^gerber:jcp:2007-19]

### HF exchange at short range (exponential screening)\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: HF exchange at short range (exponential screening)">edit</a> \| (./index.php.md)")\]

The HF exchange is used only at short-range (the long-range part is
fully semilocal, $a_{\mathrm{LR}}=0$) and the screening is done with the exponential
function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) + E_{\mathrm{c}}^{\mathrm{SL}}$

The exponential screening, also called Thomas-Fermi (TF)
screening,[^bylander:prb:90-20][^seidl:prb:96-1][^picozzi:prb:00-21]
is activated by setting [LTHOMAS](../incar-tags/LTHOMAS.md)=.TRUE.. The
mixing $a_{\mathrm{SR}}$ and screening $\mu=k_{\rm TF}$ are controlled by the [AEXX](../incar-tags/AEXX.md) and
[HFSCREEN](../incar-tags/HFSCREEN.md) tags, respectively.

|  |
|----|
| **Mind:** [LTHOMAS](../incar-tags/LTHOMAS.md)=.TRUE. automatically sets [AEXX](../incar-tags/AEXX.md)=1. However, [AEXX](../incar-tags/AEXX.md) can be set to another value. |

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong>
<ul>
<li>When <a href="/wiki/AEXX" title="AEXX">AEXX</a>=1 (the default for
<a href="/wiki/LTHOMAS" title="LTHOMAS">LTHOMAS</a>=.TRUE.), the
correlation <span class="smj-container"
style="opacity:.5">$E_{\mathrm{c}}^{\mathrm{SL}}$</span> is not included. However, it can be included by setting
<a href="/wiki/ALDAC" title="ALDAC">ALDAC</a>=1.0 and <a
href="/wiki/AGGAC" title="AGGAC">AGGAC</a>=1.0.</li>
<li>This functional should be used only with LDA (<a href="/wiki/GGA"
title="GGA">GGA</a>=CA).</li>
</ul></td>
</tr>
</tbody>
</table>

The sX-LDA functional, which uses $a_{\mathrm{SR}}=1$, is probably the first hybrid using an exponential
screening:

- [sX-LDA](List_of_hybrid_functionals.md):[^bylander:prb:90-20]

$E_{\mathrm{xc}}^{\mathrm{sX-LDA}} =
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{LDA}}(\mu) + E_{\mathrm{c}}^{\mathrm{LDA}}$

For typical semiconductors, a Thomas-Fermi screening length
$\mu=k_{\rm TF}$ of about 1.8 Å<sup>-1</sup> yields
reasonable band gaps. In principle, however, the Thomas-Fermi screening
length depends on the valence-electron density. VASP determines
$k_{\rm TF}$ from the number of valence electrons (read
from the [POTCAR](../input-files/POTCAR.md) file) and the volume (leading
to an average density $\bar{n}$) and
writes the corresponding value of $k_{\rm
TF}=\sqrt{4\bar{k}_{\rm F}/\pi}$, where
$\bar{k}_{\rm F}=(3\pi^2\bar{n})^{1/3}$ to the
[OUTCAR](../output-files/OUTCAR.md) file (**note that this value is only
printed for information and is not used during the calculation**):

     Thomas-Fermi vector in A             =   2.00000

Since VASP counts the semi-core states and *d*-states as valence
electrons, although these states do not contribute to the screening, the
values reported by VASP are often not recommended.

Another important detail concerns the implementation of the local LDA
part in VASP. Literature \[see Eqs. (3.10), (3.14), and (3.15) in Ref.
[^seidl:prb:96-1]\]
suggests to use in the enhancement factor $F(z)$ a
position-independent variable $z=k_{\rm TF}/\bar{k}_{\rm F}$ where $\bar{k}_{\rm F}$ is as defined above but using the average density
$\bar{n}$ in the unit cell. However, implemented in VASP
is a position-dependent variable $z({\bf r})=k_{\rm TF}/k_{\rm
F}({\bf r})$, where $k_{\rm F}({\bf r})=(3\pi^2
n({\bf r}))^{1/3}$ is the Fermi wave vector calculated
with the local density $n({\bf r})$,
while the constant $k_{\rm TF}$
is set by [HFSCREEN](../incar-tags/HFSCREEN.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[AEXX](../incar-tags/AEXX.md), [BEXX](../incar-tags/BEXX.md),
[ALDAX](../incar-tags/ALDAX.md), [ALDAC](../incar-tags/ALDAC.md),
[AGGAX](../incar-tags/AGGAX.md), [AGGAC](../incar-tags/AGGAC.md),
[AMGGAX](../incar-tags/AMGGAX.md), [AMGGAC](../incar-tags/AMGGAC.md),
[HFSCREEN](../incar-tags/HFSCREEN.md),
[LHFCALC](../incar-tags/LHFCALC.md),
[LMODELHF](../incar-tags/LMODELHF.md),
[LTHOMAS](../incar-tags/LTHOMAS.md),
[LRHFCALC](../incar-tags/LRHFCALC.md), [List of hybrid
functionals](List_of_hybrid_functionals.md),
[Downsampling of the Hartree-Fock
operator](Downsampling_of_the_Hartree-Fock_operator.md),
[Coulomb singularity](Coulomb_singularity.md)

## References\[<a
href="/wiki/index.php?title=Hybrid_functionals:_formalism&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^seidl:prb:96-1]: [A. Seidl, A. Görling, P. Vogl, J.A. Majewski, and M. Levy, Phys. Rev. B **53**, 3764 (1996).](https://doi.org/10.1103/PhysRevB.53.3764)
[^paier:jcp:05-2]: [J. Paier, R. Hirschl, M. Marsman, and G. Kresse, J. Chem. Phys. **122**, 234102 (2005).](https://doi.org/10.1063/1.1926272)
[^angyan:jpa:2006-3]: [J. G. Ángyán, I. Gerber, and M. Marsman, *Spherical harmonic expansion of short-range screened Coulomb interactions*, J. Phys. A: Math. Gen. **39**, 8613 (2006).](http://dx.doi.org/10.1088/0305-4470/39/27/005)
[^perdew:jcp:1996-4]: [J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys. **105**, 9982 (1996).](https://doi.org/10.1063/1.472933)
[^perdew:prl:1996-5]: [J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865 (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
[^stephens:jpc:1994-6]: [P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M. J. Frisch, J. Phys. Chem. **98**, 11623 (1994).](https://doi.org/10.1021/j100096a001)
[^becke:pra:1988-7]: [A. D. Becke, *Density-functional exchange-energy approximation with correct asymptotic behavior*, Phys. Rev. A **38**, 3098 (1988).](https://doi.org/10.1103/PhysRevA.38.3098)
[^lee:prb:1988-8]: [C. Lee, W. Yang, and R. G. Parr, *Development of the Colle-Salvetti correlation-energy formula into a functional of the electron density*, Phys. Rev. B **37**, 785 (1988).](https://doi.org/10.1103/PhysRevB.37.785)
[^vosko1980-9]: [S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. **58**, 1200 (1980).](https://doi.org/10.1139/p80-159)
[^heyd:jcp:03-10]: [J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. **118**, 8207 (2003).](https://doi.org/10.1063/1.1564060)
[^heyd:jcp:04-11]: [J. Heyd and G. E. Scuseria, J. Chem. Phys. **121**, 1187 (2004).](https://doi.org/10.1063/1.1760074)
[^heyd:jcp:06-12]: [J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. **124**, 219906 (2006).](https://doi.org/10.1063/1.2204597)
[^krukau:jcp:06-13]: [A. V. Krukau , O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**, 224106 (2006).](https://doi.org/10.1063/1.2404663)
[^skone:prb:2016-14]: [J. H. Skone, M. Govoni, and G. Galli, *Nonempirical range-separated hybrid functionals for solids and molecules*, Phys. Rev. B **93**, 235106 (2016).](http://doi.org/10.1103/PhysRevB.93.235106)
[^chen2018nonempirical-15]: [W. Chen, G. Miceli, G.M. Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent hybrid functional with range separation for semiconductors and insulators*, Phys. Rev. Mater. **2**, 073803 (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
[^cui2018doubly-16]: [Z.H. Cui, Y.C. Wang, M.Y. Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An Accurate First-Principles Approach for Both Narrow- and Wide-Gap Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345 (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
[^iikura:jcp:2001-17]: [H. Iikura, T. Tsuneda, T. Yanai, and K. Hirao, *A long-range correction scheme for generalized-gradient-approximation exchange functionals*, J. Chem. Phys. **115**, 3540 (2001).](http://doi.org/10.1063/1.1383587)
[^gerber:cpl:2005-18]: [I. C. Gerber and J. G. Ángyán, *Hybrid functional with separated range*, Chem. Phys. Lett. **415**, 100 (2005).](http://doi.org/10.1016/j.cplett.2005.08.060)
[^gerber:jcp:2007-19]: [I. C. Gerber, J. G. Ángyán, M. Marsman, and G. Kresse, *Range separated hybrid density functional with long-range Hartree-Fock exchange applied to solids*, J. Chem. Phys. **127**, 054101 (2007).](http://doi.org/10.1063/1.2759209)
[^bylander:prb:90-20]: [D. M. Bylander and L. Kleinman, Phys. Rev. B **41**, 7868 (1990).](https://doi.org/10.1103/PhysRevB.41.7868)
[^picozzi:prb:00-21]: [S. Picozzi, A. Continenza, R. Asahi, W. Mannstadt, A.J. Freeman, W. Wolf, E. Wimmer, and C.B. Geller, Phys. Rev. B **61**, 4677 (2000).](https://doi.org/10.1103/PhysRevB.61.4677)
