<!-- Source: https://vasp.at/wiki/index.php/SHAKETOLSOF | revid: 34208 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SHAKETOLSOF


[SHAKETOLSOFT](SHAKETOLSOFT.md) = \[Real\]  
Default: **SHAKETOLSOFT** = [SHAKETOL](SHAKETOL.md) 

Description: [SHAKETOLSOFT](SHAKETOLSOFT.md) specifies
the soft tolerance for the SHAKE algorithm (in case VASP was compiled
with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

Constrained molecular dynamics ([MDALGO](MDALGO.md)=1 \| 2
\| 3 \| 4 \| 5) are performed using a [SHAKE
algorithm](MDALGO.md).

[SHAKETOL](SHAKETOL.md) specifies the tolerance for the
SHAKE algorithm. If the error for all geometric constraints does not
decrease below this predefined tolerance within the allowed number of
iterations ([SHAKEMAXITER](SHAKEMAXITER.md)), VASP
terminates with an error message. This behavior can be changed by
defining the soft convergence tolerance
SHAKETOLSOF \>
[SHAKETOL](SHAKETOL.md), in which case the algorithm will
not terminate if at least accuracy specified by
SHAKETOLSOF was reached.


