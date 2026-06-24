<!-- Source: https://vasp.at/wiki/index.php/SMASS | revid: 32799 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SMASS
SMASS = -3 \| -2 \| -1 \| \[real\] ≥ 0  
Default: **SMASS** = -3 

Description: SMASS controls the velocities during an ab-initio
molecular-dynamics run.

------------------------------------------------------------------------

- SMASS=-3

For SMASS=-3 a microcanonical ensemble ([NVE
ensemble](../misc/NVE_ensemble.md)) is simulated (constant
energy molecular dynamics). The calculated Hellmann-Feynman forces serve
as an acceleration acting onto the ions. The total free energy (i.e.
free electronic energy + Madelung energy of ions + kinetic energy of
ions) is conserved.

|  |
|----|
| **Tip:** Another possible way to sample from the [NVE ensemble](../misc/NVE_ensemble.md) is to use [`MDALGO`](MDALGO.md)` = 1` and [`ANDERSEN_PROB`](ANDERSEN_PROB.md)` = 0.0`. |

- SMASS=-2

For SMASS=-2 the initial velocities are kept constant. This allows to
calculate the energy for a set of different linear dependent positions
(for instance frozen phonons, or dimers with varying bond lengths).

**Mind**: if SMASS=-2 the actual steps taken are
[POTIM](POTIM.md)×(velocities-read-from-the-[POSCAR](../input-files/POSCAR.md)-file).
To avoid ambiguities, set [POTIM](POTIM.md)=1.

- SMASS=-1

In this case the velocities are scaled each
[NBLOCK](NBLOCK.md) step (starting at the first step i.e.
MOD(NSTEP,[NBLOCK](NBLOCK.md))=1) to the temperature:
T=[TEBEG](TEBEG.md)+([TEEND](TEEND.md)-[TEBEG](TEBEG.md))×NSTEP/[NSW](NSW.md),

where NSTEP is the current step (starting from 1). This allows a
continuous increase or decrease of the kinetic energy. In the
intermediate period, a micro-canonical ensemble is simulated.

- SMASS≥0

For SMASS≥0, a canonical ensemble is simulated using the algorithm of
Nosé. The Nosé mass controls the frequency of the temperature
oscillations during the
simulation.^([\[1\]](#cite_note-nose:jcp:1984-1)[\[2\]](#cite_note-nose:ptp:1991-2)[\[3\]](#cite_note-bylander:prb:1992-3))
For SMASS=0, a Nosé-mass corresponding to period of 40 time steps will
be chosen. The Nosé-mass should be set such that the induced temperature
fluctuation show approximately the same frequencies as the typical
'phonon'-frequencies for the specific system. For liquids something like
'phonon'-frequencies might be obtained from the spectrum of the velocity
auto-correlation function. If the ionic frequencies differ by an order
of magnitude from the frequencies of the induced temperature
fluctuations, Nosé thermostat and ionic movement might decouple leading
to a non-canonical ensemble. The frequency of the approximate
temperature fluctuations induced by the Nosé-thermostat is written to
the [OUTCAR](../output-files/OUTCAR.md) file.

## Related tags and articles
[structure
optimization](../tutorials/Structure_optimization.md),
[IBRION](IBRION.md), [POTIM](POTIM.md),
[NBLOCK](NBLOCK.md), [TEBEG](TEBEG.md),
[TEEND](TEEND.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SMASS-_incategory-Examples)

## References
1.  [↑](#cite_ref-nose:jcp:1984_1-0) [S. Nosé, J. Chem. Phys. **81**,
    511 (1984).](https://doi.org/10.1063/1.447334)
2.  [↑](#cite_ref-nose:ptp:1991_2-0) [S. Nosé, Prog. Theor. Phys. Suppl.
    **103**, 1 (1991).](https://doi.org/10.1143/PTPS.103.1)
3.  [↑](#cite_ref-bylander:prb:1992_3-0) [D. M. Bylander and L.
    Kleinman, Phys. Rev. B **46**, 13756
    (1992).](https://doi.org/10.1103/PhysRevB.46.13756)

  

------------------------------------------------------------------------
