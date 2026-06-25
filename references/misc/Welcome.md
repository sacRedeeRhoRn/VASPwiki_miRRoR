<!-- Source: https://vasp.at/wiki/index.php/Welcome | revid: 35508 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Welcome


Let us take a tour through the resources that are available to you as a
VASP user!


## Contents


- [1 Become a VASP
  user](#Become_a_VASP_user)
- [2 Install
  VASP](#Install_VASP)
- [3 Basic
  usage](#Basic_usage)
- [4 Navigate the
  VASP Wiki](#Navigate_the_VASP_Wiki)
- [5 Learn a new
  method](#Learn_a_new_method)
- [6 Analyze VASP
  output](#Analyze_VASP_output)
- [7 Get
  help](#Get_help)


## Become a VASP user\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Become a VASP user">edit</a> \| (./index.php.md)\]

The standard way to become a VASP user is that the head of your research
group <a href="https://www.vasp.at/sign_in/registration_form/"
class="external text" rel="nofollow">acquires a license</a> and
registers you as a user on the
<a href="https://www.vasp.at/sign_in/portal/" class="external text"
rel="nofollow">VASP Portal</a>. At a high-performance-computing (HPC)
center, you can then immediately get access to a VASP executable by
stating your license number.

Alternatively, you can apply to participate in a workshop with hands-on
experience. The VASP developers infrequently organize workshops that are
announced in the
<a href="https://www.vasp.at/info/post/" class="external text"
rel="nofollow">news section of the VASP website</a>. Additionally, there
are many Universities offering courses where VASP is taught, as well as
independent workshops by experienced VASP collaborators.

## Install VASP\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Install VASP">edit</a> \| (./index.php.md)\]

If you have a more-or-less powerful compute infrastructure available to
you, you can [install
VASP](Installing_VASP.6.X.X.md) by compiling
it yourself. There are some calculations that can even [run on a
standard
laptop](Personal_computer_installation.md),
but we recommend a more powerful infrastructure to unlock the full
potential of VASP. Download the source code of the latest release from
the <a href="https://www.vasp.at/sign_in/portal/" class="external text"
rel="nofollow">VASP Portal</a> and follow the [installation
guide](Installing_VASP.6.X.X.md) on the [VASP
Wiki](The_VASP_Manual.md). If you need help, post
your question in the
<a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP Forum</a>. There is a section addressing solely <a
href="https://www.vasp.at/forum/viewforum.php?f=2&amp;sid=cda3c8abf5b010db3aa23a407d72beee"
class="external text" rel="nofollow">installation issues</a>. To get a
forum account, you need to be a registered VASP user.

Which hardware exactly fits your purpose depends on the kind of
calculations you want to run. Furthermore, hardware development is a
rapidly evolving field, so we cannot recommend specific hardware
specifications, e.g., node size or a specific vendor, to you. Have a
look at the \[Toolchains \|toolchains\] we are frequently testing to
ensure compatibility with the compilers that come with your desired
hardware. Run some smaller test calculations to see how the calculations
for your application scale and have a look at factors that influence the
<a href="/wiki/Performance" class="mw-redirect"
title="Performance">performance of VASP</a>. Particularly, consider what
<a href="/wiki/Parallelization" class="mw-redirect"
title="Parallelization">parallelization options</a> and
<a href="/wiki/Memory" class="mw-redirect" title="Memory">memory
requirements</a> apply.

## Basic usage\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Basic usage">edit</a> \| (./index.php.md)\]

To get hands-on experience with the
<a href="/wiki/Calculation_setup" class="mw-redirect"
title="Calculation setup">setup of a calculation</a>, check out the
<a href="https://www.vasp.at/tutorials/latest" class="external text"
rel="nofollow">tutorials based on Python notebooks</a>. You will quickly
learn how to create the input for VASP by creating the proper input
files and setting the correct tags to select the algorithm or adjust
parameters. Additionally, there are
[examples](../categories/Category-Examples.md) and
[tutorials](../categories/Category-Tutorials.md) on the VASP
Wiki. A lecture on
<a href="https://youtu.be/j3PMcAhXWUY" class="external text"
rel="nofollow">a quick start to ab-initio calculations</a> is available
on our YouTube channel.

## Navigate the VASP Wiki\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Navigate the VASP Wiki">edit</a> \| (./index.php.md)\]

The [main page of the VASP
Wiki](The_VASP_Manual.md) shows [featured
topics](The_VASP_Manual.md) that
represents a rough book-like table of contents. It covers a range from
introductory topics, (i.e., the theoretical background and calculation
setup), over the central chapters (the electronic ground state, ionic
degree of freedom, and excitations) up to some advanced considerations,
(i.e., obtaining a local basis for the electronic state or optimizing
performance).

Each [category page](https://vasp.at/wiki/index.php/Special-Categories)
provides an introduction to the topic. It links to tag and file
documentation, further [theory
pages](../categories/Category-Theory.md), and [how-to
pages](../categories/Category-Howto.md) to describe common
workflows. If the explanation is unclear or information is missing,
visit the <a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP Forum</a>. The section
<a href="https://www.vasp.at/forum/viewforum.php?f=2"
class="external text" rel="nofollow">Using VASP</a> is dedicated to
queries on the usage of VASP. The VASP developers are continuously
improving the documentation, so this kind of feedback can help identify
where we need to improve.

## Learn a new method\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Learn a new method">edit</a> \| (./index.php.md)\]

VASP has a
<a href="https://www.vasp.at/info/about/" class="external text"
rel="nofollow">broad spectrum of applications</a> in different fields
all the way from
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>
to classical <a href="/wiki/Molecular_dynamics" class="mw-redirect"
title="Molecular dynamics">molecular dynamics</a>. A quick start is
usually to find a corresponding
<a href="https://www.vasp.at/tutorials/latest/" class="external text"
rel="nofollow">tutorial</a>,
[example](../categories/Category-Examples.md) or [how-to
page](../categories/Category-Howto.md) in the corresponding
[category](https://vasp.at/wiki/index.php/Special-Categories). Also, study
the
<a href="/wiki/Theory" class="mw-redirect" title="Theory">theoretical
background</a> by watching
<a href="https://www.youtube.com/channel/UCBATkNZ7pkAXU9tx7GVhlaw"
class="external text" rel="nofollow">video lectures on the VASP
Channel</a>, attending a workshop announced in the
<a href="https://www.vasp.at/info/post/" class="external text"
rel="nofollow">news section of the VASP website</a> or a course at your
University. To dive deeper, read
<a href="/wiki/Theory" class="mw-redirect" title="Theory">theory
pages</a> in the corresponding
[category](https://vasp.at/wiki/index.php/Special-Categories) on the VASP
Wiki and follow the related references.

## Analyze VASP output\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Analyze VASP output">edit</a> \| (./index.php.md)\]

The <a href="/wiki/Output_files" class="mw-redirect"
title="Output files">output files</a> written by VASP depends on the
kind of calculation you are running.
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> is the most seamless
tool to extract data from VASP calculations. It is a Python package
developed by VASP developers and helps to get a quick look at data, as
well as parse it to other common formats. Mind that it requires a VASP
executable with [HDF5
support](Makefile.include.md).
Apart from that, most <a href="/wiki/Output_files" class="mw-redirect"
title="Output files">output files</a> are human-readable, and there are
various third-party tools to visualize the results.

## Get help\[<a href="/wiki/index.php?title=Welcome&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Get help">edit</a> \| (./index.php.md)\]

First, consider whether your issue is amongst the [known
issues](Known_issues.md) or
<a href="https://www.vasp.at/info/faq/" class="external text"
rel="nofollow">frequently asked questions (FAQs)</a>. Regarding
installing or using VASP, the VASP developers try to answer your
questions as swiftly as possible on the
<a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP Forum</a>. We also greatly appreciate any
<a href="https://www.vasp.at/forum/viewforum.php?f=3"
class="external text" rel="nofollow">bug report</a> on the
<a href="https://www.vasp.at/forum/" class="external text"
rel="nofollow">VASP Forum</a> and created some space for
<a href="https://www.vasp.at/forum/viewforum.php?f=8"
class="external text" rel="nofollow">user-to-user discussion</a>. Please
kindly understand that we offer support on a courtesy basis only and not
as a contractual service. Thus, first carefully read the [VASP
Wiki](The_VASP_Manual.md) and perhaps consider if
this is a research question that a literature search or your principal
investigator (PI) could help with.

For any other issues, see how to
<a href="https://www.vasp.at/info/contact/" class="external text"
rel="nofollow">contact the VASP team</a>!


