<!-- Source: https://vasp.at/wiki/index.php/Metadynamics_calculations | revid: 36217 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Metadynamics calculations


### Anderson thermostat\[<a
href="/wiki/index.php?title=Metadynamics_calculations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Anderson thermostat">edit</a> \| (./index.php.md)\]

- For a metadynamics run with Andersen thermostat, one has to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Set [MDALGO](../incar-tags/MDALGO.md)=1
    ([MDALGO](../incar-tags/MDALGO.md)=11 in VASP 5.x), and choose an
    appropriate setting for
    [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)
3.  Set the parameters [HILLS_H](../incar-tags/HILLS_H.md),
    [HILLS_W](../incar-tags/HILLS_W.md), and
    [HILLS_BIN](../incar-tags/HILLS_BIN.md)
4.  Define collective variables in the
    [ICONST](../input-files/ICONST.md)-file, and set the `STATUS` parameter
    for the collective variables to 5
5.  If needed, define the bias potential in the
    [PENALTYPOT](../input-files/PENALTYPOT.md)-file

The actual time-dependent bias potential is written to the
[HILLSPOT](../incar-tags/HILLSPOT.md)-file, which is updated after
adding a new Gaussian. At the beginning of the simulation, VASP attempts
to read the initial bias potential from the
[PENALTYPOT](../input-files/PENALTYPOT.md)-file. For the continuation
of a metadynamics run, copy [HILLSPOT](../incar-tags/HILLSPOT.md) to
[PENALTYPOT](../input-files/PENALTYPOT.md). The values of all
collective variables for each MD step are listed in
[REPORT](../output-files/REPORT.md)-file, check the lines after the string
[`Metadynamics`](../theory/Metadynamics.md).

### Nose-Hoover thermostat\[<a
href="/wiki/index.php?title=Metadynamics_calculations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Nose-Hoover thermostat">edit</a> \| (./index.php.md)\]

- For a metadynamics run with Nose-Hoover thermostat, one has to:

1.  Set the standard MD-related tags: [IBRION](../incar-tags/IBRION.md)=0,
    [TEBEG](../incar-tags/TEBEG.md), [POTIM](../incar-tags/POTIM.md), and
    [NSW](../incar-tags/NSW.md)
2.  Set [MDALGO](../incar-tags/MDALGO.md)=2
    ([MDALGO](../incar-tags/MDALGO.md)=21 in VASP 5.x), and choose an
    appropriate setting for [SMASS](../incar-tags/SMASS.md)
3.  Set the parameters [HILLS_H](../incar-tags/HILLS_H.md),
    [HILLS_W](../incar-tags/HILLS_W.md), and
    [HILLS_BIN](../incar-tags/HILLS_BIN.md)
4.  Define collective variables in the
    [ICONST](../input-files/ICONST.md)-file, and set the `STATUS` parameter
    for the collective variables to 5
5.  If needed, define the bias potential in the
    [PENALTYPOT](../input-files/PENALTYPOT.md)-file

The actual time-dependent bias potential is written to the
[HILLSPOT](../incar-tags/HILLSPOT.md)-file, which is updated after
adding a new Gaussian. At the beginning of the simulation, VASP attempts
to read the initial bias potential from the
[PENALTYPOT](../input-files/PENALTYPOT.md)-file. For the continuation
of a metadynamics run, copy [HILLSPOT](../incar-tags/HILLSPOT.md) to
[PENALTYPOT](../input-files/PENALTYPOT.md). The values of all
collective variables for each MD step are listed in
[REPORT](../output-files/REPORT.md)-file, check the lines after the string
`Metadynamics`.


## Related tags and sections\[<a
href="/wiki/index.php?title=Metadynamics_calculations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md), [HILLS_H](../incar-tags/HILLS_H.md),
[HILLS_W](../incar-tags/HILLS_W.md),
[HILLS_BIN](../incar-tags/HILLS_BIN.md),
[PENALTYPOT](../input-files/PENALTYPOT.md),
[HILLSPOT](../incar-tags/HILLSPOT.md), [REPORT](../output-files/REPORT.md)

[Metadynamics](../theory/Metadynamics.md), [Nucleophilic
substitution of chloromethane by chloride using
metadynamics](../misc/Nuclephile_Substitution_CH3Cl_-_mMD3.md)

  

  

------------------------------------------------------------------------


