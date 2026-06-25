<!-- Source: https://vasp.at/wiki/index.php/CUDA-C_GPU_port_of_VASP | revid: 34705 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CUDA-C GPU port of VASP


|  |
|----|
| **Warning:** As of VASP.6.3.0, the CUDA-C GPU port of VASP is deprecated. Switch to [the OpenACC GPU port of VASP](GPU_ports_of_VASP.md). |

Several core algorithms of VASP have been ported to run on
GPU-accelerated hardware (as of VASP.5.4.1.05Feb16).

Explicity ported to run on GPU-accelerated hardware  

- Electronic minimisation: the blocked-Davidson and RMM-DIIS algorithms
  ([ALGO](../incar-tags/ALGO.md)= Normal, Fast, and VeryFast).
- Hybrid functionals: the action of the Fock-exchange potential on the
  wave functions ([LHFCALC](../incar-tags/LHFCALC.md)=.TRUE.).

Unsuported (for now)

- [LREAL](../incar-tags/LREAL.md)=.FALSE. is currently unsuported . The GPU
  port of VASP requires the use of real-space-projection operators
  (i.e., [LREAL](../incar-tags/LREAL.md)= Auto \| .TRUE.).
- [LCALCEPS](../incar-tags/LCALCEPS.md)=.TRUE.
- [NCORE](../incar-tags/NCORE.md) ≠ 1 (or equivalently:
  [NPAR](../incar-tags/NPAR.md) ≠ *\#of-MPI-ranks* /
  [KPAR](../incar-tags/KPAR.md)) is not supported at the moment. The GPU
  port of VASP requires [NCORE](../incar-tags/NCORE.md)=1 (default).
- Using scaLAPACK for the orthonormalization of the wave functions is
  not supported by the GPU port of VASP. Actually, this particular
  operation has been ported to the GPU (just not by means of scaLAPACK).
  If you have compiled your code with `-DscaLAPACK` you have to set:

<!-- -->

    LSCAAWARE = .FALSE.

in your [INCAR](../input-files/INCAR.md) to avoid the use of scaLAPACK for
the orthonormalization of the wave functions.

- The gamma-only version of VASP has not been ported to GPU (yet).

  
**N.B.**: The GPU port of VASP is freely available to VASP5-licensees.


## Contents


- [1
  Hardware/Software
  requirements](#Hardware/Software_requirements)
  - [1.1 Hardware
    requirements](#Hardware_requirements)
  - [1.2
    Recommended software
    stack](#Recommended_software_stack)
- [2
  Usage](#Usage)
  - [2.1
    Building](#Building)
  - [2.2
    Running](#Running)
- [3
  People](#People)
- [4
  Publications](#Publications)
- [5 Additional
  information](#Additional_information)
- [6 Related Tags
  and Sections](#Related_Tags_and_Sections)


## Hardware/Software requirements\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Hardware/Software requirements">edit</a> \| (./index.php.md)\]

### Hardware requirements\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Hardware requirements">edit</a> \| (./index.php.md)\]

Required GPU Architecture is Kepler or newer:

- Tesla K40 or Tesla K80, with 12 and 24 GB memory respectively, are
  strongly recommended
- Tesla K20 and Tesla K20X, with 5 GB and 6 GB respectively, may run out
  of memory on larger problems

### Recommended software stack\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Recommended software stack">edit</a> \| (./index.php.md)\]

- CUDA toolkit, newer is better but anything \>=6.5 should work

## Usage\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

### Building\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Building">edit</a> \| (./index.php.md)\]

- See <a
  href="/wiki/index.php?title=Installing_VASP&amp;action=edit&amp;redlink=1"
  class="new" title="Installing VASP (page does not exist)">Installing
  VASP</a> and do not forget the <a
  href="/wiki/index.php?title=Installing_VASP&amp;action=edit&amp;redlink=1"
  class="new" title="Installing VASP (page does not exist)">patch(es)</a>.

### Running\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Running">edit</a> \| (./index.php.md)\]

## People\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: People">edit</a> \| (./index.php.md)\]

The GPU port of VASP only exist because of the excellent work of the
following people:

- Maxwell Hutchinson (University of Chicago) and Mike Widom (Carnegie
  Mellon)
- Xavier Rozanska and Paul Fleurat-Lessard (ENS-Lyon)
- Mohamed Hacene, Ani Anciaux-Sedrakian, Diego Klahr, and Thomas Guignon
  (IFPEN)
- Jeroen Bedorf, Przemyslaw Tredak, Dusan Stosic, Arash Ashari, Paul
  Springer, Darko Stosic, Christoph Angerer, and Sarah Tariq (NVIDIA)

## Publications\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Publications">edit</a> \| (./index.php.md)\]

- *Accelerating VASP Electronic Structure Calculations Using Graphic
  Processing Units*, M. Hacene *et al.*,
  <a href="http://dx.doi.org/10.1002/jcc.23096" class="external text"
  rel="nofollow">J. Comput. Chem. 33, 2581 (2012)</a>.
- *VASP on a GPU: Application to exact-exchange calculations of the
  stability of elemental boron*, M. Hutchinson and W. Widom,
  <a href="http://dx.doi.org/10.1016/j.cpc.2012.02.017"
  class="external text" rel="nofollow">Comput. Phys. Comm. 183, 1422
  (2012)</a>.
- <a
  href="http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118661788.html"
  class="external text" rel="nofollow"><em>Electronic Structure
  Calculations on Graphics Processing Units: From Quantum Chemistry to
  Condensed Matter Physics</em></a>, Ross Walker and Andreas Goetz
  (Editors), John Wiley & Sons, Inc., UK.
- *Speeding up plane-wave electronic-structure calculations using
  graphics-processing units*, S. Mainz *et al.*,
  <a href="http://dx.doi.org/10.1016/j.cpc.2011.03.010"
  class="external text" rel="nofollow">Comput. Phys. Comm. 182, 1421
  (2011)</a>.

## Additional information\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Additional information">edit</a> \| (./index.php.md)\]

- <a href="http://images.nvidia.com/events/sc15/SC5120-vasp-gpus.html"
  class="external text" rel="nofollow">The presentation at SC15 by GPU
  developer Max Hutchinson.</a>
- <a
  href="http://on-demand.gputechconf.com/gtc/2014/video/S4692-vasp-accelerating-plane-wave-dft-codes.mp4"
  class="external text" rel="nofollow">GTC 2013 audio &amp; video
  presentation on the development of GPU-accelerated VASP.</a>
- <a href="https://www.nsc.liu.se/~pla/" class="external text"
  rel="nofollow">Dr. Peter Larsson's blog (National Supercomputer Centre
  at Linköping University, Sweden).</a>

## Related Tags and Sections\[<a
href="/wiki/index.php?title=CUDA-C_GPU_port_of_VASP&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[ALGO](../incar-tags/ALGO.md), [LHFCALC](../incar-tags/LHFCALC.md),
[LREAL](../incar-tags/LREAL.md), [LCALCEPS](../incar-tags/LCALCEPS.md), <a
href="/wiki/index.php?title=Installing_VASP&amp;action=edit&amp;redlink=1"
class="new" title="Installing VASP (page does not exist)">Installing
VASP</a>

------------------------------------------------------------------------


