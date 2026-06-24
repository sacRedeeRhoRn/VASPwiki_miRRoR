<!-- Source: https://vasp.at/wiki/index.php/Vibrational_Analysis_of_the_TS | revid: 8920 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Vibrational Analysis of the TS
Description: the [Improved Dimer
Method](Improved_Dimer_Method.md) needs an
educated guess of the decay path, which is extimated from the hardest
vibration mode with imaginary frequency of the TS geometry (which is a
planar NH3 molecule):

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

&nbsp;

    SYSTEM = Ammonia flipping
    IBRION = 5
    NSW = 1
    ALGO = F
    POTIM = 0.015
    EDIFF = 1e-8
    EDIFFG = -0.01
    NWRITE = 3

- [KPOINTS](../input-files/KPOINTS.md)

&nbsp;

    k-points
     0
    G
     1 1 1

  

- [POSCAR](../input-files/POSCAR.md)

&nbsp;

    ammonia flipping
      1.00000000000000
        6.000000    0.000000    0.000000
        0.000000    7.000000    0.000000
        0.000000    0.000000    8.000000
      H    N
        3     1
    Direct
     0.6462   0.5736   0.5000
     0.5000   0.3547   0.5000
     0.3538   0.5736   0.5000
     0.5000   0.5000   0.5000

## Download
[ammonia_flipping.tgz, sub-folder
TS_vib](http://www.vasp.at/vasp-workshop/examples/ammonia_flipping.tgz)

------------------------------------------------------------------------

[To the list of
examples](https://vasp.at/wiki/index.php/index.php)")
or to the [main page](The_VASP_Manual.md)

  
