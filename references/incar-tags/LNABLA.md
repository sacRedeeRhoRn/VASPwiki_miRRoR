<!-- Source: https://vasp.at/wiki/index.php/LNABLA | revid: 18255 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNABLA
LNABLA = .TRUE. \| .FALSE.  
Default: **LNABLA** = .FALSE. 

Description: LNABLA=.TRUE. evaluates the transversal expression for the
frequency dependent dielectric matrix.

------------------------------------------------------------------------

Usually VASP uses the [longitudinal expression for the frequency
dependent dielectric matrix](LOPTICS.md). It is
however possible to switch to the computationally somewhat simpler
transversal expressions by selecting LNABLA=.TRUE. (Eqs. 17 and 20 in
Ref.^([\[1\]](#cite_note-gajdos:prb:06-1))). In this simplification the
imaginary part of the macroscopic dielectric function is given by

$\epsilon^{(2)}_{\alpha \beta} (\omega) = \frac{4
\pi^2 e^2 \hbar^4}{\Omega \omega^2 m_e^2} \mathrm{lim}_{\mathbf{q}
\rightarrow 0} \sum_{c,v, \mathbf{k}} 2 w_\mathbf{k} \delta(
\epsilon_{c\mathbf{k+q}} - \epsilon_{v\mathbf{k}} - \omega) \times
\langle u_{c\mathbf{k}} | i{\mathbf{\nabla}_{\alpha} -
\mathbf{k}}_{\alpha} | u_{v\mathbf{k}} \rangle \langle
u_{c\mathbf{k}} | i{\mathbf{\nabla}_{\beta} - \mathbf{k}}_{\beta} |
u_{v\mathbf{k}} \rangle^\*.$

Except for the purpose of testing, there is however hardly ever a reason
to use the transversal expression, since it is less accurate.

## Related tags and articles
[LOPTICS](LOPTICS.md), [CSHIFT](CSHIFT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNABLA-_incategory-Examples)

## References
1.  [↑](#cite_ref-gajdos:prb:06_1-0) [M. Gajdoš, K. Hummer, G.
    Kresse, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 73, 045112
    (2006).](http://link.aps.org/doi/10.1103/PhysRevB.73.045112)

------------------------------------------------------------------------
