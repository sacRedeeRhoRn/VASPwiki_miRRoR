<!-- Source: https://vasp.at/wiki/index.php/OMEGAMAX | revid: 31075 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# OMEGAMAX


OMEGAMAX = \[real\]  
Default: **OMEGAMAX** = outermost node in dielectric function
$\epsilon(\omega)$/1.3 

Description: OMEGAMAX
specifies the maximum frequency for the dense part of the frequency grid
for GW calculations (old GW code, does not apply to GWR). For CRPA
calculations, OMEGAMAX is the
frequency point of the interaction. For BSE calculations
OMEGAMAX determines the
maximum energy difference for excitation pairs to be included. For
calculations of the dielectric function via
[LOPTICS](LOPTICS.md)
OMEGAMAX determines the
maximum frequency of the calculated dielectric properties. Since the
flag controls different aspects of the code, be careful when setting it
(and remember to remove the tag, when you change the type of
calculations).

------------------------------------------------------------------------

GW type calculations:

For the frequency grid along the real and imaginary axis sophisticated
schemes are used, which are based on simple model functions for the
macroscopic dielectric function. The grid spacing is dense up to roughly
1.3\*OMEGAMAX and becomes
coarser for larger frequencies. The default value for
OMEGAMAX is either determined
by the outermost node in the dielectric function (corresponding to a
singularity in the inverse of the dielectric function) or the energy
difference between the valence band minimum and the conduction band
minimum. The larger of these two values is used. Except for
pseudopotentials with deep lying core states,
OMEGAMAX is usually determined
by the node in the dielectric function.

For <a href="/wiki/ACFDT_calculations" class="mw-redirect"
title="ACFDT calculations">ACFDT calculations</a>, only
[OMEGAMIN](OMEGAMIN.md) and
[OMEGATL](OMEGATL.md) determine the frequency grid (using a
minimax algorithm).

The defaults have been carefully tested, and it is recommended to leave
them unmodified, whenever possible. The grid should be solely controlled
by [NOMEGA](NOMEGA.md). The only other value that can be
modified is the complex shift [CSHIFT](CSHIFT.md). In
principle, [CSHIFT](CSHIFT.md) should NOT be chosen
independently of [NOMEGA](NOMEGA.md) and
OMEGAMAX: e.g. for less dense
grids (smaller [NOMEGA](NOMEGA.md)) the complex shift must
be accordingly increased. The default for
[CSHIFT](CSHIFT.md) has been chosen such that the
calculations are converged to 10 meV with respect to
[NOMEGA](NOMEGA.md): i.e. if [CSHIFT](CSHIFT.md)
is kept constant and [NOMEGA](NOMEGA.md) is increased, the
QP shifts should not change by more than 10 meV; at least for
[LSPECTRAL](LSPECTRAL.md) = .TRUE.. This was the case for
the considered test materials. For
[LSPECTRAL](LSPECTRAL.md) = .FALSE. this does not apply.
In this case it is recommended to set [CSHIFT](CSHIFT.md)
manually and to perform careful convergence tests.

For [LSPECTRAL](LSPECTRAL.md) = .TRUE. independent
convergence tests with respect to [NOMEGA](NOMEGA.md) and
[CSHIFT](CSHIFT.md) are usually not required, and it should
be sufficient to control the technical parameters via the single
parameter [NOMEGA](NOMEGA.md). Also note that too large
values for [NOMEGA](NOMEGA.md) in combination with coarse
k-point grids can cause a decrease in precision (see
[NOMEGA](NOMEGA.md)).

  
BSE and TD-DFT type calculations (see
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>):

In this case, OMEGAMAX allows
to reduce the number of conduction/ valence band pairs. Usually these
are determined by [NBANDSV](NBANDSV.md) and
[NBANDSO](NBANDSO.md). The number of pairs is roughly
proportional to the products of [NBANDSV](NBANDSV.md),
[NBANDSO](NBANDSO.md), and the number of k-points in the
full Brillouin zone. If
OMEGAMAX is set, pairs for
which the difference of the independent particle energy is larger than
OMEGAMAX will be removed from
the basis set (and from the BSE calculations). This can improve
performance, without significantly affecting the imaginary part of the
dielectric function. The real part of the dielectric function is,
however, rather sensitive to reducing
OMEGAMAX,
[NBANDSV](NBANDSV.md), [NBANDSO](NBANDSO.md).

Frequency dependent dielectric matrix calculations (see
[LOPTICS](LOPTICS.md)):

Here, OMEGAMAX sets the
maximum frequency of the dielectric function calculated. The number of
grid points is then defined via [NEDOS](NEDOS.md). Note, that
this parameter does not cut-off the number conduction/ valence band
pairs considered in the dielectric function. Only the dielectric
function itself is cut-off at this frequency. Hence, this does not
affect computational effort significantly. It is advisable to choose
OMEGAMAX high enough such that
the excitation spectrum is well covered, to avoid artifacts at the cut
off frequency due to the Gaussian and Lorentzian broadening (see section
[LOPTICS#Spectral
broadening](LOPTICS.md))

## Related tags and articles\[<a href="/wiki/index.php?title=OMEGAMAX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[OMEGATL](OMEGATL.md), [CSHIFT](CSHIFT.md),
[NOMEGA](NOMEGA.md), [OMEGAMIN](OMEGAMIN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-OMEGAMAX-_incategory-Examples)

------------------------------------------------------------------------


