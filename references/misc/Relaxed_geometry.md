<!-- Source: https://vasp.at/wiki/index.php/Relaxed_geometry | revid: 8921 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Relaxed geometry


Description: calculate the relaxed geometry of NH3: the total energy is
the energy of the initial state of the flipping reaction

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    SYSTEM = Ammonia flipping
    IBRION = 2
    NSW = 10
    ALGO = N
    POTIM = 0.5
    EDIFF = 1e-6
    EDIFFG = -0.01
    NELMIN = 5

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    k-points
     0
    G
     1 1 1

  

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    ammonia flipping
      1.00000000000000
        6.000000    0.000000    0.000000
        0.000000    7.000000    0.000000
        0.000000    0.000000    8.000000
      H    N
      3    1
    Selective dynamics
    Direct
    0.636429  0.567446  0.549205   T   T   T
    0.500000  0.364896  0.549205   T   T   T
    0.363571  0.567446  0.549205   T   T   T
    0.500000  0.500000  0.500000   F   F   F

## Download\[<a
href="/wiki/index.php?title=Relaxed_geometry&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="http://www.vasp.at/vasp-workshop/examples/ammonia_flipping.tgz"
class="external text" rel="nofollow">ammonia_flipping.tgz, sub-folder
scf</a>

------------------------------------------------------------------------

<a
href="/wiki/index.php?title=VASP_example_calculations&amp;action=edit&amp;redlink=1"
class="new" title="VASP example calculations (page does not exist)">To
the list of examples</a> or to the [main
page](The_VASP_Manual.md)

  


