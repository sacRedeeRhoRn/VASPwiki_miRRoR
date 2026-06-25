<!-- Source: https://vasp.at/wiki/index.php/Blue_moon_ensemble_calculations | revid: 36245 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Blue moon ensemble calculations


The information needed to determine the blue moon ensemble averages
within a [Constrained molecular
dynamics](../categories/Category-Constrained_molecular_dynamics.md)
can be obtained by setting [LBLUEOUT](../incar-tags/LBLUEOUT.md)=.TRUE.,
cf. [blue moon ensemble](../theory/Blue_moon_ensemble.md)
for details of the theory. The following output is written for each MD
step in the file [REPORT](../output-files/REPORT.md):

    >Blue_moon
           lambda        |z|^(-1/2)    GkT           |z|^(-1/2)*(lambda+GkT)
      b_m>  0.585916E+01  0.215200E+02 -0.117679E+00  0.123556E+03

  
with the four numerical terms indicating $\lambda_{\xi_k}$, $|Z|^{-1/2}$, $\left ( \frac{k_B T}{2 |Z|}
\sum_{j=1}^{r}(Z^{-1})_{kj} \sum_{i=1}^{3N} m_i^{-1}\nabla_i \xi_j
\cdot \nabla_i |Z| \right )$, and
$\left ( |Z|^{-1/2} \[\lambda_k +\frac{k_B T}{2 |Z|}
\sum_{j=1}^{r}(Z^{-1})_{kj} \sum_{i=1}^{3N} m_i^{-1}\nabla_i \xi_j
\cdot \nabla_i |Z|\] \right )$, respectively.

  

|  |
|----|
| **Mind:** $\left ( \frac{1}{2 |Z|} \sum_{j=1}^{r}(Z^{-1})_{kj} \sum_{i=1}^{3N} m_i^{-1}\nabla_i \xi_j \cdot \nabla_i |Z| \right )$ is defined as $G$ in the [REPORT](../output-files/REPORT.md) file. This is an arbitrary character and has no relation to Green's functions, reciprocal lattice vectors, etc. |

Note that one line introduced by the string 'b_m\>' is written for each
constrained coordinate. With this output, the free energy gradient with
respect to the fixed coordinate ${\xi_k}$ can
conveniently be determined (by the equation given above) as a ratio
between averages of the last and the second numerical terms. In the
simplest case when only one constraint is used, the free energy gradient
can be obtained as follows:

    grep b_m REPORT |awk 'BEGIN {a=0.;b=0.} {a+=$5;b+=$3} END {print a/b}'

As an example of a blue moon ensemble average, let us consider the
calculation of an unbiased potential energy average from constrained MD.
For simplicity, only a single constraint is assumed. Here we extract
$|Z|^{-1/2}$ for each step and store the data in an
auxiliary file zet.dat:

    grep b_m REPORT |awk '{print $3}' > zet.dat

Here we extract potential energy for each step and store the data in an
auxiliary file energy.dat:

    grep e_b REPORT |awk '{print $3}' > energy.dat

Finally, the weighted average is determined according to the first
formula shown above:

    paste energy.dat zet.dat |awk 'BEGIN {a=0.;b=0.} {a+=$1*$2;b+=$2} END {print a/b}'

## Related tags and articles\[<a
href="/wiki/index.php?title=Blue_moon_ensemble_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Blue moon ensemble](../theory/Blue_moon_ensemble.md)


