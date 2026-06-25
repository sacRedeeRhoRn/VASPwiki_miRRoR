<!-- Source: https://vasp.at/wiki/index.php/LSPECTRALGW | revid: 18019 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSPECTRALGW


LSPECTRALGW = .FALSE. \|
.TRUE.  
Default: **LSPECTRALGW** = .FALSE. 

Description: LSPECTRALGW
specifies to use the spectral method for calculating the self-energy.

------------------------------------------------------------------------

If LSPECTRALGW = .TRUE. is
set, the imaginary part of the self-energy $\Sigma(\omega)= G W$ is calculated from the imaginary part of screened
potential $W(\omega)$ by
shifting the poles of $W$ by
$\pm \epsilon$, where $\epsilon$ are
the poles of the Green's function $G$.
Generally, LSPECTRALGW affects
the compute time very little. QP energies also hardly change when
LSPECTRALGW is modified.
However, LSPECTRALGW = .TRUE.
is usually slightly more robust, and should be selected for molecules
and other systems with flat dispersion-less bands. One the other hand,
LSPECTRALGW = .TRUE. seems to
converge slightly slower, as the complex shift
[CSHIFT](CSHIFT.md) is decreased. Set this flag, if the QP
energies show erratic behavior, for instance, if QP energies or
Z-factors are not in the expected range of values (0.5\<Z\<0.9).

  

## Related tags and articles\[<a
href="/wiki/index.php?title=LSPECTRALGW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LSPECTRAL](LSPECTRAL.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSPECTRALGW-_incategory-Examples)

------------------------------------------------------------------------


