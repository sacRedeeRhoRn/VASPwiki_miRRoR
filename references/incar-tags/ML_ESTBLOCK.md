<!-- Source: https://vasp.at/wiki/index.php/ML_ESTBLOCK | revid: 36276 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_ESTBLOCK


ML_ESTBLOCK = \[integer\]  
Default: **ML_ESTBLOCK** =
[ML_OUTBLOCK](ML_OUTBLOCK.md) 

Description: Calculation and output frequency of error estimates for
[ML_MODE](ML_MODE.md)=*RUN* computations.

------------------------------------------------------------------------

|  |
|----|
| **Warning:** This tag was previously called ML_IERR in VASP versions 6.5.0 and earlier. Since VASP 6.5.1, ML_ESTBLOCK is the official variant (although ML_IERR is still supported for compatibility reasons). |

This tag sets the interval in units of molecular-dynamics steps at which
the error estimates are written to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md). The error estimate is
computed by utilizing the [spilling
factor](../methods/Machine_learning_force_field-_Theory.md)
if a refit with [ML_MODE](ML_MODE.md)=*REFIT* was done. The
[spilling
factor](../methods/Machine_learning_force_field-_Theory.md)
is calculated for each atom in the current structure and the maximum
among all atoms is written to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md) file marked with `SFF`.

The [spilling
factor](../methods/Machine_learning_force_field-_Theory.md)
measures the similarity of the local environment of each atom in the
current structure to that of the local reference configurations of the
force field. The values of the spilling factor are in the range
$\[0,1\]$. If the atomic environment is "properly"
represented by the local reference configurations the spilling factor
approaches 0. Vice versa the [spilling
factor](../methods/Machine_learning_force_field-_Theory.md)
quickly approaches 1, if the force field is extrapolating.

The calculation of the spilling factor scales quadratically with the
number of local reference configurations and linearly with the number of
species. For force fields containing many species and/or local reference
configurations, the evaluation time of the spilling factor becomes of
the order of the evaluation of a single force field step or more. Since
it is sufficient to monitor the error every
ML_ESTBLOCK MD steps, the
total time consumed by the evaluation of the spilling factor can become
insignificantly compared to the total time.

In long molecular dynamics calculations, we recommend to use at least
ML_ESTBLOCK=20-100.

ML_ESTBLOCK=0 turns off the
calculation of the spilling factor.

ML_ESTBLOCK can be freely
chosen only if [ML_MODE](ML_MODE.md)=*RUN*. In any other
calculation mode, if
ML_ESTBLOCK is not equal to 1,
the code will exit with an error and provide an error description.

For calculations using force fields obtained by
[ML_MODE](ML_MODE.md)=*REFITBAYESIAN* or without any
refitting, the Bayesian error estimates of energy, forces and stress
(`BEFF`) are additionally written out to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md) file and their output
frequency is also controlled by
ML_ESTBLOCK. Albeit having the
advantage of an additional error estimate we still do not recommend
using these force fields, since they are significantly slower than force
fields obtained by [ML_MODE](ML_MODE.md)=*REFIT*.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_ESTBLOCK&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_LFAST](ML_LFAST.md),
[ML_OUTBLOCK](ML_OUTBLOCK.md),
[ML_OUTPUT_MODE](ML_OUTPUT_MODE.md),
[ML_CALGO](ML_CALGO.md)

------------------------------------------------------------------------


