<!-- Source: https://vasp.at/wiki/index.php/LEFG | revid: 30743 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LEFG


LEFG = .TRUE. \| .FALSE.  
Default: **LEFG** = .FALSE. 

Description: The LEFG computes
the electric field gradient (EFG) at positions of the atomic nuclei.

------------------------------------------------------------------------

For LEFG=.TRUE., the electric
field gradient tensors at the positions of the atomic nuclei are
calculated using the method of Petrilli *et al.*
<sup>[\[1\]](#cite_note-petrilli:prb:1998-1)</sup>.

The EFG tensors are symmetric. The principal components *V*<sub>ii</sub>
and asymmetry parameter η are printed for each atom. Following
convention the principal components *V*<sub>ii</sub> are ordered such
that:

$|V_{zz}| > |V_{xx}| > |V_{yy}|.$

The asymmetry parameter is defined as $\eta = {(V_{yy} - V_{xx})}/
V_{zz}$. For so-called "quadrupolar nuclei", *i.e.*,
nuclei with nuclear spin I\>1/2, NMR experiments can access
*V*<sub>zz</sub> and η.

To convert the *V*<sub>zz</sub> values into the *C*<sub>q</sub> often
encountered in NMR literature, one has to specify the nuclear quadrupole
moment by means of the [QUAD_EFG](QUAD_EFG.md)-tag.

|  |
|----|
| **Mind:** Several definitions of $C_q$ are used in the NMR community, ensure that you are comparing between the same definitions in calculation and experiment. |

|  |
|----|
| **Important:** For heavy nuclei inaccuracies are to be expected because of an incomplete treatment of relativistic effects. |

A guide for calculating the electric field gradient can be found in this
[article](../tutorials/Calculating_the_electric_field_gradient.md).

## Output\[<a href="/wiki/index.php?title=LEFG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The EFG is listed atom-wise after the SCF cycle has been completed.
First, the full 3x3 tensor is printed:

      Electric field gradients (V/A^2)
     ---------------------------------------------------------------------
      ion       V_xx      V_yy      V_zz      V_xy      V_xz      V_yz
     ---------------------------------------------------------------------
        1        -         -         -         -         -         -       

The tensor is then diagonalized and reprinted:

      Electric field gradients after diagonalization (V/A^2)
      (convention: |V_zz| > |V_xx| > |V_yy|)
     ----------------------------------------------------------------------
      ion       V_xx      V_yy      V_zz     asymmetry (V_yy - V_xx)/ V_zz
     ----------------------------------------------------------------------
        1       -         -         -             -         

The corresponding eigenvectors are printed atom-wise. Finally, the
quadrupolar parameters are presented, which are commonly reported in NMR
experiments.

                NMR quadrupolar parameters

      Cq : quadrupolar parameter    Cq=e*Q*V_zz/h
      eta: asymmetry parameters     (V_yy - V_xx)/ V_zz
      Q  : nuclear electric quadrupole moment in mb (millibarn)
     ----------------------------------------------------------------------
      ion       Cq(MHz)       eta       Q (mb)
     ----------------------------------------------------------------------
        1        -             -         -                      

## Related tags and articles\[<a href="/wiki/index.php?title=LEFG&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[QUAD_EFG](QUAD_EFG.md)

[Calculating the electric field
gradient](../tutorials/Calculating_the_electric_field_gradient.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LEFG-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LEFG&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-petrilli:prb:1998_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.57.14690"
    class="external text" rel="nofollow">H. M. Petrilli, P. E. Blöchl, P.
    Blaha, and K. Schwarz, <em>Electric-field-gradient calculations using
    the projector augmented wave method</em>, Phys. Rev. B
    <strong>57</strong>, 14690 (1998).</a>


