<!-- Source: https://vasp.at/wiki/index.php/PREC | revid: 31482 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PREC


PREC = Normal \| Single \|
SingleN \| Accurate \| Low \| Medium \| High 

|                   |          |                |
|-------------------|----------|----------------|
| Default: **PREC** | = Medium | for VASP.4.X   |
|                   | = Normal | since VASP.5.X |

Description: PREC specifies
the "precision" mode.

------------------------------------------------------------------------

PREC sets default values for
the energy cutoff [ENCUT](ENCUT.md), the FFT grids
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
and
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md)),
and the accuracy of the projectors in real space
[ROPT](ROPT.md) (used only when
[LREAL](LREAL.md)=.TRUE.). Details are given below in the
table.

We recommend using PREC=Normal
or PREC=Accurate.
PREC=Normal can be used for
most routine calculations.
PREC=Accurate leads to a
denser grid
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
Thus, it reduces egg-box effects and strictly avoids any
[aliasing/wrap-around
errors](../theory/Wrap-around_errors.md).
PREC=Normal and
PREC=Accurate use an
augmentation fine grid
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
that is twice larger than the grid
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
used for the representation of the pseudo-orbitals.
PREC=Accurate increases the
memory requirements somewhat, but it should be used (in combination with
an increased value for [ENCUT](ENCUT.md)) when a very good
accuracy is required, e.g., for accurate forces, for phonons and stress
tensor or in general when second derivatives are computed. The accuracy
of forces can also be sometimes further improved by specifying
[ADDGRID](ADDGRID.md)=.TRUE., however, reports from users
are somewhat contradictory about whether this really helps. More details
can be found at
<a href="/wiki/Energy_cut_off_and_FFT_mesh" class="mw-redirect"
title="Energy cut off and FFT mesh">Energy cutoff and FFT mesh</a>.

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
<li>We strongly recommend specifying the energy cutoff <a
href="/wiki/ENCUT" title="ENCUT">ENCUT</a> always manually in the <a
href="/wiki/INCAR" title="INCAR">INCAR</a> file to ensure the same
accuracy between calculations. Otherwise, the default <a
href="/wiki/ENCUT" title="ENCUT">ENCUT</a> may differ among the
different calculations (e.g., for the calculation of the cohesive
energy), with the consequence that the total energies, for instance, can
not be compared.</li>
<li>Setting <span class="mw-selflink selflink">PREC</span>=Accurate does
not necessarily mean that the results are converged. The convergence of
the results with respect to the energy cutoff <a href="/wiki/ENCUT"
title="ENCUT">ENCUT</a> has to be checked separately.</li>
<li>Setting <a href="/wiki/ENAUG" title="ENAUG">ENAUG</a> has an effect
only if <span class="mw-selflink selflink">PREC</span> is set to one of
the deprecated settings (Low, Medium or High); otherwise, it is
ignored.</li>
</ul></td>
</tr>
</tbody>
</table>

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The value of a parameter set by <span
class="mw-selflink selflink">PREC</span> (e.g., <a href="/wiki/ENCUT"
title="ENCUT">ENCUT</a>) can be overridden by specifying explicitly the
value of that parameter in the <a href="/wiki/INCAR"
title="INCAR">INCAR</a> file.</li>
<li><span class="mw-selflink selflink">PREC</span>=Normal and <span
class="mw-selflink selflink">PREC</span>=Accurate are only available in
VASP.4.5 and newer versions. The setting <span
class="mw-selflink selflink">PREC</span>=Single is only available as of
VASP.5.1, and has been updated in VASP.6.</li>
</ul></td>
</tr>
</tbody>
</table>

|  |
|----|
| **Deprecated:** The old settings PREC=Medium, High and Low are no longer recommended and are available only for backward compatibility. Essentially, PREC=High only increases the energy cutoff by 30 %, which can also be achieved by just manually increasing [ENCUT](ENCUT.md). |

## Default values set by PREC\[<a href="/wiki/index.php?title=PREC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Default values set by PREC">edit</a> \| (./index.php.md)\]

Default values set by PREC for
the parameters [ENCUT](ENCUT.md),
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)),
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
and [ROPT](ROPT.md):

|  |  |  |  |  |  |
|----|:--:|:--:|:--:|:--:|:--:|
| PREC | [ENCUT](ENCUT.md) | [NGX](NGX.md),[Y](NGY.md),[Z](NGZ.md) | [NGXF](NGXF.md),[YF](NGYF.md),[ZF](NGZF.md) | [ROPT](ROPT.md) ([LREAL](LREAL.md)=A) | [ROPT](ROPT.md) ([LREAL](LREAL.md)=O) |
| Normal | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 3/2×$G_{\rm cut}$ | 2×[NGX](NGX.md) | -5×10<sup>-4</sup> | 1.0 |
| Single (VASP.5) | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10<sup>-4</sup> | 1.0 |
| Single (VASP.6) | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10<sup>-4</sup> | 1.0 |
| SingleN (VASP.6) | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10<sup>-4</sup> | 1.0 |
| Accurate | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 2×$G_{\rm cut}$ | 2×[NGX](NGX.md) | -2.5×10<sup>-4</sup> | 1.0 |
|  **Deprecated settings:** |  |  |  |  |  |
| Low | max([ENMIN](ENMIN.md)) | 3/2×$G_{\rm cut}$ | 3×$G_{\rm aug}$ | -1×10<sup>-2</sup> | 2/3 |
| Medium | max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 3/2×$G_{\rm cut}$ | 4×$G_{\rm aug}$ | -2×10<sup>-3</sup> | 1.0 |
| High | 1.3×max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>) | 2×$G_{\rm cut}$ | 16/3×$G_{\rm aug}$ | -4×10<sup>-4</sup> | 1.5 |

where
max(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>)
and max([ENMIN](ENMIN.md)) are the maxima of
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> and
[ENMIN](ENMIN.md) found in the
[POTCAR](../input-files/POTCAR.md) file, and $G_{\rm cut}$
and $G_{\rm aug}$
are defined by

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2 \qquad E_{\rm
aug}=\frac{\hbar^2}{2m_e}G_{\rm aug}^2$

with $E_{\rm cut}$=[ENCUT](ENCUT.md) and
$E_{\rm aug}$=[ENAUG](ENAUG.md).

## Further remarks\[<a href="/wiki/index.php?title=PREC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Further remarks">edit</a> \| (./index.php.md)\]

- With PREC=Normal, Single,
  and Accurate the grid
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
  representing the augmentation charges, charge densities and potentials
  has either the same size
  (PREC=Single) or the double
  size (PREC=Normal or
  Accurate) as the grid
  ([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
  With the deprecated (and no longer recommended) settings for
  PREC (Low, Medium and High),
  the grid
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
  is determined by some heuristic formula from
  [ENAUG](ENAUG.md).

<!-- -->

- PREC=Single uses the same
  grid
  ([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
  as PREC=Normal in VASP.5,
  but the same grid as
  PREC=Accurate in VASP.6.
  However, the double grid technique is not used, i.e.,
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))=([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
  This is convenient if one needs to cut down on storage demands or if
  one wants to reduce the size of the files [CHG](../output-files/CHG.md) and
  [CHGCAR](../input-files/CHGCAR.md). Furthermore,
  PREC=Single avoids
  high-frequency oscillations caused by the double-grid technique and
  the resulting Fourier interpolation. It is often expedient for
  scanning tunneling simulations or other calculations where
  high-frequency wiggles of the charge density in the vacuum region are
  undesirable.

<!-- -->

- PREC=High should guarantee
  that the absolute energies are converged to a few meV and the stress
  tensor converged within a few kBar.

## Related tags and articles\[<a href="/wiki/index.php?title=PREC&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NGX](NGX.md), [NGY](NGY.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [ENCUT](ENCUT.md),
[ENAUG](ENAUG.md), [ENMIN](ENMIN.md),
<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>,
[ROPT](ROPT.md), [LREAL](LREAL.md),
[ADDGRID](ADDGRID.md),
[PRECFOCK](PRECFOCK.md),
<a href="/wiki/Energy_cut_off_and_FFT_mesh" class="mw-redirect"
title="Energy cut off and FFT mesh">Energy cutoff and FFT mesh</a>,
[Wrap-around errors](../theory/Wrap-around_errors.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PREC-_incategory-Examples)


