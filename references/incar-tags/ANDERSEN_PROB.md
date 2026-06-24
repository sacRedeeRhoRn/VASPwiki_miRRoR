<!-- Source: https://vasp.at/wiki/index.php/ANDERSEN_PROB | revid: 16018 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ANDERSEN_PROB
ANDERSEN_PROB = 0≤\[real\]≤1  
Default: **ANDERSEN_PROB** = 0 

Description: ANDERSEN_PROB sets the collision probability for the
Anderson thermostat (in case VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

In the approach proposed by Andersen^([\[1\]](#cite_note-Andersen80-1))
the system is thermally coupled to a fictitious heat bath with the
desired temperature. The coupling is represented by stochastic impulsive
forces that act occasionally on randomly selected particles. The
collision probability is defined as an average number of collisions per
atom and time-step. This quantity can be controlled by the flag
ANDERSEN_PROB. The total number of collisions with the heat-bath is
written in the file [REPORT](../output-files/REPORT.md) for each MD step.

|  |
|----|
| **Tip:** Setting ANDERSEN_PROB=0, *i.e.*, no collisions with the heat-bath) generates the microcanonical (*NVE*) ensemble. |

## Related tags and articles
[MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ANDERSEN_PROB-_incategory-Examples)

## References
1.  [↑](#cite_ref-Andersen80_1-0) [H. C. Andersen, J. Chem. Phys. 72,
    2384 (1980).](http://dx.doi.org/10.1063/1.439486)

------------------------------------------------------------------------
