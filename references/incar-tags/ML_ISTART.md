<!-- Source: https://vasp.at/wiki/index.php/ML_ISTART | revid: 22174 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_ISTART
ML_ISTART = \[integer\]  
Default: **ML_ISTART** = 0 

|  |
|----|
| **Warning:** This tag is deprecated and we advise to use [ML_MODE](ML_MODE.md) instead. |

Description: This tag selects the mode of operation (e.g. start from
scratch, prediction-only,...) of the machine learning force fields
method.

------------------------------------------------------------------------

If the machine learning force fields method is enabled via
[ML_LMLFF](ML_LMLFF.md) = .TRUE., this tag further
specifies the mode of operation when VASP is run. The following cases
can be selected:

- ML_ISTART = 0: On-the-fly learning is enabled, starting from scratch.
  Force predictions from the machine learning force field are used to
  drive the MD simulation. However, if the error estimation performed in
  each time step indicates a high force error an ab initio calculation
  is performed instead and the collected energy, forces and stress are
  used to improve the machine learning force field. Setting ML_ISTART =
  0 starts the machine learning force field from scratch. Hence, in the
  beginning of the MD run there is no force field available and ab
  initio calculations will happen frequently.
- ML_ISTART = 1: Same as ML_ISTART = 0 but taking into account
  pre-existing ab initio data. This is the usual choice for continuing a
  previous MD simulation with activated machine learning. Before the MD
  run starts the [ML_AB](../input-files/ML_AB.md) file, copied from
  [ML_ABN](../output-files/ML_ABN.md) from a previous run, is read and the
  contained ab initio energies, forces and stresses are used to generate
  an initial force field. Note that this preparative learning step
  adopts the previous choice of local reference configurations, i.e. the
  reference atomic environments entering the kernel are taken from a
  list in the [ML_AB](../input-files/ML_AB.md) file. Then, the MD simulation
  is started with on-the-fly learning enabled. The
  [ML_AB](../input-files/ML_AB.md) file does not necessarily need to contain
  structures matching the current starting configuration in the
  [POSCAR](../input-files/POSCAR.md) file in terms of simulation box,
  present elements or number of atoms. However, if the same elements
  appear the initial force field is of course used for predictions. In
  any case the provided training data is included in the finally
  generated machine learning force field, i.e. the
  [ML_FFN](../output-files/ML_FFN.md) file will define a force field
  applicable to both, the structures in the [ML_AB](../input-files/ML_AB.md)
  file **and** the current MD simulation. By restarting repeatedly with
  ML_ISTART = 1 while providing an [ML_AB](../input-files/ML_AB.md) file
  from the last run it is possible to iteratively extend the
  applicability of the resulting machine learning force field, e.g. by
  exploring different temperature ranges or element compositions.

|  |
|----|
| **Tip:** Setting ML_ISTART = 1 together with [NSW](NSW.md) = 0 allows to repeat learning on the given training data and create a new force field in [ML_FFN](../output-files/ML_FFN.md) without actually performing additional MD steps. In this way force field parameters (e.g. cutoff radii, number of radial basis functions, etc.) can be varied without recalculating the entire trajectory. Moreover, because Bayesian error estimation is not required when no MD is run it is possible to switch the regression algorithm via the tag [ML_IALGO_LINREG](ML_IALGO_LINREG.md) and check whether in this way better fitting results can be achieved. In order to avoid that the starting structure in the [POSCAR](../input-files/POSCAR.md) file is processed and eventually added to the training data just set [ML_CTIFOR](ML_CTIFOR.md) to a large value (e.g. 1000). |

- ML_ISTART = 2: Prediction only. In this mode the previously trained
  machine learning force field is read from the
  [ML_FF](../input-files/ML_FF.md) file. The MD simulation is driven with
  predictions from the force field only, no ab initio calculations are
  performed and no learning is executed. However, in order to monitor
  the quality of predictions the Bayesian error estimate of forces is
  still computed and logged in the
  [ML_LOGFILE](../output-files/ML_LOGFILE.md). This setting is typically
  used when the machine learning force field is considered mature and
  ready for production runs.
- ML_ISTART = 3: Learning from given ab initio data only, no MD time
  steps. In this operation mode a new machine learning force field is
  generated from ab initio data provided in the
  [ML_AB](../input-files/ML_AB.md) file. The structures are read in and
  processed one by one as if harvested via an MD simulation. In other
  words, the same steps are performed as in on-the-fly training but the
  source of data is not an MD run but the series of structures available
  in [ML_AB](../input-files/ML_AB.md). This operation mode can be used to
  generate VASP machine learning force fields from pre-computed or
  external ab initio data sets. At first glance ML_ISTART = 3 looks very
  similar to the combination of ML_ISTART = 1 and [NSW](NSW.md)
  = 0 described above. However, there is an important difference:
  Setting ML_ISTART = 3 will ignore the list of local reference
  configurations in the [ML_AB](../input-files/ML_AB.md) file and instead
  will determine a new collection which is written to the resulting
  [ML_ABN](../output-files/ML_ABN.md) file.

|  |
|----|
| **Tip:** If calculations for ML_ISTART = 3 are too time-consuming using the default settings, it is useful to increase [ML_MCONF_NEW](ML_MCONF_NEW.md) to values around 10-16 and set [ML_CDOUB](ML_CDOUB.md) = 4. This often accelerates the calculations by a factor of 2-4. |

The [ML_AB](../input-files/ML_AB.md) file may contain values for *CTIFOR*
for each training structure. These are the thresholds used to sample
that structure from the previous training. If a value for
[ML_CTIFOR](ML_CTIFOR.md) is specified in the
[INCAR](../input-files/INCAR.md) file, that value is then used and the
thresholds from the [ML_AB](../input-files/ML_AB.md) are ignored.
Otherwise: 1) If thresholds exist in the [ML_AB](../input-files/ML_AB.md)
they are used. 2) If no thresholds are specified the default value for
[ML_CTIFOR](ML_CTIFOR.md) is used.

- ML_ISTART = 4: Refitting of the force field is done based on an
  existing [ML_AB](../input-files/ML_AB.md) file, but the number of local
  reference configurations is taken from the
  [ML_AB](../input-files/ML_AB.md) file. [NSW](NSW.md) on the input
  is ignored and only a single step is executed. No ab-initio
  calculation is carried out.

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md),
[ML_IALGO_LINREG](ML_IALGO_LINREG.md),
[ML_IWEIGHT](ML_IWEIGHT.md),
[ML_ICRITERIA](ML_ICRITERIA.md),
[ML_IREG](ML_IREG.md),
[ML_LSPARSDES](ML_LSPARSDES.md),
[ML_ISCALE_TOTEN](ML_ISCALE_TOTEN.md),
[ML_LCOUPLE](ML_LCOUPLE.md),
[ML_LHEAT](ML_LHEAT.md),
[ML_LEATOM](ML_LEATOM.md), [ML_MB](ML_MB.md),
[ML_MCONF](ML_MCONF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_ISTART-_incategory-Examples)

------------------------------------------------------------------------
