<!-- Source: https://vasp.at/wiki/index.php/NHC_NS | revid: 32340 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NHC_NS


NHC_NS = \[integer\] 1 \| 3 \|
7  
Default: **NHC_NS** = 1 

Description: The number of subdivisions of each RESPA step used in the
integration step used in propagation of thermostat variables in the
[Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md).

------------------------------------------------------------------------

The RESPA steps used in in propagation of thermostat variables in the
[Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md)
are treated by Suzuki-Yoshida
scheme<sup>[\[1\]](#cite_note-1)[\[2\]](#cite_note-2)</sup>,
whereby each step is subdivided further into
NHC_NS parts. First, fourth,
and sixth order schemes with, 1, 3, and 7 steps, respectively, are
supported.

  

## Related tags and articles\[<a href="/wiki/index.php?title=NHC_NS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NHC_PERIOD](../misc/NHC_PERIOD.md),
[NHC_NRESPA](NHC_NRESPA.md), [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md)

------------------------------------------------------------------------


1.  [↑](#cite_ref-1)
    <a
    href="https://pubs.aip.org/aip/jmp/article/26/4/601/227573/Decomposition-formulas-of-exponential-operators"
    class="external text" rel="nofollow">M. Suzuki, J. Math. Phys. 26, 601
    (1985).</a>
2.  [↑](#cite_ref-2)
    <a
    href="https://www.sciencedirect.com/science/article/abs/pii/0375960190900923"
    class="external text" rel="nofollow">H. Yoshida, Phys. Lett. A 150, 262
    (1990).</a>


