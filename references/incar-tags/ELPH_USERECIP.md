<!-- Source: https://vasp.at/wiki/index.php/ELPH_USERECIP | revid: 37252 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_USERECIP


ELPH_USERECIP = logical  
Default: **ELPH_USERECIP** = .FALSE. 

Description: Computes electron-phonon matrix elements in reciprocal
space instead of real space.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

The electron-phonon matrix element

$\langle \psi_{n\mathbf{k}} | \Delta V_{\mathbf{q}} |
\psi_{m\mathbf{k}'} \rangle$

can be evaluated either in real space (the default) or in reciprocal
space as a contraction over plane-wave coefficients.
`ELPH_USERECIP`` = .TRUE.`
selects the reciprocal-space path.

**Automatic activation for meta-GGAs.** When a meta-GGA functional is
used, VASP sets
`ELPH_USERECIP`` = .TRUE.`
automatically. This is required because the kinetic-energy density
contribution to the electron-phonon potential is non-local in real space
and can only be evaluated in reciprocal space.

**Band structure renormalization.** The reciprocal-space path can also
be beneficial for calculations where the number of bra k-points
($n_\mathbf{k}$) is much smaller than the number of ket
k-points ($n_{\mathbf{k}'}$), such as band structure renormalization along
high-symmetry lines. In this case the real-space path would require an
FFT for each bra state, whereas the reciprocal-space path works directly
with the stored plane-wave coefficients and avoids these transforms.

## Related tags and articles\[<a
href="/wiki/index.php?title=ELPH_USERECIP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ELPH_USEBLAS](ELPH_USEBLAS.md)
- [ELPH_RUN](ELPH_RUN.md)


