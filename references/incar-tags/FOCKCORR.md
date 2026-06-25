<!-- Source: https://vasp.at/wiki/index.php/FOCKCORR | revid: 22327 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# FOCKCORR


FOCKCORR = 1 \| 2 

|  |  |  |
|----|----|----|
| Default: **FOCKCORR** | = 2 | if <a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>\>0 |
|  | = 1 | else |

Description: The tag FOCKCORR
determines how the Coulomb convergence corrections are applied.

------------------------------------------------------------------------

The Coulomb potential in reciprocal space

$V(G)=\frac{4\pi e^2}{G^2}$

diverges for small G vectors. To alleviate this issue and improve the
convergence of the exact exchange integral with respect to supercell
size (or k-point mesh density) different methods have been proposed: the
auxiliary function
methods<sup>[\[1\]](#cite_note-gygi:prb:86-1)</sup>,
probe-charge Ewald
<sup>[\[2\]](#cite_note-massidda:prb:93-2)</sup>
([HFALPHA](HFALPHA.md)), and Coulomb truncation
methods<sup>[\[3\]](#cite_note-spenceralavi:prb:08-3)</sup>
([HFRCUT](HFRCUT.md)). These mostly involve modifying the
Coulomb Kernel in a way that yields the same result as the unmodified
kernel within the limit of large supercell sizes.

These corrections are implemented in VASP either by changing the
$\mathbf{G}=0$ component of the Coulomb kernel when
FOCKCORR=1

$\Phi(\mathbf{G}) = \left\\ \begin{array}{lr} \frac{4\pi e^2}{\Omega}
\frac{1}{G^2} & \mathbf{G} \neq 0\\ \chi & \mathbf{G} = 0 \end{array}
\right.$

with $\chi$ being
the value of the correction and depends on whether
[HFALPHA](HFALPHA.md) or [HFRCUT](HFRCUT.md)
are set, or by including the original orbital scaled by the convergence
correction when FOCKCORR=2

$\langle \mathbf{k}+\mathbf{G}' | V^\text{HF}_\text{x} |
\mathbf{k}+\mathbf{G} \rangle = -
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
\Phi(\mathbf{k}-\mathbf{q}+\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'')$

$\begin{aligned} \langle \mathbf{k}+\mathbf{G}'
|\hat{V}^\text{HF}_{\text{x}} | \psi_{\mathbf{k}n} \rangle &= -
\sum_{m\mathbf{q}}f_{m\mathbf{q}}\sum_{\mathbf{G}''}
C^\*_{m\mathbf{q}}(\mathbf{G}'-\mathbf{G}'')
\Phi(\mathbf{k}-\mathbf{q}+\mathbf{G}'')
C_{m\mathbf{q}}(\mathbf{G}-\mathbf{G}'') C_{n\mathbf{k}}(\mathbf{G})\\
&= - \chi\sum_{m\mathbf{q}}f_{m\mathbf{q}}
C_{m\mathbf{q}}(\mathbf{G}) \end{aligned}$

For Hartree-Fock or hybrid functional calculations, either
FOCKCORR=1 or
FOCKCORR=2 can be used and
should yield the same results when
<a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a>=-1 and there are no aliasing errors in
the exact exchange (see [PRECFOCK](PRECFOCK.md) for more
details). For post-DFT methods such as ACDFT, GW, and BSE the
FOCKCORR=2 should be used
because the overlap densities are reconstructed in the plane-wave grid
(see <a href="/wiki/LMAXFOCKAE" class="mw-redirect"
title="LMAXFOCKAE">LMAXFOCKAE</a> tag).

Note that in the case
FOCKCORR=2 the corrections are
only applied to orbitals in the $\mathbf{q}$
regular grid used to describe the exact exchange potential so this
method cannot be used to compute band structures where this potential is
applied to orbitals $n\mathbf{k}$
not in the $m\mathbf{q}$
set.

|  |
|----|
| **Warning:** FOCKCORR=2 should **not** be used when computing the band structure along a path with the [0-weight scheme](../misc/Si_HSE_bandstructure.md) or [KPOINTS_OPT](../input-files/KPOINTS_OPT.md) |

In previous versions of VASP,
FOCKCORR=1 was used when
[ALGO](ALGO.md)=Normal;
[LFOCKACE](LFOCKACE.md)=.FALSE. and
FOCKCORR=2 when
[ALGO](ALGO.md)=All or [ALGO](ALGO.md)=Normal;
[LFOCKACE](LFOCKACE.md)=.TRUE. .

|  |
|----|
| **Mind:** Only available as of VASP 6.3.1. |

## Related tags and articles\[<a href="/wiki/index.php?title=FOCKCORR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[HFRCUT](HFRCUT.md), [HFALPHA](HFALPHA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HFRCUT-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-gygi:prb:86_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.34.4405" class="external text"
    rel="nofollow">F. Gygi and A. Baldereschi, Phys. Rev. B
    <strong>34</strong>, 4405(R) (1986).</a>
2.  [↑](#cite_ref-massidda:prb:93_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.48.5058" class="external text"
    rel="nofollow">S. Massidda, M. Posternak, and A. Baldereschi, Phys. Rev.
    B <strong>48</strong>, 5058 (1993).</a>
3.  [↑](#cite_ref-spenceralavi:prb:08_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.77.193110"
    class="external text" rel="nofollow">J. Spencer and A. Alavi, Phys.
    Phys. Rev. B <strong>77</strong>, 193110 (2008).</a>


