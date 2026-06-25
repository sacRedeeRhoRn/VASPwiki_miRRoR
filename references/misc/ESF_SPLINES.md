<!-- Source: https://vasp.at/wiki/index.php/ESF_SPLINES | revid: 27629 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ESF_SPLINES


ESF_SPLINES = .FALSE. \|
.TRUE.  
Default: **ESF_SPLINES** = .FALSE. 

Description: Enable k-point interpolation of the electronic structure
factor using tricubic splines in [ACFDT/RPA
calculations](../methods/ACFDT__RPA_calculations.md).

------------------------------------------------------------------------

With ESF_SPLINES =T, the
electronic structure factor (ESF) is interpolated using tricubic splines
to accelerate k-point convergence of the [RPA-correlation
energy](../methods/RPA__ACFDT-_Correlation_energy_in_the_Random_Phase_Approximation.md)
in [ACFDT/RPA
calculations](../methods/ACFDT__RPA_calculations.md).
The default settings of the maximum number of iteration steps
([ESF_NINTER](ESF_NINTER.md)) and convergence threshold
([ESF_CONV](ESF_CONV.md)) typically yield similar k-point
convergence compared to the k-p perturbation theory approach.

|  |
|----|
| **Tip:** By means of ESF interpolation, one can obtain the RPA-correlation energy for metals and insulators, in contrast to the k-p method that fails for metals. |


## Contents


- [1
  Algorithm](#algorithm)
- [2
  ESF-interpolation method vs k-p perturbation
  theory](#esf-interpolation-method-vs-k-p-perturbation-theory)
- [3
  Output](#output)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## Algorithm\[<a
href="/wiki/index.php?title=ESF_SPLINES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Algorithm">edit</a> \| (./index.php.md)\]

This feature follows the same idea as in coupled cluster
calculations.[^liao:jcp:2016-1]
To compute the RPA-correlation energy, the electronic structure factor
in the RPA

$S({\bf q}+{\bf G}) =\int {\rm d}\omega
\left\\(\mathrm{ln}\[1-\tilde\chi^0({\mathbf{q}},\mathrm{i}\omega)V({\mathbf{q}})\])_{{\mathbf{G,G}}}
+V_{{\mathbf{G,G}}}({\mathbf{q}})\tilde\chi^0({\mathbf{q}},{\mathrm{i}}\omega)
\right\\$

is evaluated on the k-point grid defined in
[KPOINTS](../input-files/KPOINTS.md) and the correlation energy (as its
trace) is
stored.[^gelbenegger:thesis2018-2]
To obtain the correlation energy on a finer k-point grid, more q-points
are added using tricubic spline interpolation. The resulting energy is
compared to the previous correlation energy. This procedure is repeated
[ESF_NINTER](ESF_NINTER.md) times or until the
difference in energy between the interpolation steps is less than
[ESF_CONV](ESF_CONV.md).

## ESF-interpolation method vs k-p perturbation theory\[<a
href="/wiki/index.php?title=ESF_SPLINES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: ESF-interpolation method vs k-p perturbation theory">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Warning:** Remove [WAVEDER](../input-files/WAVEDER.md) and avoid setting [LOPTICS](../incar-tags/LOPTICS.md)=T when running a job with ESF_SPLINES=T. |

Note that the ESF-interpolation method is incompatible with k-p
perturbation theory, where the largest q-point integration error

$\lim_{\bf q\to 0} \tilde\chi^0_{{\bf G G}'}({\bf q},{\rm i}\omega)
\cdot {\bf V}_{\bf G G'}({\bf q})$

is added explicitly to the RPA integral. The long-wave limit is
ill-defined for metallic systems; hence, the k-p method fails for
metals. For the k-p method, the long-wave contribution is stored in the
[WAVEDER](../input-files/WAVEDER.md) file, and VASP assumes you want to
add this term if the file is present in the working directory.

## Output\[<a
href="/wiki/index.php?title=ESF_SPLINES&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The result of the ESF interpolation is reported to the
[OUTCAR](../output-files/OUTCAR.md) file in the following format

         cutoff energy     smooth cutoff   RPA   correlation   Hartree contr. to MP2  RPA spline-interp.
    -----------------------------------------------------------------------------------------------------
               166.667           133.333      -12.9738715106      -19.7255874374      -13.4968000908
               158.730           126.984      -12.8840657072      -19.6294580403      -13.4017404001
               151.172           120.937      -12.7775593388      -19.5151822998      -13.3005326847
               143.973           115.178      -12.6604147404      -19.3892142669      -13.1868498210
               137.117           109.694      -12.5530911576      -19.2733151174      -13.0861120393
               130.588           104.470      -12.4659186304      -19.1786165194      -12.9778587892
               124.369            99.495      -12.3690601643      -19.0725742983      -12.8709666989
               118.447            94.758      -12.2461267475      -18.9372318755      -12.7590723870
     linear regression    
     converged value                          -14.0340307585      -20.8751715586      -14.5828037654

The last column contains the result from the spline interpolation for
the selected energy cutoffs reported in the first column.

|  |
|----|
| **Mind:** Available as of VASP.6.5.0 |

## Related tags and articles\[<a
href="/wiki/index.php?title=ESF_SPLINES&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ESF_CONV](ESF_CONV.md),
[ESF_NINTER](ESF_NINTER.md),
[LOPTICS](../incar-tags/LOPTICS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ESF_SPLINES-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=ESF_SPLINES&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^liao:jcp:2016-1]: [K. Liao and A. Grueneis, J. Chem. Phys. **145**, 141102 (2016).](https://doi.org/10.1063/1.4964307)
[^gelbenegger:thesis2018-2]: [K. Gelbenegger, Thesis: Finite size corrections in the RPA (2018).](https://utheses.univie.ac.at/detail/47275#)
