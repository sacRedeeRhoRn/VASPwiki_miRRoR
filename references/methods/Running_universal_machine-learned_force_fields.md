<!-- Source: https://vasp.at/wiki/index.php/Running_universal_machine-learned_force_fields | revid: 37161 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Running universal machine-learned force fields


|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

Universal machine-learned force fields (uMLFF, or alternatively: uMLIP
for "universal machine-learned interatomic potentials") offer a fast
alternative to the computational demands of DFT. Pre-trained uMLFFs can
be used as an alternative to [VASP-native force
fields](../categories/Category-Machine-learned_force_fields.md)
to drive any VASP simulation that uses or could use prediction-only mode
([`ML_MODE`](../incar-tags/ML_MODE.md)` = run`). This includes [molecular
dynamics
simulations](https://vasp.at/wiki/index.php/Category:Molecular_dynamics),
[ionic
optimization](../tutorials/Structure_optimization.md)
(see [IBRION](../incar-tags/IBRION.md)), and [advanced sampling
techniques](../categories/Category-Advanced_molecular-dynamics_sampling.md).

We utilize the [Plugins](../tutorials/Plugins.md) feature to call
pre-trained uMLFF models via Python and have them calculate forces and
stresses.

|  |
|----|
| **Important:** When employing uMLFFs, the accuracy and reliability of your calculations and results may vary. Thorough validation is advised. |


## Contents


- [1 Model
  selection](#Model_selection)
- [2 Step-by-step
  instructions](#Step-by-step_instructions)
  - [2.1 Step 1:
    Compiling with Plugins
    support](#Step_1:_Compiling_with_Plugins_support)
  - [2.2 Step 2:
    Setting up
    vasp_plugin.py](#Step_2:_Setting_up_vasp_plugin.py)
    - [2.2.1
      Example A: Model inference with the
      tensorpotential package
      (GRACE)](#Example_A:_Model_inference_with_the_tensorpotential_package_(GRACE))
    - [2.2.2
      Example B: Model inference with the UPET
      package](#Example_B:_Model_inference_with_the_UPET_package)
    - [2.2.3
      Example C: Model inference with the
      DeePMD-Kit
      package](#Example_C:_Model_inference_with_the_DeePMD-Kit_package)
  - [2.3 Step 3:
    Setting up your INCAR](#Step_3:_Setting_up_your_INCAR)
  - [2.4 Step 4:
    Run calculation](#Step_4:_Run_calculation)
- [3
  Recommendations and
  advice](#Recommendations_and_advice)
- [4 Related tags
  and articles](#Related_tags_and_articles)
- [5
  References](#References)


## Model selection\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Model selection">edit</a> \| (./index.php.md)\]

A dedicated list of publicly available models, including performance
benchmarks, can be found, for example, at MaterialsProject's
<a href="https://matbench-discovery.materialsproject.org/"
class="external text" rel="nofollow">matbench-discovery</a>. As a
general rule of thumb, choose a model with good relevant metrics that
was trained on a broad choice of datasets. Between models with similar
metrics, choose a model with fewer parameters for faster inference.

## Step-by-step instructions\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

The following section, specifically Step 2, provides three examples of
running different uMLFFs in VASP. Implementations vary between models,
and the first step is always to understand how to call a particular
model in Python directly before trying to have it called via the plugin.
This also allows for easier and more comprehensive debugging.

### Step 1: Compiling with Plugins support\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Compiling with Plugins support">edit</a> \| (./index.php.md)\]

To use [Plugins](../tutorials/Plugins.md), follow the [instructions on
the Makefile.include wiki
page](../misc/Makefile.include.md) "Makefile.include").
Note that a re-compilation of VASP is required to enable Plugins
support.

### Step 2: Setting up vasp_plugin.py\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Setting up vasp_plugin.py">edit</a> \| (./index.php.md)\]

Most models specify how to call them from Python. The instructions for
how to install the corresponding packages and load their `calculator`
instances will differ from model to model, but the `vasp_plugin.py` file
should always contain (at least) the following:


    calculator = ...                                # different for each model

    from vasp.force_field import AseForceField      # VASP force field wrapper class
    force_field = AseForceField(calculator)         # apply wrapper class

    def force_and_stress(constants, additions):     # to compute force and stress via the uMLFF model instead of VASP's DFT routines
        force_field.force_and_stress(constants, additions)


Copy or move the `vasp_plugin.py` file to your calculation folder.

We will now look at three example models and how to run them via
`vasp_plugin.py`. Use a dedicated Python virtual environment to install
the required packages.

|  |
|----|
| **Mind:** These examples are chosen for demonstration purposes and are not recommendations. |

#### Example A: Model inference with the tensorpotential package (GRACE)\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Example A: Model inference with the tensorpotential package (GRACE)">edit</a> \| (./index.php.md)")\]

First, let's look at how to wire up some GRACE force fields via the
[Plugins](../tutorials/Plugins.md) infrastructure. To this end, we can
check GRACE's <a
href="https://gracemaker.readthedocs.io/en/latest/gracemaker/install/#setting-up-the-environment"
class="external text" rel="nofollow">documentation</a> to find we need a
Python environment, and then install the `tensorpotential` package.
GRACE offers <a
href="https://github.com/ICAMS/grace-tutorial/blob/main/3-foundation-models/1-python-ase/using-grace-fm.ipynb"
class="external text" rel="nofollow">some examples</a> for how to load
and run their foundation models, so we adapt this approach in
`vasp_plugin.py`:


    from tensorpotential.calculator.foundation_models import GRACEModels, grace_fm
    calculator = grace_fm(GRACEModels.GRACE_2L_OMAT)

    from vasp.force_field import AseForceField  # VASP force field wrapper class
    force_field = AseForceField(calculator)         # apply wrapper class

    def force_and_stress(constants, additions):     # to compute force and stress via the uMLFF model instead of VASP's DFT routines
        force_field.force_and_stress(constants, additions)


Note that before running this code, you may need to download the model.
Do so via `grace_models download GRACE_2L_OMAT` in a terminal of your
choice. You can also get a list of all available foundation models via
`grace_models list`. If you want to use a different model, remember to
also update the `GRACEModels` enum in `vasp_plugin.py`.

|  |
|----|
| **Important:** In case you want to run a fine-tuned GRACE model, there is another GRACE <a
href="https://github.com/ICAMS/grace-tutorial/blob/main/3-foundation-models/3a-finetuning/validate.ipynb"
class="external text" rel="nofollow">tutorial notebook</a> for how to access these using the `TPCalculator` class. In `vasp_plugin.py`, simply use that calculator and point to your fine-tuned model. |

|  |
|----|
| **Mind:** Another way of running GRACE force fields in particular is via a special compiler flag, documented on a [separate wiki page](Running_GRACE_force_fields_in_VASP.md). Future development might break feature parity, but as of VASP 6.6.0, both [plugins](../tutorials/Plugins.md) and compiler flag approach offer the same inference-only functionality. |

#### Example B: Model inference with the UPET package\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Example B: Model inference with the UPET package">edit</a> \| (./index.php.md)\]

Next, let's use the models of the `UPET` package (see also the
<a href="https://github.com/lab-cosmo/upet" class="external text"
rel="nofollow">UPET documentation</a>). The documentation clarifies how
to load different models, so install the package into your environment
and then follow their instructions in `vasp_plugin.py`:


    from upet.calculator import UPETCalculator
    calculator = UPETCalculator(model="pet-mad-s", version="1.5.0", device="cuda")

    from vasp.force_field import AseForceField      # VASP force field wrapper class
    force_field = AseForceField(calculator)         # apply wrapper class

    def force_and_stress(constants, additions):     # to compute force and stress via the uMLFF model instead of VASP's DFT routines
        force_field.force_and_stress(constants, additions)


Note that most models offer device choices depending on your CPU/GPU
setup and preferences.

#### Example C: Model inference with the DeePMD-Kit package\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Example C: Model inference with the DeePMD-Kit package">edit</a> \| (./index.php.md)\]

Next, let's use the DPA-3.1-3M-FT model. The model checkpoint needs to
be downloaded separately from the package, as indicated and linked on
its <a
href="https://matbench-discovery.materialsproject.org/models/dpa-3.1-3m-ft"
class="external text" rel="nofollow">matbench-discovery</a> page. The
documentation links to the
<a href="https://github.com/deepmodeling/deepmd-kit"
class="external text" rel="nofollow">DeePMD-kit</a> package (see <a
href="https://docs.deepmodeling.com/projects/deepmd/en/stable/getting-started/install.html#install-python-interface-with-pip"
class="external text" rel="nofollow">pip installation instructions</a>).
Notice the file checkpoint has a `.pth` file extension, which indicates
the PyTorch workflow is the one we need.

The DeePMD-kit instructions are relatively straightforward, so adapt
them for `vasp_plugin.py`:


    from deepmd.calculator import DP
    calculator = DP(model="/path/to/dpa-3.1-3m-ft.pth")

    from vasp.force_field import AseForceField      # VASP force field wrapper class
    force_field = AseForceField(calculator)         # apply wrapper class

    def force_and_stress(constants, additions):     # to compute force and stress via the uMLFF model instead of VASP's DFT routines
        force_field.force_and_stress(constants, additions)


### Step 3: Setting up your INCAR\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Setting up your INCAR">edit</a> \| (./index.php.md)\]

Add the following tags to your [INCAR](../input-files/INCAR.md) file (the
rest of your prior setup can stay largely the same):

``` vasp-dark-link-panel
PLUGINS/FORCE_AND_STRESS = True
PLUGINS/ML_MODE = run
```

Note that this can also be written differently:

    PLUGINS {
       FORCE_AND_STRESS = True
       ML_MODE = run
    }

You may find one or the other style more intuitive to read; they are
functionally identical.

|  |
|----|
| **Important:** The [ML_MODE](../incar-tags/ML_MODE.md) and [PLUGINS/ML_MODE](../incar-tags/PLUGINS__ML_MODE.md) tags differ in scope and purpose. [ML_MODE](../incar-tags/ML_MODE.md) controls [ML_FF](../input-files/ML_FF.md) interaction (not relevant here). [PLUGINS/ML_MODE](../incar-tags/PLUGINS__ML_MODE.md) specifically controls whether plugin-computed forces are added to VASP-computed forces or substitute them entirely. [`PLUGINS/ML_MODE`](../incar-tags/PLUGINS__ML_MODE.md)` = run` ensures substitution. |

### Step 4: Run calculation\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Run calculation">edit</a> \| (./index.php.md)\]

Start your calculation the same way you usually would. If everything
works as expected, you should notice a significant speedup and no
electronic steps showing up in your [OUTCAR](../output-files/OUTCAR.md).

## Recommendations and advice\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations and advice">edit</a> \| (./index.php.md)\]

- All else being equal, try picking models with good benchmark metrics,
  broader training datasets, and fewer parameters. The number of
  parameters directly affects inference speed.

## Related tags and articles\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Plugins](../tutorials/Plugins.md), [Running GRACE force fields in
VASP](Running_GRACE_force_fields_in_VASP.md)

Files:
[Makefile.include](../misc/Makefile.include.md) "Makefile.include")

Tags: [PLUGINS/ML_MODE](../incar-tags/PLUGINS__ML_MODE.md),
[PLUGINS/FORCE_AND_STRESS](../incar-tags/PLUGINS__FORCE_AND_STRESS.md)

## References\[<a
href="/wiki/index.php?title=Running_universal_machine-learned_force_fields&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


