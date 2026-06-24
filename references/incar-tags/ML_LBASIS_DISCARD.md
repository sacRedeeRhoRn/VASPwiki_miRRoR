<!-- Source: https://vasp.at/wiki/index.php/ML_LBASIS_DISCARD | revid: 26476 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_LBASIS_DISCARD
ML_LBASIS_DISCARD = \[logical\]  
Default: **ML_LBASIS_DISCARD** = .TRUE. 

Description: Controls whether calculation is continued or stopped after
the maximum number of local reference configurations
[ML_MB](ML_MB.md) for a given species is reached.

------------------------------------------------------------------------

For ML_LBASIS_DISCARD=.FALSE., whenever the number of local reference
configurations for a given species would exceed the maximum number of
allowed configurations [ML_MB](ML_MB.md), the code will
terminate (soft exit) and request the user to continue with and
increased number for [ML_MB](ML_MB.md).

For ML_LBASIS_DISCARD=.TRUE. (default) the code will not stop, when the
number of local reference configurations for a given species would
exceed the maximum, but old configurations may be replaced by new ones.

In multi-component systems it can happen that, although
[ML_MB](ML_MB.md) is set to the maximum that is
computationally affordable, one species exceeds
[ML_MB](ML_MB.md) while the other species are not
sufficiently sampled and still far below [ML_MB](ML_MB.md).
For that ML_LBASIS_DISCARD=.TRUE. should be set. In that case the fast
sampled species would retain the same number of local reference
configurations and the new local reference configurations would replace
old ones. At the same time new local reference configurations could be
added for the slowly-sampled species further improving their accuracy
for fitting.

  

## Related tags and articles
[ML_LMLFF](ML_LMLFF.md), [ML_MB](ML_MB.md),
[ML_MCONF](ML_MCONF.md),
[ML_EPS_LOW](ML_EPS_LOW.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_LBASIS_DISCARD-_incategory-Examples)
