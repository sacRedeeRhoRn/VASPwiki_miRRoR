<!-- Source: https://vasp.at/wiki/index.php/Vibrational_Analysis_of_the_TS | revid: 8920 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Vibrational Analysis of the TS


Description: the
<a href="/wiki/Improved_Dimer_Method" class="mw-redirect"
title="Improved Dimer Method">Improved Dimer Method</a> needs an
educated guess of the decay path, which is extimated from the hardest
vibration mode with imaginary frequency of the TS geometry (which is a
planar NH3 molecule):

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    SYSTEM = Ammonia flipping
    IBRION = 5
    NSW = 1
    ALGO = F
    POTIM = 0.015
    EDIFF = 1e-8
    EDIFFG = -0.01
    NWRITE = 3

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
        3     1
    Direct
     0.6462   0.5736   0.5000
     0.5000   0.3547   0.5000
     0.3538   0.5736   0.5000
     0.5000   0.5000   0.5000

## Download\[<a
href="/wiki/index.php?title=Vibrational_Analysis_of_the_TS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="http://www.vasp.at/vasp-workshop/examples/ammonia_flipping.tgz"
class="external text" rel="nofollow">ammonia_flipping.tgz, sub-folder
TS_vib</a>

------------------------------------------------------------------------

<a
href="/wiki/index.php?title=VASP_example_calculations&amp;action=edit&amp;redlink=1"
class="new" title="VASP example calculations (page does not exist)">To
the list of examples</a> or to the [main
page](The_VASP_Manual.md)

  


