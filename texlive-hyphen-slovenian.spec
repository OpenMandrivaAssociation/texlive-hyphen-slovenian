%global tl_name hyphen-slovenian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Slovenian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-slovenian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-slovenian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Slovenian in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-slovenian:
slovenian loadhyph-sl.tex
=slovene
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-slovenian:
\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}
\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-slovenian:
['slovenian'] = {
	loader = 'loadhyph-sl.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'slovene' },
	patterns = 'hyph-sl.pat.txt',
},
TL_HYPHEN_EOF
