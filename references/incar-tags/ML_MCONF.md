<!-- Source: https://vasp.at/wiki/index.php/ML_MCONF | revid: 20334 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MCONF
ML_MCONF = \[integer\]  
Default: **ML_MCONF** = see below 

Description: This tag sets the maximum number of structures stored in
memory that are used for training in the machine learning force field
method.

------------------------------------------------------------------------

The defaults for ML_MCONF are different for each different
[ML_MODE](ML_MODE.md) setting. Here are the defaults for
each mode:

- [ML_MODE](ML_MODE.md)='TRAIN':
  - No [ML_AB](../input-files/ML_AB.md) present (learning from scratch):
    min(1500, max(1,[NSW](NSW.md)))
  - [ML_AB](../input-files/ML_AB.md) present (continuation of learning):
    MCONF_AB + min(1500, max(1,[NSW](NSW.md)))
- [ML_MODE](ML_MODE.md)='SELECT': MCONF_AB + 1
- [ML_MODE](ML_MODE.md)='REFIT': MCONF_AB + 1
- [ML_MODE](ML_MODE.md)='REFITBAYESIAN': MCONF_AB + 1
- [ML_MODE](ML_MODE.md)='RUN': 1

using the following definition:

- MCONF_AB = Number of training structures read from the
  [ML_AB](../input-files/ML_AB.md) file.

  
The default value for [ML_MODE](ML_MODE.md)=*TRAIN* is
usually a safe value for solids and easy-to-learn liquids but should be
set to a higher value as soon as it is reached. When this happens the
code stops and gives an error instructing to increase ML_MCONF.

This flag sets also the maximum number of rows for the design matrix,
which is usually a huge matrix. The design matrix is to be allocated
statically at the beginning of the program since several parts of the
code use MPI shared memory and dynamic reallocation of these arrays can
cause severe problems on some systems. So most of the main arrays are
statically allocated in the code.

An estimate of the design matrix and all other large arrays are printed
out to the [ML_LOGFILE](../output-files/ML_LOGFILE.md) before
allocation. The design matrix is fully distributed in a block cyclic
fashion for scaLAPACK and should almost perfectly linearly scale with
the number of used processors.

## Related tags and articles
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_FF_MCONF-_incategory-Examples)

------------------------------------------------------------------------

[ML_LMLFF](ML_LMLFF.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_MB](ML_MB.md)
