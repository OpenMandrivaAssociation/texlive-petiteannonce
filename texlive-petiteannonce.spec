Name:		texlive-petiteannonce
Version:	25915
Release:	1
Summary:	A class for small advertisements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/petiteannonce
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class enables you to create the sort of adverts that you
pin on a noticeboard, with tear-off strips at the bottom where
you can place contact details.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/petiteannonce/petiteannonce.cls
%doc %{_texmfdistdir}/doc/latex/petiteannonce/baignoire.JPG
%doc %{_texmfdistdir}/doc/latex/petiteannonce/petiteannonce.doc.pdf
%doc %{_texmfdistdir}/doc/latex/petiteannonce/petiteannonce.doc.tex
%doc %{_texmfdistdir}/doc/latex/petiteannonce/petiteannonceexample.pdf
%doc %{_texmfdistdir}/doc/latex/petiteannonce/petiteannonceexample.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
