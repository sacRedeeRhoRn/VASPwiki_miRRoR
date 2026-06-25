<!-- Source: https://vasp.at/wiki/index.php/ICORELEVEL | revid: 31344 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ICORELEVEL


ICORELEVEL = 0 \| 1 \| 2  
Default: **ICORELEVEL** = 0 

Description: ICORELEVEL
controls whether the core energies are explicitly calculated or not and
how they are calculated.

------------------------------------------------------------------------

The binding energy of core electrons $E_{CL}$ is
given as

$E_{CL} = E(n_{c}-1) - E(n_{c})$.

Here, $E(n_{c})$ is
the energy from a standard density-functional calculation in which the
number of core electrons corresponds to the unexcited ground state.
$E(n_{c}-1)$ is the energy of a calculation where one
electron is removed from the core of one particular atom and added to
the valence or conduction band.

The core-level binding energies can be calculated either in the
initial-state approximation or the final-state approximation. In the
initial-state approximation, a core electron is removed from the core
states and added to the valence/conduction bands but no change of the
potential (by e.g. relaxation of the valence electrons) is allowed. The
core-level binding energy can then be directly calculated by the
Kohn-Sham
eigenvalues<sup>[\[1\]](#cite_note-koehler:prb:04-1)[\[2\]](#cite_note-lizzit:prb:2001-2)</sup>
of the core level $\epsilon_{c}$ and the Fermi energy $\epsilon_{F}$

$E_{CL}^{\mathrm{i}}=\epsilon_{c} - \epsilon_{F}$.

In the final-state approximation, the electrons (valence electrons in
the frozen-core approximation) are allowed to relax, so that the local
hole is screened. In other words, a fully self-consistent electronic
calculation is carried out with a core hole and an additional electron
in the valence/conduction bands.

The following options are available in VASP:

- ICORELEVEL=0: The core
  energies are not calculated (default).
- ICORELEVEL=1: The
  initial-state approximation is used. This just involves recalculating
  the KS eigenvalues of the core states

after a self-consistent calculation of the valence charge density.
ICORELEVEL=1 is a little bit
more involved than the calculations using
[LVTOT](LVTOT.md)=*.TRUE.*, since the Kohn-Sham energy of
each core state is recalculated. This adds very little extra cost to the
calculations. Usually, the shifts correspond very closely to the change
of the electrostatic potential at the lattice sites (calculated using
[LVTOT](LVTOT.md)=*.TRUE.*).

- ICORELEVEL=2: The
  final-state approximation is used. Electrons are removed from the core
  and placed into the valence (effectively increasing
  [NELECT](NELECT.md)). The VASP implementation excites all
  selected core electrons for

all atoms of one species. The species, as well as the selected
electrons, are specified using

    CLNT = species 
    CLN =  main quantum number of excited core electron 
    CLL =  l quantum number of excited core electron
    CLZ =  electron count

The electron count
[CLZ](CLZ.md)
specifies how many electrons are excited from the core. Usually, 1 or
0.5 (Slater's transition state) are sensible choices.
[CLNT](CLNT.md) selects for which species in the
[POTCAR](../input-files/POTCAR.md) file the electrons are excited. Usually
one would like to excite the electrons for only one atom, this requires
changing the [POSCAR](../input-files/POSCAR.md) and
[POTCAR](../input-files/POTCAR.md) file, such that the selected atom
corresponds to one species in the [POTCAR](../input-files/POTCAR.md) file.
i.e. if the calculation invokes a supercell with 64 atoms of one type,
the selected atom needs to be singled out, and the
[POSCAR](../input-files/POSCAR.md) file will then contain 63 "standard"
atoms as well as one special species, at which the excited core hole
will be placed (the [POTCAR](../input-files/POTCAR.md) file will hold two
identical PAW datasets in this case).

Several caveats apply to this mode. First, the excited electron is
always spherical and multipole splittings are not available. Second, the
other core electrons are not allowed to relax, which might cause a
slight error in the calculated energies. Third, absolute energies are
not meaningful, since VASP usually reports valence energies only. Only
relative shifts of the core electron binding energies are relevant (in
some cases, the VASP total energies might become even positive).


## Contents


- [1 Super-cell
  core-hole method](#super-cell-core-hole-method)
- [2 Bethe-Salpeter
  equation for XAS](#bethe-salpeter-equation-for-xas)
- [3 Related tags
  and articles](#related-tags-and-articles)
- [4
  References](#references)


## Super-cell core-hole method\[<a
href="/wiki/index.php?title=ICORELEVEL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Super-cell core-hole method">edit</a> \| (./index.php.md)\]

ICORELEVEL=2 and its related
tags are necessary for the calculation of
<a href="/wiki/XAS_theory" class="mw-redirect" title="XAS theory">X-ray
absorption spectra</a> (XAS) using the super-cell core-hole method.

A description of how to set up super-cell core-hole calculations is
given in this <a href="/wiki/SCH_calculations" class="mw-redirect"
title="SCH calculations">article</a>.

A tutorial for the calculation of XAS is given in this
[article](../tutorials/XAS_-_Tutorial.md).

## Bethe-Salpeter equation for XAS\[<a
href="/wiki/index.php?title=ICORELEVEL&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Bethe-Salpeter equation for XAS">edit</a> \| (./index.php.md)\]

ICORELEVEL=2 is required for
the calculation of
<a href="/wiki/XAS" class="mw-redirect" title="XAS">XAS</a> using the
Bethe-Salpeter equation.

A description of how to set up a BSE calculation for XAS is given in
this
[article](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md).
There is also an accompanying [theory
page](../theory/Supercell_core-hole_theory.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=ICORELEVEL&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CLNT](CLNT.md), [CLN](CLN.md),
[CLL](CLL.md), [CLZ](CLZ.md),
[CH_LSPEC](CH_LSPEC.md),
[CH_SIGMA](CH_SIGMA.md),
[CH_NEDOS](CH_NEDOS.md), [ALGO](ALGO.md),
[LADDER](LADDER.md), [LHARTREE](LHARTREE.md),
[NBANDSV](NBANDSV.md), [NBANDSO](NBANDSO.md),
[OMEGAMAX](OMEGAMAX.md),
[ANTIRES](ANTIRES.md)

[Bethe-Salpeter equation for core
excitations](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)
[Supercell core-hole
calculations](../tutorials/Supercell_core-hole_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ICORELEVEL-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=ICORELEVEL&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-koehler:prb:04_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.70.165405"
    class="external text" rel="nofollow">L. Köhler and G. Kresse, Phys. Rev.
    B <strong>70</strong>, 165405 (2004).</a>
2.  [↑](#cite_ref-lizzit:prb:2001_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.63.205419"
    class="external text" rel="nofollow">S. Lizzit, A. Baraldi, A. Groso, K.
    Reuter, M. V. Ganduglia-Pirovano, C. Stampfl, M. Scheffler, M. Stichler,
    C. Keller, W. Wurth, and D. Menzel, Phys. Rev. B <strong>63</strong>,
    205419 (2001).</a>


  

------------------------------------------------------------------------


