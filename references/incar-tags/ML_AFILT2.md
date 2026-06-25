<!-- Source: https://vasp.at/wiki/index.php/ML_AFILT2 | revid: 16596 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_AFILT2


ML_AFILT2 = \[real\]  
Default: **ML_AFILT2** = 0.002 

Description: This tag sets the filtering parameter for the angular
filtering for [ML_IAFILT2](ML_IAFILT2.md) in the machine
learning force field method.

------------------------------------------------------------------------

This tag is only used if
[ML_LAFILT2](ML_LAFILT2.md)=*.TRUE.* and
[ML_IAFILT2](ML_IAFILT2.md)=2 are used.

The angular filtering
function<sup>[\[1\]](#cite_note-boyd:book:2000-1)</sup>
for [ML_IAFILT2](ML_IAFILT2.md)=2 is described as
$\eta_{l,a_{\mathrm{FILT}}}=\frac{1}{1+a_{\mathrm{FILT}} \[l
(l+1)\]^{2}}$. The tag
ML_AFILT2 sets the parameter
$a_{\mathrm{FILT}}$.

## References\[<a
href="/wiki/index.php?title=ML_AFILT2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-boyd:book:2000_1-0)
    <a href="https://link.springer.com/gp/book/9783540514879"
    class="external text" rel="nofollow">J. P. Boyd, Chebyshev and Fourier
    Spectral Methods (Dover Publications, New York, 2000).</a>


  

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_AFILT2&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LAFILT2](ML_LAFILT2.md),
[ML_IAFILT2](ML_IAFILT2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_AFILT2-_incategory-Examples)

------------------------------------------------------------------------


