<!-- Source: https://vasp.at/wiki/index.php/LWRITE_SPN | revid: 26483 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWRITE_SPN
LWRITE_SPN = .TRUE. \| .FALSE.  
Default: **LWRITE_SPN** = .FALSE. 

Description: Write **wannier90.spn** file for noncollinear calculations.

------------------------------------------------------------------------

For noncollinear calculations
([LNONCOLLINEAR](LNONCOLLINEAR.md)=T using vasp_ncl)
the **wannier90.spn** file is written when

     LWANNIER90=T ! switch on Wannier90 interface 
     LWRITE_SPN=T 

The file is formatted, and the appropriate line
(`spn_formatted = .true.`) is automatically added to the
**wannier90.win** file.

|  |
|----|
| **Warning:** Only the default setting for [SAXIS](SAXIS.md) is supported. |

|                                                |
|------------------------------------------------|
| **Mind:** Available for VASP version \> 6.4.2. |

## Related tags and articles
[LWANNIER90](LWANNIER90.md),
[LWRITE_UNK](LWRITE_UNK.md),
[LWRITE_MMN_AMN](LWRITE_MMN_AMN.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md),
[NUM_WANN](NUM_WANN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWANNIER90-_incategory-Examples)
