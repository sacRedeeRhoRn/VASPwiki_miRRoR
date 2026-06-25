<!-- Source: https://vasp.at/wiki/index.php/ROPT | revid: 27293 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ROPT


ROPT = \[real array\], one
entry for each species on the [POTCAR](../input-files/POTCAR.md) file 

|  |  |  |
|----|----|----|
| Default: **ROPT** | = -5E-4 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=Normal |
|  | = -5E-4 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=Single or SingleN |
|  | = -2.5E-4 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=Accurate |
|  | = -0.01 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=Low |
|  | = -0.002 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=Medium |
|  | = -4E-4 | if [LREAL](LREAL.md)=Auto and [PREC](PREC.md)=High |

|  |  |  |
|----|----|----|
| Default: **ROPT** | = 2/3 | if [LREAL](LREAL.md)=On and [PREC](PREC.md)=Low |
|  | = 1.0 | if [LREAL](LREAL.md)=On and [PREC](PREC.md)=Medium |
|  | = 1.5 | if [LREAL](LREAL.md)=On and [PREC](PREC.md)=High |

  
Description: ROPT determines
how accurately the projectors are represented in real space. With
[LREAL](LREAL.md)=On, the real space projectors are optimized
using an algorithm proposed by King-Smith et
al.<sup>[\[1\]](#cite_note-king-smith:prb:1991-1)</sup>
[LREAL](LREAL.md)=Auto<sup>[\[2\]](#cite_note-kresse:tobepublished-2)</sup>
is the recommended scheme since it is considerably more accurate,
resulting in more localized projector functions than with the King-Smith
et al. method.

------------------------------------------------------------------------

  

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>Whether the user supplies negative or positive values in the INCAR
file is irrelevant. With <a href="/wiki/LREAL"
title="LREAL">LREAL</a>=Auto and On, <span
class="mw-selflink selflink">ROPT</span> are internally set to negative
and positive values, respectively.</li>
<li><a href="/wiki/LREAL" title="LREAL">LREAL</a>=On is outdated and
should be only used, if compatibility to old calculations is
desired.</li>
</ul></td>
</tr>
</tbody>
</table>

Depending on their value, VASP interprets
ROPT entries in one of two
ways:

- ABS\|ROPT\| ≥ 0.1:
  "conventional"-mode:

Sets the number of real space points within the cutoff sphere for a
particular species to approximately
1000×ROPT. So for instance,
the line

    ROPT = 0.7 1.5

will set the number of real space points within the cutoff sphere for
the first species to approximately 700, and that for the second species
to 1500.

- ABS\|ROPT\| \< 0.1 :
  "precision"-mode:

In this case, the real-space operators will be optimized for an accuracy
of approximately ROPT eV/atom.
So, for instance specifying the following line in the
[INCAR](../input-files/INCAR.md) file

    ROPT = 1E-3 1E-3

tells VASP to optimize the real-space projector operators for species 1
and 2 for an accuracy of approximately 1 meV/atom (10<sup>-3</sup>). The
estimate is, however, fairly rough: this means that even if an error of
say 0.5 meV/atom is selected, the actual error might well approach 5
meV/atom for transition metals with many electrons. It is recommended to
first perform reference calculations using
[LREAL](LREAL.md)=.FALSE., then switch to
[LREAL](LREAL.md)=Auto and decrease
ROPT until the desired
accuracy is reached.

The "precision" and "conventional" modes may be intermixed, i.e., it is
possible to specify

    ROPT = 0.7 -1E-3

In this case, the number of real space points within the cutoff sphere
for the first species will be approximately 700, whereas the real space
projector functions for the second species are optimized for an accuracy
of approximately 1 meV. We recommend to use the "precision" mode with a
target accuracy of around 2x10<sup>-4</sup> - 10<sup>-3</sup> eV/atom.

If you use the "conventional" mode, in which the number of grid points
in the real space projection sphere is specified, you have to select
ROPT carefully, especially if
a hard species is mixed with a soft species. In that case the following
lines in the [OUTCAR](../output-files/OUTCAR.md) file must be checked (here
is the output for [LREAL](LREAL.md)=Auto, however, the one
for [LREAL](LREAL.md)=On is quite similar)

    Optimization of the real space projectors
    maximal supplied QI-value         = 13.98
    optimisation between [QCUT,QGAM] = [  8.81, 17.62] = [ 21.73, 86.94] Ry
    Optimized for a Real-space Cutoff    1.41 Angstroem
      l    n(q)    QCUT    max X(q) W(low)/X(q) W(high)/X(q)  e(spline)
      2      6     8.810    59.645    0.61E-03    0.18E-02    0.11E-06
      2      6     8.810    58.460    0.65E-03    0.19E-02    0.12E-06
      0      7     8.810    97.683    0.18E-02    0.15E-03    0.13E-06
      0      7     8.810    53.223    0.17E-02    0.15E-03    0.12E-06
      1      7     8.810    13.596    0.47E-02    0.65E-02    0.33E-06
      1      7     8.810     7.885    0.35E-02    0.48E-02    0.25E-06

<a href="/wiki/index.php?title=QCUT&amp;action=edit&amp;redlink=1"
class="new" title="QCUT (page does not exist)">QCUT</a> and
<a href="/wiki/index.php?title=QGAM&amp;action=edit&amp;redlink=1"
class="new" title="QGAM (page does not exist)">QGAM</a> are parameters
chosen for the generation of this particular PAW dataset (or ultrasoft
pseudopotential). The most important information is given in the columns
`W(low)/X(q)` and `W(high)/X(q)` for [LREAL](LREAL.md)=Auto).
In these columns, the values must be as small as possible. If these
values are too large increase the
ROPT value from the default
value (or decrease it if it smaller than 0.1). As a rule of thumb, the
maximum allowed value in this column is 10<sup>-3</sup> for
[PREC](PREC.md)=Normal. (For [PREC](PREC.md)=Low
errors might be around 10<sup>-2</sup>. If W(q)/X(q) is larger than
10<sup>-2</sup> the errors introduced by the real space projections can
be substantial. In this case
ROPT must be specified in the
[INCAR](../input-files/INCAR.md) file to avoid incorrect results.

## Related tags and sections\[<a href="/wiki/index.php?title=ROPT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[LREAL](LREAL.md), [PREC](PREC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ROPT-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=ROPT&amp;veaction=edit&amp;section=2"
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


