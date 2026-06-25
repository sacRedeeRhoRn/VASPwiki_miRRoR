<!-- Source: https://vasp.at/wiki/index.php/TITEL | revid: 25191 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TITEL


TITEL = \[string\] 

Definition: The
TITEL[^1]
tag specifies the title of a specific [POTCAR](../input-files/POTCAR.md)
file. It is also the first line of any [POTCAR](../input-files/POTCAR.md)
file. It is not possible nor necessary to set this tag in the
[INCAR](../input-files/INCAR.md) file.

------------------------------------------------------------------------

The [POTCAR](../input-files/POTCAR.md) tag
TITEL is a string composed of:

- the type of pseudopotential (either PAW for the
  [projector-augmented-wave
  formalism](../methods/Projector-augmented-wave_formalism.md)
  or US for [ultrasoft
  pseudopotentials](../input-files/Available_pseudopotentials.md) "Available pseudopotentials"),
- information about the
  <a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
  title="Exchange-correlation functional">exchange-correlation
  functional</a> (GGA for PW91, PBE for PBE, missing for LDA),
- the element symbol,
- a
  [suffix](../input-files/Available_pseudopotentials.md)
  specifying the type of potential.
- the date of the <a href="/wiki/Pseudopotential" class="mw-redirect"
  title="Pseudopotential">pseudopotential</a> creation.

In very early <a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a> releases, not all of this
information is necessarily present.

## Examples\[<a href="/wiki/index.php?title=TITEL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Examples">edit</a> \| (./index.php.md)\]

- TITEL =
  `PAW Ti_sv 26Sep2005` (Ti potential with the semicore *s* and *p*
  states added to the valence from the [potpaw_LDA.64 potential
  set](../input-files/Available_pseudopotentials.md).
- TITEL =
  `PAW_PBE Ti_sv_GW 05Dec2013` (Ti potential for
  <a href="/wiki/GW" class="mw-redirect" title="GW">GW</a> calculations
  with the semicore *s* and *p* states added to the valence from the
  [potpaw_PBE.64 potential
  set](../input-files/Available_pseudopotentials.md)
- TITEL =
  `PAW_GGA Ti_pv 07Sep2000` (Ti potential with the semicore *p* states
  added to the valence from the [PW91 (2010) potential
  set](../input-files/Available_pseudopotentials.md).
- TITEL = `US Ti` (Ti
  potential with the semicore *p* states added to the valence from the
  [PW91 USPP (2002) potential
  set](../input-files/Available_pseudopotentials.md) "Available pseudopotentials").
  For this very old pseudopotential, no information on functional,
  valency, or creation date is available.

## Related tags and articles\[<a href="/wiki/index.php?title=TITEL&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[POTCAR](../input-files/POTCAR.md),
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">pseudopotentials</a>, [available
pseudopotentials](../input-files/Available_pseudopotentials.md)

## References\[<a href="/wiki/index.php?title=TITEL&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^1]: Note that "Titel" is the German translation of the English word "title"
