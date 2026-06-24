<!-- Source: https://vasp.at/wiki/index.php/POSNICS | revid: 34574 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# POSNICS
|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

The POSNICS file is an input file that defines the positions to
calculate the NMR nucleus-independent chemical shielding (NICS). If it
is present in the directory running the job, it will be used by default,
though it can be made explicit using
[`LPOSNICS`](LPOSNICS.md)` = True`. The first line defines
the number of NICS positions, followed by the positions of the NICS in
direct coordinates, i.e., as fractions of the lattice parameters
${\vec a}_1, {\vec a}_2$ and
${\vec a}_3$:

    10000
    0.0 0.0 0.5
    0.0 0.01 0.5
    0.0 0.02 0.5
    ...
    0.99 0.97 0.5
    0.99 0.98 0.5
    0.99 0.99 0.5

## Related tags and articles
[LCHIMAG](LCHIMAG.md), [NUCIND](NUCIND.md),
[LPOSNICS](LPOSNICS.md)
