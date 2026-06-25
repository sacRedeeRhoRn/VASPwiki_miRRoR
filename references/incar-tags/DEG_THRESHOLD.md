<!-- Source: https://vasp.at/wiki/index.php/DEG_THRESHOLD | revid: 36280 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DEG_THRESHOLD


DEG_THRESHOLD = \[real\] 

|                            |                        |     |
|----------------------------|------------------------|-----|
| Default: **DEG_THRESHOLD** | = \$2 \times 10^{-3}\$ |     |

Description: DEG_THRESHOLD
specifies whether two eigenvalues should be treated as degenerate during
clustering of orbitals in the linear response code.
DEG_THRESHOLD is specified in
units of eV.

------------------------------------------------------------------------

This parameter is used to find degenerate clusters of orbitals. It is
used within VASP whenever linear-response calculations are performed
(either with respect to external fields or with respect to ionic
displacements). VASP internally uses an inverse-iteration solver with
imaginary shifting to solve the Sternheimer linear-response equation. If
the value is too large, non-degenerate eigenvalue pairs may be detected
as degenerate pairs. This can lead to very poor convergence or erroneous
results, in particular, for systems with low symmetry and flat semi-core
bands. Conversely, too small a value might not lead to a proper
detection of all degenerate eigenvalues. For insulating systems, this
usually does not lead to substantial errors, since the imaginary shift
can handle degenerate eigenvalue/eigenvector pairs (so VASP implements
two strategies to handle degenerate pairs and combining them yields more
robust results).

It is recommended to use small values for systems without symmetry
(e.g., around \$10^{-5}\$). For highly symmetric insulators, results
should be largely insensitive to the choice of
DEG_THRESHOLD. For metals,
degenerate states with partial occupancies must be correctly resolved to
obtain highly accurate results (so
DEG_THRESHOLD must be set to a
value that allows safe detection of degenerate states).

  

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vblue); --box-emph-color: var(--vblue); padding: 5px; color: var(--vdefault-text-nb); background: var(--vblue-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vblue);">Tip:</span></strong> If
you experience large drifts in the Born effective charges and adding
more k-points does not help, try adjusting this parameter. The total
drift in the Born effective charges (calculated with <a
href="/wiki/LEPSILON"
title="LEPSILON"><code>LEPSILON</code></a><code> = .TRUE.</code>) can be
found in the <a href="/wiki/OUTCAR" title="OUTCAR">OUTCAR</a> file, in a
block with the following form (see the final line):
<pre><code>      POSITION         DIRECTION 1           BORN EFFECTIVE CHARGE    (rigid.aug.   ionic)
 -----------------------------------------------------------------------------------------
        ***          ***          ***         ***      ***      ***   (    ***      ***  )
 -----------------------------------------------------------------------------------------
    total drift (improves with k-points):     XXX      XXX      XXX  </code></pre>
<p>This block is printed separately for each Cartesian direction. For
example, <code>DIRECTION 1</code> is the $x$ direction.</p></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=DEG_THRESHOLD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LSUBROT](LSUBROT.md),
[LEPSILON](LEPSILON.md)


