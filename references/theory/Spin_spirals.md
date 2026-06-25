<!-- Source: https://vasp.at/wiki/index.php/Spin_spirals | revid: 37306 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Spin spirals


Spin spirals are magnetic structures in which the direction of the
magnetization rotates continuously from one unit cell to the next. In
VASP they are modeled with a generalization of the Bloch condition,
which captures incommensurate magnetic order in the primitive cell and
avoids the need for large
supercells.<sup>[\[1\]](#cite_note-marsman:prb:02-1)</sup>

This page describes the underlying formalism. For step-by-step
instructions on setting up, running, and analyzing a spin-spiral
calculation, see [Spin-spiral
calculations](../tutorials/Spin-spiral_calculations.md).


## Contents


- [1 Generalized
  Bloch condition](#Generalized_Bloch_condition)
  - [1.1
    Magnetization
    density](#Magnetization_density)
- [2 Modified
  Hamiltonian](#Modified_Hamiltonian)
- [3 Basis-set
  considerations](#Basis-set_considerations)
- [4
  Symmetry](#Symmetry)
- [5 Related tags
  and articles](#Related_tags_and_articles)
- [6
  References](#References)


## Generalized Bloch condition\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Generalized Bloch condition">edit</a> \| (./index.php.md)\]

Spin spirals may be conveniently modeled using a generalization of the
Bloch
condition<sup>[\[2\]](#cite_note-sandratskii:pssb:86-2)[\[1\]](#cite_note-marsman:prb:02-1)</sup>
(set [`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = .TRUE.`
and [`LSPIRAL`](../incar-tags/LSPIRAL.md)` = .TRUE.`):

 

$\left\[ \begin{array}{c} \Psi^{\uparrow}_{\bf k}(\bf r) \\
\Psi^{\downarrow}_{\bf k}(\bf r) \end{array} \right\] = \left(
\begin{array}{cc} e^{-i\bf q \cdot \bf R / 2} & 0\\ 0 & e^{+i\bf q \cdot
\bf R / 2} \end{array}\right) \left\[ \begin{array}{c}
\Psi^{\uparrow}_{\bf k}(\bf r-R) \\ \Psi^{\downarrow}_{\bf k}(\bf r-R)
\end{array} \right\],$

*i.e.*, from one unit cell to the next the up- and down-spinors pick up
an additional phase factor of $\exp(-i{\bf q}\cdot {\bf R}/2)$ and $\exp(+i{\bf q}\cdot {\bf R}/2)$, respectively, where **R** is a lattice vector of the
crystalline lattice, and **q** is the so-called spin-spiral propagation
vector.

The spin-spiral propagation vector is commonly chosen to lie within the
first Brillouin zone of the reciprocal lattice, and is specified by
means of the [QSPIRAL](../incar-tags/QSPIRAL.md) tag.

### Magnetization density\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Magnetization density">edit</a> \| (./index.php.md)\]

The generalized Bloch condition above gives rise to the following
behavior of the magnetization density:

${\bf m} ({\bf r} + {\bf R})= \left( \begin{array}{c} m_x({\bf r})
\cos({\bf q} \cdot {\bf R}) - m_y({\bf r}) \sin({\bf q} \cdot {\bf R})
\\ m_x({\bf r}) \sin({\bf q} \cdot {\bf R}) + m_y({\bf r}) \cos({\bf q}
\cdot {\bf R}) \\ m_z({\bf r}) \end{array} \right)$

The components of the magnetization in the *xy*-plane rotate about the
spin-spiral propagation vector **q**, while the out-of-plane component
$m_z$ retains the usual cell periodicity. This is
depicted schematically below:

<figure class="mw-halign-center" typeof="mw:File">
<a href="/wiki/File:Spinspiral.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/1/1f/Spinspiral.png/400px-Spinspiral.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/1/1f/Spinspiral.png/600px-Spinspiral.png 1.5x, /wiki/images/1/1f/Spinspiral.png 2x"
width="400" height="169" /></a>
</figure>

  

|  |
|----|
| **Mind:** The generalized Bloch condition does not mean that the magnetization density may not have contributions along the *z*-direction; these are simply unaffected by it. To keep the magnetization density from developing a component along *z*, set [`LZEROZ`](../incar-tags/LZEROZ.md)` = .TRUE.`, which sets $m_z({\bf r}) = 0$ at each step of the electronic minimization. |

## Modified Hamiltonian\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Modified Hamiltonian">edit</a> \| (./index.php.md)\]

The generalized Bloch condition redefines the Bloch functions as
follows:

$\Psi^{\uparrow}_{\bf k}(\bf r) = \sum _{\bf G} \rm C^{\uparrow}_{\bf
k \bf G} e^{i(\bf k + \bf G -\frac{\bf q}{2})\cdot \bf r}$

$\Psi^{\downarrow}_{\bf k}(\bf r) = \sum _{\bf G} \rm
C^{\downarrow}_{\bf k \bf G} e^{i(\bf k + \bf G +\frac{\bf q}{2})\cdot
\bf r}$

This changes the Hamiltonian only minimally:

$\left( \begin{array}{cc} H^{\uparrow\uparrow} &
V^{\uparrow\downarrow}_{\rm xc} \\ V^{\downarrow\uparrow}_{\rm xc} &
H^{\downarrow\downarrow} \end{array}\right) \rightarrow \left(
\begin{array}{cc} H^{\uparrow\uparrow} & V^{\uparrow\downarrow}_{\rm
xc} e^{-i\bf q \cdot \bf r} \\ V^{\downarrow\uparrow}_{\rm xc}e^{+i\bf
q \cdot \bf r} & H^{\downarrow\downarrow} \end{array}\right),$

where in $H^{\uparrow\uparrow}$ and $H^{\downarrow\downarrow}$ the kinetic energy of a plane-wave component changes
to:

$H^{\uparrow\uparrow}:\qquad |{\bf k} + {\bf G}|^2 \rightarrow |{\bf
k} + {\bf G} - {\bf q} /2|^2$

$H^{\downarrow\downarrow}:\qquad |{\bf k} + {\bf G}|^2 \rightarrow
|{\bf k} + {\bf G} + {\bf q} /2|^2$

Because the only change to the off-diagonal exchange-correlation
potential is a phase modulation, a spin-spiral calculation has
approximately the same computational cost as a standard noncollinear
calculation<sup>[\[3\]](#cite_note-hobbs:prb:00-3)</sup>
of the primitive cell.

## Basis-set considerations\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Basis-set considerations">edit</a> \| (./index.php.md)\]

Because the two spinor components are shifted in reciprocal space by
$\pm{\bf q}/2$, the plane-wave cutoff must be chosen
carefully. The cutoff of the basis set of the individual spinor
components is specified by means of the [ENINI](../incar-tags/ENINI.md)
tag, while
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> must
be chosen large enough that the plane-wave components of both spinors
have a kinetic energy below
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>. This
is the case when

$\mathtt{ENMAX} \geq \frac{\hbar^2}{2m}\left( G_{\rm ini} + |q|
\right)^2, \qquad G_{\rm ini}=\sqrt{\frac{2m}{\hbar^2}\mathtt{ENINI}}.$

In practice it is more than sufficient to set
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> to
[ENINI](../incar-tags/ENINI.md) + 100 eV. The practical settings, and the
runtime warning VASP prints when
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> is too
small, are described in [Spin-spiral
calculations](../tutorials/Spin-spiral_calculations.md).

## Symmetry\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Symmetry">edit</a> \| (./index.php.md)\]

The introduction of a spin spiral generally lowers the symmetry of the
system, and VASP cannot currently account for the presence of a spin
spiral in its symmetry analysis. For this reason the use of symmetry has
to be switched off completely ([`ISYM`](../incar-tags/ISYM.md)` = -1`) in
spin-spiral calculations.

## Related tags and articles\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Spin-spiral
calculations](../tutorials/Spin-spiral_calculations.md)

[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md),
[LSPIRAL](../incar-tags/LSPIRAL.md), [QSPIRAL](../incar-tags/QSPIRAL.md),
[LZEROZ](../incar-tags/LZEROZ.md), [ENINI](../incar-tags/ENINI.md),
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>,
[ISYM](../incar-tags/ISYM.md), [MAGMOM](../incar-tags/MAGMOM.md)

## References\[<a
href="/wiki/index.php?title=Spin_spirals&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-marsman:prb:02_1-0)</sup>
    <sup>[b](#cite_ref-marsman:prb:02_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.66.224409"
    class="external text" rel="nofollow">M. Marsman and J. Hafner,
    <em>Broken symmetries in the crystalline and magnetic structures of
    γ-iron</em>, Phys. Rev. B <strong>66</strong>, 224409 (2002).</a>
2.  [↑](#cite_ref-sandratskii:pssb:86_2-0)
    <a href="https://doi.org/10.1002/pssb.2221360119" class="external text"
    rel="nofollow">L. M. Sandratskii, <em>Energy band structure calculations
    for crystals with spiral magnetic structure</em>, Phys. Status Solidi B
    <strong>136</strong>, 167 (1986).</a>
3.  [↑](#cite_ref-hobbs:prb:00_3-0)
    <a href="http://doi.org/10.1103/PhysRevB.62.11556" class="external text"
    rel="nofollow">Hobbs, D., G. Kresse, and J. Hafner, <em>Fully
    unconstrained noncollinear magnetism within the projector augmented-wave
    method.</em>, Phys. Rev. B <strong>62</strong>, 11556 (2000).</a>


