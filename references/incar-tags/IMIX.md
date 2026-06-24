<!-- Source: https://vasp.at/wiki/index.php/IMIX | revid: 27203 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IMIX
IMIX = 0 \| 1 \| 2 \| 4  
Default: **IMIX** = 4 

Description: IMIX specifies the type of [density
mixing](../categories/Category-Density_mixing.md).

------------------------------------------------------------------------

## Contents

- [1 IMIX=0: No mixing](#IMIX=0:_No_mixing)
- [2 IMIX=1: Kerker mixing](#IMIX=1:_Kerker_mixing)
- [3 IMIX=2: Variant of Tchebycheff
  mixing](#IMIX=2:_Variant_of_Tchebycheff_mixing)
- [4 IMIX=4: Broyden's 2^(nd) method and Pulay-mixing method
  (default)](#IMIX=4:_Broyden's_2nd_method_and_Pulay-mixing_method_(default))
- [5 Related tags and articles](#Related_tags_and_articles)
- [6 References](#References)

## IMIX=0: No mixing
$\rho_{\rm mix}=\rho_{\rm out}\\$

## IMIX=1: Kerker mixing
For Kerker mixing^([\[1\]](#cite_note-kerker:prb:81-1)), the mixed
density is given by

$\rho_{\rm mix}\left(G\right)=\rho_{\rm
in}\left(G\right)+A \frac{G^2}{G^2+B^2}\Bigl(\rho_{\rm
out}\left(G\right)-\rho_{\rm in}\left(G\right)\Bigr)$

with $A$=[AMIX](AMIX.md) and
$B$=[BMIX](BMIX.md). If
[BMIX](BMIX.md) is very small, e.g.,
[BMIX](BMIX.md)=0.0001, a straight mixing is obtained.

|  |
|----|
| **Mind:** [BMIX](BMIX.md)=0 might cause floating-point exceptions on some platforms. |

## IMIX=2: Variant of Tchebycheff mixing
VASP uses a variant of the popular Tchebycheff-mixing
scheme^([\[2\]](#cite_note-akai:jpc:85-2)). Here, the following second
order equation of motion is used:

$\ddot{\rho}_{\rm in}\left(G\right) = 2\*A
\frac{G^2}{G^2+B^2}\Bigl(\rho_{\rm out}\left(G\right)-\rho_{\rm
in}\left(G\right)\Bigr)-\mu \dot{\rho}_{\rm in}\left(G\right)$

with $A$=[AMIX](AMIX.md),
$B$=[BMIX](BMIX.md), and
$\mu$=[AMIN](AMIN.md). A
velocity Verlet algorithm is used to integrate this equation. The
discretized equation reads:

$\dot{\rho}_{N+1/2} = \Bigl(\left(1-\mu/2\right)
\dot{\rho}_{N-1/2} + 2\*F_N \Bigr)/\left(1+\mu/2\right)$

where

$F\left(G\right)=A\frac{G^2}{G^2+B^2}
\Bigl(\rho_{\rm out}\left(G\right)-\rho_{\rm in}\left(G\right)\Bigr)$

and

$\rho_{N+1}=\rho_{N+1}+\dot{\rho}_{N+1/2}$,

where the index *N* is the electronic iteration, and *F* is the force
acting on the charge.

For [BMIX](BMIX.md)≈0, no model for the dielectric matrix is
used. For $\mu=2$ a simple straight
mixing is obtained. Therefore, $\mu=2$
corresponds to maximal damping, while $\mu=0$ implies no damping. To determine the optimal parameters for
$\mu$ and [AMIX](AMIX.md),
first converge to the ground state with the Pulay mixer (IMIX=4). Then,
search for the the eigenvalues of the charge-dielectric matrix in the
[OUTCAR](../output-files/OUTCAR.md) file at the last occurrence of

    eigenvalues of (default mixing * dielectric matrix)

The optimal parameters are then given by:

|  |  |  |
|----|----|----|
| [AMIX](AMIX.md) |  | $={\rm AMIX}({\rm as\\ used\\ in\\ Pulay\\ run})\*{\rm smallest\\ eigenvalue}$ |
| [AMIN](AMIN.md) |  | $=\mu=2\sqrt{{\rm smallest\\ eigenvalue}/{\rm largest\\ eigenvalue}}$ |

## IMIX=4: Broyden's 2^(nd) method and Pulay-mixing method (default)
For [WC](WC.md)=0, VASP uses Broyden's 2^(nd)
method,^([\[3\]](#cite_note-bluegel:thesis:88-3)[\[4\]](#cite_note-johnson:prb:88-4))
and, for [WC](WC.md)\>0, VASP uses Pulay-mixing
method^([\[5\]](#cite_note-pulay:cpl:80-5)).

The default is a Pulay mixer with an initial approximation for the
charge-dielectric function according to
Kerker^([\[1\]](#cite_note-kerker:prb:81-1))

$A\times\max\left(\frac{G^2}{G^2+B^2},A_{\rm
min}\right)$

where $A$=[AMIX](AMIX.md),
$B$=[BMIX](BMIX.md), and
$A_{\rm min}$=[AMIN](AMIN.md).

[AMIN](AMIN.md)=0.4 usually yields good convergence.
[AMIX](AMIX.md) strongly depends on the system, for instance,
it should be small, e.g., [AMIX](AMIX.md)= 0.02, for metals.

In the Broyden scheme, the functional form of the initial mixing matrix
is determined by [AMIX](AMIX.md) and [BMIX](BMIX.md)
or the [INIMIX](INIMIX.md) tag. The metric used in the
Broyden scheme is specified through [MIXPRE](MIXPRE.md).

## Related tags and articles
[INIMIX](INIMIX.md), [MAXMIX](MAXMIX.md),
[AMIX](AMIX.md), [BMIX](BMIX.md),
[AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md), [WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IMIX-_incategory-Examples)

## References
1.  ↑ ^([a](#cite_ref-kerker:prb:81_1-0))
    ^([b](#cite_ref-kerker:prb:81_1-1)) [G. P. Kerker, Phys. Rev. B 23,
    3082 (1981).](http://link.aps.org/doi/10.1103/PhysRevB.23.3082)
2.  [↑](#cite_ref-akai:jpc:85_2-0) [H. Akai and P.H. Dederichs, J. Phys.
    C 18 (1985).](http://dx.doi.org/10.1088/0022-3719/18/12/009)
3.  [↑](#cite_ref-bluegel:thesis:88_3-0) S. Blügel, PhD Thesis, RWTH
    Aachen (1988).
4.  [↑](#cite_ref-johnson:prb:88_4-0) [D. D. Johnson, Phys. Rev. B38,
    12807 (1988).](http://link.aps.org/doi/10.1103/PhysRevB.38.12807)
5.  [↑](#cite_ref-pulay:cpl:80_5-0) [P. Pulay, Chem. Phys. Lett. 73, 393
    (1980).](http://dx.doi.org/10.1016/0009-2614(80)80396-4)

------------------------------------------------------------------------
