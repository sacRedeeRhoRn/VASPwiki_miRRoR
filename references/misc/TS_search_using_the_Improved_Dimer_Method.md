<!-- Source: https://vasp.at/wiki/index.php/TS_search_using_the_Improved_Dimer_Method | revid: 8918 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TS search using the Improved Dimer Method
Description:

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

&nbsp;

    SYSTEM = Ammonia flipping
    IBRION = 44
    NSW = 100
    EDIFF = 1e-6
    EDIFFG = -0.01

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
     ! decay direction
     0.000004   -0.000001    0.511990
     0.000000   -0.000003    0.547859
    -0.000004   -0.000001    0.511988
     0.000000    0.000000   -0.111986

## Download
[ammonia_flipping.tgz, sub-folder
improved_dimer](http://www.vasp.at/vasp-workshop/examples/ammonia_flipping.tgz)

------------------------------------------------------------------------

[To the list of
examples](https://vasp.at/wiki/index.php/index.php)")
or to the [main page](The_VASP_Manual.md)

  
