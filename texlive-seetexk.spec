Name:		texlive-seetexk
Version:	57972
Release:	2
Summary:	Utilities for manipulating DVI files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvibook
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seetexk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seetexk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-seetexk.bin

%description
The collection comprises: dvibook, which will rearrange the
pages of a DVI file into 'signatures' as used when printing a
book; dviconcat, for concatenating pages of DVI file(s);
dviselect, which will select pages from one DVI file to create
a new DVI file; dvitodvi, which will rearrange the pages of a
DVI file to create a new file; and libtex, a library for
manipulating the files, from the old SeeTeX project. The
utilities are provided as C source with Imakefiles, and an MS-
DOS version of dvibook is also provided.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvibook.1*
%doc %{_texmfdistdir}/doc/man/man1/dvibook.man1.pdf
%doc %{_mandir}/man1/dviconcat.1*
%doc %{_texmfdistdir}/doc/man/man1/dviconcat.man1.pdf
%doc %{_mandir}/man1/dviselect.1*
%doc %{_texmfdistdir}/doc/man/man1/dviselect.man1.pdf
%doc %{_mandir}/man1/dvitodvi.1*
%doc %{_texmfdistdir}/doc/man/man1/dvitodvi.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
