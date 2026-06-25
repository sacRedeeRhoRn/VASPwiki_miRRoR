<!-- Source: https://vasp.at/wiki/index.php/LREAL | revid: 27291 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LREAL


LREAL = .FALSE. \| Auto (or A)
\| On (or O) \| .TRUE.  
Default: **LREAL** = .FALSE. 

Description: LREAL determines
whether the projection operators are evaluated in real-space or in
reciprocal space.

------------------------------------------------------------------------

|  |  |
|----|----|
| LREAL=.FALSE. | projection done in reciprocal space |
| LREAL=Auto or A | projection done in real space, fully automatic optimization of projection operators (little to no user interference required) |
| LREAL=On or O | projection done in real space, projection operators are re-optimized (not recommended) |
| LREAL=.TRUE. | projection done in real space, use projectors on file (not recommended) |

  
The nonlocal part of the
[pseudopotential](../categories/Category-Pseudopotentials.md)
requires the evaluation of an expression:

  

$\sum_{ij}D_{ij}|\beta_j\rangle\langle\beta_i|\tilde{\psi}_{n\mathbf{k}}\rangle$.

where the "projected wavefunction character" is defined as:

 

$\begin{align}C_{in\mathbf{k}}=\langle\beta_i|\tilde{\psi}_{n\mathbf{k}}\rangle
&=\frac{\Omega}{N_{\rm
FFT}}\sum_{\mathbf{r}}\langle\beta_i|\mathbf{r}\rangle\langle\mathbf{r}|\tilde{\psi}_{n\mathbf{k}}\rangle=\frac{\Omega}{N_{\rm
FFT}}\sum_{\mathbf{r}}\beta(\mathbf{r})\tilde{\psi}_{n\mathbf{k}}(\mathbf{r})
\\
&=\sum_{\mathbf{G}}\langle\beta_i|\mathbf{k}+\mathbf{G}\rangle\langle\mathbf{k}+\mathbf{G}|\tilde{\psi}_{n\mathbf{k}}\rangle=\sum_\mathbf{G}\bar\beta(\mathbf{k}+\mathbf{G})
C_{\mathbf{G}n\mathbf{k}}\end{align}$

This expression can be evaluated in reciprocal or real space: In
reciprocal space (second line), the number of operations scales with the
size of the basis set, i.e., number of plane waves. In real space (first
line), the projection operators are confined to spheres around each
atom. Therefore, the number of operations necessary to evaluate one
C<sub>in**k**</sub> does not increase with the system size (usually, the
number of grid points within the cutoff sphere is between 500 and 2000).
One of the major obstacles to the method working in real space is that
the projection operators must be optimized, i.e., all high Fourier
components must be removed from the projection operators. If this is not
done, [aliasing](../theory/Wrap-around_errors.md) can
happen, i.e., the high Fourier components of the projection operators
are downfolded to low Fourier components, and random noise is
introduced).

Currently, VASP supports three different schemes to remove the high
Fourier components from the projectors.
LREAL=.TRUE. is the simplest
one. For LREAL=.TRUE., the
real-space projectors that the pseudopotential generation code has
generated are used. This requires no user interference but is
potentially very inaccurate. For the outdated
LREAL=On, the real space
projectors are optimized by VASP using an algorithm proposed by
King-Smith et
al.<sup>[\[1\]](#cite_note-king-smith:prb:1991-1)</sup>
For the recommended
LREAL=Auto, an unpublished
scheme<sup>[\[2\]](#cite_note-kresse:tobepublished-2)</sup>
is used which results in simultaneously more accurate and localized
projector functions than for the King-Smith et al. method. To fine-tune
the optimization procedure, the tag [ROPT](ROPT.md) can and
should be used, if LREAL=Auto
(or LREAL=On) is used.
Specifically, perform first reference calculations using
LREAL=.False. and decrease
[ROPT](ROPT.md) until an acceptable accuracy, e.g., 1
meV/atom, is attained. Please also check carefully the documentation for
[ROPT](ROPT.md).

We recommend using the real-space projection scheme for systems
containing more than about 30 atoms. We also strongly recommend using
only LREAL=Auto.

For LREAL=A (and
LREAL=O) the projection
operators are optimized by VASP on the fly (i.e. on startup). Several
tags influence the optimization:

- [ENCUT](ENCUT.md) (i.e., the energy cutoff), components
  beyond the energy cutoff are 'removed' from the projection operators.

<!-- -->

- [PREC](PREC.md) tag specifies how precise the real-space
  projectors should be and sets the variables [ROPT](ROPT.md)
  accordingly to the following values:

For LREAL=Auto

|  |  |
|----|----|
| [ROPT](ROPT.md)=-5E-4 | if [PREC](PREC.md)=Normal |
| [ROPT](ROPT.md)=-5E-4 | if [PREC](PREC.md)=Single or SingleN |
| [ROPT](ROPT.md)=-2.5E-4 | if [PREC](PREC.md)=Accurate |
| [ROPT](ROPT.md)=-0.01 | if [PREC](PREC.md)=Low |
| [ROPT](ROPT.md)=-0.002 | if [PREC](PREC.md)=Medium |
| [ROPT](ROPT.md)=-4E-4 | if [PREC](PREC.md)=High |

For LREAL=On

|                               |                                     |
|-------------------------------|-------------------------------------|
| [ROPT](ROPT.md)=2/3 | if [PREC](PREC.md)=Low    |
| [ROPT](ROPT.md)=1.0 | if [PREC](PREC.md)=Medium |
| [ROPT](ROPT.md)=1.5 | if [PREC](PREC.md)=High   |

These defaults can be superseded by specifying the
[ROPT](ROPT.md) tag in the [INCAR](../input-files/INCAR.md) file.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>Real-space optimization (<span
class="mw-selflink selflink">LREAL</span>=Auto) always results in a
small (not necessarily negligible) error. The error is usually a
constant energy shift for each atom. If you are interested in energy
differences, use only calculations with the same setup (i.e., same <a
href="/wiki/ENCUT" title="ENCUT">ENCUT</a>, <a href="/wiki/PREC"
title="PREC">PREC</a>, <span class="mw-selflink selflink">LREAL</span>
and <a href="/wiki/ROPT" title="ROPT">ROPT</a> setting) for all
calculations. For example, if you want to calculate surface or defect
energies, recalculate the bulk ground-state energy with exactly the same
setting you are using for the surface. Another possibility is to relax
the structure using real-space projection and to perform one final
total-energy calculation using <span
class="mw-selflink selflink">LREAL</span>=.FALSE. to get exact energies.
For <a href="/wiki/PREC" title="PREC">PREC</a>=Normal, the errors
introduced by the real-space projection are usually of the same order of
magnitude as those introduced by the <a href="/wiki/Wrap-around_errors"
title="Wrap-around errors">wrap-around errors</a>. For <a
href="/wiki/PREC" title="PREC">PREC</a>=Accurate errors are usually less
than 1 meV/atom. <a href="/wiki/PREC" title="PREC">PREC</a>=Low should
be used only for, say, fast <a href="/wiki/MD" class="mw-redirect"
title="MD">molecular-dynamics calculations</a>, if compute resources are
really an issue.</li>
<li>When the energy cutoff <a href="/wiki/ENCUT" title="ENCUT">ENCUT</a>
is increased significantly w.r.t. their defaults, the real-space
projection scheme sometimes becomes unreliable, and it might be
necessary to decrease <a href="/wiki/ROPT" title="ROPT">ROPT</a> to
values as small as <a href="/wiki/ROPT" title="ROPT">ROPT</a>=1E-4.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=LREAL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ROPT](ROPT.md), [PREC](PREC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LREAL-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LREAL&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-king-smith:prb:1991_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.44.13063"
    class="external text" rel="nofollow">R. D. King-Smith, M. C. Payne, and
    J. S. Lin, <em>Real-space implementation of nonlocal pseudopotentials
    for first-principles total-energy calculations</em>, Phys. Rev. B
    <strong>44</strong>, 13063 (1991).</a>
2.  [↑](#cite_ref-kresse:tobepublished_2-0)
    G. Kresse, Unpublished.


------------------------------------------------------------------------


