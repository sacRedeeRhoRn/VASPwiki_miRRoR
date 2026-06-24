<!-- Source: https://vasp.at/wiki/index.php/PENALTYPOT | revid: 36171 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PENALTYPOT
File that defines the bias potential for a [biased
molecular-dynamics](../categories/Category-Biased_molecular_dynamics.md)
run.

At the beginning of each
[metadynamics](../theory/Metadynamics.md) simulation, VASP
attempts to read the file PENALTYPOT containing the bias potential
acting on the geometric parameters with `STATUS=5` defined in the
[ICONST](ICONST.md) file. In analogy to the time-dependent
bias potential generated in metadynamics, the bias potential is defined
as a superposition of Gaussian hills. Each line in the PENALTYPOT file
represents one (multidimensional) Gaussian:

$x_1 x_2 ... x_m h w$,

where $x_1$ to $x_m$ stand for the position in the space of active
coordinates, and $h$ and
$w$ are the height and width of the
Gaussian, respectively. Note that both positive and negative values are
allowed for the parameter $h$.

For example, if two active coordinates with `STATUS=5` are defined in
the [ICONST](ICONST.md) file:

    R 1 5 5
    R 1 6 5 

then each line in the PENALTYPOT must contain four items. The bias
potential is defined in the following lines:

    1.6 0.8 1.0 0.2
    1.6 1.0 1.0 0.2
    1.6 1.2 1.0 0.2
    1.6 1.4 1.0 0.2
    1.6 1.6 1.0 0.2
    1.6 1.8 1.0 0.2
    1.6 2.0 1.0 0.2

## Related tags and articles
[MDALGO](../incar-tags/MDALGO.md), [ICONST](ICONST.md)

------------------------------------------------------------------------
