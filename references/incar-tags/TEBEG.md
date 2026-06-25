<!-- Source: https://vasp.at/wiki/index.php/TEBEG | revid: 32295 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TEBEG


TEBEG = \[real\]  
Default: **TEBEG** = 0 

Description: TEBEG sets the
starting temperature (in K) for an ab-initio molecular dynamics run
([IBRION](IBRION.md)=0) and other routines (e.g.
[Electron-phonon interactions from Monte-Carlo
sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md)).

------------------------------------------------------------------------

If no initial velocities are supplied on the
[POSCAR](../input-files/POSCAR.md) file, the velocities are set randomly
according to a Maxwell-Boltzmann distribution at the initial temperature
TEBEG. Velocities are only
used for molecular dynamics ([IBRION](IBRION.md)=0).

**Mind**: If [MDALGO](MDALGO.md)\>0 is used VASP defines the
temperature as

$T=
\frac{1}{ k_B T 3 (N_{\rm ions}-N_{\rm constraints})}
\sum\limits_{n}^{N_{\rm ions}} M_n | \vec v_n |^2.$

This temperature is written to the [OUTCAR](../output-files/OUTCAR.md) file.
Depending on the type of thermostat this temperature has to be rescaled
to obtain the real simulation temperature.

- [Nosé-Hoover
  thermostat](../tutorials/Nosé-Hoover_thermostat.md):

In this thermostat the number of degrees of freedom including
constraints are already accounted for in the potential energy term. In
this this method the center of mass is conserved. This lowers the
degrees of freedom by one which is also taken into account in the
[OUTCAR](../output-files/OUTCAR.md) file.

- [Andersen
  thermostat](../tutorials/Andersen_thermostat.md):

Same as for [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md).

- [Langevin
  thermostat](../tutorials/Langevin_thermostat.md):

As for the [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
and [Andersen
thermostat](../tutorials/Andersen_thermostat.md) in this
thermostat the number of degrees of freedom including constraints are
already accounted for. The center of mass is not conserved in this
method, hence this method has 3 degrees of freedom more than the
[Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
and the [Andersen
thermostat](../tutorials/Andersen_thermostat.md).

## Related tags and articles\[<a href="/wiki/index.php?title=TEBEG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[TEEND](TEEND.md), [IBRION](IBRION.md),
[SMASS](SMASS.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-TEBEG-_incategory-Examples)

------------------------------------------------------------------------


