<!-- Source: https://vasp.at/wiki/index.php/GAMMA | revid: 29221 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GAMMA


The GAMMA file is an input
file used when [ICHARG](../incar-tags/ICHARG.md)=5 is set. It is read by
VASP during an
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a> to
incorporate additional occupation changes per k-point and orbital before
calculating a new charge density. The file's format is structured as
follows:

     567  -1  ! Number of k-points, default number of bands
     1  81  92 ! k-point index, band window of occupations to be added
     -0.88697620213424  -0.00000000000110 0.00952263319978  -0.00013538025816 -0.00003023919061  0.00036153047962 ... ! 1 nbnd row per line
      0.00952263319978   0.00013538025816 -0.90621349117750 -0.00000000000092 -0.00002036611614  0.00020787085249 ...
      ... (10 more lines)
     2  81  92
     -0.89265621432703 -0.00000000000107 -0.00944765243065  -0.00671452451385 -0.00029309275635  -0.00012146585216 
      ... (11 more lines)
     ...
     567  82  91
     -0.89056253498876  -0.00000000000112 -0.00449699353373  0.00290102672201 -0.00014095045304  0.00000787119531 ... 
     …

The file contains a small header marking the number of k-points (must be
consistent with the current number of k-points in the irreducible
Brillouin zone), and if there is a default number of bands to be assumed
per k-point. Next, is a line that increments through the k-point indices
and the current band window, i.e. the indices of bands for which the
occupation changes are read in (indices must be smaller or equal to
[NBANDS](../incar-tags/NBANDS.md)). This is followed by the actual
occupation changes as a nband times nband matrix (one row per line),
where complex number formatting is used. First number is the real part
and the second is the complex part, third is again real part, etc.

While [ICHARG](../incar-tags/ICHARG.md)=5 is set, VASP will read this file
right before the new charge density is calculated. However, VASP will
only read the file and continues calculation if an additional file
called [vasp.lock](Vasp.lock.md) is present in the
current directory. This design allows to interface to an external code
that performs between the SCF step some extra computation and updates
the KS occupations.

|  |
|----|
| **Tip:** For VASP 6.5.0 or newer compiled with [HDF5 support](../categories/Category-HDF5_support.md) enabled VASP can also read the occupation update more efficiently from the [vaspgamma.h5](Vaspgamma.h5.md) instead (the text file will take priority if both files are present). |

The procedure to construct a new charge density from the combined
occupations (KS occupations +
GAMMA file) is as follows: The
additional occupation changes from the
GAMMA can be a off-diagonal
matrix $\Delta N_{n n'}({\bf k})$, new natural orbitals are found by a transformation
matrix $V$. This
transformation is found by diagonalizing the total correlated density
matrix:

 $f'_{\nu {\bf k}} \delta_{\nu
\nu'} = \sum_{n n'} V_{\nu n} \left\[ f_{n {\bf k}} \delta_{n n'} +
\Delta N_{n n'} \right\] V^\*_{n' \nu'},$ 

 $|\Psi'_{\nu {\bf k}}\rangle
= \sum_n V_{\nu n} |\Psi_{n {\bf k}}\rangle$ 

The new orbitals $|\Psi'_{\nu {\bf k}}\rangle$ together with $f'_{\nu {\bf k}}$ are then used to calculate the new charge density. For
more information see
Ref.<sup>[\[1\]](#cite_note-schueler:jpcm:30-1)</sup>
Eq. (30)-(32).

The TRIQS software
package<sup>[\[2\]](#cite_note-parcollet:cpc:196-2)</sup>
makes use of it to perform charge self-consistent DFT plus dynamical
mean field theory (DMFT)
calculations<sup>[\[3\]](#cite_note-merkel:joss:7-3)[\[4\]](#cite_note-aichhorn:cpc:204-4)</sup>,
and provides tutorials on how to perform such calculations with
VASP<sup>[\[5\]](#cite_note-triqsdfttoolstutorial:web-5)[\[6\]](#cite_note-soliddmfttutorial:web-6)</sup>.

|  |
|----|
| **Mind:** The text file based reading of occupation updates only works for non spin-polarized calculations when reading from the GAMMA file. Please use the hdf5 interface in VASP 6.5.0 or newer ([vaspgamma.h5](Vaspgamma.h5.md)) for spin polarized calculations. |

## Related tags and articles\[<a href="/wiki/index.php?title=GAMMA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICHARG](../incar-tags/ICHARG.md),
[vasp.lock](Vasp.lock.md),
[vaspgamma.h5](Vaspgamma.h5.md),[DFT+DMFT](../tutorials/DFT+DMFT_calculations.md)

## References\[<a href="/wiki/index.php?title=GAMMA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-schueler:jpcm:30_1-0)
    <a href="https://doi.org/10.1088/1361-648X/aae80a" class="external text"
    rel="nofollow">M. Schüler, O. E. Peil, G. J. Kraberger, R. Pordzik, M.
    Marsman, G. Kresse, T. O. Wehling, and M. Aichhorn, Journal of Physics:
    Condensed Matter <strong>30</strong>, 475901 (2018).</a>
2.  [↑](#cite_ref-parcollet:cpc:196_2-0)
    <a href="http://dx.doi.org/10.1016/j.cpc.2015.04.023"
    class="external text" rel="nofollow">O. Parcollet, M. Ferrero, T. Ayral,
    H. Hafermann, I. Krivenko, L. Messio and P. Seth, Computer Physics
    Communications <strong>196</strong>, 398 (2015).</a>
3.  [↑](#cite_ref-merkel:joss:7_3-0)
    <a href="https://doi.org/10.21105/joss.04623" class="external text"
    rel="nofollow">M. E. Merkel, A. Carta, S. Beck and Alexander Hampel,
    Journal of Open Source Software <strong>7</strong>, 77 (2022).</a>
4.  [↑](#cite_ref-aichhorn:cpc:204_4-0)
    <a href="https://doi.org/10.1016/j.cpc.2016.03.014"
    class="external text" rel="nofollow">M. Aichhorn, L. Pourovskii, P.
    Seth, V. Vildosola, M. Zingl, O. E. Peil, X. Deng, J. Mravlje, G. J.
    Kraberger, C. Martins, M. Ferrero, O. Parcollet, Computer Physics
    Communications <strong>204</strong>, 200 (2016).</a>
5.  [↑](#cite_ref-triqsdfttoolstutorial:web_5-0)
    <a
    href="https://triqs.github.io/dft_tools/latest/tutorials.html#vasp-interface-examples"
    class="external text"
    rel="nofollow">triqs.github.io/dft_tools/latest/tutorials.html#vasp-interface-examples
    (2024).</a>
6.  [↑](#cite_ref-soliddmfttutorial:web_6-0)
    <a
    href="https://triqs.github.io/solid_dmft/tutorials/PrNiO3_csc_vasp_plo_cthyb/tutorial.html"
    class="external text"
    rel="nofollow">triqs.github.io/solid_dmft/tutorials/PrNiO3_csc_vasp_plo_cthyb/tutorial
    (2024).</a>


