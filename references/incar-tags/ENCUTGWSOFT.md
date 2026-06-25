<!-- Source: https://vasp.at/wiki/index.php/ENCUTGWSOFT | revid: 26011 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUTGWSOFT


ENCUTGWSOFT = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ENCUTGWSOFT** | = [ENCUTGW](ENCUTGW.md)$\times 0.8$ | for [ALGO](ALGO.md)=*ACFDT* |
|  | = [ENCUTGW](ENCUTGW.md)$\times 0.8$ | as of VASP.6.3 |
|  | = [ENCUTGW](ENCUTGW.md) | else |

|  |
|----|
| **Important:** For vasp.6.3 and later releases ENCUTGWSOFT always defaults to [ENCUTGW](ENCUTGW.md)$\times 0.8$. |

Descprition: The flag
ENCUTGWSOFT sets the energy
cutoff for the response function, such that it allows to truncate the
Coulomb kernel slowly between the energy specified by
ENCUTGWSOFT and
[ENCUTGW](ENCUTGW.md) using a cosine window function.

------------------------------------------------------------------------

RPA/ACFDT correlation energies converge very slowly with respect to
$\mathbf{G}_{\rm max }$. Thus VASP automatically
extrapolates to the infinite basis set limit using a linear regression
to the equation:
<sup>[\[1\]](#cite_note-harl:2008-1)[\[2\]](#cite_note-harl:2010-2)[\[3\]](#cite_note-klimes:2014-3)</sup>

$E_{\mathrm{c}}({\mathbf{G}})=E_{\mathrm{c}}(\infty)+\frac{A}{{\mathbf{G}}^3}$.

This usually leads to much smoother energy-volume curves in
<a href="/wiki/ACFDT_calculations" class="mw-redirect"
title="ACFDT calculations">ACFDT calculations</a> and [MP2
calculations](../tutorials/MP2_calculations.md). The modified
Coulomb kernel is in this case: $v_{G} = \frac{4 \pi e^2}
{G^2} \frac{1}{2} \left( 1 + \cos \left( \pi \\ \frac{ \frac{\hbar^{2}
G^2 }{2 m_e} - \mathrm{ ENCUTGWSOFT} }{ \mathrm{ENCUTGW} -
\mathrm{ENCUTGWSOFT}} \right) \right) \qquad \mbox{for} \quad
\frac{\hbar^2 G^2 }{2 m_e} > \mathrm{ENCUTGWSOFT}$

If [LSCK](LSCK.md) is set to .TRUE., the squeezed Coulomb
kernel is used instead of the cosine
window:<sup>[\[4\]](#cite_note-riemelmoser:jcp:2020-4)</sup>

$v_{G} = 4 \pi e^2 \frac{ (G_{max}-G_{min})(G_{max}-G) }{
(G_{min}^2 - G(2G_{min}-G_{max}))^2 } \qquad \mbox{for} \quad
\mathrm{ENCUTGWSOFT}=\frac{\hbar^2G_{min}^2}{2m_e}<\frac{\hbar^2
G^2}{2m_e}<\frac{\hbar^2G_{max}^2}{2m_e}=\mathrm{ENCUTGW}$

This kernel *squeezes* contributions from large wave vectors
$G>G_{max}$ into the window given by
ENCUTGWSOFT.
For GW type calculations the squeezed Coulomb kernel was the default
(when
ENCUTGWSOFT
was set in the INCAR file) before version vasp.6.3, but in newer
releases the code always defaults to a smoothed Coulomb kernel (both for
GW and RPA type calculations). If one desires to recover the behavior of
vasp.6.2 and older versions, [LSCK](LSCK.md)=.TRUE. must be
set in the INCAR file for GW type calculations if
ENCUTGWSOFT
is set in the INCAR file.

  

|  |
|----|
| **Mind:** The infinite basis set limit extrapolation for RPA/ACFDT is described in more detail [here](../methods/ACFDT__RPA_calculations.md). |

## Related tags and articles\[<a
href="/wiki/index.php?title=ENCUTGWSOFT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PRECFOCK](PRECFOCK.md), [ENCUT](ENCUT.md),
[ENCUTGW](ENCUTGW.md),
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>, [LSCK](LSCK.md),
[RPA/ACFDT basis set
convergence](../methods/ACFDT__RPA_calculations.md),
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENCUTGWSOFT-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-harl:2008_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.81.115126"
    class="external text" rel="nofollow">J. Harl and G. Kresse, Phys. Rev. B
    <strong>77</strong>, 045136 (2008).</a>
2.  [↑](#cite_ref-harl:2010_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.81.115126"
    class="external text" rel="nofollow">J. Harl, L. Schimka, and G. Kresse,
    Phys. Rev. B <strong>81</strong>, 115126 (2010).</a>
3.  [↑](#cite_ref-klimes:2014_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.90.075125"
    class="external text" rel="nofollow">J. Klimeš, M. Kaltak, and G.
    Kresse, Phys. Rev. B <strong>90</strong>, 075125 (2014).</a>
4.  [↑](#cite_ref-riemelmoser:jcp:2020_4-0)
    <a href="https://doi.org/10.1063/5.0002246" class="external text"
    rel="nofollow">S. Riemelmoser, M. Kaltak, and G. Kresse, J. Chem. Phys.
    <strong>152(13)</strong>, 134103 (2020).</a>


