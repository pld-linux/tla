Name: tla
Summary: tla arch is a revision control system
Version: 1.1pre5
Release: 1
License: GPL
Group: Development/Tools
Provides: %{name}
Source0: http://regexps.srparish.net/src/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	16512739150bdb81764a9d2fffb6a423
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://regexps.srparish.net/www/

%description
tla arch is a revision control system: a program that let's programmers
archive a history of changes made to the software they maintain and
that, more importantly, helps programmers to coordinate, syncronize,
and combine multiple lines of development for a single project.

arch version tla is a C version of the reference arch concepts.


%prep
%setup

## using: rpmbuild -ba --target=i686-redhat-linux tls-1.0.6.spec

%build
cd %{_builddir}/%{name}-%{version}/src
mkdir =build
cd =build
## imitate what an rpm macro would export
export CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}" FFLAGS="${RPM_OPT_FLAGS}";
../configure --prefix=%{_prefix} --destdir=%{buildroot}
make
# ok, I tested already
make test


%install
rm -rf %{buildroot}
cd %{_builddir}/%{name}-%{version}/src/=build
make install
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
%defattr(-, root, root)
%doc COPYING =INSTALL =RELEASE-ID html ps texi
%{_bindir}
#{_includedir}
#{_libdir}
#{_libexecdir}

%changelog
* Thu Jul 10 2003 Angles <angles@aminvestments.com>
- bump to version tls 1.0.6

* Mon Jun 30 2003 Angles <angles@aminvestments.com>
- this is c version of larch called tls
- bump to version tls 1.0.4

* Sun May 21 2002 Angles <angles@aminvestments.com>
- bump to version 1.0pre16

* Sun May 05 2002 Angles <angles@aminvestments.com>
- bump to version 1.0pre15

* Thu Apr 11 2002 Angles <angles@aminvestments.com>
- bump to version 1.0pre14
- automate patch2 to match build hosts actual vars

* Mon Mar 27 2002 Angles <angles@phpgroupware.org>
- bump to version 1.0pre13
- redo patches so no version-name strings are in the patch paths

* Mon Mar 11 2002 Angles <angles@phpgroupware.org>
- initial package release, version 1.0pre11
- make symlinks in linexec tree relative to remove hard coded rpm buildroot path
- find useful docs and assemble for the rpm doc macro
