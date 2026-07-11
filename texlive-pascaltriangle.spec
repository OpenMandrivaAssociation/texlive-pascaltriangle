%global tl_name pascaltriangle
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Draw beautiful Pascal (Yanghui) triangles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pascaltriangle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pascaltriangle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pascaltriangle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX3 package based on TikZ helps to generate beautiful Pascal
(Yanghui) triangles. It provides a unique drawing macro \pascal which
can generate isosceles or right-angle triangles customized by means of
different \pascal macro options or the \pascalset macro.

