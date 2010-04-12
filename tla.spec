Summary:	tla arch - revision control system
Summary(pl.UTF-8):	tla arch - system kontroli wersji
Name:		tla
Version:	1.3.5
Release:	5
Epoch:		1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://ftp.gnu.org/gnu/gnu-arch/%{name}-%{version}.tar.gz
# Source0-md5:	db31ee89bc4788eef1eba1cee6c176ef
Patch0:		%{name}-neon.patch
URL:		http://www.gnu.org/software/gnu-arch/
BuildRequires:	findutils
BuildRequires:	libtool
BuildRequires:	neon-devel
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
%patch0 -p1

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
find html -type f ! -name "*.html" -exec rm -rf "{}" ";"
find html -type d -name ".arch-ids" -exec rm -rf "{}" ";" || :
find html -type d -name "{arch}" -exec rm -rf "{}" ";" || :

rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_bindir}/*
