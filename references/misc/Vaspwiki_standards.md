<!-- Source: https://vasp.at/wiki/index.php/Vaspwiki_standards | revid: 14682 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Vaspwiki standards
- You might start a page on the INCAR-tag "tagname" as follows

&nbsp;

    {{TAGDEF|TAGNAME|val1 [{{!}} val2 {{!}} val3 {{!}} .. ] [|default] }}

Examples:

1.  {{TAGDEF|NELM|[integer]}}

    [NELM](../incar-tags/NELM.md) = \[integer\] 

2.  {{TAGDEF|NELM|[integer]|60}}

    [NELM](../incar-tags/NELM.md) = \[integer\]  
    Default: **NELM** = 60 

3.  {{TAGDEF|ISTART|0 {{!}} 1  {{!}} 2|0}}

    [ISTART](../incar-tags/ISTART.md) = 0 \| 1 \| 2  
    Default: **ISTART** = 0 

- When an INCAR-tag has more than one default (a conditional default)
  use the following construct

&nbsp;

    {{TAGDEF|TAGNAME|val1 {{!}} val2 {{!}} val3}}
    {{DEF|TAGNAME|default1|condition1|default2|condition2 [|default3|condition3] ... }}

[TAGNAME](https://vasp.at/wiki/index.php/index.php)") =
val1 \| val2 \| val3 

|                      |            |            |
|----------------------|------------|------------|
| Default: **TAGNAME** | = default1 | condition1 |
|                      | = default2 | condition2 |
|                      | = default3 | condition3 |

for instance

    {{TAGDEF|ICHARG|0 {{!}} 1 {{!}} 2 {{!}} 4}}
    {{DEF|ICHARG|2|if {{TAG|ISTART}}{{=}}0|0|else}}

[ICHARG](../incar-tags/ICHARG.md) = 0 \| 1 \| 2 \| 4 

|                     |     |                                      |
|---------------------|-----|--------------------------------------|
| Default: **ICHARG** | = 2 | if [ISTART](../incar-tags/ISTART.md)=0 |
|                     | = 0 | else                                 |

  
The TAGDEF template can harbor up to six "default\|condition"
combinations.

- Followed by

&nbsp;

    Description: {{TAG|TAGNAME}} ...
    ----
    and maybe lots of text ... like if you want to know how to put
    in an equation in LaTeX style then have a look at the source of the {{TAG|PREC}} page

Description:
[TAGNAME](https://vasp.at/wiki/index.php/index.php)")
...

------------------------------------------------------------------------

and your text maybe lots of text ... like if you want to know how to put
in an equation in LaTeX style then have a look at the source of [an
equation array](#mathsrc).

- By the way this is how to refer to all tags and files

&nbsp;

    {{TAG|TAGNAME}} and {{FILE|FILENAME}}

[TAGNAME](https://vasp.at/wiki/index.php/index.php)")
and
[FILENAME](https://vasp.at/wiki/index.php/index.php)")

- If you want to know how to quote whole pieces of input and output have
  a look at the source of [ROPT](../incar-tags/ROPT.md) and [a page with
  pieces of INCAR
  text](../methods/List_of_hybrid_functionals.md),
  or to the source of this page of course.

&nbsp;

- To create a hook to which one may jump, for instance to the following
  equation array:

    <span id="eqnarray">
    <math>
    \begin{align}
    \frac{e}{\pi} & =\int_\Omega \psi (\mathbf{r}) d\mathbf{r} \\
    a & = b \\
    \end{align}
    </math>
    </span>

$\begin{align} \frac{e}{\pi} & =\int_\Omega \psi
(\mathbf{r}) d\mathbf{r} \\ a & = b \\ \end{align}$

  
You may then jump to the aformention equation array with

    [[Vaspwiki_standards#eqnarray|an equation array]]

[an equation array](#eqnarray) or to [another
example](../incar-tags/LREAL.md) in another section.

  

- Optionally put in

&nbsp;

    == Related Tags and Sections ==
    {{TAG|PREC}},
    [[list_of_hybrid_functionals|an internal link]]

    [http://www.mediawiki.org/wiki/Help:Formatting How to format text etc]

    [http://www.mediawiki.org/wiki/Help:Links Links in a mediawiki environment]

## Related Tags and Sections
[PREC](../incar-tags/PREC.md), [an internal
link](../methods/List_of_hybrid_functionals.md)

[How to format text etc](http://www.mediawiki.org/wiki/Help:Formatting)

[Links in a mediawiki
environment](http://www.mediawiki.org/wiki/Help:Links)

- And if applicable

&nbsp;

    .... in your text somewhere ... <ref name="name1"/>
    and .. somewhere else <ref name="name2"/>
    ....
    ....
    == References ==
    <references>
    <ref name="name1">[http://link.aps.org/doi/10.1103/PhysRevB.39.4997 I. Stich, R. Car, M. Parrinello and S. Baroni, Phys Rev. B 39, 4997 (1989).]</ref>
    <ref name="name2">[http://dx.doi.org/10.1088/0953-8984/1/4/005 M.J. Gillan, J. Phys.: Condens. Matter 1, 689 (1989).]</ref>
    </references>

.... in your text somewhere ... ^([\[1\]](#cite_note-name1-1)) and ..
somewhere else ^([\[2\]](#cite_note-name2-2)) .... ....

## References
1.  [↑](#cite_ref-name1_1-0) [\|I. Stich, R. Car, M. Parrinello and S.
    Baroni, Phys Rev. B 39, 4997
    (1989).](http://link.aps.org/doi/10.1103/PhysRevB.39.4997)
2.  [↑](#cite_ref-name2_2-0) [\|M.J. Gillan, J. Phys.: Condens. Matter
    1, 689 (1989).](http://dx.doi.org/10.1088/0953-8984/1/4/005)

- End with

&nbsp;

    ----
    [[Category:INCAR]]
