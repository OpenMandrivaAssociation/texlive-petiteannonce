Name:		texlive-petiteannonce
Version:	0.001
Release:	1
Summary:	A class for small advertisements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/petiteannonce
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class enables you to create the sort of adverts that you
pin on a noticeboard, with tear-off strips at the bottom where
you can place contact details.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
