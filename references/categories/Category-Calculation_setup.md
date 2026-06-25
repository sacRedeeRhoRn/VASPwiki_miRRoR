<!-- Source: https://vasp.at/wiki/index.php/Category:Calculation_setup | revid: 29970 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Calculation setup


The Vienna ab-initio simulation package (VASP) is a computer program for
atomic scale materials modeling from first principles. To get a license,
please refer to the
<a href="https://www.vasp.at/sign_in/registration_form/"
class="external text" rel="nofollow">registration form on the VASP
website</a>. You will get access to the VASP source and [compile
it](Category-Installation.md) directly on
your hardware to achieve optimal
<a href="/wiki/Performance" class="mw-redirect"
title="Performance">performance</a>.

For **instructions of a basic calculation** read [how to perform an
electronic
minimization](../tutorials/Setting_up_an_electronic_minimization.md).

In a nutshell, after the
[installation](Category-Installation.md),
VASP can be executed from the command line of a Terminal. Navigate to a
working directory. In the working directory, VASP looks for
<a href="/wiki/Input_files" class="mw-redirect"
title="Input files">input files</a> that determine what calculation is
performed. The most important input files are

- the [POSCAR](../input-files/POSCAR.md) file: Defines the structure of the
  material, i.e., lattice vectors, ionic positions, etc.
- the [INCAR](../input-files/INCAR.md) file: General selection of the
  algorithm, setting parameters, etc.
- the [POTCAR](../input-files/POTCAR.md) file: Contains the
  <a href="/wiki/Pseudopotentials" class="mw-redirect"
  title="Pseudopotentials">pseudopotentials</a> and other information
  relevant for the
  <a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
  method</a>
- the [KPOINTS](../input-files/KPOINTS.md) file: Defines the Bloch vectors
  **k** in reciprocal space.

The central way to control the calculation is by setting [INCAR
tags](Category-INCAR_tag.md) in the
[INCAR](../input-files/INCAR.md) file. Depending on the VASP calculation,
there are other <a href="/wiki/Input_files" class="mw-redirect"
title="Input files">input files</a> to provide settings for the
calculation, e.g., the [ICONST](../input-files/ICONST.md) file.

|  |
|----|
| **Tip:** To learn how to set up a calculation, we recommend following some of our <a href="https://www.vasp.at/tutorials/latest/" class="external text"
rel="nofollow">tutorials</a>. |

Finally, VASP will write [output
files](https://vasp.at/wiki/index.php/Category:Output_files) to the
working directory.

|  |
|----|
| **Tip:** For postprocessing, <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> is a convenient Python package to read and visualize the produced data. |

This category contains all pages and topics relevant to the
**computational setup**. For instance,
<a href="/wiki/Installation" class="mw-redirect"
title="Installation">installation</a>,
<a href="/wiki/Files" class="mw-redirect" title="Files">files</a>,
<a href="/wiki/Performance" class="mw-redirect"
title="Performance">performance</a>, etc.


