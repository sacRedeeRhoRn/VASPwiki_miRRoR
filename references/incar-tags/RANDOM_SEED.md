<!-- Source: https://vasp.at/wiki/index.php/RANDOM_SEED | revid: 37188 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# RANDOM_SEED
RANDOM_SEED = \[integer\]\[integer\]\[integer\]  
Default: **RANDOM_SEED** = based on the system clock 

Description: RANDOM_SEED specifies the seed of the random-number
generator (compile VASP with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

The random-number generator (RNG) generates a sequence of random
numbers, which is initialized by the tag RANDOM_SEED. For example, in
molecular dynamics simulations, the RNG can be used to initialize atomic
velocities. Hence, the seed for the RNG influences the trajectory of a
molecular dynamics simulation. The three integers of RANDOM_SEED must
fulfill these conditions:

    0 <= RANDOM_SEED(1) < 900000000
    0 <= RANDOM_SEED(2) < 1000000
    0 <= RANDOM_SEED(3)

A typical input for the RANDOM_SEED looks like this:

    RANDOM_SEED =         248489752                0                0

The initial value of RANDOM_SEED and the value after each MD step are
written to the [REPORT](../output-files/REPORT.md) file.

|  |
|----|
| **Tip:** If multiple molecular dynamics runs with different random seeds result in inconsistent time averages, then not enough configurations were sampled. Hence, longer or more trajectories are required to get converged ensemble averages. |

|  |
|----|
| **Mind:** If no RANDOM_SEED is set in the [INCAR](../input-files/INCAR.md) then the used value will depend on the system time. For example, in molecular dynamics simulations, initial velocities will be different each time VASP is executed (if [TEBEG](TEBEG.md) is used and no velocities are provided in the [POSCAR](../input-files/POSCAR.md) file). Hence, the trajectories will diverge. If reproducibility is desired the RANDOM_SEED has to be set manually. |

## Related tags and articles
[RANDOM_GENERATOR](RANDOM_GENERATOR.md),
[IBRION](IBRION.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-RANDOM_SEED-_incategory-Examples)

------------------------------------------------------------------------
