<!-- Source: https://vasp.at/wiki/index.php/LCHIMAG | revid: 35877 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LCHIMAG


LCHIMAG = .TRUE. \| .FALSE.  
Default: **LCHIMAG** = .FALSE. 

Description: Calculate the chemical shifts and magnetic susceptibility
within linear response theory.

------------------------------------------------------------------------

For `LCHIMAG`` = True`, the
chemical shift tensors and magnetic susceptibility is computed. The
implementation<sup>[\[1\]](#cite_note-dewijs:laskowski:jcp:2017-1)</sup>
is based on linear response theory using the gauge-invariant PAW method
of Yates, Pickard, and Mauri
<sup>[\[2\]](#cite_note-pickard:prb:2001-2)[\[3\]](#cite_note-yates:prb:2007-3)</sup>,
that is an extension to the standard
<a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
method</a> to account for the effects of a vector gauge field
$A$. The NMR response currents are computed and the
induced B field is calculated based on the Biot-Savart law.

See also [WRT_NMRCUR](WRT_NMRCUR.md) to write the
currents and [NUCIND](NUCIND.md) to compute the
nucleus-independent chemical shielding (NICS).

|  |
|----|
| **Warning:** This method only works for non-metallic systems, i.e., that have a finite bandgap. |

Follow these guides for [calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md)
and [calculating the magnetic
susceptibility](../tutorials/Calculating_the_magnetic_susceptibility.md).


## Contents


- [1
  Definitions](#Definitions)
- [2
  Output](#Output)
  - [2.1 Magnetic
    susceptibility](#Magnetic_susceptibility)
  - [2.2 Chemical
    shielding](#Chemical_shielding)
- [3 Related tags
  and articles](#Related_tags_and_articles)
- [4
  References](#References)


## Definitions\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Definitions">edit</a> \| (./index.php.md)\]

The chemical shielding tensor is defined as:

$\sigma_{ij}(\mathbf{R}) = - \frac{ \partial
B^{\mathrm{in}}_i(\mathbf{R})}{ \partial B^{\mathrm{ext}}_j}$

Here $\mathbf{R}$
denotes the atomic nuclear site, $i$ and
$j$ denote Cartesian indices, $\mathbf{B}^{\mathrm{ext}}$ an applied DC external magnetic field and
$\mathbf{B}^{\mathrm{in}}(\mathbf{R})$ the induced
magnetic field at the nucleus.

NMR experiments yield information on the shielding relative to a
reference compound:

$\delta_{ij}(\mathbf{R}) = \sigma_{ij}^{\mathrm{ref}} -
\sigma_{ij}(\mathbf{R})$

Here, $\sigma_{ij}^{\mathrm{ref}}$ is the isotropic shielding of the nucleus in the
reference compound. $\delta_{ij}(\mathbf{R})$ is the chemical shift tensor. In order to compare
numerical results with the experimental data, one usually considers a
series of compounds and references them to the experimental series.

VASP calculates chemical "shifts" for non-metallic crystalline systems
using the linear response method of Yates, Pickard, and Mauri
<sup>[\[2\]](#cite_note-pickard:prb:2001-2)[\[3\]](#cite_note-yates:prb:2007-3)</sup>.

The isotropic chemical "shift" $\sigma_{iso}$, span $\Omega$, and
skew $\kappa$ are
also reported, according to the following Herzfeld-Berger convention
<sup>[\[4\]](#cite_note-mason:ssn:1993-4)</sup>:

$\sigma_{iso} = (\sigma_{11} + \sigma_{22} + \sigma_{33})/3$

$\Omega = \sigma_{33} - \sigma_{11}$

$\kappa = 3(\sigma_{iso} - \sigma_{22})/\Omega.$

The orbital magnetic susceptibility $\chi$ is
calculated according to a finite-differences approach:

$\chi_{\textrm{bare}} = \lim_{q\to0} \frac{F(q) 2F(q) + F(-q)}{q^2}$

where $F_{ij}(q)=(2-\delta_{ij})Q_{ij}(q)$.

*Q<sub>ij</sub>* is approximated in two ways. The so-called
*pGv*-approximation is used by default
<sup>[\[3\]](#cite_note-yates:prb:2007-3)</sup>,
where *p* is momentum, *v* is velocity, and *G* is a Green's function.
An alternative approach, the *vGv*-approximation is also used to
calculate an alternative susceptibility since VASP 6.4.0
<sup>[\[5\]](#cite_note-avezac:prb:2007-5)</sup>.
*Q* is defined for the *pGv*-approximation as:

$Q(q) = - \frac{1}{c^2 N_k V_c} \sum_{i=x,y,z} \sum_{o,\textbf{k}}
\textrm{Re}\[\langle \bar{u}^{(0)}_{o,\textbf{k}} |
\hat{\textbf{u}}_i \times (-i \nabla + \textbf{k}) \times
\mathcal{G}_{\textbf{k} + \textbf{q}_i}(\epsilon_{o,\textbf{k}})
\hat{\textbf{u}}_i \times \textbf{v}_{\textbf{k} + \textbf{q}_i,
\textbf{k}}(\epsilon_{o,\textbf{k}}) | \bar{u}^{(0)}_{o,\textbf{k}}
\rangle\]$

and for the *vGv*-approximation as:

$Q(q) = - \frac{1}{c^2 N_k V_c} \sum_{i=x,y,z} \sum_{o,\textbf{k}}
\textrm{Re}\[\langle \bar{u}^{(0)}_{o,\textbf{k}} |
\hat{\textbf{u}}_i \times \textbf{v}_{\textbf{k} + \textbf{q}_i,
\textbf{k}}(\epsilon_{o,\textbf{k}}) \times \mathcal{G}_{\textbf{k} +
\textbf{q}_i}(\epsilon_{o,\textbf{k}}) \hat{\textbf{u}}_i \times
\textbf{v}_{\textbf{k} + \textbf{q}_i,
\textbf{k}}(\epsilon_{o,\textbf{k}}) | \bar{u}^{(0)}_{o,\textbf{k}}
\rangle\]$.

## Output\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The isotropic chemical shieldings are printed towards the end of the
[OUTCAR](../output-files/OUTCAR.md) file, after the self-consistent
calculation has finished. The chemical shift tensors both before and
after space group symmetrization. These are the absolute tensors for the
infinite lattice, excluding core contributions. They can be searched for
under the `UNSYMMETRIZED TENSORS` and `SYMMETRIZED TENSORS` after
`Absolute Chemical Shift tensors`. Additionally, the magnetic
susceptibility is printed shortly after and found under
`ORBITAL MAGNETIC SUSCEPTIBILITY`.

### Magnetic susceptibility\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Magnetic susceptibility">edit</a> \| (./index.php.md)\]

The magnetic susceptibility is found at the start of the
`ORBITAL MAGNETIC SUSCEPTIBILITY, excluding core contribution`. The
magnetic susceptibility is split into that obtained by the
*pGv*-approximation and obtained by the *vGv*-approximation:

    -------------------------------------------------------------
      ORBITAL MAGNETIC SUSCEPTIBILITY, excluding core contribution
     -------------------------------------------------------------
      Approximate magnetic susceptibility, pGv (10^-6 cm^3/mole)
         1        -70.928534         -0.000000          0.000000
         2         -0.000000        -70.928534          0.000000
         3          0.000000          0.000000        -70.928534
     -------------------------------------------------------------
      Approximate magnetic susceptibility, vGv (10^-6 cm^3/mole)
         1        -63.412095         -0.000000          0.000000
         2         -0.000000        -63.412095          0.000000
         3          0.000000          0.000000        -63.412095

             principal value                      axis
           (10^-6 cm^3/mole)           x,          y,          z
          --------------------------------------------------------
                  -63.412095      0.1652     -0.9863      0.0000
                  -63.412095     -0.9863     -0.1652      0.0000
                  -63.412095      0.0000      0.0000      1.0000
     -------------------------------------------------------------

### Chemical shielding\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Chemical shielding">edit</a> \| (./index.php.md)\]

To obtain the full absolute tensors requires adding both the
$\mathbf{G=0}$ contribution (cf.
`G=0 CONTRIBUTION TO CHEMICAL SHIFT`) and the contributions due to the
core electrons. The latter consists of contributions for each chemical
species separately (depending on [POTCAR](../input-files/POTCAR.md)) and a
global $\mathbf{G=0}$
susceptibility contribution.

The reference shift experienced by the core is given first:

      Core NMR properties

      typ  El   Core shift (ppm)
     ----------------------------
        1  C     -200.5098801
     ----------------------------

      Core contribution to magnetic susceptibility:     -0.31  10^-6 cm^3/mole
     --------------------------------------------------------------------------

|  |
|----|
| **Important:** The isotropic chemical shift $\delta_{\mathrm{iso}}\mathrm{\[VASP\]}$ (ISO_SHIFT) is the negative of the isotropic shielding. To make it a *real shift* one should add the reference shielding. |

Next, the tensor is processed and its chemical shielding anisotropy
(CSA) characteristics are printed in the
[OUTCAR](../output-files/OUTCAR.md). The tensor is symmetrized
($\sigma_{ij} = \sigma_{ji}$ is enforced) and
diagonalized. From the three diagonal values the isotropic chemical
"shift" $\delta_{\mathrm{iso}}\mathrm{\[VASP\]}$, span
$\Omega$, and skew $\kappa$ are
calculated and printed see Ref.
<sup>[\[4\]](#cite_note-mason:ssn:1993-4)</sup>
for unambiguous definitions. Note that $\kappa$ is
ill-defined if $\Omega = 0$.
Units are ppm, except for the skew. A typical output is given below:

|  |
|----|
| **Mind:** As of VASP 6.6.0, the following is legacy format (cf. [LNMRLEG](LNMRLEG.md)). |

                                                                                                              
       ---------------------------------------------------------------------------------
        CSA tensor (J. Mason, Solid State Nucl. Magn. Reson. 2, 285 (1993))
       ---------------------------------------------------------------------------------
                   EXCLUDING G=0 CONTRIBUTION             INCLUDING G=0 CONTRIBUTION
               -----------------------------------   -----------------------------------
        ATOM    ISO_SHIFT        SPAN        SKEW     ISO_SHIFT        SPAN        SKEW
       ---------------------------------------------------------------------------------
        (absolute, valence only)
           1    4598.8125      0.0000      0.0000     4589.9696      0.0000      0.0000
           2     291.5486      0.0000      0.0000      282.7058      0.0000      0.0000
           3     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
           4     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
           5     736.5979    344.8803      1.0000      727.7550    344.8803      1.0000
       ---------------------------------------------------------------------------------
        (absolute, valence and core)
           1   -6536.1417      0.0000      0.0000    -6547.9848      0.0000      0.0000
           2   -5706.3864      0.0000      0.0000    -5718.2296      0.0000      0.0000
           3   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
           4   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
           5   -2369.4015    344.8803      1.0000    -2381.2446    344.8803      1.0000
       ---------------------------------------------------------------------------------
        IF SPAN.EQ.0, THEN SKEW IS ILL-DEFINED
       ---------------------------------------------------------------------------------

The isotropic chemical shielding for each atom, excluding and including
G=0 contributions, as well as the span and skew (descriptions of
asymmetry), follow. Finally, core contributions are taken into account
for the `ISO_SHIFT`, `SPAN`, and `SKEW`.

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
<li>The columns excluding the <span class="smj-container"
style="opacity:.5">$\mathbf{G=0}$</span>
contribution are useful for supercell calculations on molecules.</li>
<li>The columns including the <span class="smj-container"
style="opacity:.5">$\mathbf{G=0}$</span>
contribution are for crystals.</li>
<li>The upper block gives the shielding due to only the electrons
included in the SCF calculation.</li>
<li>The lower block has the contributions due to the frozen PAW cores
added. These core contributions are rigid <sup><a
href="#cite_note-gregor:jcp:1999-6"><span
class="cite-bracket">[</span>6<span
class="cite-bracket">]</span></a></sup>. They depend on <a
href="/wiki/POTCAR" title="POTCAR">POTCAR</a> and are isotropic, i.e.
affect neither SPAN nor SKEW.</li>
</ul></td>
</tr>
</tbody>
</table>

As of VASP.6.6.0, in [OUTCAR](../output-files/OUTCAR.md) a summary of the
tensors per ion is also printed. This is done both excluding and
including the **G**=0 contribution. The summary starts with, for each
ion, its number, the isotropic shielding, the shielding tensor and the
symmetrized shielding tensor. Next the principal components and the
principal axes are printed (from the symmetrized tensor). They are
ordered following Mason
<sup>[\[4\]](#cite_note-mason:ssn:1993-4)</sup>,
i.e. σ<sub>11</sub> \< σ<sub>22</sub> \< σ<sub>33</sub>. Finally a line
is printed with (again) the isotropic shielding σ<sub>iso</sub>, the
span Ω & skew κ (Herzfeld-Berger, Mason sections 2.2 and 2.3) and the
shielding anisotropy Δ & asymmetry η (Haeberlen, Mason section 2.6).

     ---------------------------------------------------------------------------------------
      CSA tensor (J. Mason, Solid State Nucl. Magn. Reson. 2, 285 (1993))
      for chemical shielding  (including the isotropic core contribution)

      BDIR labels direction of applied magnetic field (i.e. B0)
      For BDIR==1, B0 along x-axis, etc.
      Induced field listed along cartesian directions for each BDIR
     ---------------------------------------------------------------------------------------
                     EXCLUDING G=0 CONTRIBUTION             INCLUDING G=0 CONTRIBUTION
                ------------------------------------   ------------------------------------
      ion  BDIR            X           Y           Z              X           Y           Z
              (   iso_shield        span        skew) (  iso_shield        span        skew)
     ---------------------------------------------------------------------------------------
        1     1     142.5256     -0.0000      0.0000       229.8645     -0.0000      0.0000
              2      -0.0000    142.5256      0.0000        -0.0000    229.8645     -0.0000
              3      -0.0000      0.0000    142.5256        -0.0000      0.0000    229.8645
              (     142.5256      0.0000      0.0000) (    229.8645      0.0000      0.0000)

        2     1     142.5256     -0.0000      0.0000       229.8645     -0.0000      0.0000
              2      -0.0000    142.5256      0.0000        -0.0000    229.8645     -0.0000
              3      -0.0000      0.0000    142.5256        -0.0000      0.0000    229.8645
              (     142.5256      0.0000      0.0000) (    229.8645      0.0000      0.0000)
     ---------------------------------------------------------------------------------------
      IF SPAN.EQ.0, THEN SKEW IS ILL-DEFINED
     ---------------------------------------------------------------------------------------

## Related tags and articles\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[DQ](DQ.md), [ICHIBARE](ICHIBARE.md),
[LNMR_SYM_RED](LNMR_SYM_RED.md),
[NLSPLINE](NLSPLINE.md), [LLRAUG](LLRAUG.md),
[LBONE](LBONE.md), [LVGVCALC](LVGVCALC.md),
[LVGVAPPL](LVGVAPPL.md), [NUCIND](NUCIND.md)

[Calculating the chemical
shieldings](../tutorials/Calculating_the_chemical_shieldings.md),
[Calculating the magnetic
susceptibility](../tutorials/Calculating_the_magnetic_susceptibility.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LCHIMAG-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LCHIMAG&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-dewijs:laskowski:jcp:2017_1-0)
    <a href="https://doi.org/10.1063/1.4975122" class="external text"
    rel="nofollow">G. A. de Wijs, R. Laskowski, P. Blaha, R. W. A. Havenith,
    G. Kresse, and M. Marsman, <em>NMR shieldings from density functional
    perturbation theory: GIPAW versus all-electron calculations</em>, J.
    Chem. Phys. <strong>146</strong>, 064115 (2017).</a>
2.  ↑
    <sup>[a](#cite_ref-pickard:prb:2001_2-0)</sup>
    <sup>[b](#cite_ref-pickard:prb:2001_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.63.245101"
    class="external text" rel="nofollow">C. J. Pickard and F. Mauri,
    <em>All-electron magnetic response with pseudopotentials: NMR chemical
    shifts</em>, Phys. Rev. B <strong>63</strong>, 245101 (2001).</a>
3.  ↑
    <sup>[a](#cite_ref-yates:prb:2007_3-0)</sup>
    <sup>[b](#cite_ref-yates:prb:2007_3-1)</sup>
    <sup>[c](#cite_ref-yates:prb:2007_3-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.76.024401"
    class="external text" rel="nofollow">J. R. Yates, C. J. Pickard, and F.
    Mauri, <em>Calculation of NMR chemical shifts for extended systems using
    ultrasoft pseudopotentials</em>, Phys. Rev. B <strong>76</strong>,
    024401 (2007).</a>
4.  ↑
    <sup>[a](#cite_ref-mason:ssn:1993_4-0)</sup>
    <sup>[b](#cite_ref-mason:ssn:1993_4-1)</sup>
    <sup>[c](#cite_ref-mason:ssn:1993_4-2)</sup>
    <a href="https://doi.org/10.1016/0926-2040(93)90010-K"
    class="external text" rel="nofollow">J. Mason, <em>Conventions for the
    reporting of nuclear magnetic shielding (or shift) tensors suggested by
    participants in the NATO ARW on NMR shielding constants at the
    University of Maryland, College Park, July 1992</em>, Solid State Nucl.
    Magn. Reson. <strong>2</strong>, 285 (1993).</a>
5.  [↑](#cite_ref-avezac:prb:2007_5-0)
    <a href="https://doi.org/10.1103/PhysRevB.76.165122"
    class="external text" rel="nofollow">M. d'Avezac, N. Marzari, and F.
    Mauri, <em>Spin and orbital magnetic response in metals: Susceptibility
    and NMR shifts</em>, Phys. Rev. B <strong>76</strong>, 165122
    (2007).</a>
6.  [↑](#cite_ref-gregor:jcp:1999_6-0)
    <a href="https://doi.org/10.1063/1.479451" class="external text"
    rel="nofollow">T. Gregor, F. Mauri, and R. Car, <em>A comparison of
    methods for the calculation of NMR chemical shifts</em>, J. Chem. Phys.
    <strong>111</strong>, 1815 (1999).</a>


