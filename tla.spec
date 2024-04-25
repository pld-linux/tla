Summary:	tla arch - revision control system
Summary(pl.UTF-8):	tla arch - system kontroli wersji
Name:		tla
Version:	1.3.5
Release:	12
Epoch:		1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://ftp.gnu.org/gnu/gnu-arch/%{name}-%{version}.tar.gz
# Source0-md5:	db31ee89bc4788eef1eba1cee6c176ef
Patch1:		0001-Fixes-segmentation-fault-on-ia64.patch
Patch2:		0002-Fixes-alignment-errors-on-hppa-and-sparc.patch
Patch3:		0003-fix-bashisms.patch
Patch4:		0004-fix-machine-alignment.patch
Patch5:		0005-disable-builtin-expat.patch
Patch6:		0006-tar-preserve.patch
Patch7:		0007-fix-some-includes.patch
Patch8:		0008-fix-spelling.patch
Patch9:		0009-Remove-rpath-from-libneon.patch
Patch10:	0010-add-missing-include.patch
Patch11:	0011-Fix-malformed-comment-in-tla-doc-handbook-index.html.patch
Patch12:	0012-update-tla-tree-list-to-point-to-tla-add-id.patch
Patch13:	0013-fix-libneon-configure-options.patch
Patch14:	0014-do-not-show-the-build-date.patch
Patch15:	0015-changeset-fd-leak.patch
Patch20:		%{name}-neon.patch
Patch21:		libtool-tag.patch
URL:		http://www.gnu.org/software/gnu-arch/
BuildRequires:	libtool
BuildRequires:	neon-devel
# required by the configure script
BuildRequires:	patch
BuildRequires:	which
Requires:	diffutils
Requires:	patch
Requires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tla arch is a revision control system: a program that lets programmers
archive a history of changes made to the software they maintain and
that, more importantly, helps programmers to coordinate, synchronize,
and combine multiple lines of development for a single project.

arch version tla is a C version of the reference arch concepts.

%description -l pl.UTF-8
tla arch jest systemem kontroli wersji - programem, który pozwala
programistom archiwizować historię zmian wykonanych w rozwijanym przez
nich oprogramowaniu oraz, co ważniejsze, pomaga programistom
koordynować, synchronizować i łączyć wiele linii kodu podczas rozwoju
projektu.

arch w wersji tla to wersja w C wzorcowych idei arch.

%prep
%setup -q
# Patches from Debian
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
# Other patches
%patch20 -p1
%patch21 -p1

rm -rf src/libneon src/expat

%build
cd src
mkdir =build
cd =build

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
FFLAGS="%{rpmcflags}"
export CFLAGS CXXFLAGS FFLAGS

# custom configure script
../configure \
	--destdir=$RPM_BUILD_ROOT \
	--prefix=%{_prefix} \
	--with-cc="%{__cc}" \
	--with-ssh-type=openssh
%{__make} -j1

# ok, I tested already
%{__make} -j1 test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C src/=build install

rm -rf html
cp -a src/docs-tla html
find html -type f ! -name "*.html" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_bindir}/tla
