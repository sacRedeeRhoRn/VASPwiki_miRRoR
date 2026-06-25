<!-- Source: https://vasp.at/wiki/index.php/PLUGINS/MACHINE_LEARNING | revid: 34715 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PLUGINS/MACHINE LEARNING


PLUGINS/MACHINE_LEARNING =
.True. \| .False.  
Default: **PLUGINS/MACHINE_LEARNING** = .False. 

Description:
PLUGINS/MACHINE_LEARNING calls
the Python plugin for the machine learning interface for each ionic
relaxation step

|  |
|----|
| **Deprecated:** We do not recommend using this interface anymore. There is a mismatch in the units of ASE and VASP that makes this hard to use. Please use [PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md) in combination with [`PLUGINS/ML_MODE`](PLUGINS__ML_MODE.md)` = run`. |

------------------------------------------------------------------------

When
PLUGINS/MACHINE_LEARNING=.TRUE.,
VASP calls the `machine_learning` Python function at the end of each
ionic relaxation step. You can use this tag to replace VASP forces and
the stress tensor to represent an external machine-learned interatomic
potential. This can be used if you want to combine an machine-learned
interatomic potential with the different features of
[IBRION](IBRION.md). For example, you could compute the
phonon frequencies of the interatomic potential and compare it to
ab-initio data and be sure that the workflow is the same.

## Expected inputs\[<a
href="/wiki/index.php?title=PLUGINS/MACHINE_LEARNING&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Expected inputs">edit</a> \| (./index.php.md)\]

The `machine_learning` Python function is different from the other
plugins because it does not provide any input from VASP. Instead the
plugin infrastructure handles the communication with VASP. The only
requirement of the plugin is that the function returns a class
compatible with an
<a href="https://wiki.fysik.dtu.dk/ase/development/calculators.html"
class="external text" rel="nofollow">ASE Calculator</a>.


    def machine_learning():
        # code to setup calculator
        return calculator


VASP will take care to convert its internal data to be compatible with
the Calculator. We compute the forces and stress using the calculator on
this data. VASP packages the results on the Python side and sends them
back to Fortran where they replace the usual force and stress values.

## Related tags and articles\[<a
href="/wiki/index.php?title=PLUGINS/MACHINE_LEARNING&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md),
[PLUGINS/FORCE_AND_STRESS](PLUGINS__FORCE_AND_STRESS.md),
[PLUGINS/LOCAL_POTENTIAL](PLUGINS__LOCAL_POTENTIAL.md),
[PLUGINS/ML_MODE](PLUGINS__ML_MODE.md),
[PLUGINS/STRUCTURE](PLUGINS__STRUCTURE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PLUGINS/MACHINE_LEARNING-_incategory-Examples)


