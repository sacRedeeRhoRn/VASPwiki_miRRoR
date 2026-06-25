<!-- Source: https://vasp.at/wiki/index.php/ML_LCOUPLE | revid: 35686 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LCOUPLE


ML_LCOUPLE = \[logical\] 

|  |  |  |
|----|----|----|
| Default: **ML_LCOUPLE** | = .TRUE. | if [ML_LEMPPOT](ML_LEMPPOT.md)=.TRUE. |
|  | = .FALSE. | otherwise |

Description: This tag specifies whether thermodynamic integration is
activated in order to calculate the chemical potentials within the
machine learning force field method.

------------------------------------------------------------------------

In thermodynamic integration a coupling parameter
$\lambda$ is introduced to the Hamiltonian to smoothly
switch between a "non-interacting" reference state and a
"fully-interacting" state. The change of the free energy along this path
is written as

$\Delta \mu = \int\limits_{0}^{1} \langle \frac{dH(\lambda)}{d\lambda}
\rangle_{\lambda} d\lambda.$

Using machine learning force fields the Hamiltonian can be written as

$H
(\lambda) = \sum\limits_{i=1}^{N_{a}}
\frac{|\mathbf{p}_{i}|^2}{2m_{i}} + \sum\limits_{i \notin M}
U_{i}(\lambda) + \lambda \sum\limits_{i \in M} U_{i}(\lambda) +
\sum\limits_{i}^{N_{a}} U_{i,\mathbf{atom}}.$

where $N_{a}$
denotes the number of atoms and $U_{i,\mathbf{atom}}$ is an atomic reference energy for a single non
interacting atom. The first term in the equation describes the potential
energy and the second and third term describe the potential energy of an
atom $i$. The index
$M$ denotes the atoms whose interaction is controlled by a
coupling parameter. The interactions of the atoms are controlled by
scaling the contributions to the atom density via the coupling parameter

$\rho (\mathbf{r},\lambda) = \sum\limits_{j\notin M} f_{\mathrm{cut}}
\left( \left| \mathbf{r}_{j} - \mathbf{r}_{i} \right| \right) g
\left\[ \mathbf{r} - \left( \mathbf{r}_{j} - \mathbf{r}_{i} \right)
\right\] + \lambda \sum\limits_{j\in M} f_{\mathrm{cut}} \left(
\left| \mathbf{r}_{j} - \mathbf{r}_{i} \right| \right) g \left\[
\mathbf{r} - \left( \mathbf{r}_{j} - \mathbf{r}_{i} \right) \right\].$

  
Further details on the implementation can be found in reference
<sup>[\[1\]](#cite_note-jinnouchiti:prb:2020-1)</sup>.

For thermodynamic integration the following parameters have to be set:

- [`ML_MODE`](ML_MODE.md)` = run`.
- `ML_LCOUPLE`` = .TRUE.`.
- The number of atoms for which a coupling parameter is introduced
  ($i \in M$):
  [ML_NATOM_COUPLED](ML_NATOM_COUPLED.md).
- The list of atom indices that for that the coupling parameter is
  applied in the interaction:
  [ML_ICOUPLE](ML_ICOUPLE.md).
- The strength of the coupling parameter $\lambda$
  between 0 and 1: [ML_RCOUPLE](ML_RCOUPLE.md).

The derivative of the hamiltonian with respect to the coupling constant
$dH/d\lambda$ is written out at every MD step to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md). A sample output should look
like this:

    # DCOUPLE ################################
    # DCOUPLE This line shows the derivative of the Hamiltonian with respect to coupling constant (dH/dlambda).
    # DCOUPLE 
    # DCOUPLE nstep .......... MD time step or input structure counter
    # DCOUPLE der_H_lambda ... dH/dlambda
    # DCOUPLE ################################
    # DCOUPLE           nstep     der_H_lambda
    # DCOUPLE               2                3
    # DCOUPLE ################################
    DCOUPLE                 1  -1.08332135E+01
    DCOUPLE                 2  -1.08132321E+01
    DCOUPLE                 3  -1.07631992E+01
    DCOUPLE                 4  -1.06786675E+01
    DCOUPLE                 5  -1.05493088E+01
    DCOUPLE                 6  -1.03561161E+01
    DCOUPLE                 7  -1.00762443E+01
    DCOUPLE                 8  -9.69961878E+00
    DCOUPLE                 9  -9.25531640E+00
    DCOUPLE                10  -8.82525354E+00
    ...

## References\[<a
href="/wiki/index.php?title=ML_LCOUPLE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-jinnouchiti:prb:2020_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.101.060201"
    class="external text" rel="nofollow">R. Jinnouchi, F. Karsai, and G.
    Kresse, Phys. Rev. B <strong>101</strong>, 060201 (2020).</a>


## Related tags and articles\[<a
href="/wiki/index.php?title=ML_LCOUPLE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_NATOM_COUPLED](ML_NATOM_COUPLED.md),
[ML_ICOUPLE](ML_ICOUPLE.md),
[ML_RCOUPLE](ML_RCOUPLE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LCOUPLE-_incategory-Examples)

------------------------------------------------------------------------


