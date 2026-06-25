<!-- Source: https://vasp.at/wiki/index.php/Toolchains | revid: 34945 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Toolchains


Below we list the toolchains
(compilers + assorted libraries) that we have used to build and test
VASP in our nightly tests during the development. Starting from
VASP.6.3.0, the toolchains are
listed separately for each version of VASP.

- These lists of toolchains
  are not comprehensive. They show what we have employed on a regular
  basis. Other/newer versions of the compilers and libraries than those
  listed below will, in all probability, work just as well (or better).

|  |
|----|
| **Tip:** We encourage using up-to-date versions of compilers and libraries since they are continuously improved and bugs are identified and fixed. |

- Also for older versions of VASP, we recommend using up-to-date
  versions of compilers and libraries. In most cases, this will not be a
  problem. Except in some cases, VASP code was adjusted, e.g., to
  accommodate changes in the behavior of a compiler. This happens when
  compilers became more strict and do not accept certain code constructs
  used in older VASP versions. Here are a few known examples:
  - Compilation with GCC \> 7.X.X is only possible as of VASP.6.2.0
    .[^gcc-beyond-7-support-1]
  - Compilation with GCC \> 14.2.X is currently (as of VASP.6.5.1) not
    possible since it dropped legacy code support in C and Fortran
    formatted strings. This can be worked around by adding the compiler
    flag `-std=legacy`


## Contents


- [1
  VASP.6.6.0](#vasp660)
- [2
  VASP.6.5.1](#vasp651)
- [3
  VASP.6.4.3](#vasp643)
- [4
  VASP.6.3.0](#vasp630)
- [5 Older versions
  of VASP.6](#older-versions-of-vasp6)
- [6 Footnotes and
  references](#footnotes-and-references)
- [7 Related
  articles](#related-articles)


## VASP.6.6.0\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: VASP.6.6.0">edit</a> \| (./index.php.md)\]

<table class="wikitable" style="text-align: center;">
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr>
<th>Compilers</th>
<th>MPI</th>
<th>FFT</th>
<th>BLAS</th>
<th>LAPACK</th>
<th>ScaLAPACK</th>
<th>OpenMP</th>
<th>CUDA</th>
<th>HDF5</th>
<th>Other</th>
<th>Remarks</th>
<th>Known issues</th>
</tr>
&#10;<tr>
<td>aocc-5.0.0</td>
<td>openmpi-5.0.6</td>
<td>amdfftw-5.0</td>
<td>amdblis-5.0</td>
<td>amdlibflame-5.0</td>
<td>amdscalapack-5.0</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.14.5</td>
<td>wannier90-3.1.0<br />
libxc-7.0.0</td>
<td>Rocky Linux 8.8<br />
AMD CPUs</td>
<td>-</td>
</tr>
<tr>
<td>cce/19.0.0</td>
<td>cray-mpich/8.1.32</td>
<td>cray-fftw</td>
<td colspan="3">cray-libsci/25.03.0</td>
<td>yes</td>
<td>rocm-6.4.3</td>
<td>-</td>
<td>-</td>
<td>SLES 15 SP5<br />
AMD GPUs (MI210,MI250,MI300)<br />
OpenMP offload</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>fftw-3.3.10</td>
<td colspan="2">openblas-0.3.18</td>
<td>netlib-scalapack-2.1.0</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>amdfftw-3.1</td>
<td>amdblis-3.1</td>
<td>amdlibflame-3.1</td>
<td>amdscalapack-3.1</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Rocky Linux 8.8<br />
AMD CPUs</td>
<td>-</td>
</tr>
<tr>
<td>gcc-12.3.0</td>
<td>openmpi-4.1.6</td>
<td colspan="3">intel-oneapi-mkl-2023.2.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>intel-compilers-2022.0.1</td>
<td>openmpi-4.1.2</td>
<td colspan="3">intel-oneapi-mkl-2022.0.1</td>
<td>netlib-scalapack-2.1.0</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>intel-oneapi-compilers-2024.0.2</td>
<td>intel-oneapi-mpi-2021.10.0</td>
<td colspan="4">intel-oneapi-mkl-2023.2.0</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>intel-oneapi-compilers-2025.3.2</td>
<td>intel-oneapi-mpi-2021.17.2</td>
<td colspan="4">intel-oneapi-mkl-2025.3.1</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.14.5</td>
<td>wannier90-3.1.0</td>
<td>Rocky Linux 9.4<br />
Intel GPU (PVC)<br />
OpenMP offload</td>
<td>-</td>
</tr>
<tr>
<td>nec-5.0.1</td>
<td>nmpi-2.25.0</td>
<td colspan="3">nlc-3.0.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>no</td>
<td>-</td>
<td>-</td>
<td>wannier90-3.1.0</td>
<td>Rocky Linux 8.8<br />
NEC SX-Aurora TSUBASA<br />
vector engine</td>
<td>VASP &gt;= 6.3.0[^nec-aurora-support-2]</td>
</tr>
<tr>
<td>nvhpc-25.1<br />
(OpenACC)</td>
<td>openmpi-4.1.7<br />
(CUDA-aware)</td>
<td colspan="3">intel-oneapi-mkl-2025.0.1</td>
<td>netlib-scalapack-2.2.0</td>
<td>yes</td>
<td>cuda-12.6</td>
<td>hdf5-1.14.3</td>
<td>wannier90-3.1.0</td>
<td>Rocky Linux 8.8<br />
NVIDIA GPUs<br />
(A30)</td>
<td>-</td>
</tr>
</tbody>
</table>

  

## VASP.6.5.1\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: VASP.6.5.1">edit</a> \| (./index.php.md)\]

<table class="wikitable" style="text-align: center;">
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr>
<th>Compilers</th>
<th>MPI</th>
<th>FFT</th>
<th>BLAS</th>
<th>LAPACK</th>
<th>ScaLAPACK</th>
<th>OpenMP</th>
<th>CUDA</th>
<th>HDF5</th>
<th>Other</th>
<th>Remarks</th>
<th>Known issues</th>
</tr>
&#10;<tr>
<td>intel-oneapi-compilers-2024.0.2</td>
<td>intel-oneapi-mpi-2021.10.0</td>
<td colspan="4">intel-oneapi-mkl-2023.2.0</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>fftw-3.3.10</td>
<td colspan="2">openblas/0.3.18</td>
<td>netlib-scalapack-2.1.0</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>amdfftw/3.1</td>
<td colspan="2">amdblis/3.1 amdlibflame/3.1</td>
<td>amdscalapack/3.1</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>gcc-12.3.0</td>
<td>openmpi-4.1.6</td>
<td colspan="3">intel-oneapi-mkl-2023.2.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>nvhpc-23.7<br />
(OpenACC)</td>
<td>openmpi-4.1.6<br />
(CUDA-aware)</td>
<td colspan="3">intel-oneapi-mkl-2023.2.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>yes</td>
<td>cuda-11.8</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0</td>
<td>Rock Linux 8.8<br />
NVIDIA GPUs<br />
(A30)</td>
<td><span style="background:#f5d9da"><a
href="/wiki/Known_issues#KnownIssue32" title="Known issues">not working
with python plugins</a></span></td>
</tr>
<tr>
<td style="background-color: #f5d9da">aocc-4.0.0</td>
<td>openmpi-4.1.3</td>
<td>amdfftw-4.0</td>
<td>amdblis-4.0</td>
<td>amdlibflame-4.0</td>
<td>amdscalapack-4.0</td>
<td>yes</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>On AMD CPUs<br />
(Zen3)</td>
<td><span style="background:#f5d9da"><a
href="/wiki/Known_issues#KnownIssue11" title="Known issues">Reduce
optimization level</a></span></td>
</tr>
<tr>
<td>nec-5.0.1</td>
<td>nmpi-2.25.0</td>
<td colspan="3">nlc-3.0.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>no</td>
<td>-</td>
<td>-</td>
<td>wannier90-3.1.0</td>
<td>Rocky Linux 8.8<br />
NEC SX-Aurora TSUBASA<br />
vector engine</td>
<td>VASP &gt;= 6.3.0[^nec-aurora-support-2]</td>
</tr>
</tbody>
</table>

## VASP.6.4.3\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: VASP.6.4.3">edit</a> \| (./index.php.md)\]

<table class="wikitable" style="text-align: center;">
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr>
<th>Compilers</th>
<th>MPI</th>
<th>FFT</th>
<th>BLAS</th>
<th>LAPACK</th>
<th>ScaLAPACK</th>
<th>CUDA</th>
<th>HDF5</th>
<th>Other</th>
<th>Remarks</th>
<th>Known issues</th>
<th></th>
</tr>
&#10;<tr>
<td>intel-oneapi-compilers-2024.0.2</td>
<td>intel-oneapi-mpi-2021.10.0</td>
<td colspan="4">intel-oneapi-mkl-2023.2.0</td>
<td>both</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
</tr>
<tr>
<td>gcc-12.3.0</td>
<td>openmpi-4.1.6</td>
<td colspan="3">intel-oneapi-mkl-2023.2.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>-</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.3</td>
<td>Rocky Linux 8.8</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>nvhpc-23.7<br />
(OpenACC)</td>
<td>openmpi-4.1.6<br />
(CUDA-aware)</td>
<td colspan="3">intel-oneapi-mkl-2023.2.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>cuda-11.8</td>
<td>hdf5-1.14.0</td>
<td>wannier90-3.1.0</td>
<td>Rock Linux 8.8<br />
NVIDIA GPUs<br />
(A30)</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td style="background-color: #f5d9da">aocc-4.0.0</td>
<td>openmpi-4.1.4</td>
<td>amdfftw-4.0</td>
<td>amdblis-4.0</td>
<td>amdlibflame-4.0</td>
<td>amdscalapack-4.0</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>On AMD CPUs<br />
(Zen3)</td>
<td><span style="background:#f5d9da"><a
href="/wiki/Known_issues#KnownIssue11" title="Known issues">Reduce
optimization level</a></span></td>
<td></td>
</tr>
<tr>
<td>nec-5.0.2</td>
<td>nmpi-2.25.0</td>
<td colspan="3">nlc-3.0.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>-</td>
<td>-</td>
<td>wannier90-3.1.0</td>
<td>Rocky Linux 8.8<br />
NEC SX-Aurora TSUBASA<br />
vector engine</td>
<td>VASP &gt;= 6.3.0[^nec-aurora-support-2]</td>
<td></td>
</tr>
</tbody>
</table>

## VASP.6.3.0\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: VASP.6.3.0">edit</a> \| (./index.php.md)\]

<table class="wikitable" style="text-align: center;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr>
<th>Compilers</th>
<th>MPI</th>
<th>FFT</th>
<th>BLAS</th>
<th>LAPACK</th>
<th>ScaLAPACK</th>
<th>CUDA</th>
<th>HDF5</th>
<th>Other</th>
<th>Remarks</th>
<th>Known issues</th>
</tr>
&#10;<tr>
<td>intel-oneapi-compilers-2022.0.1</td>
<td>intel-oneapi-mpi-2021.5.0</td>
<td colspan="4">intel-oneapi-mkl-2022.0.1</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td>-</td>
</tr>
<tr>
<td colspan="5">intel-parallel-studio-xe-2021.4.0</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td colspan="3">intel-oneapi-mkl-2022.0.1</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>fftw-3.3.10</td>
<td colspan="2">openblas-0.3.18</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td>-</td>
</tr>
<tr>
<td>gcc-11.2.0</td>
<td>openmpi-4.1.2</td>
<td>amdfftw-3.1</td>
<td>amdblis-3.1</td>
<td>amdlibflame-3.1</td>
<td>amdscalapack-3.1</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>Centos 8.3<br />
AMD Zen3</td>
<td>-</td>
</tr>
<tr>
<td>gcc-9.3.0</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td>fftw-3.3.8</td>
<td colspan="2">openblas-0.3.10</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>gcc-7.5.0</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-22.2<br />
(OpenACC)</td>
<td>openmpi-4.1.2</td>
<td colspan="3">intel-oneapi-mkl-2022.0.1</td>
<td>netlib-scalapack-2.1.0</td>
<td>nvhpc-22.2<br />
(cuda-11.0)</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
NVIDIA GPUs<br />
(P100 &amp; V100)</td>
<td>OpenACC<br />
+<br />
OpenMP[^omp-acc-bug-1-4]</td>
</tr>
<tr>
<td>nvhpc-21.2<br />
(OpenACC)</td>
<td style="background-color: #f5d9da">openmpi-4.0.5<br />
(CUDA-aware)</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>nvhpc-21.2<br />
(cuda-11.0)</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
NVIDIA GPUs<br />
(P100 &amp; V100)</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-21.2</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-21.2</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td>fftw-3.3.8</td>
<td colspan="2">openblas-0.3.10</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>aocc-3.2.0</td>
<td>openmpi-4.1.2</td>
<td>amdfftw-3.1</td>
<td>amdblis-3.1</td>
<td>amdlibflame-3.1</td>
<td>amdscalapack-3.1</td>
<td>-</td>
<td>hdf5-1.13.0</td>
<td>wannier90-3.1.0<br />
libxc-5.2.2</td>
<td>On AMD CPUs<br />
(Zen3)</td>
<td>-</td>
</tr>
<tr>
<td>nec-3.4.0</td>
<td>nmpi-2.18.0</td>
<td colspan="3">nlc-2.3.0</td>
<td>netlib-scalapack-2.2.0</td>
<td>-</td>
<td>-</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
NEC SX-Aurora TSUBASA<br />
vector engine</td>
<td>VASP &gt;= 6.3.0[^nec-aurora-support-2]</td>
</tr>
</tbody>
</table>

## Older versions of VASP.6\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Older versions of VASP.6">edit</a> \| (./index.php.md)\]

<table class="wikitable" style="text-align: center;">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr>
<th>Compilers</th>
<th>MPI</th>
<th>FFT</th>
<th>BLAS</th>
<th>LAPACK</th>
<th>ScaLAPACK</th>
<th>CUDA</th>
<th>HDF5</th>
<th>Other</th>
<th>Remarks</th>
<th>Known issues</th>
</tr>
&#10;<tr>
<td colspan="5">intel-parallel-studio-xe-2021.1.1</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td>-</td>
</tr>
<tr>
<td>gcc-9.3.0</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td>fftw-3.3.8</td>
<td colspan="2">openblas-0.3.10</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span><br />
VASP &gt;= 6.2.0[^gcc-beyond-7-support-1]</td>
</tr>
<tr>
<td>gcc-7.5.0</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-21.2<br />
(OpenACC)</td>
<td style="background-color: #f5d9da">openmpi-4.0.5<br />
(CUDA-aware)</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>nvhpc-21.2<br />
(cuda-11.0)</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
NVIDIA GPUs<br />
(P100 &amp; V100)</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-21.2</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td colspan="3">intel-mkl-2020.2.254</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
<tr>
<td>nvhpc-21.2</td>
<td style="background-color: #f5d9da">openmpi-4.0.5</td>
<td>fftw-3.3.8</td>
<td colspan="2">openblas-0.3.10</td>
<td>netlib-scalapack-2.1.0</td>
<td>-</td>
<td>hdf5-1.10.7</td>
<td>wannier90-3.1.0</td>
<td>Centos 8.3<br />
Intel Broadwell</td>
<td><span style="background:#f5d9da">Memory-leak[^ompi-bug-1-3]</span></td>
</tr>
</tbody>
</table>

## Footnotes and references\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Footnotes and references">edit</a> \| (./index.php.md)\]
## Related articles\[<a
href="/wiki/index.php?title=Toolchains&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Related articles">edit</a> \| (./index.php.md)\]

[Installing
VASP.6.X.X](Installing_VASP.6.X.X.md),
[makefile.include](Makefile.include.md), [Compiler
options](Compiler_options.md), [Precompiler
options](Precompiler_options.md), [Linking to
libraries](Linking_to_libraries.md), [GPU
ports of VASP](GPU_ports_of_VASP.md), [Validation
tests](Validation_tests.md), [Known
issues](Known_issues.md), [Personal computer
installation](Personal_computer_installation.md)

[^gcc-beyond-7-support-1]: Support for GCC \> 7.X.X was added with VASP.6.2.0. Do not use GCC-8.X.X compilers: the way we use the `CONTIGUOUS` construct in VASP is broken when using these compilers.
[^nec-aurora-support-2]: The NEC SX-Aurora TSUBASA vector engine is supported as of VASP.6.3.0.
[^ompi-bug-1-3]: A bug in OpenMPI versions 4.0.4-4.1.1 causes a memory leak in some ScaLAPACK calls. This mainly affects long [molecular-dynamics](/wiki/Category:Molecular_dynamics "Category:Molecular dynamics") runs. This issue is fixed as of openmpi-4.1.2.
[^omp-acc-bug-1-4]: The NVIDIA HPC-SDK versions 22.1 and 22.2 have a serious bug that prohibits the execution of the OpenACC GPU port of VASP in conjunction with OpenMP-threading. When using these compiler versions you should compile the OpenACC GPU port of VASP without OpenMP-support. This bug is fixed as of NVIDIA HPC-SDK version 22.3.
