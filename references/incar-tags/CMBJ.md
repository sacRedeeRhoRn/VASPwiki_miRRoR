<!-- Source: https://vasp.at/wiki/index.php/CMBJ | revid: 29388 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CMBJ
CMBJ = \[real (array)\]  
Default: **CMBJ** = calculated self-consistently 

Description: defines the $c$ parameter
in the MBJ potential.

------------------------------------------------------------------------

The CMBJ tag can be set in the following ways:

- Specify a constant that is used at every point of space
  $\mathbf{r}$

      CMBJ = c

&nbsp;

- Specify one entry per atomic type

      CMBJ = c_1 c_2 .. c_n

  where the order and number $n$ is in
  accordance with atomic types in your [POSCAR](../input-files/POSCAR.md)
  file. The MBJ exchange potential at a point $\mathbf{r}$ will then be calculated using the parameter
  $c_{i}$ belonging to the atomic
  species of the atomic site nearest to $\mathbf{r}$.

If CMBJ is not set, $c$ is calculated at
each electronic step as the average of $\left\vert\nabla n\right\vert/n$ in the unit cell, as
explained in the description of the [METAGGA](METAGGA.md)
tag.

## Related tags and articles
[METAGGA](METAGGA.md), [CMBJA](CMBJA.md),
[CMBJB](CMBJB.md), [CMBJE](CMBJE.md),
[SMBJ](SMBJ.md), [RSMBJ](RSMBJ.md),
[LASPH](LASPH.md), [LMAXTAU](LMAXTAU.md),
[LMIXTAU](LMIXTAU.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CMBJ-_incategory-Examples)

## References
------------------------------------------------------------------------
