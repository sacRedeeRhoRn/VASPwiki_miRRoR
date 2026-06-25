<!-- Source: https://vasp.at/wiki/index.php/LSFBXC | revid: 31419 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSFBXC


LSFBXC  = .TRUE. \| .FALSE.  
Default: **LSFBXC** = .FALSE. 

Description: Removes sources and drains from the exchange-correlation B
field.

------------------------------------------------------------------------

With LSFBXC=T, the sources and
drains are removed from the exchange-correlation (XC) B
field[^sharma:jctc:2018-1]
at each step of the electronic minimization. Thus, any
<a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC potential</a> can be constrained to correspond
to a Maxwellian magnetic field at the cost of becoming a potential-only
<a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC functional</a>, since there is no correction
applied to the XC energy. In other words, it is strictly necessary to
optimize the Kohn-Sham orbitals using [iterative
methods](../categories/Category-Electronic_minimization.md),
e.g. [ALGO](ALGO.md) = Normal , and it is *not* possible to
use [direct
optimizers](../categories/Category-Electronic_minimization.md),
e.g. [ALGO](ALGO.md) = Conjugate , etc., as they require
consistency between XC energy and XC potential.

Moore et al. implemented the same feature in a parallel
work[^guy:patch:2024-2][^guy:arxiv:2024-3]
and performed more extensive applications. Whether the two
implementations are identical has not been tested, and no publication is
associated with the present implementation (by Marie-Therese Huebsch)
using LSFBXC.

## Related tags and articles\[<a href="/wiki/index.php?title=LSFBXC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[XC](XC.md), [GGA](GGA.md)

## References\[<a href="/wiki/index.php?title=LSFBXC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^sharma:jctc:2018-1]: [Sharma, S., Gross, E. K. U., Sanna, A., and Dewhurst, J. K., *Source-free exchange-correlation magnetic fields in density functional theory*, J. Chem. Theory Comput., **14**, 1247-1253 (2018).](https://.doi.org/10.1021/acs.jctc.7b01049)
[^guy:patch:2024-2]: [Source free Bxc field patch by Moore et al.](https://github.com/guycmoore/source_free_Bxc_VASP)
[^guy:arxiv:2024-3]: [Moore, G. C., Horton, M. K., Kaplan, A. D., Ashour, O. A., Griffin, S. M., Persson, K. A. *Noncollinear ground states of solids with a source-free exchange correlation functional*, Phys. Rev. B, **111**, 094417 (2025).](https://doi.org/10.1103/PhysRevB.111.094417)
