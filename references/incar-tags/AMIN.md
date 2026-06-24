<!-- Source: https://vasp.at/wiki/index.php/AMIN | revid: 27037 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# AMIN
AMIN = \[real\]  
Default: **AMIN** =
min(0.1,[AMIX](AMIX.md),[AMIX_MAG](AMIX_MAG.md)) 

Description: AMIN specifies the minimal mixing parameter in Kerker's
initial approximation^([\[1\]](#cite_note-kerker:prb:1981-1)) to the
charge-dielectric function used in the
Broyden^([\[2\]](#cite_note-bluegel:phd:1988-2)[\[3\]](#cite_note-johnson:prb:1988-3))/Pulay^([\[4\]](#cite_note-pulay:cpl:1980-4))
mixing scheme ([IMIX](IMIX.md)=4,
[INIMIX](INIMIX.md)=1).

------------------------------------------------------------------------

Kerker's initial approximation^([\[1\]](#cite_note-kerker:prb:1981-1))
for the charge-dielectric function is given by

$\max\left(\frac{AG^2}{G^2+B^2},A_{\rm
min}\right),$

where $A$=[AMIX](AMIX.md),
$B$=[BMIX](BMIX.md), and
$A_{\rm min}$=AMIN.

## Related tags and articles
[IMIX](IMIX.md), [INIMIX](INIMIX.md),
[MAXMIX](MAXMIX.md), [AMIX](AMIX.md),
[BMIX](BMIX.md), [AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md), [MIXPRE](MIXPRE.md),
[WC](WC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-AMIN-_incategory-Examples)

## References
1.  ↑ ^([a](#cite_ref-kerker:prb:1981_1-0))
    ^([b](#cite_ref-kerker:prb:1981_1-1)) [G. P. Kerker, *Efficient
    iteration scheme for self-consistent pseudopotential calculations*,
    Phys. Rev. B **23**, 3082
    (1981).](https://doi.org/10.1103/PhysRevB.23.3082)
2.  [↑](#cite_ref-bluegel:phd:1988_2-0) [S. Blügel, PhD Thesis, RWTH
    Aachen (1988).](http://hdl.handle.net/2128/18476)
3.  [↑](#cite_ref-johnson:prb:1988_3-0) [D. D. Johnson, Phys. Rev. B
    **38**, 12807 (1988)](https://doi.org/10.1103/PhysRevB.38.12807)
4.  [↑](#cite_ref-pulay:cpl:1980_4-0) [P. Pulay, Chem. Phys. Lett.
    **73**, 393 (1980).](https://doi.org/10.1016/0009-2614(80)80396-4)
