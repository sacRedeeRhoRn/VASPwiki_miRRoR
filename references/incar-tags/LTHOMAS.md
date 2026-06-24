<!-- Source: https://vasp.at/wiki/index.php/LTHOMAS | revid: 34304 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTHOMAS
LTHOMAS = .TRUE. \| .FALSE.  
Default: **LTHOMAS** = .FALSE. 

Description: LTHOMAS selects a decomposition of the exchange functional
based on Thomas-Fermi exponential screening.

------------------------------------------------------------------------

If LTHOMAS=.TRUE. the decomposition of the exchange operator (in a
[range-separated hybrid
functional](../methods/Hybrid_functionals-_formalism.md))
into a short range (SR) and a long range (LR) part will be based on
Thomas-Fermi exponential screening:

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a_{\mathrm{SR}}
E_{\mathrm{x,SR}}^{\mathrm{HF}}(\mu) +
(1-a_{\mathrm{SR}})E_{\mathrm{x,SR}}^{\mathrm{SL}}(\mu) +
E_{\mathrm{x,LR}}^{\mathrm{SL}}(\mu) + E_{\mathrm{c}}^{\mathrm{SL}}$

The mixing $a_{\mathrm{SR}}$ and
screening $\mu=k_{\rm TF}$ are
controlled by the [AEXX](AEXX.md) and
[HFSCREEN](HFSCREEN.md) tags, respectively.

For typical semiconductors, a Thomas-Fermi screening length
$k_{\rm TF}$ of about 1.8 Å⁻¹ yields
reasonable band gaps. In principle, however, the Thomas-Fermi screening
length depends on the valence-electron density. VASP determines
$k_{\rm TF}$ from the number of valence
electrons (read from the [POTCAR](../input-files/POTCAR.md) file) and the
volume (leading to an average density $\bar{n}$) and writes the corresponding value of $k_{\rm TF}=\sqrt{4\bar{k}_{\rm F}/\pi}$, where
$\bar{k}_{\rm F}=(3\pi^2\bar{n})^{1/3}$
to the [OUTCAR](../output-files/OUTCAR.md) file (**note that this value is
only printed for information and is not used during the calculation**):

     Thomas-Fermi vector in A             =   2.00000

The setting of the sX-LDA functional is shown on the [page listing the
hybrid
functionals](../methods/List_of_hybrid_functionals.md).

[TABLE]

[TABLE]

Since VASP counts the semi-core states and *d*-states as valence
electrons, although these states do not contribute to the screening, the
values reported by VASP are often not recommended.

Another important detail concerns the implementation of the local LDA
part in VASP. Literature \[see Eqs. (3.10), (3.14), and (3.15) in Ref.
^([\[1\]](#cite_note-seidl:prb:96-1))\] suggests to use in the
enhancement factor $F(z)$ a
position-independent variable $z=k_{\rm
TF}/\bar{k}_{\rm F}$ where $\bar{k}_{\rm F}$ is as defined above but using the average
density $\bar{n}$ in the unit cell.
However, implemented in VASP is a position-dependent variable
$z({\bf r})=k_{\rm TF}/k_{\rm F}({\bf r})$, where $k_{\rm F}({\bf r})=(3\pi^2
n({\bf r}))^{1/3}$ is the Fermi wave vector calculated with
the local density $n({\bf r})$, while
the constant $k_{\rm TF}$ is set by
[HFSCREEN](HFSCREEN.md).

## Related tags and articles
[LHFCALC](LHFCALC.md),
[HFSCREEN](HFSCREEN.md), [AEXX](AEXX.md),
[LMODELHF](LMODELHF.md),
[LRHFCALC](LRHFCALC.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LTHOMAS-_incategory-Examples)

------------------------------------------------------------------------

1.  [↑](#cite_ref-seidl:prb:96_1-0) [A. Seidl, A. Görling, P. Vogl, J.A.
    Majewski, and M. Levy, Phys. Rev. B **53**, 3764
    (1996).](https://doi.org/10.1103/PhysRevB.53.3764)
