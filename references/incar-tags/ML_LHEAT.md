<!-- Source: https://vasp.at/wiki/index.php/ML_LHEAT | revid: 17626 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LHEAT


ML_LHEAT = \[logical\]  
Default: **ML_LHEAT** = .FALSE. 

Description: This tag specifies whether the heat flux is calculated or
not in the machine learning force field method.

------------------------------------------------------------------------

The heat flux within machine learning force fields is decomposed into
atomic contributions written as

$\mathbf{q}(t) = \sum\limits_{i=1}^{N_{a}} \frac{d}{dt} \left(
\mathbf{r}_{i} E_{i} \right),$

$E_{i}=\frac{m_{i} \left|\mathbf{v}_{i} \right|^{2}}{2} + U_{i}$

where $\mathbf{r}_{i}$, $\mathbf{v}_{i}$ and $E_{i}$
denote the position vector, velocity and energy of atom
$i$, respectively. The number of atoms in the system is
denoted by $N_{a}$. The
heat flux can be further rewritten as

$\mathbf{q}(t) = \sum\limits_{i=1}^{N_{a}} \mathbf{v}_{i} E_{i} +
\sum\limits_{i=1}^{N_{a}} \mathbf{r}_{i} \left( m_{i}
\mathbf{v}_{i} \cdot \frac{d\mathbf{v}_{i}}{dt} +
\sum\limits_{j=1}^{N_{a}} \mathbf{v}_{j} \cdot \nabla_{j} U_{i}
\right).$

Using the equation of motions

$m_{i} \frac{d \mathbf{v}_{i}}{dt} = - \sum\limits_{j=1}^{N_{a}}
\nabla_{i} U_{j}$

the heat flux can be simplified to

$\mathbf{q}(t) = \sum\limits_{i=1}^{N_{a}} \mathbf{v}_{i} E_{i} -
\sum\limits_{i=1}^{N_{a}} \sum\limits_{j=1}^{N_{a}} \mathbf{r}_{i}
\left( \mathbf{v}_{i} \cdot \nabla_{i} U_{j} \right) +
\sum\limits_{i=1}^{N_{a}} \sum\limits_{j=1}^{N_{a}} \mathbf{r}_{i}
\left( \mathbf{v}_{j} \cdot \nabla_{j} U_{i} \right) =
\sum\limits_{i=1}^{N_{a}} \mathbf{v}_{i} E_{i} +
\sum\limits_{i=1}^{N_{a}} \sum\limits_{j=1}^{N_{a}} \left(
\mathbf{r}_{i} - \mathbf{r}_{j} \right) \left( \mathbf{v}_{j} \cdot
\nabla_{j} U_{i} \right).$

Finally (in a post-processing step), the thermal conductivity at
temperature $T$ in the
Green-Kubo formalism can be calculated from the correlation of the heat
flux $\mathbf{q}$
as

$\kappa = \frac{1}{3Vk_{b}T^{2}} \int\limits_{0}^{\infty} \langle
\mathbf{q}(t) \cdot \mathbf{q}(0) \rangle dt,$

  
where $V$ and
$k_{b}$ denotes the volume of the system and the
Boltzmann constant, respectively.

  

The heat flux is written to the file [ML_HEAT](../output-files/ML_HEAT.md).

## Related tags and articles\[<a href="/wiki/index.php?title=ML_LHEAT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LEATOM](ML_LEATOM.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LHEAT-_incategory-Examples)

------------------------------------------------------------------------


