<!-- Source: https://vasp.at/wiki/index.php/SHAKETOLSOFT | revid: 36166 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SHAKETOLSOFT
SHAKETOLSOFT = \[Real\]  
Default: **SHAKETOLSOFT** = [SHAKETOL](SHAKETOL.md) 

Description: SHAKETOLSOFT specifies the soft tolerance for the SHAKE
algorithm (in case VASP was compiled with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

Constrained molecular dynamics ([MDALGO](MDALGO.md)=1 \| 2
\| 3 \| 4 \| 5) are performed using a [SHAKE
algorithm](MDALGO.md).^([\[1\]](#cite_note-Ryckaert77-1))

[SHAKETOL](SHAKETOL.md) specifies the tolerance for the
SHAKE algorithm. If the error for all geometric constraints does not
decrease below this predefined tolerance within the allowed number of
iterations ([SHAKEMAXITER](SHAKEMAXITER.md)), VASP
terminates with an error message. This behavior can be changed by
defining the soft convergence tolerance SHAKETOLSOFT \>
[SHAKETOL](SHAKETOL.md), in which case the algorithm will
not terminate if at least accuracy specified by SHAKETOLSOFT was
reached.

## Related tags and articles
SHAKETOLSOFT, [SHAKEMAXITER](SHAKEMAXITER.md),
[MDALGO](MDALGO.md)

[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SHAKETOL-_incategory-Examples)

## References
1.  [↑](#cite_ref-Ryckaert77_1-0) [J. P. Ryckaert, G. Ciccotti,
    and H. J. C. Berendsen, J. Comp. Phys. 23, 327
    (1977).](http://dx.doi.org/10.1016/0021-9991(77)90098-5)

------------------------------------------------------------------------
