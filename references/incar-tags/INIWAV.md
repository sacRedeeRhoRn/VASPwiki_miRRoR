<!-- Source: https://vasp.at/wiki/index.php/INIWAV | revid: 32791 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# INIWAV
INIWAV = 0 \| 1 

|                     |     |     |
|---------------------|-----|-----|
| Default: **INIWAV** | = 1 |     |

Description: Specifies how to set up the initial orbitals in case
[`ISTART`](ISTART.md)` = 0`.

------------------------------------------------------------------------

- `INIWAV`` = 0`

Take 'jellium orbitals', i.e., fill the Kohn-Sham–orbital arrays with
plane waves of lowest kinetic energy = lowest eigenvectors for a
constant potential ('jellium').

|  |
|----|
| **Important:** 'jellium' calculations require a specific [POTCAR](../input-files/POTCAR.md) file, not included in the standard potential database. |

- `INIWAV`` = 1`

Fill the Kohn-Sham–orbital arrays with random numbers. It is definitely
the safest fool-proof switch. If you see long times for the wave
function initialization, i.e. between the two messages "WAVECAR not
read" and "entering main loop", in large systems consider using the
parallel random number generator
[`RANDOM_GENERATOR`](RANDOM_GENERATOR.md)` = pcg_32`.

|                                                |
|------------------------------------------------|
| **Tip:** Use `INIWAV`` = 1` whenever possible. |

|  |
|----|
| **Mind:** The INIWAV tag is only used for jobs that start from scratch ([`ISTART`](ISTART.md)` = 0`) and has no meaning otherwise. |

## Related tags and sections
[ISTART](ISTART.md)
[RANDOM_GENERATOR](RANDOM_GENERATOR.md)
