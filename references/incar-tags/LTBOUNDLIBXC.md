<!-- Source: https://vasp.at/wiki/index.php/LTBOUNDLIBXC | revid: 29391 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTBOUNDLIBXC


LTBOUNDLIBXC = .TRUE. \|
.FALSE.  
Default: **LTBOUNDLIBXC** = .FALSE. 

Description: LTBOUNDLIBXC
specifies whether or not the lower bound for the Kohn-Sham
kinetic-energy density $\tau_{\sigma}$ ($\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$) is
enforced before $\tau_{\sigma}$ is used in a [METAGGA](METAGGA.md)
functional from Libxc.

------------------------------------------------------------------------

The Kohn-Sham kinetic-energy density

$\tau_{\sigma}=\frac{1}{2}\sum_{i}\nabla\psi_{i\sigma}^{\*}\cdot\nabla\psi_{i\sigma}$

should, in principle, be larger than the von Weizsäcker kinetic-energy
density[^kurth:ijqc:1999-1]

$\tau_{\sigma}^{\textrm{W}}=\frac{\left\vert\nabla
n_{\sigma}\right\vert^{2}}{8 n_{\sigma}}.$

However, for numerical reasons $\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$ may not be
fulfilled, which can potentially lead to problems, in particular if the
meta-GGA functional is not defined for negative values of
$\tau_{\sigma}-\tau_{\sigma}^{\textrm{W}}$. If
LTBOUNDLIBXC=.TRUE. in
[INCAR](../input-files/INCAR.md), then $\tau_{\sigma}=\max(\tau_{\sigma},\tau_{\sigma}^{\mathrm{W}})$ is applied before $\tau_{\sigma}$ is used in a meta-GGA functional from Libxc.

However, according to tests, for some of the most common meta-GGA
functionals like
SCAN[^sun:prl:15-2],
a violation of the lower bound is technically not a problem.
Furthermore, it has been observed that applying
$\tau_{\sigma}=\max(\tau_{\sigma},\tau_{\sigma}^{\mathrm{W}})$ may possibly lead to very inaccurate forces and stress
tensor. Therefore, by default
LTBOUNDLIBXC=.FALSE. and Libxc
should be compiled with the option `--disable-fhc` has explained
[here](../misc/Makefile.include.md).

Thus, the recommendation is to set
LTBOUNDLIBXC=.TRUE. only in
the case convergence shows an erratic behavior. If this choice is made,
then the forces and stress tensor should be carefully monitored if a
geometry optimization is done.

## Related tags and articles\[<a
href="/wiki/index.php?title=LTBOUNDLIBXC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LIBXC1](LIBXC1.md), [LIBXC2](LIBXC2.md),
[METAGGA](METAGGA.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LTBOUNDLIBXC-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=LTBOUNDLIBXC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^kurth:ijqc:1999-1]: [S. Kurth, J. P. Perdew, and P. Blaha, *Molecular and solid-state tests of density functional approximations: LSD, GGAs, and meta-GGAs*, Int. J. Quantum Chem. **75**, 889 (1999).](https://doi.org/10.1002/(SICI)1097-461X(1999)75:4/5%3C889::AID-QUA54%3E3.0.CO;2-8)
[^sun:prl:15-2]: [J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. **115**, 036402 (2015).](https://doi.org/10.1103/PhysRevLett.115.036402)
