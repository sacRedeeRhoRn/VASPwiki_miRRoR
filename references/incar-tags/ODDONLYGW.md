<!-- Source: https://vasp.at/wiki/index.php/ODDONLYGW | revid: 18044 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ODDONLYGW
ODDONLYGW = \[logical\]  
Default: **ODDONLYGW** = .FALSE. 

Description: ODDONLYGW allows to avoid the inclusion of the
$\Gamma$ point in the evaluation of
response functions (in [GW
calculations](../redirects/GW_calculations.md)).

------------------------------------------------------------------------

The independent particle polarizability $\chi_{{\mathbf{q}}}^0 ({\mathbf{G}}, {\mathbf{G}}', \omega)$
is given by:

$\chi_{{\mathbf{q}}}^0 ({\mathbf{G}},
{\mathbf{G}}', \omega) = \frac{1}{\Omega} \sum_{n,n',{\mathbf{k}}}2
w_{{\mathbf{k}}} (f_{n'{\mathbf{k}}+{\mathbf{q}}} -
f_{n{\mathbf{k}}}) \times \frac{\langle \psi_{n{\mathbf{k}}}| e^{-i
({\mathbf{q}}+{\mathbf{G}}){\mathbf{r}}} |
\psi_{n'{\mathbf{k}}+{\mathbf{q}}}\rangle \langle
\psi_{n'{\mathbf{k}}+{\mathbf{q}}}| e^{i
({\mathbf{q}}+{\mathbf{G}}'){\mathbf{r'}}} |
\psi_{n{\mathbf{k}}}\rangle} {
\epsilon_{n'{\mathbf{k}}+{\mathbf{q}}}-\epsilon_{n{\mathbf{k}}} -
\omega - i \eta }$

If the $\Gamma$ point is included in the
summation over $\mathbf{k}$, convergence
is very slow for some materials (e.g. GaAs).

To deal with this problem the flag ODDONLYGW has been included. In the
automatic mode, the $\mathbf{k}$-grid is
given by (see Sec. \ref{sec:autok}):

    $\vec{k} = \vec{b}_{1} \frac{n_{1}}{N_{1}} + \vec{b}_{2} \frac{n_{2}}{N_{2}}  + \vec{b}_{3} \frac{n_{3}}{N_{3}} ,\qquad  n_1=0...,N_1-1 \quad  n_2=0...,N_2-1 \quad  n_3=0...,N_3-1.$

## Related tags and articles
[EVENONLYGW](EVENONLYGW.md), [GW
calculations](../redirects/GW_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ODDONLYGW-_incategory-Examples)

------------------------------------------------------------------------
