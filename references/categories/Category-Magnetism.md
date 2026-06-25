<!-- Source: https://vasp.at/wiki/index.php/Category:Magnetism | revid: 33271 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Magnetism


There are three ingredients to obtain **magnetism**:

- The first is the *electronic spin*. The origin of spin is explained by
  Dirac theory, that is the relativistic quantum theory of an electron.
- The second ingredient is *quantum mechanical statistics*. The Bohr–Van
  Leeuwen theorem states that a classical particle that follows
  Boltzmann statistics can never give rise to magnetism, even if the
  particle carries charge and spin. Therefore, in addition to spin,
  proper quantum mechanical statistics are necessary to explain
  magnetism.
- And finally, there is one more necessary ingredient:
  *electron–electron interaction*. Only the specific details of the
  interaction between electrons leads to a finite magnetization,
  otherwise any material would be magnetic.

In summary, magnetism is a *collective, quantum electrodynamic
phenomenon*. The challenge is now to describe magnetism from first
principles using ab-initio simulations.

In VASP, the electronic spin can be treated either within a so-called
*spin-polarized calculation* ([ISPIN](../incar-tags/ISPIN.md)=2) or a
*noncollinear calculation*
([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=T)[^hobbs:prb:00-1].
The aim is to solve the Kohn-Sham (KS) equations including the spin
degree of freedom to yield spin-dependent KS orbitals, thus fulfilling
quantum mechanical statistics. In this context it is important to choose
the <a href="/wiki/Pseudopotential" class="mw-redirect"
title="Pseudopotential">pseudopotential</a> such that the electrons that
give rise to magnetism are treated as valence electrons. The
electron–electron interaction is included based on the selected
<a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
title="Exchange-correlation functional">exchange-correlation
functional</a>. For a general introduction to magnetism in the context
of density-functional theory (DFT), we recommend the book *Theory of
itinerant electron magnetism* by Jürgen Kübler
[^kuebler2000:book-2].

|  |
|----|
| **Tip:** In magnetic systems the <a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> is often hard to converge, see [troubleshooting electronic convergence](../tutorials/Troubleshooting_electronic_convergence.md) for help. |


## Contents


- [1 Spin-polarized
  calculation](#spin-polarized-calculation)
- [2 Noncollinear
  calculation](#noncollinear-calculation)
- [3 Advanced
  methods](#advanced-methods)
  - [3.1
    Constrained magnetic
    moments](#constrained-magnetic-moments)
  - [3.2 Spin
    spirals](#spin-spirals)
  - [3.3 Spin-orbit
    coupling](#spin-orbit-coupling)
  - [3.4 Nuclear
    magnetic resonance](#nuclear-magnetic-resonance)
  - [3.5 External
    magnetic field](#external-magnetic-field)
- [4 Additional
  resources](#additional-resources)
  - [4.1
    Tutorials](#tutorials)
- [5
  References](#references)


## Spin-polarized calculation\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Spin-polarized calculation">edit</a> \| (./index.php.md)\]

In spin-polarized calculations, there is a distinct spin-up and
spin-down charge density

$n_\sigma(\mathbf{r}) = \sum_{n=1}^N |\psi_{\sigma
n}(\mathbf{r})|^2,$

similar to the well-known Stoner model. As in standard DFT, one electron
moves in an effective potential, but the effective potential
$v_\sigma^{eff}({\bf r})$ of a spin-polarized
calculation ([ISPIN](../incar-tags/ISPIN.md)=2) has an additional spin
index

$v_\sigma^{eff}({\bf r})=v^{ext}({\bf r}) + v^{H}({\bf r}) +
v_\sigma^{xc}({\bf r}).$

The <a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">exchange-correlation potential</a> is

$v_\sigma^{xc}=\frac{\delta E_{xc}\[n_\uparrow,n_\downarrow\]}{\delta
n_{\sigma}}.$

The spin-dependent effective potential enters the KS equations

$\left\[-{\mathbf \nabla}^2_n + v^{eff}_\uparrow({\mathbf
r}_n)\right\]\psi_{\uparrow n}= \varepsilon_{n} \psi_{\uparrow n}$

$\left\[-{\mathbf \nabla}^2_n + v^{eff}_\downarrow({\mathbf
r}_n)\right\]\psi_{\downarrow n}= \varepsilon_{n} \psi_{\downarrow
n}$

and leads to spin-dependent solutions for the KS orbitals
$\psi_{\uparrow n}$. Finally, the spin-up and spin-down
KS orbitals are used to update the spin-up and spin-down charge
densities until self-consistency is reached. Note that, the spin species
only couple to one another through the
<a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">exchange-correlation potential</a> where both, the
spin-up and spin-down charge densities enter as an argument.

Spin-polarized calculations are enabled by setting
[ISPIN](../incar-tags/ISPIN.md)=2 in the [INCAR](../input-files/INCAR.md) file
and executing **vasp_std**. It is useful in order to describe collinear
magnetic systems without spin-orbit coupling. Also see
[MAGMOM](../incar-tags/MAGMOM.md), [LORBIT](../incar-tags/LORBIT.md).

## Noncollinear calculation\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Noncollinear calculation">edit</a> \| (./index.php.md)\]

For noncollinear magnetism
([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)) and spin-orbit
coupling ([LSORBIT](../incar-tags/LSORBIT.md)), the Hohenberg-Kohn-Sham
DFT is extended, once again, by introducing an additional spin index. We
introduce the spin-density matrix

$n_{\sigma'\sigma}(\mathbf{r}) = \sum_{n=1}^N \psi_{\sigma'
n}(\mathbf{r})\psi^\*_{\sigma n}(\mathbf{r}).$

Accordingly, also the potential becomes a 2x2 matrix

$v_{\sigma'\sigma}^{eff}({\bf r})=v^{ext}_{\sigma'\sigma}({\bf r}) +
\delta_{\sigma'\sigma} v^{H}({\bf r}) + v_{\sigma'\sigma}^{xc}({\bf
r})$

and the KS orbitals in the KS equations are two-component spinors

$\sum_{\sigma} \left\[-{\mathbf \delta_{\sigma'\sigma} \nabla}^2_n +
v^{eff}_{\sigma'\sigma}({\mathbf r}_n)\right\]\psi_{\sigma n}=
\varepsilon_{\sigma' n} \psi_{\sigma' n}.$

Note that in the noncollinear case, the KS equations do not decouple for
spin-up and spin-down because the potential has off-diagonal elements
that couple the two spin species. This is the SCF loop of noncollinear
spin-density functional theory (SDFT).

As VASP needs to treat many quantities as matrices instead of arrays,
you need to use the **vasp_ncl** executable for these calculations in
addition to setting
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=T and/or
[LSORBIT](../incar-tags/LSORBIT.md)=T for spin-orbit coupling. The
magnetization ([CHGCAR](../input-files/CHGCAR.md),
[PROCAR](../output-files/PROCAR.md)) and on-site magnetic moments (see
[MAGMOM](../incar-tags/MAGMOM.md), [LORBIT](../incar-tags/LORBIT.md)) live
in spinor space as defined by [SAXIS](../incar-tags/SAXIS.md).

## Advanced methods\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Advanced methods">edit</a> \| (./index.php.md)\]

Some methods below can be applied in the context of both spin-polarized
and noncollinear calculations.

### Constrained magnetic moments\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Constrained magnetic moments">edit</a> \| (./index.php.md)\]

See [I_CONSTRAINED_M](../incar-tags/I_CONSTRAINED_M.md).

### Spin spirals\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Spin spirals">edit</a> \| (./index.php.md)\]

[Spin spirals](../theory/Spin_spirals.md), or spin waves, are a
magnetic order that can be described in terms of the generalized Bloch
theorem. It states that the spin-up and spin-down components, and thus
the magnetization, are rotated based on a certain spin-spiral
propagation vector $\mathbf{q}$.
If the corresponding wavelength is a multiple of the lattice vector of
the crystal unit cell, the spin wave is commensurate. While the method
can be used for both commensurate and incommensurable spin spirals, in
practice it is more useful in case of incommensurable spin spirals. This
is because spin spirals cannot be combined with spin orbit coupling and
often systems with commensurate spin waves exhibit strong SOC, while in
many compounds with incommensurable spin spirals SOC can be neglected.
The main tag is [LSPIRAL](../incar-tags/LSPIRAL.md).

To learn how to apply the method read more on [spin
spirals](../theory/Spin_spirals.md).

### Spin-orbit coupling\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Spin-orbit coupling">edit</a> \| (./index.php.md)\]

Spin-orbit coupling (SOC) is supported as of VASP.4.5 and later
described in Ref.
[^Steiner:2016-3].
The main tag is [LSORBIT](../incar-tags/LSORBIT.md), which automatically
sets [LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md) and requires
using `vasp_ncl`. SOC couples the spin degrees of freedom with the
lattice degrees of freedom, see [SAXIS](../incar-tags/SAXIS.md).

### Nuclear magnetic resonance\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Nuclear magnetic resonance">edit</a> \| (./index.php.md)\]

The chemical shielding can be calculated using
[LCHIMAG](../incar-tags/LCHIMAG.md). The hyperfine coupling constant can
also be calculated using [LHYPERFINE](../incar-tags/LHYPERFINE.md).
Further options are listed in the [NMR category
page](Category-NMR.md).

### External magnetic field\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: External magnetic field">edit</a> \| (./index.php.md)\]

Apply a constant external magnetic field (Zeeman-like term):
[BEXT](../incar-tags/BEXT.md)

## Additional resources\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Tutorials\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part1/"
  class="external text" rel="nofollow">spin-polarized calculations</a>.
- Tutorial for
  <a href="https://www.vasp.at/tutorials/latest/magnetism/part2/"
  class="external text" rel="nofollow">noncollinear calculations</a>.

## References\[<a
href="/wiki/index.php?title=Category:Magnetism&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^hobbs:prb:00-1]: [Hobbs, D., G. Kresse, and J. Hafner, *Fully unconstrained noncollinear magnetism within the projector augmented-wave method.*, Phys. Rev. B **62**, 11556 (2000).](http://doi.org/10.1103/PhysRevB.62.11556)
[^kuebler2000:book-2]: [J. Kübler, *Theory of itinerant electron magnetism*, Vol. 106. Oxford University Press (2000).](https://books.google.at/books?id=voGKDgAAQBAJ&lpg=PP1&ots=4gJEMsQUYo&dq=itinerant%20electrons%20magnetism&lr&pg=PP1#v=onepage&q=itinerant%20electrons%20magnetism&f=false)
[^Steiner:2016-3]: [S. Steiner, S. Khmelevskyi, M. Marsman, and G. Kresse, Phys. Rev. B **93**, 224425 (2016).](https://doi.org/10.1103/PhysRevB.93.224425)
