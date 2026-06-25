<!-- Source: https://vasp.at/wiki/index.php/Running_GRACE_force_fields_in_VASP | revid: 35699 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Running GRACE force fields in VASP


|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

Pre-trained
<a href="https://gracemaker.readthedocs.io/" class="external text"
rel="nofollow">GRACE</a> machine-learned force fields can be used as an
alternative to [VASP-native force
fields](../categories/Category-Machine-learned_force_fields.md)
to drive essentially every VASP simulation which uses the the
prediction-only mode [`ML_MODE`](../incar-tags/ML_MODE.md)` = run`. This
includes [molecular dynamics
simulations](https://vasp.at/wiki/index.php/Category:Molecular_dynamics),
[ionic
optimization](../tutorials/Structure_optimization.md)
(see [IBRION](../incar-tags/IBRION.md)) and [advanced sampling
techniques](../categories/Category-Advanced_molecular-dynamics_sampling.md).
To be able to use GRACE force fields VASP must be built with
[VASPml](VASPml_library.md) (`-Dlibvaspml`) **and**
GRACE support (`-DVASPML_ENABLE_GRACE`), for details see the [build
customization
options](../misc/Makefile.include.md) "Makefile.include").

|  |
|----|
| **Warning:** Due to an incompatibility in the interface layer GRACE force fields from versions 0.5.8 and 0.5.9 of `tensorpotential` cannot be used together with VASP. A fix is currently work in progress. In the meantime please use force fields from `tensorpotential` 0.5.7. Be aware that for these models the `metadata.json` file generation step is mandatory (see box below). |

## Models\[<a
href="/wiki/index.php?title=Running_GRACE_force_fields_in_VASP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Models">edit</a> \| (./index.php.md)\]

The easiest way to obtain <a
href="https://gracemaker.readthedocs.io/en/latest/gracemaker/foundation/"
class="external text" rel="nofollow">GRACE models</a> is to download
them via the <a href="https://pypi.org/project/tensorpotential/"
class="external text" rel="nofollow">tensorpotential package</a>,
directly with `pip` or within a dedicated
<a href="https://en.wikipedia.org/wiki/Conda_(package_manager)"
class="external text" rel="nofollow">conda</a> environment.

|  |
|----|
| **Tip:** The `tensorpotential` package is **not** a runtime dependency of VASP but the most convenient way of listing and retrieving available models. Besides downloading a model the package is neither required for compiling nor for running VASP with GRACE force fields. |

Install `tensorpotential` and all its dependencies simply with:

    pip install tensorpotential==0.5.7

After installation the command line tool `grace_models` becomes
available. First, inspect available models with

    grace_models list

which will produce output like this:


    ...
    Available models:
    ...
    ================================================================================
    GRACE-2L-OMAT
        DESCRIPTION: A two-layer semi-local GRACE model, fitted on the OMat24 dataset, with fixed 6 A cutoff.
        PATH: /fsc/home/singraber/.cache/grace/GRACE-2L-OMAT
        CHECKPOINT: AVAILABLE, BUT NOT DOWNLOADED
        LICENSE: Academic Software License
    ================================================================================
    ...


<a
href="https://gracemaker.readthedocs.io/en/latest/gracemaker/foundation/"
class="external text" rel="nofollow">Select a model</a> and download it
with the following command:

    grace_models download [MODEL_NAME]

Given the example model above the command would be
`grace_models download GRACE-2L-OMAT`. The GRACE model will be
automatically downloaded and unpacked to the directory
`~/.cache/grace/`.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vgrey); --box-emph-color: var(--vgrey); padding: 5px; color: var(--vdefault-text-nb); background: var(--vgrey-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vgrey);">Hint for models created
with <code>tensorpotential</code> version &lt; 0.5.9:</span></strong>
VASP requires the file <code>metadata.json</code> to be present inside
the model directory. This file is automatically shipped with
<code>tensorpotential</code> for models created since version 0.5.9. If
you have an older version and the file is not present, please try to
upgrade <code>tensorpotential</code> and re-download the models. Or,
alternatively, create it from the <code>metadata.yaml</code> file with a
Python script containing the following code snippet:
<div
class="mw-highlight mw-highlight-lang-python mw-content-ltr mw-highlight-lines"
dir="ltr">
<pre><code>#!/usr/bin/env python
import yaml
import json
import pathlib
import sys
&#10;path = pathlib.Path(sys.argv[1])
&#10;with path.open() as f:
    data = yaml.safe_load(f)
&#10;with path.with_suffix(&quot;.json&quot;).open(&#39;w&#39;) as f:
    json.dump(data, f)</code></pre>
</div>
Save the Python code in a file, e.g. <code>grace_yaml2json.py</code>,
and run it with:
<div class="mw-highlight mw-highlight-lang-shell mw-content-ltr"
dir="ltr">
<pre><code>python grace_yaml2json.py ~/.cache/grace/MODEL_NAME/metadata.yaml</code></pre>
</div>
This will automatically generate the missing JSON file in the model
directory.</td>
</tr>
</tbody>
</table>

## Select GRACE model in VASP\[<a
href="/wiki/index.php?title=Running_GRACE_force_fields_in_VASP&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Select GRACE model in VASP">edit</a> \| (./index.php.md)\]

In the [INCAR](../input-files/INCAR.md) file the GRACE force field method
must be selected via [`ML_TYPE`](../incar-tags/ML_TYPE.md)` = grace` and
the model may be specified via
[ML_GRACE_MODEL](../incar-tags/ML_GRACE_MODEL.md). A minimal block
of tags could look like this:

    ...
    # MD related settings, etc.
    ...
    # ML force field settings
    ML_LMLFF       = .TRUE.
    ML_LIB         = .TRUE.
    ML_MODE        = run
    ML_TYPE        = grace
    ML_GRACE_MODEL = GRACE-2L-OMAT
    ...

|  |
|----|
| **Important:** The GRACE force field predictions are automatically offloaded to the GPU if one is available. However, currently parallelism via MPI is not supported when running GRACE force fields. Hence, start VASP with `mpirun -np 1 ...`. |


