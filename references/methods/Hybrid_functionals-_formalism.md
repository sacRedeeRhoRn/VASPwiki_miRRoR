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
scheme<sup>[\[1\]](#cite_note-seidl:prb:96-1)</sup>.
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
formalism](Projector-augmented-wave_formalism.md).<sup>[\[2\]](#cite_note-paier:jcp:05-2)[\[3\]](#cite_note-angyan:jpa:2006-3)</sup>

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

- [PBE0](List_of_hybrid_functionals.md):<sup>[\[4\]](#cite_note-perdew:jcp:1996-4)</sup>

$E_{\mathrm{xc}}^{\mathrm{PBE0}}=\frac{1}{4}
E_{\mathrm{x}}^{\mathrm{HF}} + \frac{3}{4}
E_{\mathrm{x}}^{\mathrm{PBE}} + E_{\mathrm{c}}^{\mathrm{PBE}}$

It is based on the PBE GGA
functional<sup>[\[5\]](#cite_note-perdew:prl:1996-5)</sup>
and $a=1/4$.

- [B3LYP](List_of_hybrid_functionals.md)<sup>[\[6\]](#cite_note-stephens:jpc:1994-6)</sup>,
  well known and popular amongst quantum chemists:

 

$\begin{align} E_{\mathrm{x}}^{\mathrm{B3LYP}} &=0.8
E_{\mathrm{x}}^{\mathrm{LDA}}+ 0.2 E_{\mathrm{x}}^{\mathrm{HF}} + 0.72
(E_{\mathrm{x}}^{\mathrm{B88}}-E_{\mathrm{x}}^{\mathrm{LDA}}) + 0.19
E_{\mathrm{c}}^{\mathrm{VWN3}}+ 0.81 E_{\mathrm{c}}^{\mathrm{LYP}}
\end{align}$

The exchange part consists of 80% of LDA exchange plus 20% of HF
exchange, and 72% of the gradient corrections of the B88 GGA
functional.<sup>[\[7\]](#cite_note-becke:pra:1988-7)</sup>
The correlation consists of 81% of
LYP<sup>[\[8\]](#cite_note-lee:prb:1988-8)</sup>
correlation energy, which contains a LDA and a GGA part, and 19% of the
LDA Vosko-Wilk-Nusair correlation functional
III,<sup>[\[9\]](#cite_note-vosko1980-9)</sup>
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

- [HSE03](List_of_hybrid_functionals.md)<sup>[\[10\]](#cite_note-heyd:jcp:03-10)[\[11\]](#cite_note-heyd:jcp:04-11)[\[12\]](#cite_note-heyd:jcp:06-12)</sup>
  and
  [HSE06](List_of_hybrid_functionals.md)<sup>[\[13\]](#cite_note-krukau:jcp:06-13)</sup>:

$E_{\mathrm{xc}}^{\mathrm{HSE}}=
\frac{1}{4}E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + \frac{3}{4}
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

They are based on the PBE GGA
functional<sup>[\[5\]](#cite_note-perdew:prl:1996-5)</sup>
and $a_{\mathrm{SR}}=1/4$. It has been shown that the optimum
$\mu$, controlling the range separation is approximately
0.2-0.3
Å<sup>-1</sup>.<sup>[\[10\]](#cite_note-heyd:jcp:03-10)[\[11\]](#cite_note-heyd:jcp:04-11)[\[12\]](#cite_note-heyd:jcp:06-12)[\[13\]](#cite_note-krukau:jcp:06-13)</sup>
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

- [RS-DDH](List_of_hybrid_functionals.md):<sup>[\[14\]](#cite_note-skone:prb:2016-14)</sup>

$E_{\mathrm{xc}}^{\mathrm{RS-DDH}}=\frac{1}{4}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
\frac{3}{4}E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{c}}^{\mathrm{PBE}}$

where $a_{\mathrm{SR}}=1/4$ and $a_{\mathrm{LR}}=\varepsilon^{-1}$ is chosen as the
inverse of the dielectric constant $\varepsilon^{-1}$.

- [DD-RSH-CAM](List_of_hybrid_functionals.md),<sup>[\[15\]](#cite_note-chen2018nonempirical-15)</sup>
  [DSH](List_of_hybrid_functionals.md):<sup>[\[16\]](#cite_note-cui2018doubly-16)</sup>

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
  [RSHXPBE](List_of_hybrid_functionals.md):<sup>[\[17\]](#cite_note-iikura:jcp:2001-17)[\[18\]](#cite_note-gerber:cpl:2005-18)[\[19\]](#cite_note-gerber:jcp:2007-19)</sup>

$E_{\mathrm{xc}}^{\mathrm{RSHXLDA}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{LDA}}(\mu) + E_{\mathrm{c}}^{\mathrm{LDA}}$

$E_{\mathrm{xc}}^{\mathrm{RSHXPBE}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

When LDA is chosen, a value of $\mu=0.75$
Å<sup>-1</sup> is recommended for
solids.<sup>[\[19\]](#cite_note-gerber:jcp:2007-19)</sup>

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
screening,<sup>[\[20\]](#cite_note-bylander:prb:90-20)[\[1\]](#cite_note-seidl:prb:96-1)[\[21\]](#cite_note-picozzi:prb:00-21)</sup>
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

- [sX-LDA](List_of_hybrid_functionals.md):<sup>[\[20\]](#cite_note-bylander:prb:90-20)</sup>

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
<sup>[\[1\]](#cite_note-seidl:prb:96-1)</sup>\]
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


1.  ↑
    <sup>[a](#cite_ref-seidl:prb:96_1-0)</sup>
    <sup>[b](#cite_ref-seidl:prb:96_1-1)</sup>
    <sup>[c](#cite_ref-seidl:prb:96_1-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.53.3764" class="external text"
    rel="nofollow">A. Seidl, A. Görling, P. Vogl, J.A. Majewski, and M.
    Levy, Phys. Rev. B <strong>53</strong>, 3764 (1996).</a>
2.  [↑](#cite_ref-paier:jcp:05_2-0)
    <a href="https://doi.org/10.1063/1.1926272" class="external text"
    rel="nofollow">J. Paier, R. Hirschl, M. Marsman, and G. Kresse, J. Chem.
    Phys. <strong>122</strong>, 234102 (2005).</a>
3.  [↑](#cite_ref-angyan:jpa:2006_3-0)
    <a href="http://dx.doi.org/10.1088/0305-4470/39/27/005"
    class="external text" rel="nofollow">J. G. Ángyán, I. Gerber, and M.
    Marsman, <em>Spherical harmonic expansion of short-range screened
    Coulomb interactions</em>, J. Phys. A: Math. Gen. <strong>39</strong>,
    8613 (2006).</a>
4.  [↑](#cite_ref-perdew:jcp:1996_4-0)
    <a href="https://doi.org/10.1063/1.472933" class="external text"
    rel="nofollow">J. P. Perdew, M. Ernzerhof, and K. Burke, J. Chem. Phys.
    <strong>105</strong>, 9982 (1996).</a>
5.  ↑
    <sup>[a](#cite_ref-perdew:prl:1996_5-0)</sup>
    <sup>[b](#cite_ref-perdew:prl:1996_5-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.77.3865"
    class="external text" rel="nofollow">J. P. Perdew, K. Burke, and M.
    Ernzerhof, Phys. Rev. Lett., <strong>77</strong>, 3865 (1996).</a>
6.  [↑](#cite_ref-stephens:jpc:1994_6-0)
    <a href="https://doi.org/10.1021/j100096a001" class="external text"
    rel="nofollow">P. J. Stephens, F. J. Devlin, C. F. Chabalowski, and M.
    J. Frisch, J. Phys. Chem. <strong>98</strong>, 11623 (1994).</a>
7.  [↑](#cite_ref-becke:pra:1988_7-0)
    <a href="https://doi.org/10.1103/PhysRevA.38.3098" class="external text"
    rel="nofollow">A. D. Becke, <em>Density-functional exchange-energy
    approximation with correct asymptotic behavior</em>, Phys. Rev. A
    <strong>38</strong>, 3098 (1988).</a>
8.  [↑](#cite_ref-lee:prb:1988_8-0)
    <a href="https://doi.org/10.1103/PhysRevB.37.785" class="external text"
    rel="nofollow">C. Lee, W. Yang, and R. G. Parr, <em>Development of the
    Colle-Salvetti correlation-energy formula into a functional of the
    electron density</em>, Phys. Rev. B <strong>37</strong>, 785 (1988).</a>
9.  [↑](#cite_ref-vosko1980_9-0)
    <a href="https://doi.org/10.1139/p80-159" class="external text"
    rel="nofollow">S. H. Vosko, L. Wilk, and M. Nusair, Can. J. Phys.
    <strong>58</strong>, 1200 (1980).</a>
10. ↑
    <sup>[a](#cite_ref-heyd:jcp:03_10-0)</sup>
    <sup>[b](#cite_ref-heyd:jcp:03_10-1)</sup>
    <a href="https://doi.org/10.1063/1.1564060" class="external text"
    rel="nofollow">J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys.
    <strong>118</strong>, 8207 (2003).</a>
11. ↑
    <sup>[a](#cite_ref-heyd:jcp:04_11-0)</sup>
    <sup>[b](#cite_ref-heyd:jcp:04_11-1)</sup>
    <a href="https://doi.org/10.1063/1.1760074" class="external text"
    rel="nofollow">J. Heyd and G. E. Scuseria, J. Chem. Phys.
    <strong>121</strong>, 1187 (2004).</a>
12. ↑
    <sup>[a](#cite_ref-heyd:jcp:06_12-0)</sup>
    <sup>[b](#cite_ref-heyd:jcp:06_12-1)</sup>
    <a href="https://doi.org/10.1063/1.2204597" class="external text"
    rel="nofollow">J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys.
    <strong>124</strong>, 219906 (2006).</a>
13. ↑
    <sup>[a](#cite_ref-krukau:jcp:06_13-0)</sup>
    <sup>[b](#cite_ref-krukau:jcp:06_13-1)</sup>
    <a href="https://doi.org/10.1063/1.2404663" class="external text"
    rel="nofollow">A. V. Krukau , O. A. Vydrov, A. F. Izmaylov, and G. E.
    Scuseria, J. Chem. Phys. <strong>125</strong>, 224106 (2006).</a>
14. [↑](#cite_ref-skone:prb:2016_14-0)
    <a href="http://doi.org/10.1103/PhysRevB.93.235106"
    class="external text" rel="nofollow">J. H. Skone, M. Govoni, and G.
    Galli, <em>Nonempirical range-separated hybrid functionals for solids
    and molecules</em>, Phys. Rev. B <strong>93</strong>, 235106 (2016).</a>
15. [↑](#cite_ref-chen2018nonempirical_15-0)
    <a href="https://doi.org/10.1103/PhysRevMaterials.2.073803"
    class="external text" rel="nofollow">W. Chen, G. Miceli, G.M. Rignanese,
    and A. Pasquarello, <em>Nonempirical dielectric-dependent hybrid
    functional with range separation for semiconductors and insulators</em>,
    Phys. Rev. Mater. <strong>2</strong>, 073803 (2018).</a>
16. [↑](#cite_ref-cui2018doubly_16-0)
    <a href="https://doi.org/10.1021/acs.jpclett.8b00919"
    class="external text" rel="nofollow">Z.H. Cui, Y.C. Wang, M.Y. Zhang, X.
    Xu, and H. Jiang, <em>Doubly Screened Hybrid Functional: An Accurate
    First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors</em> J. Phys. Chem. Lett., <strong>9</strong>, 2338-2345
    (2018).</a>
17. [↑](#cite_ref-iikura:jcp:2001_17-0)
    <a href="http://doi.org/10.1063/1.1383587" class="external text"
    rel="nofollow">H. Iikura, T. Tsuneda, T. Yanai, and K. Hirao, <em>A
    long-range correction scheme for generalized-gradient-approximation
    exchange functionals</em>, J. Chem. Phys. <strong>115</strong>, 3540
    (2001).</a>
18. [↑](#cite_ref-gerber:cpl:2005_18-0)
    <a href="http://doi.org/10.1016/j.cplett.2005.08.060"
    class="external text" rel="nofollow">I. C. Gerber and J. G. Ángyán,
    <em>Hybrid functional with separated range</em>, Chem. Phys. Lett.
    <strong>415</strong>, 100 (2005).</a>
19. ↑
    <sup>[a](#cite_ref-gerber:jcp:2007_19-0)</sup>
    <sup>[b](#cite_ref-gerber:jcp:2007_19-1)</sup>
    <a href="http://doi.org/10.1063/1.2759209" class="external text"
    rel="nofollow">I. C. Gerber, J. G. Ángyán, M. Marsman, and G. Kresse,
    <em>Range separated hybrid density functional with long-range
    Hartree-Fock exchange applied to solids</em>, J. Chem. Phys.
    <strong>127</strong>, 054101 (2007).</a>
20. ↑
    <sup>[a](#cite_ref-bylander:prb:90_20-0)</sup>
    <sup>[b](#cite_ref-bylander:prb:90_20-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.41.7868" class="external text"
    rel="nofollow">D. M. Bylander and L. Kleinman, Phys. Rev. B
    <strong>41</strong>, 7868 (1990).</a>
21. [↑](#cite_ref-picozzi:prb:00_21-0)
    <a href="https://doi.org/10.1103/PhysRevB.61.4677" class="external text"
    rel="nofollow">S. Picozzi, A. Continenza, R. Asahi, W. Mannstadt, A.J.
    Freeman, W. Wolf, E. Wimmer, and C.B. Geller, Phys. Rev. B
    <strong>61</strong>, 4677 (2000).</a>


