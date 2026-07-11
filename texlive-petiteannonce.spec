%global tl_name petiteannonce
%global tl_revision 25915

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0001
Release:	%{tl_revision}.1
Summary:	A class for small advertisements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/petiteannonce
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/petiteannonce.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class enables you to create the sort of adverts that you pin on a
noticeboard, with tear-off strips at the bottom where you can place
contact details.

