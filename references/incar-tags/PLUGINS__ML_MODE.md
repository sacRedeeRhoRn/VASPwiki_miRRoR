<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/ML_MODE | revid: 34743 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/ML MODE
PLUGINS/ML_MODE = none \| run  
Default: **PLUGINS/ML_MODE** = none 

Description: String-based tag selecting operation mode for running
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md)
plugins.

------------------------------------------------------------------------

- `PLUGINS/ML_MODE`` = none` Forces and stress provided by the plugin
  are added to the ab-initio forces computed by VASP.
- `PLUGINS/ML_MODE`` = run` VASP skips the ab-initio calculation and
  uses the forces and stress of the plugin to replace the forces of
  VASP.

## Related tags and articles
[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/ML_OUTBLOCK](PLUGINS__ML_OUTBLOCK.md),
[PLUGINS/ML_OUTPUT_MODE](PLUGINS__ML_OUTPUT_MODE.md),
[PLUGINS/NEIGHBOR_CUTOFF](PLUGINS__NEIGHBOR_CUTOFF.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/ML_MODE-_incategory-Examples)
