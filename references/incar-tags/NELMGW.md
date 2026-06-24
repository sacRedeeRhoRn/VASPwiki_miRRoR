<!-- Source: https://vasp.at/wiki/index.php/NELMGW | revid: 26712 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NELMGW
NELMGW = \[integer\]  
Default: **NELMGW** = 1 

Description: NELMGW sets the number of self-consistent GW steps.
Available as of 6.3.0.

------------------------------------------------------------------------

This tag is effective for [ALGO](ALGO.md)=EVGW\[0\] \|
QPGW\[0\] \| GW\[0\]\[R\]\[K\] and ignored otherwise. For instance

    ALGO = EVGW0
    NELMGW = 4

performs a [partially self-consistent GW
calculations](../redirects/GW_calculations.md), where
$G$ is updated four times.

Omit [NBANDS](NBANDS.md) and [NELM](NELM.md) to
select the [single-step GW
procedure](../redirects/GW_calculations.md).

  

## Related tags and articles
[ALGO](ALGO.md), [GW
calculations](../redirects/GW_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NELMGW-_incategory-Examples)

------------------------------------------------------------------------
