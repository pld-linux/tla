Summary:	tla arch - revision control system
Summary(pl):	tla arch - system kontroli wersji
Name:		tla
Version:	1.3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.seyza.com/releases/%{name}-%{version}.tar.gz
# Source0-md5:	6093412e85d63fe79469bf386308d437
# http://people.debian.org/~asuffield/daily/tla/lord/
Patch0:		%{name}-neon.patch
URL:		http://www.gnu.org/software/gnu-arch/
Requires:	diffutils
Requires:	patch
Requires:	tar
BuildRequires:	neon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tla arch is a revision control system: a program that lets programmers
archive a history of changes made to the software they maintain and
that, more importantly, helps programmers to coordinate, synchronize,
and combine multiple lines of development for a single project.

arch version tla is a C version of the reference arch concepts.

%description -l pl
tla arch jest systemem kontroli wersji - programem, który pozwala
programistom archiwizowaæ historiê zmian wykonanych w rozwijanym przez
nich oprogramowaniu oraz, co wa¿niejsze, pomaga programistom
koordynowaæ, synchronizowaæ i ³±czyæ wiele linii kodu podczas rozwoju
projektu.

arch w wersji tla to wersja w C wzorcowych idei arch.

%prep
%setup -q
%patch0 -p1

%build
rm -rf src/tla/libneon
ln -s /usr/include/neon src/tla/libneon
cd src
mkdir =build
cd =build

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
FFLAGS="%{rpmcflags}"
export CFLAGS CXXFLAGS FFLAGS

# custom configure script
../configure \
	--prefix=%{_prefix} \
	--destdir=$RPM_BUILD_ROOT \
	--with-ssh-is-openssh=1 \
	--with-cc="%{__cc}"
%{__make} -j1

# ok, I tested already
%{__make} -j1 test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C src/=build install

cp --recursive src/docs-tla/html html

rm -rf html/.arch-ids
rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html
%attr(755,root,root) %{_bindir}/*
