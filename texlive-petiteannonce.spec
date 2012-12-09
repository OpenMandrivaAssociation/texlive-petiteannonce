# revision 25915
# category Package
# catalog-ctan /macros/latex/contrib/petiteannonce
# catalog-date 2012-04-11 15:11:02 +0200
# catalog-license lppl
# catalog-version 1.0001
Name:		texlive-petiteannonce
Version:	1.0001
Release:	1
Summary:	A class for small advertisements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/petiteannonce
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0001-1
+ Revision: 805029
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.001-2
+ Revision: 754813
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.001-1
+ Revision: 719238
- texlive-petiteannonce
- texlive-petiteannonce
- texlive-petiteannonce
- texlive-petiteannonce

