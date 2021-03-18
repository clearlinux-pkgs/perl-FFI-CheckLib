#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-FFI-CheckLib
Version  : 0.27
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-CheckLib-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-CheckLib-0.27.tar.gz
Summary  : 'Check that a library is available for FFI'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-FFI-CheckLib-license = %{version}-%{release}
Requires: perl-FFI-CheckLib-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Importer)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Term::Table)
BuildRequires : perl(Test2::Require::EnvVar)
BuildRequires : perl(Test2::Require::Module)
BuildRequires : perl(Test2::V0)

%description
NAME
FFI::CheckLib - Check that a library is available for FFI
VERSION
version 0.27

%package dev
Summary: dev components for the perl-FFI-CheckLib package.
Group: Development
Provides: perl-FFI-CheckLib-devel = %{version}-%{release}
Requires: perl-FFI-CheckLib = %{version}-%{release}

%description dev
dev components for the perl-FFI-CheckLib package.


%package license
Summary: license components for the perl-FFI-CheckLib package.
Group: Default

%description license
license components for the perl-FFI-CheckLib package.


%package perl
Summary: perl components for the perl-FFI-CheckLib package.
Group: Default
Requires: perl-FFI-CheckLib = %{version}-%{release}

%description perl
perl components for the perl-FFI-CheckLib package.


%prep
%setup -q -n FFI-CheckLib-0.27
cd %{_builddir}/FFI-CheckLib-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-FFI-CheckLib
cp %{_builddir}/FFI-CheckLib-0.27/LICENSE %{buildroot}/usr/share/package-licenses/perl-FFI-CheckLib/8c55a3fb07df5b7d899c736fabd29f2dc765210c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/FFI::CheckLib.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-FFI-CheckLib/8c55a3fb07df5b7d899c736fabd29f2dc765210c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/FFI/CheckLib.pm
