<!-- Source: https://vasp.at/wiki/index.php/ML_MB_MIN | revid: 32857 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_MB_MIN


ML_MB_MIN = \[integer\]  
Default: **ML_MB_MIN** = 3 

Description: ML_MB_MIN sets
the minimum number of local reference configurations required for
generation of a machine-learned force field.

|  |
|----|
| **Mind:** Available as of VASP 6.4.3. Previous versions do not support this tag but act as if its default was `ML_MB_MIN`` = 2`. |

------------------------------------------------------------------------

Machine-learned force fields based on the kernel method require a
reasonable amount of reference atomic environments in order to provide
meaningful predictions. Typically, the on-the-fly algorithm in VASP
collects these local reference configurations (also called kernel basis
functions) during an MD simulation
([`ML_MODE`](ML_MODE.md)` = train`). However, at the start
of the trajectory usually only very few local reference configurations
are available. How many depends on the system size, symmetry and number
of atoms (per type). This tag controls how many local reference
configurations are required **for each atom type** before training of a
force field is allowed. Setting a higher value may yield a more robust
initial force field at the cost of more *ab initio* calculations during
the first few MD steps.

If a training is scheduled in the current step, i.e., the `STATUS` line
in the [ML_LOGFILE](../output-files/ML_LOGFILE.md) shows `learning` or
`critical`, but not enough atomic environments were collected, a text
message will be emitted in the `MSG` line. Here is an example:

    --------------------------------------------------------------------------------
    STATUS                  1  critical  4      T      F         0         1
    LCONF                   1 Ni         0         4
    SPRSC                   1         1         1 Ni         4         1
    MSG                     1      info Number of local reference configurations after sparsification below ML_MB_MIN, skipping training.
    BEEF                    1   1.00000000E-06   3.46410162E-02   2.00000000E-02   2.00000000E-03   0.00000000E+00   0.00000000E+00
    --------------------------------------------------------------------------------
    STATUS                  2  critical  4      T      F         0         2
    LCONF                   2 Ni         1         5
    SPRSC                   2         2         2 Ni         5         2
    MSG                     2      info Number of local reference configurations after sparsification below ML_MB_MIN, skipping training.
    BEEF                    2   1.00000000E-06   3.46410162E-02   2.00000000E-02   2.00000000E-03   0.00000000E+00   0.00000000E+00
    --------------------------------------------------------------------------------
    STATUS                  3  critical  4      T      F         0         3
    LCONF                   3 Ni         2         6
    SPRSC                   3         3         3 Ni         6         3
    REGR                    3    1    1   6.42271768E+01   1.36891529E+00   6.43938951E-14   3.76458019E+01
    REGR                    3    1    2   7.43557292E+01   1.35099932E+00   5.48943502E-14   3.71479653E+01
    REGR                    3    1    3   7.81437752E+01   1.34829112E+00   5.21286212E-14   3.70727138E+01
    REGRF                   3    1    4   7.95268527E+01   1.34739777E+00   5.11880969E-14   3.70478685E+01    2.31498305E+15   3.30988608E+11
    NDESC                   3        12 Ni       113
    NDESC_SIC               3 Ni       113
    STDAB                   3   1.41895828E-04   3.22944034E-02   9.66711031E-02
    ERR                     3   1.45620371E-04   3.32055814E-02   9.84035846E-02
    CFE                     3   0.00000000E+00   0.00000000E+00   0.00000000E+00
    LASTE                   3   1.99936842E-04   5.14296619E-02   1.37823063E-01
    BEE                     3   1.00000000E-06   3.46410162E-02   2.00000000E-02   2.00000000E-03   0.00000000E+00   0.00000000E+00
    BEEF                    3   2.37926034E-05   2.21630107E-03   8.49321832E-04   2.00000000E-03   5.19041973E-02   3.66970792E-02
    -------------------------------------------------------------------------------- 
    ...

Here, in the first two steps the
ML_MB_MIN threshold prevents
training of an MLFF, even if the Bayesian error estimation signals a
`critical` step. The force field is then only generated in the third
step, after the minimum number of three local reference configurations
have been collected.

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_MB_MIN&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_MODE](ML_MODE.md), [ML_MB](ML_MB.md),
[ML_MCONF_NEW](ML_MCONF_NEW.md),
[ML_MCONF](ML_MCONF.md),
[ML_LBASIS_DISCARD](ML_LBASIS_DISCARD.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_MB_MIN-_incategory-Examples)

------------------------------------------------------------------------


