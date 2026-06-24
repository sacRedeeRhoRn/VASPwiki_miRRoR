<!-- Source: https://vasp.at/wiki/index.php/LNICSALL | revid: 34599 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNICSALL
LNICSALL = .TRUE. \| .FALSE.  
Default: **LNICSALL** = .FALSE. 

Description: LNICSALL=.TRUE. calculates the NICS at the positions on the
fine FFT grid [NGXF](NGXF.md) x [NGYF](NGYF.md) x
[NGZF](NGZF.md).

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

LNICSALL=.TRUE. ensures that the FFT grid [NGXF](NGXF.md) x
[NGYF](NGYF.md) x [NGZF](NGZF.md) is used to
calculate the NICS (nucleus-independent chemical shift) points. These
chemical shieldings will be printed to [NICS](NICS.md).

|  |
|----|
| **Mind:** If `LNICSALL`` = True` is set, and [POSNICS](POSNICS.md) is also present, LNICSALL will take precedent. |

## Related tags and articles
[LCHIMAG](LCHIMAG.md), [NUCIND](NUCIND.md),
[NICS](NICS.md),
[tutorial](https://www.vasp.at/tutorials/latest/nmr/part3/#NMR-e11)
