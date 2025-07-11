Name:		texlive-hyphen-slovenian
Version:	73410
Release:	1
Summary:	Slovenian hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-slovenian.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-slovenian
%_texmf_language_def_d/hyphen-slovenian
%_texmf_language_lua_d/hyphen-slovenian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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
