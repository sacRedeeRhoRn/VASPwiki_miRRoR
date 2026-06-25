<!-- Source: https://vasp.at/wiki/index.php/LSELFENERGY | revid: 32808 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSELFENERGY


LSELFENERGY = \[logical\]  
Default: **LSELFENERGY** = .FALSE. 

Description: Controls whether the frequency-dependent self-energy is
calculated or not.

------------------------------------------------------------------------

- If `LSELFENERGY`` = .FALSE.`
  (default), quasi-particle (QP) shifts are evaluated.


    QP shifts <psi_nk| G(iteration)W_0 |psi_nk>: iteration 1
     for sc-GW calculations column KS-energies equals QP-energies in previous step 
     and V_xc(KS)=  KS-energies - (<T + V_ion + V_H > + <T+V_H+V_ion>^1  + <V_x>^1)
     
     k-point   1 :       0.0000    0.0000    0.0000
      band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation Imag(sigma)
     
          1      -7.1627      -8.3040     -14.5626     -12.7276     -21.6682       0.6219       2.0000       1.2037
          2      -2.0901      -3.4347     -15.7660     -14.2799     -21.7439       0.9048       2.0000       0.6914
          3      -2.0901      -3.4347     -15.7660     -14.2799     -21.7439       0.9048       2.0000       0.6914
          4      -2.0901      -3.4347     -15.7660     -14.2799     -21.7439       0.9048       2.0000       0.6914
          5       0.4603      -0.4663     -13.7603     -12.5200     -18.1532       0.7471       2.0000       0.2167
          6       0.4603      -0.4663     -13.7603     -12.5200     -18.1532       0.7471       2.0000       0.2167


- If `LSELFENERGY`` = .TRUE.`,
  the frequency dependent self-energy $\langle \psi_{n
  {\mathbf{k}}} | \Sigma(\omega) |\psi_{n {\mathbf{k}}} \rangle$ is evaluated and printed to
  [vasprun.xml](../output-files/Vasprun.xml.md). An example output
  looks like the following:


    <varray name="selfenergy" >                                                                                                                                                                                                                                               
      <v>    -150.00000000     -25.40060536       0.24429448 </v>                                                                                                                                                                                                              
      <v>    -149.70000000     -25.40600800       0.24673910 </v>                                                                                                                                                                                                              
      <v>    -149.40000000     -25.41141065       0.24918372 </v>                                                                                                                                                                                                              
      <v>    -149.10000000     -25.41681330       0.25162834 </v>                                                                                                                                                                                                              
      <v>    -148.80000000     -25.42221682       0.25406890 </v>                                                                                                                                                                                                              
      <v>    -148.50000000     -25.42762671       0.25647992 </v>                                                                                                                                                                                                              
      <v>    -148.20000000     -25.43303731       0.25888834 </v>


To print the self-energy is a slight extra computational effort since,
within the GW algorithms, the self-energy is usually just evaluated near
KS eigenenergies $\epsilon_{nk}$ and not the entire frequency range.

|  |
|----|
| **Mind:** In quartic-scaling GW the self-energy is given on the real-frequency axis, while for low-scaling GW the self-energy is given on the imaginary-frequency axis. |


## Contents


- [1
  Format](#format)
  - [1.1 Real
    frequencies](#real-frequencies)
  - [1.2 Imaginary
    frequencies](#imaginary-frequencies)
- [2 Related tags
  and articles](#related-tags-and-articles)


## Format\[<a
href="/wiki/index.php?title=LSELFENERGY&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

### Real frequencies\[<a
href="/wiki/index.php?title=LSELFENERGY&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Real frequencies">edit</a> \| (./index.php.md)\]

If **quartic-scaling GW algorithms** are selected, e.g.
[ALGO](ALGO.md)=EVGW0, the first column corresponds to points
on the real-frequency axis (in eV). The second and third columns are the
real and imaginary parts of the self-energy (in eV) at a given band
index and **k** point. To identify the band index and **k** point, the
ordering has to be taken from the [OUTCAR](../output-files/OUTCAR.md):
Instead of the QP shifts, a small set of self-energy points are printed
to [OUTCAR](../output-files/OUTCAR.md), similar to the following output

    calculating selfenergy CALC_SELFENERGY_LINEAR between w=-150.00 150.00                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                               
    k-point   1 :       0.0000    0.0000    0.0000                                                                                                                                                                                     
     band No.  band energies     occupation                                                                                                                                                                                            
                                                                                                                                                                                                                                       
         1     -11.4323      2.00000  selfenergy along real axis                                                                                                                                                                       
     -150.0000000   -24.0756124     0.2065066                                                                                                                                                                                          
     -147.0000000   -24.1277845     0.2302741                                                                                                                                                                                          
     -144.0000000   -24.1803224     0.2537669                                                                                                                                                                                          
     ...
      147.0000000   -20.3498375    -2.8348252                                                                                                                                                                                          
      150.0000000   -20.2310127    -2.7491028                                                                                                                                                                                          
                                                                                                                                                                                                                                       
         2      -2.7832      2.00000  selfenergy along real axis                                                                                                                                                                       
     -150.0000000   -13.0060959     0.1938781                                                                                                                                                                                          
     -147.0000000   -13.0530569     0.2231126                                                                                                                                                                                          
     -144.0000000   -13.1030584     0.2520593 
     ...

Here, the first and second band at the Gamma point are printed. The line
with `selfenergy along real axis` contains band No., the KS energy, and
the occupation of this state. The output in
[vasprun.xml](../output-files/Vasprun.xml.md) has the same ordering of
bands and **k** points, i.e., the band index is always the fastest. The
frequency grid cannot be controlled. It is always 1000 points in the
range of -150 to 150.

### Imaginary frequencies\[<a
href="/wiki/index.php?title=LSELFENERGY&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Imaginary frequencies">edit</a> \| (./index.php.md)\]

For [low-scaling GW
algorithms](../methods/Practical_guide_to_GW_calculations.md),
the QP shifts are evaluated and printed to
[OUTCAR](../output-files/OUTCAR.md) for both,
LSELFENERGY=T and F. For
LSELFENERGY=T, the
[vasprun.xml](../output-files/Vasprun.xml.md) file additionally
contains the self-energy for a given band index and **k** point on the
imaginary-frequency axis:

    <varray name="selfenergy along imaginary axis" >                                                                                                                                                                                                                          
      <v>       0.1570801806644298    -23.7971327349915711     -0.0179645094529067</v>                                                                                                                                                                                         
      <v>       0.4718033117773284    -23.7968260788831572     -0.0537856829291801</v>                                                                                                                                                                                         
      <v>       0.8108804505648752    -23.7966749072893577     -0.0932103588740998</v>                                                                                                                                                                                         
      <v>       1.3058951128526406    -23.7949927690568188     -0.1482973553314607</v>         
    ...

To identify the band index and **k** point, the ordering has to be taken
from the QP shifts block in the [OUTCAR](../output-files/OUTCAR.md). The
band index is faster than the **k** point. The imaginary frequency is
selected by the Minimax
routines[^Kaltak:PRB:2020-1],
and the number of points depends on [NOMEGA](NOMEGA.md).

## Related tags and articles\[<a
href="/wiki/index.php?title=LSELFENERGY&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- for a practical guide to
  <a href="/wiki/GW_calculations" class="mw-redirect"
  title="GW calculations">GW calculations</a>
- [ALGO](ALGO.md) for response functions and *RPA*
  calculations
- [LFINITE_TEMPERATURE](LFINITE_TEMPERATURE.md)
  finite temperature formalism
- [NOMEGA](NOMEGA.md) number of real or imaginary frequency
  points

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LSELFENERGY-_incategory-Examples)

------------------------------------------------------------------------

[^Kaltak:PRB:2020-1]: [M. Kaltak and G. Kresse, Phys. Rev. B. **101**, 205145 (2020).](https://doi.org/10.1103/PhysRevB.101.205145)
