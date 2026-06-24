<!-- Source: https://vasp.at/wiki/index.php/LDAU | revid: 36499 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDAU
LDAU = .TRUE. \| .FALSE.  
Default: **LDAU** = .FALSE. 

Description: LDAU=.TRUE. switches on DFT+U.

------------------------------------------------------------------------

LDAU is the main control tag to switch on DFT+U. Check
[LDAUTYPE](LDAUTYPE.md) for an overview of the available
methods. A typical setup in the INCAR file may include

     LDAU      = .TRUE.
     LDAUTYPE  = 2 
     LDAUL     = 2 -1      # l quantum number where U is added for each atom; -1 is no U added
     LDAUU     = 7.00 0.00 # on-site Coulomb interaction (in eV) for each atom 
     LDAUJ     = 1.00 0.00 # on-site exchange interaction (in eV) for each atom
     LMAXMIX   = 4

**Note on band-structure calculation**: The
[CHGCAR](../input-files/CHGCAR.md) file contains only information up to
angular momentum quantum number $l$=[LMAXMIX](LMAXMIX.md) for the [on-site PAW
occupancy matrices](LDAUTYPE.md). When the
[CHGCAR](../input-files/CHGCAR.md) file is read and kept fixed in the
course of the calculations ([ICHARG](ICHARG.md)=11), the
results will necessarily be not identical to a self-consistent run. The
deviations are often large for DFT+U calculations. For the calculation
of band structures within the DFT+U approach, it is hence strictly
required to increase [LMAXMIX](LMAXMIX.md) to 4
($d$ elements) and 6
($f$ elements).

## Related tags and articles
[LDAUTYPE](LDAUTYPE.md), [LDAUL](LDAUL.md),
[LDAUU](LDAUU.md), [LDAUJ](LDAUJ.md),
[LDAUPRINT](LDAUPRINT.md),
[LMAXMIX](LMAXMIX.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LDAU-_incategory-Examples)

------------------------------------------------------------------------
