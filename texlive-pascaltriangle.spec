Name:		texlive-pascaltriangle
Version:	61774
Release:	2
Summary:	Draw beautiful Pascal (Yanghui) triangles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pascaltriangle
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pascaltriangle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pascaltriangle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX3 package based on TikZ helps to generate beautiful
Pascal (Yanghui) triangles. It provides a unique drawing macro
\pascal which can generate isosceles or right-angle triangles
customized by means of different \pascal macro options or the
\pascalset macro.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pascaltriangle
%doc %{_texmfdistdir}/doc/latex/pascaltriangle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
