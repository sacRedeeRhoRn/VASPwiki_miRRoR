<!-- Source: https://vasp.at/wiki/index.php/ML_HEAT | revid: 30652 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_HEAT
This file contains the local heat flux at every MD step in units of
$\mathrm{ eV \\ \AA / fs}$. This file is
only written if [ML_LHEAT](../incar-tags/ML_LHEAT.md)=**.TRUE.**.

A sample output should look like the following:

    NSTEP=         1 QXYZ=  0.36329995E-03 -0.18158424E-03 -0.89885493E-03
    NSTEP=         2 QXYZ=  0.12017813E+00 -0.24353637E+00 -0.24858697E-02
    NSTEP=         3 QXYZ=  0.16434205E+00 -0.25889449E+00  0.86212831E-02
    NSTEP=         4 QXYZ=  0.20636827E+00 -0.24238677E+00 -0.33029653E-01
    NSTEP=         5 QXYZ=  0.22888948E+00 -0.19732842E+00 -0.15981468E-02
    NSTEP=         6 QXYZ=  0.18517072E+00 -0.19821527E+00  0.34029701E-01
    NSTEP=         7 QXYZ=  0.20600383E+00 -0.17943287E+00 -0.28752284E-01
    NSTEP=         8 QXYZ=  0.25245149E+00 -0.17896799E+00  0.66038212E-01
    NSTEP=         9 QXYZ=  0.22178615E+00 -0.13178134E+00  0.23810433E-01
    NSTEP=        10 QXYZ=  0.20140372E+00 -0.11168534E+00  0.90583309E-01

Here "NSTEP" is the number of the MD step and "QXYZ" is the heat flux in
three Cartesian directions.

------------------------------------------------------------------------
