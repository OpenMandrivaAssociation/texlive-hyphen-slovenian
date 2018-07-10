# revision 25990
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-slovenian
Version:	20180303
Release:	2
Summary:	Slovenian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-slovenian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Slovenian in T1/EC and UTF-8
encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-slovenian
%_texmf_language_def_d/hyphen-slovenian
%_texmf_language_lua_d/hyphen-slovenian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-slovenian <<EOF
\%% from hyphen-slovenian:
slovenian loadhyph-sl.tex
=slovene
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-slovenian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-slovenian <<EOF
\%% from hyphen-slovenian:
\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}
\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-slovenian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-slovenian <<EOF
-- from hyphen-slovenian:
	['slovenian'] = {
		loader = 'loadhyph-sl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'slovene' },
		patterns = 'hyph-sl.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120611-1
+ Revision: 804815
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767586
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759938
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718680
- texlive-hyphen-slovenian
- texlive-hyphen-slovenian
- texlive-hyphen-slovenian
- texlive-hyphen-slovenian

