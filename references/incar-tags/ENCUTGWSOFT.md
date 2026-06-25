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
[^harl:2008-1][^harl:2010-2][^klimes:2014-3]

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
window:[^riemelmoser:jcp:2020-4]

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

[^harl:2008-1]: [J. Harl and G. Kresse, Phys. Rev. B **77**, 045136 (2008).](https://doi.org/10.1103/PhysRevB.81.115126)
[^harl:2010-2]: [J. Harl, L. Schimka, and G. Kresse, Phys. Rev. B **81**, 115126 (2010).](https://doi.org/10.1103/PhysRevB.81.115126)
[^klimes:2014-3]: [J. Klimeš, M. Kaltak, and G. Kresse, Phys. Rev. B **90**, 075125 (2014).](https://doi.org/10.1103/PhysRevB.90.075125)
[^riemelmoser:jcp:2020-4]: [S. Riemelmoser, M. Kaltak, and G. Kresse, J. Chem. Phys. **152(13)**, 134103 (2020).](https://doi.org/10.1063/5.0002246)
