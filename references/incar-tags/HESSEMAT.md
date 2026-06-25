<!-- Source: https://vasp.at/wiki/index.php/HESSEMAT | revid: 36964 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HESSEMAT


HESSEMAT defines the Hesse
matrix in Cartesian coordinates ($\underline{\mathbf{H}}^\mathbf{x}$ ) for the use in
[Thermodynamic integration with harmonic
reference](../theory/Thermodynamic_integration.md).
For a system containing $N$ atoms,
HESSEMAT has
$(3N+1)(N+1)$ lines. The first line specifies potential
energy $V_{0,\mathbf{x}}(\mathbf{x}_0)$ (in eV) of the
relaxed system for which $\underline{\mathbf{H}}^\mathbf{x}$ is computed. The
following $3N$ lines are
reserved for positions in fractional coordinates of all atoms
constituting the system, whereby each line should contain three
components of position vector of a single atom. The remaining part of
HESSEMAT consist of
$3N$ block of $N+1$ lines
each. Each block contains information related to a single eigenmode of
$\underline{\mathbf{H}}^\mathbf{x}$: the first line
specified the eigenvalue (in eV/${\AA}^2$) and
remaining and $N$ lines the
corresponding eigenvector (in Cartesian coordinates) in a 3-column
format.

    0.0
     -0.036085604 0.076532881 0.201816325
     0.039916413 -0.004546843 -0.247837560
     -0.038534014 0.141427355 0.040890125
     -0.092442988 0.033140338 0.826785057
     0.039918890 0.053102950 -0.410224011
    ...
    11.4727211094758
     -0.114601402 0.254426349 -0.000007448
     0.334610544 0.179303391 0.000007134
     -0.102146090 -0.705453702 0.000006701
     -0.386604822 0.060633342 0.000000305
     0.268741770 0.211090621 -0.000006692

How to run thermodynamic integration calculations is given
[here](../tutorials/Thermodynamic_integration_calculations.md).

## Related tags and articles\[<a href="/wiki/index.php?title=HESSEMAT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[TILAMBDA](TILAMBDA.md), [REPORT](../output-files/REPORT.md)


