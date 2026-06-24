<!-- Source: https://vasp.at/wiki/index.php/LEPSILON | revid: 34646 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LEPSILON
LEPSILON = .TRUE. \| .FALSE.  
Default: **LEPSILON** = .FALSE. 

Description: LEPSILON=.TRUE. determines the static dielectric matrix,
ion-clamped piezoelectric tensor, and the Born effective charges using
density functional perturbation theory.

------------------------------------------------------------------------

Determines the static ion-clamped dielectric matrix using [density
functional perturbation
theory](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)
(DFPT). The dielectric matrix is calculated with and without local field
effects. Usually, local field effects are determined on the Hartree
level, i.e. including changes of the Hartree potential. To include
microscopic changes of the exchange-correlation potential the tag
[LRPA](LRPA.md)=.FALSE. must be set. The method is explained
in detail in paper by Gajdoš *et al.*
^([\[1\]](#cite_note-gajdos:hummer:2006-1)) and closely follows the
original work of Baroni and Resta
^([\[2\]](#cite_note-baroni:resta:1986-2)). A summation over empty
conduction band states is not required, instead the usual expressions in
perturbation theory ([LOPTICS](LOPTICS.md)=.TRUE.),

$| \nabla_{\mathbf{k}}
|\tilde{u}_{n\mathbf{k}} \rangle = \sum_{n'\ne n} \frac{ |
\tilde{u}_{n'\mathbf{k}} \rangle \langle \tilde{u}_{n'\mathbf{k}} |
\frac{\partial\\ (\mathbf{H}(\mathbf k) -\epsilon_{n\mathbf{k}}
\mathbf{S}(\mathbf k))}{ \partial {\mathbf{k}}} |
\tilde{u}_{n\mathbf{k}} \rangle }{\epsilon_{n\mathbf{k}}-
\epsilon_{n'\mathbf{k}}},$

are rewritten as linear Sternheimer equations:

$\left( \mathbf{H}(\mathbf k) -
\epsilon_{n\mathbf k} \mathbf{S}(\mathbf k) \right) |
\nabla_{\mathbf{k}} \tilde{u}_{n\mathbf{k}} \rangle = - \frac{\partial
\\(\mathbf{H}(\mathbf k)- \epsilon_{n\mathbf{k}} \mathbf{S}(\mathbf k))
} { \partial {\mathbf{k}}} | \tilde{u}_{n\mathbf{k}} \rangle .$

The solution of this equation involves similar iterative techniques as
the conventional selfconsistency cycles. Hence, for each element of the
dielectric matrix several lines will be written to the `stdout` and
[OSZICAR](../output-files/OSZICAR.md). These possess a similar structure as
for conventional selfconsistent or non-selfconsistent calculations (a
residual minimization scheme is used to solve the linear equation, other
schemes such as Davidson do not apply to a linear equation):

           N       E              dE             d eps       ncg     rms          rms(c)
    RMM:   1    -0.14800E+01   -0.85101E-01   -0.72835E+00   220   0.907E+00    0.146E+00
    RMM:   2    -0.14248E+01    0.55195E-01   -0.27994E-01   221   0.449E+00    0.719E-01
    RMM:   3    -0.13949E+01    0.29864E-01   -0.10673E-01   240   0.322E+00    0.131E-01
    RMM:   4    -0.13949E+01    0.13883E-04   -0.31511E-03   242   0.600E-01    0.336E-02
    RMM:   5    -0.13949E+01    0.28357E-04   -0.25757E-04   228   0.177E-01    0.126E-02

It is important to note that exact values for the dielectric matrix are
obtained even if only valence band states are calculated. Hence this
method does not require increasing the [NBANDS](NBANDS.md)
parameter. The final values for the static dielectric matrix can be
found in the [OUTCAR](../output-files/OUTCAR.md) file after the lines

     MICROSCOPIC STATIC DIELECTRIC TENSOR (excluding local field effects)

and

     MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT)

The values found after
`MACROSCOPIC STATIC DIELECTRIC TENSOR (excluding local field effects)`
should match exactly to the zero frequency values ω→0 determined by the
method selected using [LOPTICS](LOPTICS.md)=.TRUE.. This
offers a convenient way to determine how many empty bands are required
for [LOPTICS](LOPTICS.md)=.TRUE.. Simply execute VASP using
LEPSILON=.TRUE. in order to determine the exact values for the
dielectric constants. Next, switch to
[LOPTICS](LOPTICS.md)=.TRUE. and increase the number of
conduction bands until the same values are obtained using density
functional perturbation theory.

Note that the routine also parses and uses the value supplied in the
[LNABLA](LNABLA.md) tag. Furthermore, the routine calculates
the Born effective charge tensor (dynamical charges) and electronic
contribution to the piezoelectric tensor, and prints them after

     BORN EFFECTIVE CHARGES (in e, cumulative output)

and

     PIEZOELECTRIC TENSOR  for field in x, y, z        (C/m^2)

if [LRPA](LRPA.md)=.FALSE. is set (the calculated tensors are
not sensible in the random phase approximation
[LRPA](LRPA.md)=.TRUE.). Regarding the piezoelectric tensor,
mind the [definition/sign convention of the stress
tensor](ISIF.md).

  

Pros compared to [LOPTICS](LOPTICS.md)=.TRUE.

- no conduction bands required.
- local field effects included on the RPA and DFT level (see [ACFDT/RPA
  calculations](../methods/ACFDT__RPA_calculations.md)).

  

Cons compared to [LOPTICS](LOPTICS.md)=.TRUE.

- presently only static properties available.
- requires a relatively time consuming iterative process.
- does not support HF or hybrid functionals, whereas
  [LOPTICS](LOPTICS.md)=.TRUE. and the GW routines do.

  
We do not recommend to select [LOPTICS](LOPTICS.md)=.TRUE.
and LEPSILON=.TRUE. in a single run (although it might work in some
versions). Density functional perturbation theory LEPSILON=.TRUE. does
not require to increase [NBANDS](NBANDS.md) and is, in fact,
much slower if [NBANDS](NBANDS.md) is increased, whereas the
summation over empty conduction band states requires a large number of
such states.

## Related tags and articles
[LOPTICS](LOPTICS.md), [LRPA](LRPA.md),
[LCALCEPS](LCALCEPS.md), [IBRION](IBRION.md),
[Electric field response from density-functional-perturbation
theory](../theory/Electric_field_response_from_density-functional-perturbation_theory.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LEPSILON-_incategory-HowTo)

## References
1.  [↑](#cite_ref-gajdos:hummer:2006_1-0) [M. Gajdoš, K. Hummer, G.
    Kresse, J. Furthmüller, and F. Bechstedt, *Linear optical properties
    in the projector-augmented wave methodology*, Phys. Rev. B **73**,
    045112 (2006).](https://doi.org/10.1103/PhysRevB.73.045112)
2.  [↑](#cite_ref-baroni:resta:1986_2-0) [S. Baroni and R. Resta, *Ab
    initio calculation of the macroscopic dielectric constant in
    silicon*, Phys. Rev. B **33**, 7017
    (1986).](https://doi.org/10.1103/PhysRevB.33.7017)
