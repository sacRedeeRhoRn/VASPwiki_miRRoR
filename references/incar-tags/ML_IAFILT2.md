<!-- Source: https://vasp.at/wiki/index.php/ML_IAFILT2 | revid: 18616 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_IAFILT2


ML_IAFILT2 = \[integer\]  
Default: **ML_IAFILT2** = 2 

Description: This tag specifies the type of angular filtering used in
the machine learning force field method.

------------------------------------------------------------------------

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Angular_filtering_MLFF_cropped.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/5b/Angular_filtering_MLFF_cropped.png/400px-Angular_filtering_MLFF_cropped.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/5b/Angular_filtering_MLFF_cropped.png/600px-Angular_filtering_MLFF_cropped.png 1.5x, /wiki/images/thumb/5/5b/Angular_filtering_MLFF_cropped.png/800px-Angular_filtering_MLFF_cropped.png 2x"
width="400" height="277" /></a>
<figcaption>Fig. 1: Square of filtering function.</figcaption>
</figure>

This tag is only used if
[ML_LAFILT2](ML_LAFILT2.md)=*.TRUE.* is set.

Following cases are possible for the angular filtering function
$\eta$ (see also <a
href="/wiki/On-the-fly_machine_learning_force_field_generation_using_Bayesian_linear_regression#Basis_set_expansion"
class="mw-redirect"
title="On-the-fly machine learning force field generation using Bayesian linear regression">here</a>):

- ML_IAFILT2=1: The angular
  filtering function is described as $\eta_{l}=\frac{1}{(2l+1)^{1/4}}$.
- ML_IAFILT2=2: The angular
  filtering
  function<sup>[\[1\]](#cite_note-boyd:book:2000-1)</sup>
  is described as $\eta_{l,a_{\mathrm{FILT}}}=\frac{1}{1+a_{\mathrm{FILT}} \[l
  (l+1)\]^{2}}$. Using this function the parameter
  $a_{\mathrm{FILT}}$ has to be defined too. It is set
  in the [INCAR](../input-files/INCAR.md) file by setting
  [ML_AFILT2](ML_AFILT2.md). This option is the default.

In the case of the angular descriptor two radial basis functions are
multiplied by each other (see <a
href="/wiki/On-the-fly_machine_learning_force_field_generation_using_Bayesian_linear_regression#Basis_set_expansion"
class="mw-redirect"
title="On-the-fly machine learning force field generation using Bayesian linear regression">here</a>).
Both basis functions use the same filtering function and hence the
filtering is done by the square of the filtering function. This is
plotted in Fig. 1 for the two different functions used for
ML_IAFILT2=1 and 2 (labeled as
TYPE1 and TYPE2, respectively). In the case of
ML_IAFILT2=2 it can be seen
that for the filtering parameter
[ML_AFILT2](ML_AFILT2.md)=0.002 and
$l$=5 the function has only a contribution of 0.15. Using
this filtering parameter the maximum cut-off for the angular quantum
number can be reduced to [ML_LMAX2](ML_LMAX2.md)=4.

  

  

## References\[<a
href="/wiki/index.php?title=ML_IAFILT2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-boyd:book:2000_1-0)
    <a href="https://link.springer.com/gp/book/9783540514879"
    class="external text" rel="nofollow">J. P. Boyd, Chebyshev and Fourier
    Spectral Methods (Dover Publications, New York, 2000).</a>


  

## Related tags and articles\[<a
href="/wiki/index.php?title=ML_IAFILT2&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ML_LMLFF](ML_LMLFF.md),
[ML_LAFILT2](ML_LAFILT2.md),
[ML_AFILT2](ML_AFILT2.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ML_IAFILT2-_incategory-Examples)

------------------------------------------------------------------------


