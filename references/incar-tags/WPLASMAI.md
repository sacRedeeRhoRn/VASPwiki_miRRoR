<!-- Source: https://vasp.at/wiki/index.php/WPLASMAI | revid: 35854 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WPLASMAI


WPLASMAI = \[real\]  
Default: **WPLASMAI** = 0 

Description: WPLASMAI sets the
complex shift (in eV) for the Drude term in the dielectric function.

------------------------------------------------------------------------

Metallic systems show a characteristic peak at \$\omega=0\$ in the
imaginary dielectric function, which originates from intraband
transitions. When WPLASMAI\>0
in the calculation of the dielectric function with
[LOPTICS](LOPTICS.md), these intraband transitions are
accounted for via the Drude term:

\begin{equation} \varepsilon(\omega)=1-\frac{\omega_p^2}{\omega(\omega+i
\gamma)}. \end{equation} Here, \$\omega_p\$ is the plasma frequency and
the complex shift \$\gamma\$ introduces a Lorentzian broadening of the
Drude peak which serves to account for scattering effects due to
phonons, impurities, and electron-electron interactions. If
WPLASMAI\>0, the Drude term is
introduced in both the density-density and current-current response
functions.

## Related Tags and Sections\[<a href="/wiki/index.php?title=WPLASMAI&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

- [LOPTICS](LOPTICS.md)


