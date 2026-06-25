<!-- Source: https://vasp.at/wiki/index.php/LMODELHF | revid: 34378 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMODELHF


LMODELHF = .TRUE. \| .FALSE.  
Default: **LMODELHF** = .FALSE. 

Description: LMODELHF selects
dielectric-dependent range-separated hybrid functionals with
[AEXX](AEXX.md) and [BEXX](BEXX.md) for the exact
Hartree-Fock exchange at long- and short-range, respectively.

------------------------------------------------------------------------

By setting LMODELHF=.TRUE.
various types of range-separated hybrid functionals using the error
function for the screening can be specified. The general form of hybrid
functionals that can be constructed with
LMODELHF is given by

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) + a_{\mathrm{LR}}
E_{\mathrm{x,LR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
(1-a_{\mathrm{LR}})E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{c}}^{\mathrm{SL}}$

where

- $a_{\mathrm{SR}}$ ([BEXX](BEXX.md)) and
  $a_{\mathrm{LR}}$ ([AEXX](AEXX.md)) are the
  **mixing parameters (fraction of HF exchange) at short and long
  range**, respectively.
- $\mu$ ([HFSCREEN](HFSCREEN.md)) is the
  **screening parameter** that determines the separation between short
  range (SR) and long range (LR).

Examples of such functionals are those proposed in Refs.
[^skone:prb:2016-1][^chen2018nonempirical-2][^cui2018doubly-3].
These hybrid functionals are based on a common model for the dielectric
function, but differ in the way how the range-separation parameters are
obtained from first-principles calculations. Their connection and
performance have been discussed for instance in Ref.
[^liu2019assessing-4].
In principle, they can be considered to be a smartly constructed
approximation to COH-SEX (local Coulomb hole plus screened exchange),
albeit fulfilling many important constraints that the exact exchange
correlation functional must observe.

The corresponding functional has been available in VASP since VASP.5.2
released in 2009 (before the two publications), although the gradient
contribution had been erroneously implemented in all VASP.5 releases and
is only correct in VASP.6. The related bug fix has been made available
by the authors of Ref.
[^cui2018doubly-3].
The nonlocal exchange part of the functional has also been used and
documented in Ref.
[^bokdam:scr:2016-5]
and is covered in [Improving the dielectric
function](../misc/Improving_the_dielectric_function.md).

An example of tags to specify in the [INCAR](../input-files/INCAR.md) file
is given for the DD-RSH-CAM
functional:[^chen2018nonempirical-2][^cui2018doubly-3]

    LHFCALC = .TRUE.
    LMODELHF = .TRUE.
    AEXX = $\varepsilon_{\infty}^{-1}$
    BEXX = 1.0   #The default value. Available since VASP.6.6.0.
    HFSCREEN = $\mu$
    GGA = PE

where $\varepsilon_{\infty}^{-1}$ is the inverse dielectric constant and
$\mu$ is the screening parameter.
[AEXX](AEXX.md) and [BEXX](BEXX.md) specify the
amount of exact exchange in the long and short range, respectively, that
is for short ($\mathbf{G} \to 0$) and large ($\mathbf{G} \to \infty$) wave vectors, respectively. The screening parameter
[HFSCREEN](HFSCREEN.md) determines how quickly the
nonlocal exchange changes from [AEXX](AEXX.md) to
[BEXX](BEXX.md).

Other examples of dielectric-dependent range-separated functionals
proposed in the
literature[^skone:prb:2016-1][^chen2018nonempirical-2][^cui2018doubly-3]
can be found
[here](../methods/Hybrid_functionals-_formalism.md)_with_different_mixings "Hybrid functionals: formalism")
and their corresponding INCAR files at [list of hybrid
functionals](../methods/List_of_hybrid_functionals.md).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>If <span class="mw-selflink selflink">LMODELHF</span>=.TRUE., then
<a href="/wiki/LHFCALC" title="LHFCALC">LHFCALC</a>=.TRUE. is
automatically set.</li>
<li>The <a href="/wiki/BEXX" title="BEXX">BEXX</a> tag is available only
since VASP.6.6.0. <a href="/wiki/BEXX" title="BEXX">BEXX</a> was
hard-coded to 1 in versions prior to VASP.6.6.0.</li>
</ul></td>
</tr>
</tbody>
</table>

Specifically, in VASP, the Coulomb kernel $4 \pi e^2 /
(\mathbf{q}+\mathbf{G})^2$ in the exact exchange is
multiplied by a model for the dielectric function
$\epsilon^{-1} (\mathbf{q}+\mathbf{G})$:

$\epsilon^{-1}
(\mathbf{q}+\mathbf{G})=1-(1-{{\varepsilon}_{\infty}^{-1}})\text{exp}\left(-\frac{|\mathbf{q+G}|^2}{4{\mu}^2}\right)$.

where $\mu$
corresponds to [HFSCREEN](HFSCREEN.md), and
${{\varepsilon}_{\infty}^{-1}}$ is specified by
[AEXX](AEXX.md). In real space this correspond to a Coulomb
kernel

$V(r) =\left\[1-\left(1-{{\varepsilon}_{\infty}^{-1}}\right)\text{erf}(
{\mu} r)\right\] \frac{e^2}{r}$.

  
The remaining part of the exchange is handled by an appropriate
semi-local exchange correlation functional. For further detail we refer
to the literature listed below.

Typical values for [HFSCREEN](HFSCREEN.md) are listed in
the table below

    AlP  1.24
    AlAs 1.18
    AlSb 1.13
    BN   1.7
    CdO  1.34
    CdS  1.19
    CdSe 1.18
    CdTe 1.07
    C    1.70
    GaN  1.39
    GaP  1.24
    GaAs 1.18
    GaSb 1.12
    Ge   1.18
    InP  1.14
    InAs 1.09
    InSb 1.05
    LiF  1.47
    MgO  1.39
    SiC  1.47
    Si   1.26
    ZnO  1.34
    ZnS  1.27
    ZnSe 1.20
    ZnTe 1.12

These values have been obtained from fits of the dielectric function
using the Nanoquanta kernel and partially self-consistent GW
calculations as used in Ref.
[^grueneis2014ionization-6].
The values can be also estimated from simple dimensional scaling
relations of the valence electron density. Furthermore band gap
predictions are not very sensitive to the choice of
[HFSCREEN](HFSCREEN.md).

## Related tags and articles\[<a href="/wiki/index.php?title=LMODELHF&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LHFCALC](LHFCALC.md),
[HFSCREEN](HFSCREEN.md), [AEXX](AEXX.md),
[BEXX](BEXX.md), [LTHOMAS](LTHOMAS.md),
[LRHFCALC](LRHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md),

## References\[<a href="/wiki/index.php?title=LMODELHF&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^skone:prb:2016-1]: [J. H. Skone, M. Govoni, and G. Galli, *Nonempirical range-separated hybrid functionals for solids and molecules*, Phys. Rev. B **93**, 235106 (2016).](http://doi.org/10.1103/PhysRevB.93.235106)
[^chen2018nonempirical-2]: [W. Chen, G. Miceli, G.M. Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent hybrid functional with range separation for semiconductors and insulators*, Phys. Rev. Mater. **2**, 073803 (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
[^cui2018doubly-3]: [Z.H. Cui, Y.C. Wang, M.Y. Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An Accurate First-Principles Approach for Both Narrow- and Wide-Gap Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345 (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
[^liu2019assessing-4]: [P. Liu, C. Franchini, M. Marsman, and G. Kresse, *Assessing model-dielectric-dependent hybrid functionals on the antiferromagnetic transition-metal monoxides MnO, FeO, CoO, and NiO*, J. Phys.: Condens. Matter **32**, 015502 (2020).](https://doi.org/10.1088/1361-648x/ab4150)
[^bokdam:scr:2016-5]: [M. Bokdam, T. Sander, A. Stroppa, S. Picozzi, D. D. Sarma, C. Franchini, and G. Kresse, Sci. Rep. **6**, 28618 (2016).](https://doi.org/10.1038/srep28618)
[^grueneis2014ionization-6]: [A. Grüneis, G. Kresse, Y. Hinuma, and F. Oba, Phys. Rev. Lett. **112**, 096401 (2014).](https://doi.org/10.1103/PhysRevLett.112.096401)
