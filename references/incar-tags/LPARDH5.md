<!-- Source: https://vasp.at/wiki/index.php/LPARDH5 | revid: 31720 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LPARDH5


LPARDH5 = \[logical\]  
Default: **LPARDH5** = .FALSE. 

Description: LPARDH5
determines whether the partial charges are written to
[PARCHG](../output-files/PARCHG.md) or
[vaspout.h5](../output-files/Vaspout.h5.md).

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">Partial charges</a> can be
calculated as a postprocessing step when [LPARD](LPARD.md) =
.TRUE.. The output is written to one or several
[PARCHG](../output-files/PARCHG.md) files if
LPARDH5=.FALSE., and to
[vaspout.h5](../output-files/Vaspout.h5.md) if
LPARDH5=.TRUE.. If
[NBMOD](NBMOD.md) = -1, the setting of
[LPARD](LPARD.md) is irrelevant. Instead of a
[PARCHG](../output-files/PARCHG.md) file, or a partial_charges group in the
[vaspout.h5](../output-files/Vaspout.h5.md) hdf5 file, a
[CHGCAR](../input-files/CHGCAR.md) file *without* augmentation charges will
be written.

If the output is redirected to
[vaspout.h5](../output-files/Vaspout.h5.md),
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> can be used to analyze
the partial charge density and to simulate STM pictures.

For example, the following Python code would create a dictionary with
the partial charge output and plot an STM simulation.


      import py4vasp as pv
      calc = pv.Calculation.from_path(".")
      part_charge_dict = calc.partial_density.to_dict()
      calc.partial_density.to_stm()


The command below prints the table of contents of the
[vaspout.h5](../output-files/Vaspout.h5.md) file.

     h5ls -r vaspout.h5

The section relevant to partial charges will look similar to this:

     /results/partial_charges Group
     /results/partial_charges/bands Dataset {1}
     /results/partial_charges/grid Dataset {3}
     /results/partial_charges/kpoints Dataset {1}
     /results/partial_charges/parchg Dataset {1, 1, 2, 480, 48, 48}

[LPARD](LPARD.md), [LWAVEH5](LWAVEH5.md),
[LCHARGH5](LCHARGH5.md), [IBAND](IBAND.md),
[EINT](EINT.md), [NBMOD](NBMOD.md),
[KPUSE](KPUSE.md), [LSEPB](LSEPB.md),
[LSEPK](LSEPK.md), [PARCHG](../output-files/PARCHG.md),
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">band-decomposed charge
densities</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LPARDH5-_incategory-Examples)

------------------------------------------------------------------------


