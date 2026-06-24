<!-- Source: https://vasp.at/wiki/index.php/Plugins | revid: 36550 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Plugins
Implementing features over VASP carries a significant overhead, both in
term of code development and maintenance. An alternative approach is to
use our Python plugin infrastructure. Simply write
[Python](https://www.python.org/) functions in a pre-defined format and
VASP will recognize and execute your code while it is running. This page
describes the steps that you will need to write your first Python script
and link it with VASP.

## Contents

- [1 Compiling with Plugins support](#Compiling_with_Plugins_support)
- [2 Python scripting](#Python_scripting)
- [3 Exposing interfaces through entry-points
  (advanced)](#Exposing_interfaces_through_entry-points_(advanced))
- [4 Related tags and articles](#Related_tags_and_articles)

## Compiling with Plugins support
Follow the instructions for compiling VASP with Plugins support on the
[Makefile.include](../misc/Makefile.include.md) "Makefile.include")
page.

## Python scripting
Start by creating a file called `vasp_plugin.py` in the folder in which
you are running a VASP calculation. An alternative route through
entry-points is also possible (see below for further instructions). In
`vasp_plugin.py` implement one or all of the following Python functions.

    def structure(constants, additions):
        """Defines the PLUGINS/STRUCTURE interface"""

    def force_and_stress(constants, additions):
        """Defines the PLUGINS/FORCE_AND_STRESS interface"""

    def local_potential(constants, additions):
        """Defines the PLUGINS/LOCAL_POTENTIAL interface"""

    def occupancies(constants, additions):
        """Defines the PLUGINS/OCCUPANCIES interface"""

As the names of the input variables suggest,

1.  `constants` provides a
    [dataclass](https://docs.python.org/3/library/dataclasses.html) with
    quantities computed in VASP that must stay constant through the
    interface. Typically these include "metadata" such as the lattice
    vectors, number of grid points, etc. Some interfaces also pass in
    quantities such as the charge density as `constants`. Please check
    the page of the specific plugins' tag for more details on which
    quantities are available as constants. Alternatively, you may print
    the contents of `constants`.
2.  `additions` stores quantities that are allowed to change in the
    interface. You must use the syntax
    `additions.<quantity-name> += ...` in order to change additions.
    That is, quantities must be "added" (or subtracted) to `additions`
    instead assigning them a new value. We use additions for two
    reasons. First, it makes sure that you use the memory from VASP;
    otherwise assigning might create a new array in memory and return
    zero to VASP. Secondly, adding the values allows multiple compatible
    plugins running at the same time.

Each of the above interfaces may be called by VASP depending on the
following [INCAR](../input-files/INCAR.md) tags

       PLUGINS/FORCE_AND_STRESS = T        ! Modifies the force and stress at the end of the SCF loop
       PLUGINS/LOCAL_POTENTIAL = T         ! Modifies the local potential every SCF step
       PLUGINS/OCCUPANCIES = T             ! Modifies NELECT, EFERMI, SIGMA, ISMEAR, EMIN, EMAX, NUPDOWN at the end of the SCF loop
       PLUGINS/STRUCTURE = T               ! Modifies the structure at the end of the SCF loop

Navigate to the relevant [INCAR](../input-files/INCAR.md) tag pages for
further information.

## Exposing interfaces through entry-points (advanced)
Consider using [entry
points](https://packaging.python.org/en/latest/specifications/entry-points/)
in cases where you do not want to move `vasp_plugin.py` to each new VASP
calculation directory. This is also the approach you should take, if you
want to distribute your plugin to other users. Within the group "vasp",
add the following lines to your `pyproject.toml` file for each interface
you would like to introduce new functions. For example, if you wanted to
access the `force_and_stress` interface through an entry point, add the
following lines to your `pyproject.toml` file,

       force_and_stress = "/path/to/python_function:force_and_stress"

## Related tags and articles
Files:
[Makefile.include](../misc/Makefile.include.md) "Makefile.include")

Tags:
[PLUGINS/FORCE_AND_STRESS](../incar-tags/PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](../incar-tags/PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/ML_MODE](../incar-tags/PLUGINS__ML_MODE.md),
[PLUGINS/ML_OUTBLOCK](../incar-tags/PLUGINS__ML_OUTBLOCK.md),
[PLUGINS/ML_OUTPUT_MODE](../incar-tags/PLUGINS__ML_OUTPUT_MODE.md),
[PLUGINS/NEIGHBOR_CUTOFF](../incar-tags/PLUGINS__NEIGHBOR_CUTOFF.md),
[PLUGINS/OCCUPANCIES](../incar-tags/PLUGINS__OCCUPANCIES.md),
[PLUGINS/STRUCTURE](../incar-tags/PLUGINS__STRUCTURE.md)
