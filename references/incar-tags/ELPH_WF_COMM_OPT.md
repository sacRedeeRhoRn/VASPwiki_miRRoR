<!-- Source: https://vasp.at/wiki/index.php/ELPH_WF_COMM_OPT | revid: 32914 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WF_COMM_OPT


ELPH_WF_COMM_OPT =
\[integer\]  
Default: **ELPH_WF_COMM_OPT** = 0 

Description: Selects the MPI communication pattern used to exchange
orbitals between different MPI ranks.

|  |
|----|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The available options are:

- **0** — Use two-sided MPI communication (default)
- **1** — Use one-sided MPI communication

Some MPI libraries have shown instability or performance issues when
using one-sided communication. If unexpected behavior occurs, it is
recommended to keep the default setting
`ELPH_WF_COMM_OPT`` = 0`.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_WF_COMM_OPT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_WF_CACHE_PREFILL](ELPH_WF_CACHE_PREFILL.md)
- [ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md)


