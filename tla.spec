Name:		tla
Summary:	tla arch - revision control system
Summary(pl):	tla arch - systeme kontroli wersji
Version:	1.1pre5
Release:	1
License:	GPL v2
Group:		Development/Version Control
URL:		http://regexps.srparish.net/www/
Source0:	http://regexps.srparish.net/src/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	16512739150bdb81764a9d2fffb6a423
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tla arch is a revision control system: a program that lets
programmers archive a history of changes made to the software they
maintain and that, more importantly, helps programmers to coordinate,
synchronize, and combine multiple lines of development for a single
project.

arch version tla is a C version of the reference arch concepts.

%prep
%setup -q

## using: rpmbuild -ba --target=i686-redhat-linux tls-1.0.6.spec

%build
cd %{_builddir}/%{name}-%{version}/src
mkdir =build
cd =build
## imitate what an rpm macro would export
export CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}" FFLAGS="${RPM_OPT_FLAGS}";
../configure --prefix=%{_prefix} --destdir=%{buildroot}
%{__make}
# ok, I tested already
%{__make} test


%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}/src/=build
%{__make} install
## move some docs to a place the rpm doc macro likes
cd %{_builddir}/%{name}-%{version}
cp src/tla/=THANKS =THANKS
cp --recursive src/docs-tla/html html
cp --recursive src/docs-tla/ps ps
cp --recursive src/docs-tla/texi texi

# CLEANUP UNKNOWN USAGE DIRS
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_prefix}/src


%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING =INSTALL =RELEASE-ID html ps texi
%attr(755,root,root) %{_bindir}
#{_includedir}
#{_libdir}
#{_libexecdir}
