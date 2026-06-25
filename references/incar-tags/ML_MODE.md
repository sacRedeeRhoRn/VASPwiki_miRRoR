<!-- Source: https://vasp.at/wiki/index.php/ML_MODE | revid: 35233 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MODE


ML_MODE = train \| select \|
refit \| refitbayesian \| run \| delta \| none  
Default: **ML_MODE** = none 

Description: String-based tag selecting operation mode for machine
learning force fields.

|  |
|----|
| **Mind:** This tag is only available as of VASP.6.4.0. |

------------------------------------------------------------------------

This tag acts as a "super tag" and selects the operation mode by
selecting the defaults for all other tags. Every tag that is affected by
this "super tag" can be overwritten by the user by simply specifying the
value for that tag. The following options are available for this tag:

- `ML_MODE`` = train`**:
  On-the-fly training**

  Force predictions from the machine learning force field are used to
  drive the molecular dynamics (MD) simulation. However, if the error
  estimation performed in each time step indicates a high force error an
  ab initio calculation is performed instead and the collected energy,
  forces, and stress are used to improve the machine learning force
  field. There are two possible cases depending on, whether an
  [ML_AB](../input-files/ML_AB.md) is present in the calculation folder or
  not:

  1.  No [ML_AB](../input-files/ML_AB.md) file found:

      On-the-fly training is starting from scratch. Note that at the
      beginning of the MD run, when there is no force field available or
      it is still poorly trained, *ab initio* calculations will happen
      frequently. For VASP versions prior to 6.4.0 this corresponds to
      [`ML_ISTART`](ML_ISTART.md)` = 0`.

  2.  [ML_AB](../input-files/ML_AB.md) file present:

      Restart on-the-fly training from existing training database.
      Before the MD run starts the [ML_AB](../input-files/ML_AB.md) file (a
      copy of the [ML_ABN](../output-files/ML_ABN.md) from a previous
      training run!) is read and the *ab initio* data (energies, forces,
      and stresses) and local reference configurations it contains are
      used to generate an initial force field. Subsequently, the
      on-the-fly training MD is started. For VASP versions prior to
      6.4.0 this corresponds to
      [`ML_ISTART`](ML_ISTART.md)` = 1`.

      <table class="vasp-dark-link-panel"
      style="border: 0px solid var(--vblue); --box-emph-color: var(--vblue); padding: 5px; color: var(--vdefault-text-nb); background: var(--vblue-bg)">
      <colgroup>
      <col style="width: 100%" />
      </colgroup>
      <tbody>
      <tr>
      <td><strong><span style="color: var(--vblue);">Tip:</span></strong> None
      of the structures in the <a href="/wiki/ML_AB" title="ML AB">ML_AB</a>
      file need to match he <a href="/wiki/POSCAR" title="POSCAR">POSCAR</a>
      file for the current MD training run in terms of the simulation box,
      elements, or number of atoms. However, if the same elements appear the
      initial force field is used for predictions in the current MD run.
      <p>The training data contained in the <a href="/wiki/ML_AB"
      title="ML AB">ML_AB</a> file is included in the final machine learning
      force field, i.e., the <a href="/wiki/ML_FFN" title="ML FFN">ML_FFN</a>
      file will define a force field applicable to both the structures on the
      <a href="/wiki/ML_AB" title="ML AB">ML_AB</a> file as well as to the
      current MD simulation. This means that by restarting repeatedly with
      <span class="mw-selflink selflink"><code class="vasp-dark-link-panel"
      style="padding: 2px">ML_MODE</code></span><code
      class="vasp-dark-link-panel" style="padding: 2px"> = train</code>, and
      copying the <a href="/wiki/ML_ABN" title="ML ABN">ML_ABN</a> file from
      the previous run to <a href="/wiki/ML_AB" title="ML AB">ML_AB</a>(!), it
      is possible to iteratively extend the applicability of the a machine
      learning force field, e.g., by exploring different temperature ranges or
      element compositions.</p></td>
      </tr>
      </tbody>
      </table>

    

- `ML_MODE`` = select`**:
  Re-selection of local reference configurations**

  A new machine learning force field is generated from the *ab initio*
  data provided in the [ML_AB](../input-files/ML_AB.md) file. The structures
  are read and processed one by one as if harvested in an MD simulation.
  In other words, the same steps are performed as in on-the-fly training
  but the source of the data are not actual *ab initio* calculations in
  an MD run but the series of structures available in the
  [ML_AB](../input-files/ML_AB.md) file. The list of local reference
  configurations on the [ML_AB](../input-files/ML_AB.md) file will be
  ignored. Instead a new collection of local reference configurations is
  determined and written to the resulting
  [ML_ABN](../output-files/ML_ABN.md) file.

  |  |
  |----|
  | **Important:** This operation mode allows to generate a VASP machine learning force field from pre-computed or external *ab initio* data sets. In contrast to `ML_MODE`` = refit` also the local reference configurations are selected from the entire data set. For example, an [ML_AB](../input-files/ML_AB.md) file created manually by extracting *ab initio* data (energies, forces, stresses) from [OUTCAR](../output-files/OUTCAR.md) files (or even other external sources) can be processed in this mode without prior knowledge of local reference configurations (only a dummy section must be added to the [ML_AB](../input-files/ML_AB.md) file, see its documentation). Similar to on-the-fly training this mode generates [ML_FFN](../output-files/ML_FFN.md) files and [ML_ABN](../output-files/ML_ABN.md) **with** local reference configurations. |

  A new iteration through the training structures can lead to a frequent
  update of the force field. This is quite time-consuming. Hence, for
  this mode the default value of [ML_CDOUB](ML_CDOUB.md)
  is automatically increased from 2 to 4 which will result in a much
  less frequent update of the force field. This leads to much more
  efficient calculations while practically not changing the results.

  |  |
  |----|
  | **Tip:** If calculations for `ML_MODE`` = select` are too time-consuming, it is useful to increase [ML_MCONF_NEW](ML_MCONF_NEW.md) to values around 10-16. Together with [`ML_CDOUB`](ML_CDOUB.md)` = 4`, this often accelerates the calculations by a factor of 2-4. |

  The [ML_AB](../input-files/ML_AB.md) file may contain values for `CTIFOR`
  for each training structure. These are the thresholds used to sample
  that structure from the previous training. The thresholds found on the
  [ML_AB](../input-files/ML_AB.md) will be re-used unless a threshold is
  explicitly specified in the [INCAR](../input-files/INCAR.md) file, by
  means of the [ML_CTIFOR](ML_CTIFOR.md) tag. In the
  latter case the thresholds from the [ML_AB](../input-files/ML_AB.md) file
  are ignored. In case the [ML_AB](../input-files/ML_AB.md) contains **no**
  `CTIFOR` information and **no** threshold is specified in the
  [INCAR](../input-files/INCAR.md) file, the default value for
  [ML_CTIFOR](ML_CTIFOR.md) is used.

  This mode automatically sets [`NSW`](NSW.md)` = 1` and
  [`ML_CDOUB`](ML_CDOUB.md)` = 4`.For VASP versions prior
  to 6.4.0 this corresponds to
  [`ML_ISTART`](ML_ISTART.md)` = 3`.

  |  |
  |----|
  | **Warning:** `ML_MODE`` = select` ignores the structure in the [POSCAR](../input-files/POSCAR.md) and hence no error, force and stress predictions are made at the end of this calculation (instead zeros are written to stdout, [OSZICAR](../output-files/OSZICAR.md) and [OUTCAR](../output-files/OUTCAR.md)). |

    

- `ML_MODE`` = refit`**: Refit
  a force field for "fast" evaluation**

  Similar to
  `ML_MODE`` = select`,
  refitting is done based on an existing [ML_AB](../input-files/ML_AB.md)
  file, but the number of local reference configurations for each
  species is taken from the [ML_AB](../input-files/ML_AB.md) file.
  Sparsification is performed on the local reference configurations, so
  the resulting [ML_ABN](../output-files/ML_ABN.md) file will contain the
  same number or fewer local reference configurations than the
  [ML_AB](../input-files/ML_AB.md) file.

  By default the resulting force field is geared towards "fast"
  evaluation to speed up production runs
  ([`ML_LFAST`](ML_LFAST.md)` = .TRUE.`). This comes at
  the cost of not being able to evaluate Bayesian error estimates.

  |  |
  |----|
  | **Warning:** We strongly advise to use `ML_MODE`` = refit` if no Bayesian error estimates are required during production runs. |

  This mode automatically sets
  [`ML_LFAST`](ML_LFAST.md)` = .TRUE.`,
  [`NSW`](NSW.md)` = 1`,
  [`ML_IALGO_LINREG`](ML_IALGO_LINREG.md)` = 4`,
  [`ML_SIGW0`](ML_SIGW0.md)` = 1E-7`,
  [`ML_SIGV0`](ML_SIGV0.md)` = 1` and
  [`ML_EPS_LOW`](ML_EPS_LOW.md)` = 1E-11`. For VASP
  versions prior to 6.4.0 this corresponds to
  [`ML_ISTART`](ML_ISTART.md)` = 4`.

    

- `ML_MODE`` = refitbayesian`**:
  Refit a force field with Bayesian regression (deprecated)**

  Same as `ML_MODE`` = refit`,
  but Bayesian regression is employed. This results in lower accuracy
  and much slower force fields than using
  `ML_MODE`` = refit` and
  should be used with caution. On the other hand, this mode allows the
  generation of [ML_FFN](../output-files/ML_FFN.md) files that can calculate
  Bayesian error estimates in addition to predictions.

  This modes sets [`NSW`](NSW.md)` = 1`,
  [`ML_IALGO_LINREG`](ML_IALGO_LINREG.md)` = 1` and
  [`ML_LFAST`](ML_LFAST.md)` = .FALSE.`. For VASP versions
  prior to 6.4.0 this corresponds to
  [`ML_ISTART`](ML_ISTART.md)` = 4`.

    

- `ML_MODE`` = run`**: Perform
  only force field predictions**

  A previously trained machine learning force field is read from the
  [ML_FF](../input-files/ML_FF.md) file, and the MD simulation is driven
  with predictions from the force field only. **No** *ab initio*
  calculations are performed and **no** learning is executed. This
  setting is typically used when the machine learning force field is
  considered mature and ready for production runs.

  Optionally, if the force field was refitted using
  `ML_MODE`` = refitbayesian`,
  the Bayesian error estimate of the energies, forces, and stress can be
  computed and logged in the
  [ML_LOGFILE](../output-files/ML_LOGFILE.md). The output frequency of
  the Bayesian errors can be set via the
  <a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>
  tag, the default is 0.

  For VASP versions prior to 6.4.0 this corresponds to
  [`ML_ISTART`](ML_ISTART.md)` = 2`.

- `ML_MODE`` = delta`**:
  Performs ab-initio calcutions and force field predictions**

  A previously trained machine learning force field is read from the
  [ML_FF](../input-files/ML_FF.md) file, and the MD simulation is driven by
  the sum of *ab initio* forces and machine learning predictions. The
  machine learning force field ideally has been trained to predict the
  difference between two levels of *ab initio* theory — referred to as
  the target and reference levels — so that the combined result
  approximates the target level of theory at the computational cost of
  the reference level. Typical use cases include correcting a low-cost
  exchange-correlation functional (e.g., PBE) toward a higher-accuracy
  one (e.g., a hybrid functional such as HSE06), or bridging differences
  in k-mesh density, plane-wave energy cutoff, or other convergence
  parameters. In this way, near-hybrid accuracy can be achieved at a
  cost approaching that of a semi-local DFT calculation.

  This mode is available for VASP version 6.6.0 or higher.

    

- `ML_MODE`` = none`**: The
  tag is ignored**

  

|  |
|----|
| **Warning:** If any option other than the above is chosen or there is a spelling error (be careful to write everything in upper case or lower case letters) the code will exit with an error. |

|  |
|----|
| **Tip:** Some choices of ML_MODE will automatically set other machine-learned force field tags. However, it is still possible to overwrite the defaults by specifying the corresponding tags in the [INCAR](../input-files/INCAR.md) file. |

## Related tags and articles\[<a href="/wiki/index.php?title=ML_MODE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_ISTART](ML_ISTART.md),
[ML_LFAST](ML_LFAST.md),
<a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>,
[ML_OUTBLOCK](ML_OUTBLOCK.md),
[ML_OUTPUT_MODE](ML_OUTPUT_MODE.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_CDOUB](ML_CDOUB.md),
[ML_CTIFOR](ML_CTIFOR.md),
<a href="/wiki/ML_IERR" class="mw-redirect" title="ML IERR">ML_IERR</a>

------------------------------------------------------------------------


