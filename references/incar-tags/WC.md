<!-- Source: https://vasp.at/wiki/index.php/WC | revid: 27059 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WC
WC = \[real\]  
Default: **WC** = 1000. 

Description: WC specifies the weight factor for each step in Broyden
mixing scheme ([IMIX](IMIX.md)=4).

------------------------------------------------------------------------

- WC\>0

Set all weights identical to WC (resulting in Pulay's mixing method), up
to now Pulay's scheme was always superior to Broyden's 2^(nd) method.

- WC=0

Switch to Broyden's 2^(nd) method, i.e., set the weight for the last
step equal to 1000 and all other weights equal to 0.

- WC\<0 (implemented for test purposes: **not** recommended)

Try some automatic setting of the weights according to:

$W_{\rm iter}=0.01 |{\rm WC}|/||\rho_{\rm
out}-\rho_{\rm in}||_{\rm precond.}\\$

in order to set small weights for the first steps and increase weights
for the last steps.

## Related tags and sections
[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[BMIX](BMIX.md), [AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [AMIN](AMIN.md),
[MIXPRE](MIXPRE.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-WC-_incategory-Examples)
