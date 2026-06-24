<!-- Source: https://vasp.at/wiki/index.php/ML_OUTBLOCK | revid: 35213 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_OUTBLOCK
ML_OUTBLOCK = \[integer\] 

|  |  |  |
|----|----|----|
| Default: **ML_OUTBLOCK** | = 1 | if 0\<=[VCAIMAGES](VCAIMAGES.md)\<=1 and [ML_LMLFF](ML_LMLFF.md)=.FALSE. in one of the two images |
|  | = 10 | else |

Description: Output distance in number of steps for molecular-dynamics
simulations with machine-learned force fields in prediction-only mode
([`ML_MODE`](ML_MODE.md)` = run`).

|  |
|----|
| **Important:** This tag is only available as of VASP.6.4.0. Unfortunately, the implementation of this feature was incomplete before VASP.6.4.3. In VASP versions prior to 6.4.3 there was still substantial remaining per-time-step output, in particular in [vasprun.xml](../output-files/Vasprun.xml.md) and [vaspout.h5](../output-files/Vaspout.h5.md) (see table below). If possible, please use VASP.6.4.3 or higher for production runs with potentially large file output. |

------------------------------------------------------------------------

By default VASP writes all results at every molecular-dynamics step
(`ML_OUTBLOCK`` = 1`). However, this may become inefficient when running
long trajectories in production runs with a machine-learned force field
in prediction-only mode ([`ML_MODE`](ML_MODE.md)` = run`).
This is particularly true if the force field supports the fast execution
mode, i.e., refitting was performed with
[`ML_MODE`](ML_MODE.md)` = refit`. Then, depending on the
system size, writing output each time step may hinder performance, cause
heavy I/O load and create unnecessary large files. In order to
circumvent these problems `ML_OUTBLOCK`` = n` instructs VASP to write
screen and file output only every `n` time steps.

In order to further increase the efficiency, calculation and output of
pair-correlation functions can be completely switched off by setting
[`ML_OUTPUT_MODE`](ML_OUTPUT_MODE.md)` = 0`.

|  |
|----|
| **Warning:** This tag will potentially override defaults and [INCAR](../input-files/INCAR.md) values of [NBLOCK](NBLOCK.md)! [NBLOCK](NBLOCK.md) will be automatically set to the maximum of ML_OUTBLOCK and [NBLOCK](NBLOCK.md). |

A comparison of the effects of [NBLOCK](NBLOCK.md) and
ML_OUTBLOCK on the output frequency of different files/properties is
given in the following table. Here, "yes" means the output will only be
written in the interval in time steps given by the tag value. On the
other hand, "no" indicates that the output will be written every time
step regardless of the tag value.

|  |  |  |  |
|----|----|----|----|
| Output file/property | [NBLOCK](NBLOCK.md) | ML_OUTBLOCK |  |
|  |  | ≤ 6.4.2 | ≥ 6.4.3 |
| screen output | no | yes | yes |
| [OSZICAR](../output-files/OSZICAR.md) | no | yes | yes |
| [OUTCAR](../output-files/OUTCAR.md) |  |  |  |
|   ↳ energies and time | no | no | yes |
|   ↳ forces and stress | yes | yes | yes |
| [CONTCAR](../output-files/CONTCAR.md) | no | yes | yes |
| [XDATCAR](../output-files/XDATCAR.md) | yes | yes | yes |
| [PCDAT](../output-files/PCDAT.md) ⁽¹⁾ | yes | yes | yes |
| [REPORT](../output-files/REPORT.md) | yes | yes | yes |
| [ML_LOGFILE](../output-files/ML_LOGFILE.md) | no | yes | yes |
| [ML_HEAT](../output-files/ML_HEAT.md) | no | no | yes |
| [ML_EATOM](../output-files/ML_EATOM.md) | no | no | yes |
| [vasprun.xml](../output-files/Vasprun.xml.md) |  |  |  |
|   ↳ energy | no | no | yes |
|   ↳ forces ⁽¹⁾ | no | no | yes |
|   ↳ stress ⁽¹⁾ | no | no | yes |
|   ↳ structure ⁽¹⁾ | no | no | yes |
|   ↳ time | no | no | yes |
| [vaspout.h5](../output-files/Vaspout.h5.md) |  |  |  |
|   ↳ energies | no | no⁽²⁾ | yes |
|   ↳ forces | no | no⁽²⁾ | yes |
|   ↳ stress | no | no⁽²⁾ | yes |
|   ↳ position_ions | yes | yes | yes |
|   ↳ lattice_vectors | yes | yes | yes |
|   ↳ ion_velocities | yes | yes | yes |
|   ↳ pair_correlation ⁽¹⁾ | yes | yes | yes |

[INCAR](../input-files/INCAR.md) tag controls output frequency: yes/no

\(1\) [`ML_OUTPUT_MODE`](ML_OUTPUT_MODE.md)` = 0`
can disable output completely

\(2\) Zeros are written for intermediate steps

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md),
[ML_LFAST](ML_LFAST.md),
[ML_ESTBLOCK](ML_ESTBLOCK.md),
[ML_OUTPUT_MODE](ML_OUTPUT_MODE.md),
[NBLOCK](NBLOCK.md)

------------------------------------------------------------------------
