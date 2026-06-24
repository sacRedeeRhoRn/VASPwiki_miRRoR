<!-- Source: https://vasp.at/wiki/index.php/Welcome | revid: 35508 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Welcome
Let us take a tour through the resources that are available to you as a
VASP user!

## Contents

- [1 Become a VASP user](#Become_a_VASP_user)
- [2 Install VASP](#Install_VASP)
- [3 Basic usage](#Basic_usage)
- [4 Navigate the VASP Wiki](#Navigate_the_VASP_Wiki)
- [5 Learn a new method](#Learn_a_new_method)
- [6 Analyze VASP output](#Analyze_VASP_output)
- [7 Get help](#Get_help)

## Become a VASP user
The standard way to become a VASP user is that the head of your research
group [acquires a
license](https://www.vasp.at/sign_in/registration_form/) and registers
you as a user on the [VASP Portal](https://www.vasp.at/sign_in/portal/).
At a high-performance-computing (HPC) center, you can then immediately
get access to a VASP executable by stating your license number.

Alternatively, you can apply to participate in a workshop with hands-on
experience. The VASP developers infrequently organize workshops that are
announced in the [news section of the VASP
website](https://www.vasp.at/info/post/). Additionally, there are many
Universities offering courses where VASP is taught, as well as
independent workshops by experienced VASP collaborators.

## Install VASP
If you have a more-or-less powerful compute infrastructure available to
you, you can [install
VASP](Installing_VASP.6.X.X.md) by compiling
it yourself. There are some calculations that can even [run on a
standard
laptop](Personal_computer_installation.md),
but we recommend a more powerful infrastructure to unlock the full
potential of VASP. Download the source code of the latest release from
the [VASP Portal](https://www.vasp.at/sign_in/portal/) and follow the
[installation
guide](Installing_VASP.6.X.X.md) on the [VASP
Wiki](The_VASP_Manual.md). If you need help, post
your question in the [VASP Forum](https://www.vasp.at/forum/). There is
a section addressing solely [installation
issues](https://www.vasp.at/forum/viewforum.php?f=2&sid=cda3c8abf5b010db3aa23a407d72beee).
To get a forum account, you need to be a registered VASP user.

Which hardware exactly fits your purpose depends on the kind of
calculations you want to run. Furthermore, hardware development is a
rapidly evolving field, so we cannot recommend specific hardware
specifications, e.g., node size or a specific vendor, to you. Have a
look at the \[Toolchains \|toolchains\] we are frequently testing to
ensure compatibility with the compilers that come with your desired
hardware. Run some smaller test calculations to see how the calculations
for your application scale and have a look at factors that influence the
[performance of VASP](../redirects/Performance.md). Particularly,
consider what [parallelization
options](../redirects/Parallelization.md) and [memory
requirements](../redirects/Memory.md) apply.

## Basic usage
To get hands-on experience with the [setup of a
calculation](../redirects/Calculation_setup.md), check out the
[tutorials based on Python
notebooks](https://www.vasp.at/tutorials/latest). You will quickly learn
how to create the input for VASP by creating the proper input files and
setting the correct tags to select the algorithm or adjust parameters.
Additionally, there are
[examples](../categories/Category-Examples.md) and
[tutorials](../categories/Category-Tutorials.md) on the VASP
Wiki. A lecture on [a quick start to ab-initio
calculations](https://youtu.be/j3PMcAhXWUY) is available on our YouTube
channel.

## Navigate the VASP Wiki
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
visit the [VASP Forum](https://www.vasp.at/forum/). The section [Using
VASP](https://www.vasp.at/forum/viewforum.php?f=2) is dedicated to
queries on the usage of VASP. The VASP developers are continuously
improving the documentation, so this kind of feedback can help identify
where we need to improve.

## Learn a new method
VASP has a [broad spectrum of
applications](https://www.vasp.at/info/about/) in different fields all
the way from [many-body perturbation
theory](../redirects/Many-body_perturbation_theory.md)
to classical [molecular
dynamics](../redirects/Molecular_dynamics.md). A quick start
is usually to find a corresponding
[tutorial](https://www.vasp.at/tutorials/latest/),
[example](../categories/Category-Examples.md) or [how-to
page](../categories/Category-Howto.md) in the corresponding
[category](https://vasp.at/wiki/index.php/Special-Categories). Also, study
the [theoretical background](../redirects/Theory.md) by watching [video
lectures on the VASP
Channel](https://www.youtube.com/channel/UCBATkNZ7pkAXU9tx7GVhlaw),
attending a workshop announced in the [news section of the VASP
website](https://www.vasp.at/info/post/) or a course at your University.
To dive deeper, read [theory pages](../redirects/Theory.md) in the
corresponding [category](https://vasp.at/wiki/index.php/Special-Categories)
on the VASP Wiki and follow the related references.

## Analyze VASP output
The [output files](../redirects/Output_files.md) written by VASP
depends on the kind of calculation you are running.
[py4vasp](https://vasp.at/py4vasp/latest/index.html) is the most
seamless tool to extract data from VASP calculations. It is a Python
package developed by VASP developers and helps to get a quick look at
data, as well as parse it to other common formats. Mind that it requires
a VASP executable with [HDF5
support](Makefile.include.md).
Apart from that, most [output files](../redirects/Output_files.md)
are human-readable, and there are various third-party tools to visualize
the results.

## Get help
First, consider whether your issue is amongst the [known
issues](Known_issues.md) or [frequently asked
questions (FAQs)](https://www.vasp.at/info/faq/). Regarding installing
or using VASP, the VASP developers try to answer your questions as
swiftly as possible on the [VASP Forum](https://www.vasp.at/forum/). We
also greatly appreciate any [bug
report](https://www.vasp.at/forum/viewforum.php?f=3) on the [VASP
Forum](https://www.vasp.at/forum/) and created some space for
[user-to-user discussion](https://www.vasp.at/forum/viewforum.php?f=8).
Please kindly understand that we offer support on a courtesy basis only
and not as a contractual service. Thus, first carefully read the [VASP
Wiki](The_VASP_Manual.md) and perhaps consider if
this is a research question that a literature search or your principal
investigator (PI) could help with.

For any other issues, see how to [contact the VASP
team](https://www.vasp.at/info/contact/)!
