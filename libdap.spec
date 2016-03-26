#
# Conditional build:
%bcond_with	tests		# perform tests
#
Summary:	OPeNDAP C++ implementation of the Data Access Protocol
Summary(pl.UTF-8):	OPeNDAP - implementacja w C++ protokołu DAP (Data Access Protocol)
Name:		libdap
Version:	3.17.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opendap.org/pub/source/%{name}-%{version}.tar.gz
# Source0-md5:	ebeff3892b45fb95ea80fc6ffafb6448
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	bison >= 3.0
%{?with_tests:BuildRequires:	cppunit-devel >= 1.12.0}
BuildRequires:	curl-devel >= 7.19.0
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.7.0
BuildRequires:	pkgconfig
Requires:	curl >= 7.19.0
Requires:	libxml2 >= 1:2.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the OPeNDAP C++ implementation of the Data
Access Protocol version 2 (DAP2) with some extensions that will be
part of DAP3.

The DAP2 is used to provide a uniform way of accessing a variety of
different types of data across the Internet. It was originally part of
the DODS and then NVODS projects. The focus of those projects was
access to Earth-Science data, so much of the software developed using
the DAP2 to date has centered on that discipline. However, the DAP2
data model is very general (and similar to a modern structured
programming language) so it can be applied to a wide variety of
fields.

%description -l pl.UTF-8
Ten pakiet zawiera OPeNDAP - implementację w C++ protokołu dostępu do
danych Data Access Protocol w wersji 2 (DAP2) z pewnymi
rozszerzeniami, które będą częścią DAP3.

DAP2 ma za zadanie udostępnienie jednolitego sposobu dostępu do wielu
różnych rodzajów danych w Internecie. Był oryginalnie częścią
projektów DODS, a następnie NVODS. Projekty te skupiały się na
dostępie do danych Earth-Science, więc większość programów
tworzonych przy użyciu DAP2 była związana z tą dyscypliną nauki.
Jednak model danych DAP2 jest bardzo ogólny (i podobny do
współczesnych strukturalnych języków programowania), więc może
dotyczyć wielu różnych dziedzin.

%package devel
Summary:	Header files for OPeNDAP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OPeNDAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.19.0
Requires:	libstdc++-devel
Requires:	libuuid-devel
Requires:	libxml2-devel >= 1:2.7.0

%description devel
Header files for OPeNDAP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OPeNDAP.

%package static
Summary:	Static OPeNDAP library
Summary(pl.UTF-8):	Statyczna biblioteka OPeNDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OPeNDAP library.

%description static -l pl.UTF-8
Statyczna biblioteka OPeNDAP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I conf -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdap*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT_* NEWS README*
%attr(755,root,root) %{_bindir}/getdap
%attr(755,root,root) %{_bindir}/getdap4
%attr(755,root,root) %{_libdir}/libdap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdap.so.21
%attr(755,root,root) %{_libdir}/libdapclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdapclient.so.6
%attr(755,root,root) %{_libdir}/libdapserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdapserver.so.7
%{_mandir}/man1/getdap.1*
%{_mandir}/man1/getdap4.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dap-config
%attr(755,root,root) %{_bindir}/dap-config-pkgconfig
%attr(755,root,root) %{_libdir}/libdap.so
%attr(755,root,root) %{_libdir}/libdapclient.so
%attr(755,root,root) %{_libdir}/libdapserver.so
%{_libdir}/libtest-types.a
%{_includedir}/libdap
%{_pkgconfigdir}/libdap.pc
%{_pkgconfigdir}/libdapclient.pc
%{_pkgconfigdir}/libdapserver.pc
%{_aclocaldir}/libdap.m4
%{_mandir}/man1/dap-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdap.a
%{_libdir}/libdapclient.a
%{_libdir}/libdapserver.a
