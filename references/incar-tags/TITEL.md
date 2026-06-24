<!-- Source: https://vasp.at/wiki/index.php/TITEL | revid: 25191 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TITEL
TITEL = \[string\] 

Definition: The TITEL^([\[1\]](#cite_note-1)) tag specifies the title of
a specific [POTCAR](../input-files/POTCAR.md) file. It is also the first
line of any [POTCAR](../input-files/POTCAR.md) file. It is not possible nor
necessary to set this tag in the [INCAR](../input-files/INCAR.md) file.

------------------------------------------------------------------------

The [POTCAR](../input-files/POTCAR.md) tag TITEL is a string composed of:

- the type of pseudopotential (either PAW for the
  [projector-augmented-wave
  formalism](../methods/Projector-augmented-wave_formalism.md)
  or US for [ultrasoft
  pseudopotentials](../input-files/Available_pseudopotentials.md) "Available pseudopotentials"),
- information about the [exchange-correlation
  functional](../redirects/Exchange-correlation_functional.md)
  (GGA for PW91, PBE for PBE, missing for LDA),
- the element symbol,
- a
  [suffix](../input-files/Available_pseudopotentials.md)
  specifying the type of potential.
- the date of the
  [pseudopotential](../redirects/Pseudopotential.md) creation.

In very early
[pseudopotentials](../redirects/Pseudopotentials.md) releases,
not all of this information is necessarily present.

## Examples
- TITEL = `PAW Ti_sv 26Sep2005` (Ti potential with the semicore *s* and
  *p* states added to the valence from the [potpaw_LDA.64 potential
  set](../input-files/Available_pseudopotentials.md).
- TITEL = `PAW_PBE Ti_sv_GW 05Dec2013` (Ti potential for
  [GW](../redirects/GW.md) calculations with the semicore *s* and *p* states
  added to the valence from the [potpaw_PBE.64 potential
  set](../input-files/Available_pseudopotentials.md)
- TITEL = `PAW_GGA Ti_pv 07Sep2000` (Ti potential with the semicore *p*
  states added to the valence from the [PW91 (2010) potential
  set](../input-files/Available_pseudopotentials.md).
- TITEL = `US Ti` (Ti potential with the semicore *p* states added to
  the valence from the [PW91 USPP (2002) potential
  set](../input-files/Available_pseudopotentials.md) "Available pseudopotentials").
  For this very old pseudopotential, no information on functional,
  valency, or creation date is available.

## Related tags and articles
[POTCAR](../input-files/POTCAR.md),
[pseudopotentials](../redirects/Pseudopotentials.md),
[available
pseudopotentials](../input-files/Available_pseudopotentials.md)

## References
1.  [↑](#cite_ref-1) Note that "Titel" is the German translation of the
    English word "title"
