Summary:	tla arch - revision control system
Summary(pl):	tla arch - system kontroli wersji
Name:		tla
Version:	1.2
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://regexps.srparish.net/src/tla/%{name}-%{version}.tar.gz
# Source0-md5:	1fbc9cd83c37ad6e88e9e6a5f0b62871
URL:		http://www.gnu.org/software/gnu-arch/
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

%build
cd src
mkdir =build
cd =build
## imitate what an rpm macro would export
export CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}" FFLAGS="%{rpmcflags}"
../configure --prefix=%{_prefix} --destdir=%{buildroot}
%{__make}

# ok, I tested already
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src/=build install

## move some docs to a place the rpm doc macro likes
cp src/tla/=THANKS =THANKS
cp --recursive src/docs-tla/html html
cp --recursive src/docs-tla/ps ps
cp --recursive src/docs-tla/texi texi

# CLEANUP UNKNOWN USAGE DIRS
rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html ps texi
%attr(755,root,root) %{_bindir}/*
#{_includedir}
#{_libdir}
#{_libexecdir}
