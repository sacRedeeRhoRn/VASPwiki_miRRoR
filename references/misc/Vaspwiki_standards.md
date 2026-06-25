<!-- Source: https://vasp.at/wiki/index.php/Vaspwiki_standards | revid: 14682 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Vaspwiki standards


- You might start a page on the INCAR-tag "tagname" as follows

<!-- -->

    TAGDEF|TAGNAME|val1 [| val2 | val3 | .. ] [|default]

Examples:

1.  TAGDEF|NELM|[integer]

    [NELM](../incar-tags/NELM.md) = \[integer\] 

2.  TAGDEF|NELM|[integer]|60

    [NELM](../incar-tags/NELM.md) = \[integer\]  
    Default: **NELM** = 60 

3.  TAGDEF|ISTART|0 | 1  | 2|0

    [ISTART](../incar-tags/ISTART.md) = 0 \| 1 \| 2  
    Default: **ISTART** = 0 

- When an INCAR-tag has more than one default (a conditional default)
  use the following construct

<!-- -->

    TAGDEF|TAGNAME|val1 | val2 | val3
    DEF|TAGNAME|default1|condition1|default2|condition2 [|default3|condition3] ...

<a href="/wiki/index.php?title=TAGNAME&amp;action=edit&amp;redlink=1"
class="new" title="TAGNAME (page does not exist)">TAGNAME</a> = val1 \|
val2 \| val3 

|                      |            |            |
|----------------------|------------|------------|
| Default: **TAGNAME** | = default1 | condition1 |
|                      | = default2 | condition2 |
|                      | = default3 | condition3 |

for instance

    TAGDEF|ICHARG|0 | 1 | 2 | 4
    DEF|ICHARG|2|if ISTART=0|0|else

[ICHARG](../incar-tags/ICHARG.md) = 0 \| 1 \| 2 \| 4 

|                     |     |                                      |
|---------------------|-----|--------------------------------------|
| Default: **ICHARG** | = 2 | if [ISTART](../incar-tags/ISTART.md)=0 |
|                     | = 0 | else                                 |

  
The TAGDEF template can harbor up to six "default\|condition"
combinations.

- Followed by

<!-- -->

    Description: TAGNAME ...
    ----
    and maybe lots of text ... like if you want to know how to put
    in an equation in LaTeX style then have a look at the source of the PREC page

Description:
<a href="/wiki/index.php?title=TAGNAME&amp;action=edit&amp;redlink=1"
class="new" title="TAGNAME (page does not exist)">TAGNAME</a> ...

------------------------------------------------------------------------

and your text maybe lots of text ... like if you want to know how to put
in an equation in LaTeX style then have a look at the source of
<a href="#mathsrc" class="mw-selflink-fragment">an equation array</a>.

- By the way this is how to refer to all tags and files

<!-- -->

    TAGNAME and FILENAME

<a href="/wiki/index.php?title=TAGNAME&amp;action=edit&amp;redlink=1"
class="new" title="TAGNAME (page does not exist)">TAGNAME</a> and
<a href="/wiki/index.php?title=FILENAME&amp;action=edit&amp;redlink=1"
class="new" title="FILENAME (page does not exist)">FILENAME</a>

- If you want to know how to quote whole pieces of input and output have
  a look at the source of [ROPT](../incar-tags/ROPT.md) and [a page with
  pieces of INCAR
  text](../methods/List_of_hybrid_functionals.md),
  or to the source of this page of course.

<!-- -->

- To create a hook to which one may jump, for instance to the following
  equation array:

 

    
    <math>
    \begin{align}
    \frac{e}{\pi} & =\int_\Omega \psi (\mathbf{r}) d\mathbf{r} \\
    a & = b \\
    \end{align}
    </math>
    

 $\begin{align} \frac{e}{\pi} &
=\int_\Omega \psi (\mathbf{r}) d\mathbf{r} \\ a & = b \\ \end{align}$ 

  
You may then jump to the aformention equation array with

    [[Vaspwiki_standards#eqnarray|an equation array]]

<a href="#eqnarray" class="mw-selflink-fragment">an equation array</a>
or to [another example](../incar-tags/LREAL.md) in another section.

  

- Optionally put in

<!-- -->

    == Related Tags and Sections ==
    PREC,
    [[list_of_hybrid_functionals|an internal link]]

    [http://www.mediawiki.org/wiki/Help:Formatting How to format text etc]

    [http://www.mediawiki.org/wiki/Help:Links Links in a mediawiki environment]

## Related Tags and Sections\[<a
href="/wiki/index.php?title=Vaspwiki_standards&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[PREC](../incar-tags/PREC.md), [an internal
link](../methods/List_of_hybrid_functionals.md)

<a href="http://www.mediawiki.org/wiki/Help:Formatting"
class="external text">How to format text etc</a>

<a href="http://www.mediawiki.org/wiki/Help:Links"
class="external text">Links in a mediawiki environment</a>

- And if applicable

<!-- -->

    .... in your text somewhere ... <ref name="name1"/>
    and .. somewhere else <ref name="name2"/>
    ....
    ....
    == References ==
    <references>
    <ref name="name1">[http://link.aps.org/doi/10.1103/PhysRevB.39.4997 I. Stich, R. Car, M. Parrinello and S. Baroni, Phys Rev. B 39, 4997 (1989).]</ref>
    <ref name="name2">[http://dx.doi.org/10.1088/0953-8984/1/4/005 M.J. Gillan, J. Phys.: Condens. Matter 1, 689 (1989).]</ref>
    </references>

.... in your text somewhere ...
<sup>[\[1\]](#cite_note-name1-1)</sup>
and .. somewhere else
<sup>[\[2\]](#cite_note-name2-2)</sup>
.... ....

## References\[<a
href="/wiki/index.php?title=Vaspwiki_standards&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-name1_1-0)
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.39.4997"
    class="external text" rel="nofollow">|I. Stich, R. Car, M. Parrinello
    and S. Baroni, Phys Rev. B 39, 4997 (1989).</a>
2.  [↑](#cite_ref-name2_2-0)
    <a href="http://dx.doi.org/10.1088/0953-8984/1/4/005"
    class="external text" rel="nofollow">|M.J. Gillan, J. Phys.: Condens.
    Matter 1, 689 (1989).</a>


- End with

<!-- -->

    ----
    [[Category:INCAR]]


