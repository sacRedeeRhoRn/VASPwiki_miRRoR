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

- $a_{\mathrm{SR}}$ and
  $a_{\mathrm{LR}}$ are the **mixing
  parameters (fraction of HF exchange) at short and long range**,
  respectively.
- $\mu$ is the **screening parameter**
  that determines the separation between short range (SR) and long range
  (LR).

The SR and LR components of the full-range $E_{\mathrm{x}}^{\mathrm{SL}}$ and $E_{\mathrm{x}}^{\mathrm{HF}}$ exchange energies are
constructed such that at all values of $\mu$

- $E_{\mathrm{x}}^{\mathrm{HF}}=E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu)+E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu)$
- $E_{\mathrm{x}}^{\mathrm{SL}}=E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu)+E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu)$

The HF exchange energy (full-range, SR, or LR) is given by

$E_{\mathrm{x,(SR/LR)}}^{\rm HF}(\mu)=
-\frac{1}{2}\sum_{n\mathbf{k},m\mathbf{q}} f_{n\mathbf{k}}
f_{m\mathbf{q}} \int \int d^3\mathbf{r} d^3\mathbf{r}'
v(\mu,|\mathbf{r}-\mathbf{r}'|)
\psi_{n\mathbf{k}}^{\*}(\mathbf{r})\psi_{m\mathbf{q}}^{\*}(\mathbf{r}')
\psi_{n\mathbf{k}}(\mathbf{r}')\psi_{m\mathbf{q}}(\mathbf{r})$

with $\\\psi_{n\mathbf{k}}(\mathbf{r})\\$ being the set of one-electron Bloch states of the system, and
$\\f_{n\mathbf{k}}\\$ the corresponding
set of (possibly fractional) occupational numbers. The sums over
${\bf k}$ and ${\bf q}$ run over all k-points chosen to sample the Brillouin
zone, whereas the sums over $m$ and
$n$ run over all bands at these
k-points. The corresponding nonlocal HF exchange potential is given by

$V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}}\left(\mu,\mathbf{r},\mathbf{r}'\right)=
-\sum_{m\mathbf{q}}f_{m\mathbf{q}}v(\mu,|\mathbf{r}-\mathbf{r}'|)\psi_{m\mathbf{q}}^{\*}(\mathbf{r}')\psi_{m\mathbf{q}}(\mathbf{r})$

The orbital-dependent form of the HF exchange energy is such that hybrid
functionals are implemented within the generalized KS
scheme^([\[1\]](#cite_note-seidl:prb:96-1)). Thus, the total energy is
minimized with respect to the orbitals instead of the electron density
as in LDA and GGA, which means that the HF potential is a nonlocal
operator as in the Hartree-Fock-Roothaan theory.

## Contents

- [1 Expressions of the Hartree-Fock potential for the plane-wave basis
  set](#Expressions_of_the_Hartree-Fock_potential_for_the_plane-wave_basis_set)
- [2 Types of potentials](#Types_of_potentials)
- [3 Families of hybrid functionals](#Families_of_hybrid_functionals)
  - [3.1 HF exchange at full range](#HF_exchange_at_full_range)
  - [3.2 HF exchange at short range (error-function
    screening)](#HF_exchange_at_short_range_(error-function_screening))
  - [3.3 HF exchange at short range and long range with different
    mixings (error-function
    screening)](#HF_exchange_at_short_range_and_long_range_with_different_mixings_(error-function_screening))
  - [3.4 HF exchange at long range (error-function
    screening)](#HF_exchange_at_long_range_(error-function_screening))
  - [3.5 HF exchange at short range (exponential
    screening)](#HF_exchange_at_short_range_(exponential_screening))
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

### Expressions of the Hartree-Fock potential for the plane-wave basis set
Using the decomposition of the Bloch states $\psi_{m\mathbf{q}}$ in plane waves,

$\psi_{m\mathbf{q}}(\mathbf{r})=
\frac{1}{\sqrt{\Omega}}
\sum_\mathbf{G}C_{m\mathbf{q}}(\mathbf{G})e^{i(\mathbf{q}+\mathbf{G})
\cdot \mathbf{r}}$

the HF exchange potential can be written as

$V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}}\left(\mu,\mathbf{r},\mathbf{r}'\right)=
\sum_{\mathbf{k}}\sum_{\mathbf{G}\mathbf{G}'}
e^{i(\mathbf{k}+\mathbf{G})\cdot\mathbf{r}} V_{\mathbf{k}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)
e^{-i(\mathbf{k}+\mathbf{G}')\cdot\mathbf{r}'}$

where

$V_{\mathbf{k}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)= \langle \mathbf{k}+\mathbf{G} |
V_{\mathrm{x,(SR/LR)}}^{\mathrm{HF}} | \mathbf{k}+\mathbf{G}'\rangle$

## Types of potentials
For most hybrid functionals proposed in the literature, the
interelectronic Coulomb potential $v(\mu,|\mathbf{r}-\mathbf{r}'|)$ is one of these types
($r=|\mathbf{r}-\mathbf{r}'|$):

- Full range (bare Coulomb potential):

$v^{\mathrm{bare}}(r)=\frac{1}{r}$

$V_{\mathbf{k}}^{\mathrm{bare}}\left(
\mathbf{G},\mathbf{G}'\right)= -\frac{4\pi}{\Omega}
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
\frac{C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')}
{|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2}$

- Short-range with error function:

$v_{\mathrm{SR}}^{\mathrm{erf}}(\mu,r)=\frac{\mathrm{erfc}(\mu r)}{r}$

$\begin{align}
V_{\mathbf{k},\mathrm{SR}}^{\mathrm{erf}}\left(\mu,
\mathbf{G},\mathbf{G}'\right)= -\frac{4\pi}{\Omega}
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
\frac{C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')}
{|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2} \left(
1-e^{-|\mathbf{k}-\mathbf{q}+\mathbf{G}''|^2 /(4\mu^2)} \right)
\end{align}$

[![](https://vasp.at/wiki/images/thumb/0/07/Screened_operator.png/340px-Screened_operator.png)](https://vasp.at/wiki/File:Screened_operator.png)

Short- and long-range potentials using the error or exponential
screening compared to the bare potential. $\mu=1$ is used.

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
formalism](Projector-augmented-wave_formalism.md).^([\[2\]](#cite_note-paier:jcp:05-2)[\[3\]](#cite_note-angyan:jpa:2006-3))

The families of hybrid functionals implemented in VASP are listed below
along with examples, whose corresponding [INCAR](../input-files/INCAR.md)
files can be found at the page [list of hybrid
functionals](List_of_hybrid_functionals.md).

|  |
|----|
| **Important:** The screening $\mu$ ([HFSCREEN](../incar-tags/HFSCREEN.md) tag) can be used only when the semilocal functional is PBE, PBEsol, or LDA ([GGA](../incar-tags/GGA.md)=PE, PS, or CA, respectively). The other [GGA](../incar-tags/GGA.md) and [METAGGA](../incar-tags/METAGGA.md) functionals have no screened version available in VASP. |

## Families of hybrid functionals
### HF exchange at full range
There is no range separation, i.e. the same fraction of HF exchange is
applied at full range, $a_{\mathrm{SR}}=a_{\mathrm{LR}}=a$
([AEXX](../incar-tags/AEXX.md) tag):

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a
E_{\mathrm{x}}^{\mathrm{HF}} + (1-a)E_{\mathrm{x}}^{\mathrm{SL}} +
E_{\mathrm{c}}^{\mathrm{SL}}$

[TABLE]

These are the original and most simple forms of hybrid functionals. Two
examples, PBE0 and B3LYP, are given below.

- [PBE0](List_of_hybrid_functionals.md):^([\[4\]](#cite_note-perdew:jcp:1996-4))

$E_{\mathrm{xc}}^{\mathrm{PBE0}}=\frac{1}{4}
E_{\mathrm{x}}^{\mathrm{HF}} + \frac{3}{4}
E_{\mathrm{x}}^{\mathrm{PBE}} + E_{\mathrm{c}}^{\mathrm{PBE}}$

It is based on the PBE GGA
functional^([\[5\]](#cite_note-perdew:prl:1996-5)) and
$a=1/4$.

- [B3LYP](List_of_hybrid_functionals.md)^([\[6\]](#cite_note-stephens:jpc:1994-6)),
  well known and popular amongst quantum chemists:

$\begin{align} E_{\mathrm{x}}^{\mathrm{B3LYP}}
&=0.8 E_{\mathrm{x}}^{\mathrm{LDA}}+ 0.2
E_{\mathrm{x}}^{\mathrm{HF}} + 0.72
(E_{\mathrm{x}}^{\mathrm{B88}}-E_{\mathrm{x}}^{\mathrm{LDA}}) + 0.19
E_{\mathrm{c}}^{\mathrm{VWN3}}+ 0.81 E_{\mathrm{c}}^{\mathrm{LYP}}
\end{align}$

The exchange part consists of 80% of LDA exchange plus 20% of HF
exchange, and 72% of the gradient corrections of the B88 GGA
functional.^([\[7\]](#cite_note-becke:pra:1988-7)) The correlation
consists of 81% of LYP^([\[8\]](#cite_note-lee:prb:1988-8)) correlation
energy, which contains a LDA and a GGA part, and 19% of the LDA
Vosko-Wilk-Nusair correlation functional
III,^([\[9\]](#cite_note-vosko1980-9)) which was fitted to the
correlation energy in the random phase approximation of the homogeneous
electron gas.

### HF exchange at short range (error-function screening)
The HF exchange is used only at short-range (the long-range part is
fully semilocal, $a_{\mathrm{LR}}=0$)
and the screening is done with the error function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) + E_{\mathrm{c}}^{\mathrm{SL}}$

The mixing $a_{\mathrm{SR}}$ and
screening $\mu$ are controlled by the
[AEXX](../incar-tags/AEXX.md) and [HFSCREEN](../incar-tags/HFSCREEN.md)
tags, respectively.

The most popular range-separated functional, HSE, is given below.

- [HSE03](List_of_hybrid_functionals.md)^([\[10\]](#cite_note-heyd:jcp:03-10)[\[11\]](#cite_note-heyd:jcp:04-11)[\[12\]](#cite_note-heyd:jcp:06-12))
  and
  [HSE06](List_of_hybrid_functionals.md)^([\[13\]](#cite_note-krukau:jcp:06-13)):

$E_{\mathrm{xc}}^{\mathrm{HSE}}=
\frac{1}{4}E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + \frac{3}{4}
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

They are based on the PBE GGA
functional^([\[5\]](#cite_note-perdew:prl:1996-5)) and
$a_{\mathrm{SR}}=1/4$. It has been
shown that the optimum $\mu$,
controlling the range separation is approximately 0.2-0.3
Å⁻¹.^([\[10\]](#cite_note-heyd:jcp:03-10)[\[11\]](#cite_note-heyd:jcp:04-11)[\[12\]](#cite_note-heyd:jcp:06-12)[\[13\]](#cite_note-krukau:jcp:06-13))
[HSE03](List_of_hybrid_functionals.md)
and
[HSE06](List_of_hybrid_functionals.md)
correspond to [HFSCREEN](../incar-tags/HFSCREEN.md)=0.3 and 0.2,
respectively. Note that the two limit cases of HSE are
[PBE0](List_of_hybrid_functionals.md)
at $\mu=0$ and PBE at
$\mu\rightarrow\infty$.

### HF exchange at short range and long range with different mixings (error-function screening)
The fractions of HF exchange at short and long range
($a_{\mathrm{SR}}$ and
$a_{\mathrm{LR}}$, respectively) can be
different:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

These functionals are selected with
[LMODELHF](../incar-tags/LMODELHF.md)=.TRUE. The mixings
$a_{\mathrm{LR}}$ and
$a_{\mathrm{SR}}$ are controlled by the
[AEXX](../incar-tags/AEXX.md) and [BEXX](../incar-tags/BEXX.md) tags,
respectively, and the screening $\mu$ by
the [HFSCREEN](../incar-tags/HFSCREEN.md) tag.

|  |
|----|
| **Important:** The possibility to set $a_{\mathrm{SR}}$ with [BEXX](../incar-tags/BEXX.md) within the [LMODELHF](../incar-tags/LMODELHF.md)=.TRUE. method was introduced in VASP.6.6.0. Until VASP.6.5.1 $a_{\mathrm{SR}}$ was fixed to 1 and could not be changed. |

This functional form has been used in the context of
dielectric-dependent hybrids. Examples are provided below.

- [RS-DDH](List_of_hybrid_functionals.md):^([\[14\]](#cite_note-skone:prb:2016-14))

$E_{\mathrm{xc}}^{\mathrm{RS-DDH}}=\frac{1}{4}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
\frac{3}{4}E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{c}}^{\mathrm{PBE}}$

where $a_{\mathrm{SR}}=1/4$ and
$a_{\mathrm{LR}}=\varepsilon^{-1}$ is
chosen as the inverse of the dielectric constant $\varepsilon^{-1}$.

- [DD-RSH-CAM](List_of_hybrid_functionals.md),^([\[15\]](#cite_note-chen2018nonempirical-15))
  [DSH](List_of_hybrid_functionals.md):^([\[16\]](#cite_note-cui2018doubly-16))

$E_{\mathrm{xc}}^{\mathrm{DD-RSH-CAM}}=E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
a_{\mathrm{LR}} E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{PBE}}(\mu) +
E_{\mathrm{c}}^{\mathrm{PBE}}$

where $a_{\mathrm{SR}}=1$ and
$a_{\mathrm{LR}}=\varepsilon^{-1}$ is
chosen as the inverse of the dielectric constant $\varepsilon^{-1}$.

### HF exchange at long range (error-function screening)
The HF exchange is used only at long-range (the short-range part is
fully semilocal, $a_{\mathrm{SR}}=0$)
and the screening is done with the error function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

These functionals are selected with
[LRHFCALC](../incar-tags/LRHFCALC.md)=.TRUE. The mixing
$a_{\mathrm{LR}}$ and screening
$\mu$ are controlled by the
[AEXX](../incar-tags/AEXX.md) and [HFSCREEN](../incar-tags/HFSCREEN.md)
tags, respectively.

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
  [RSHXPBE](List_of_hybrid_functionals.md):^([\[17\]](#cite_note-iikura:jcp:2001-17)[\[18\]](#cite_note-gerber:cpl:2005-18)[\[19\]](#cite_note-gerber:jcp:2007-19))

$E_{\mathrm{xc}}^{\mathrm{RSHXLDA}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{LDA}}(\mu) + E_{\mathrm{c}}^{\mathrm{LDA}}$

$E_{\mathrm{xc}}^{\mathrm{RSHXPBE}} =
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,SR}}^{\mathrm{PBE}}(\mu) + E_{\mathrm{c}}^{\mathrm{PBE}}$

When LDA is chosen, a value of $\mu=0.75$ Å⁻¹ is recommended for
solids.^([\[19\]](#cite_note-gerber:jcp:2007-19))

### HF exchange at short range (exponential screening)
The HF exchange is used only at short-range (the long-range part is
fully semilocal, $a_{\mathrm{LR}}=0$)
and the screening is done with the exponential function:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) + E_{\mathrm{c}}^{\mathrm{SL}}$

The exponential screening, also called Thomas-Fermi (TF)
screening,^([\[20\]](#cite_note-bylander:prb:90-20)[\[1\]](#cite_note-seidl:prb:96-1)[\[21\]](#cite_note-picozzi:prb:00-21))
is activated by setting [LTHOMAS](../incar-tags/LTHOMAS.md)=.TRUE.. The
mixing $a_{\mathrm{SR}}$ and screening
$\mu=k_{\rm TF}$ are controlled by the
[AEXX](../incar-tags/AEXX.md) and [HFSCREEN](../incar-tags/HFSCREEN.md)
tags, respectively.

|  |
|----|
| **Mind:** [LTHOMAS](../incar-tags/LTHOMAS.md)=.TRUE. automatically sets [AEXX](../incar-tags/AEXX.md)=1. However, [AEXX](../incar-tags/AEXX.md) can be set to another value. |

[TABLE]

The sX-LDA functional, which uses $a_{\mathrm{SR}}=1$, is probably the first hybrid using an
exponential screening:

- [sX-LDA](List_of_hybrid_functionals.md):^([\[20\]](#cite_note-bylander:prb:90-20))

$E_{\mathrm{xc}}^{\mathrm{sX-LDA}} =
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{LDA}}(\mu) + E_{\mathrm{c}}^{\mathrm{LDA}}$

For typical semiconductors, a Thomas-Fermi screening length
$\mu=k_{\rm TF}$ of about 1.8 Å⁻¹
yields reasonable band gaps. In principle, however, the Thomas-Fermi
screening length depends on the valence-electron density. VASP
determines $k_{\rm TF}$ from the number
of valence electrons (read from the [POTCAR](../input-files/POTCAR.md)
file) and the volume (leading to an average density
$\bar{n}$) and writes the corresponding
value of $k_{\rm TF}=\sqrt{4\bar{k}_{\rm F}/\pi}$, where $\bar{k}_{\rm
F}=(3\pi^2\bar{n})^{1/3}$ to the
[OUTCAR](../output-files/OUTCAR.md) file (**note that this value is only
printed for information and is not used during the calculation**):

     Thomas-Fermi vector in A             =   2.00000

Since VASP counts the semi-core states and *d*-states as valence
electrons, although these states do not contribute to the screening, the
values reported by VASP are often not recommended.

Another important detail concerns the implementation of the local LDA
part in VASP. Literature \[see Eqs. (3.10), (3.14), and (3.15) in Ref.
^([\[1\]](#cite_note-seidl:prb:96-1))\] suggests to use in the
enhancement factor $F(z)$ a
position-independent variable $z=k_{\rm
TF}/\bar{k}_{\rm F}$ where $\bar{k}_{\rm F}$ is as defined above but using the average
density $\bar{n}$ in the unit cell.
However, implemented in VASP is a position-dependent variable
$z({\bf r})=k_{\rm TF}/k_{\rm F}({\bf r})$, where $k_{\rm F}({\bf r})=(3\pi^2
n({\bf r}))^{1/3}$ is the Fermi wave vector calculated with
the local density $n({\bf r})$, while
the constant $k_{\rm TF}$ is set by
[HFSCREEN](../incar-tags/HFSCREEN.md).

## Related tags and articles
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

## References
1.  ↑ ^([a](#cite_ref-seidl:prb:96_1-0))
    ^([b](#cite_ref-seidl:prb:96_1-1))
    ^([c](#cite_ref-seidl:prb:96_1-2)) [A. Seidl, A. Görling, P. Vogl,
    J.A. Majewski, and M. Levy, Phys. Rev. B **53**, 3764
    (1996).](https://doi.org/10.1103/PhysRevB.53.3764)
2.  [↑](#cite_ref-paier:jcp:05_2-0) [J. Paier, R. Hirschl, M. Marsman,
    and G. Kresse, J. Chem. Phys. **122**, 234102
    (2005).](https://doi.org/10.1063/1.1926272)
3.  [↑](#cite_ref-angyan:jpa:2006_3-0) [J. G. Ángyán, I. Gerber, and M.
    Marsman, *Spherical harmonic expansion of short-range screened
    Coulomb interactions*, J. Phys. A: Math. Gen. **39**, 8613
    (2006).](http://dx.doi.org/10.1088/0305-4470/39/27/005)
4.  [↑](#cite_ref-perdew:jcp:1996_4-0) [J. P. Perdew, M. Ernzerhof,
    and K. Burke, J. Chem. Phys. **105**, 9982
    (1996).](https://doi.org/10.1063/1.472933)
5.  ↑ ^([a](#cite_ref-perdew:prl:1996_5-0))
    ^([b](#cite_ref-perdew:prl:1996_5-1)) [J. P. Perdew, K. Burke,
    and M. Ernzerhof, Phys. Rev. Lett., **77**, 3865
    (1996).](https://doi.org/10.1103/PhysRevLett.77.3865)
6.  [↑](#cite_ref-stephens:jpc:1994_6-0) [P. J. Stephens, F. J.
    Devlin, C. F. Chabalowski, and M. J. Frisch, J. Phys. Chem. **98**,
    11623 (1994).](https://doi.org/10.1021/j100096a001)
7.  [↑](#cite_ref-becke:pra:1988_7-0) [A. D. Becke, *Density-functional
    exchange-energy approximation with correct asymptotic behavior*,
    Phys. Rev. A **38**, 3098
    (1988).](https://doi.org/10.1103/PhysRevA.38.3098)
8.  [↑](#cite_ref-lee:prb:1988_8-0) [C. Lee, W. Yang, and R. G. Parr,
    *Development of the Colle-Salvetti correlation-energy formula into a
    functional of the electron density*, Phys. Rev. B **37**, 785
    (1988).](https://doi.org/10.1103/PhysRevB.37.785)
9.  [↑](#cite_ref-vosko1980_9-0) [S. H. Vosko, L. Wilk, and M. Nusair,
    Can. J. Phys. **58**, 1200 (1980).](https://doi.org/10.1139/p80-159)
10. ↑ ^([a](#cite_ref-heyd:jcp:03_10-0))
    ^([b](#cite_ref-heyd:jcp:03_10-1)) [J. Heyd, G. E. Scuseria, and M.
    Ernzerhof, J. Chem. Phys. **118**, 8207
    (2003).](https://doi.org/10.1063/1.1564060)
11. ↑ ^([a](#cite_ref-heyd:jcp:04_11-0))
    ^([b](#cite_ref-heyd:jcp:04_11-1)) [J. Heyd and G. E. Scuseria, J.
    Chem. Phys. **121**, 1187
    (2004).](https://doi.org/10.1063/1.1760074)
12. ↑ ^([a](#cite_ref-heyd:jcp:06_12-0))
    ^([b](#cite_ref-heyd:jcp:06_12-1)) [J. Heyd, G. E. Scuseria, and M.
    Ernzerhof, J. Chem. Phys. **124**, 219906
    (2006).](https://doi.org/10.1063/1.2204597)
13. ↑ ^([a](#cite_ref-krukau:jcp:06_13-0))
    ^([b](#cite_ref-krukau:jcp:06_13-1)) [A. V. Krukau , O. A.
    Vydrov, A. F. Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**,
    224106 (2006).](https://doi.org/10.1063/1.2404663)
14. [↑](#cite_ref-skone:prb:2016_14-0) [J. H. Skone, M. Govoni, and G.
    Galli, *Nonempirical range-separated hybrid functionals for solids
    and molecules*, Phys. Rev. B **93**, 235106
    (2016).](http://doi.org/10.1103/PhysRevB.93.235106)
15. [↑](#cite_ref-chen2018nonempirical_15-0) [W. Chen, G. Miceli, G.M.
    Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent
    hybrid functional with range separation for semiconductors and
    insulators*, Phys. Rev. Mater. **2**, 073803
    (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
16. [↑](#cite_ref-cui2018doubly_16-0) [Z.H. Cui, Y.C. Wang, M.Y.
    Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An
    Accurate First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345
    (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
17. [↑](#cite_ref-iikura:jcp:2001_17-0) [H. Iikura, T. Tsuneda, T.
    Yanai, and K. Hirao, *A long-range correction scheme for
    generalized-gradient-approximation exchange functionals*, J. Chem.
    Phys. **115**, 3540 (2001).](http://doi.org/10.1063/1.1383587)
18. [↑](#cite_ref-gerber:cpl:2005_18-0) [I. C. Gerber and J. G. Ángyán,
    *Hybrid functional with separated range*, Chem. Phys. Lett. **415**,
    100 (2005).](http://doi.org/10.1016/j.cplett.2005.08.060)
19. ↑ ^([a](#cite_ref-gerber:jcp:2007_19-0))
    ^([b](#cite_ref-gerber:jcp:2007_19-1)) [I. C. Gerber, J. G.
    Ángyán, M. Marsman, and G. Kresse, *Range separated hybrid density
    functional with long-range Hartree-Fock exchange applied to
    solids*, J. Chem. Phys. **127**, 054101
    (2007).](http://doi.org/10.1063/1.2759209)
20. ↑ ^([a](#cite_ref-bylander:prb:90_20-0))
    ^([b](#cite_ref-bylander:prb:90_20-1)) [D. M. Bylander and L.
    Kleinman, Phys. Rev. B **41**, 7868
    (1990).](https://doi.org/10.1103/PhysRevB.41.7868)
21. [↑](#cite_ref-picozzi:prb:00_21-0) [S. Picozzi, A. Continenza, R.
    Asahi, W. Mannstadt, A.J. Freeman, W. Wolf, E. Wimmer, and C.B.
    Geller, Phys. Rev. B **61**, 4677
    (2000).](https://doi.org/10.1103/PhysRevB.61.4677)
