<!-- Source: https://vasp.at/wiki/index.php/OFIELD_KAPPA | revid: 35868 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# OFIELD_KAPPA
OFIELD_KAPPA = \[real\] 

Description: The tag OFIELD_KAPPA sets the strength of the bias
potential in the [Interface
pinning](../categories/Category-Interface_pinning.md)
method.

------------------------------------------------------------------------

The bias potential in the [Interface
pinning](../categories/Category-Interface_pinning.md)
method is written as

$U_\text{bias}(\mathbf{R}) = \frac\kappa2
\left(Q_6(\mathbf{R}) - A\right)^2$.

The tag OFIELD_KAPPA method sets the strength of the bias potential
$\kappa$. The unit of
$\kappa$ is $\textrm{eV}/(\textrm{unit} \\\\ \textrm{ of }\\\\ Q)^2$.

## Related tags and articles
[Interface
pinning](../categories/Category-Interface_pinning.md),
[OFIELD_Q6_NEAR](OFIELD_Q6_NEAR.md),
[OFIELD_Q6_FAR](OFIELD_Q6_FAR.md),
[OFIELD_A](OFIELD_A.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-OFIELD_KAPPA-_incategory-Examples)

------------------------------------------------------------------------
