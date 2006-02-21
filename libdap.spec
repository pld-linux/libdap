Summary:	OPeNDAP C++ implementation of the Data Access Protocol
Summary(pl):	OPeNDAP - implementacja w C++ protoko³u DAP (Data Access Protocol)
Name:		libdap
Version:	3.5.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.unidata.ucar.edu/pub/dods/DODS-3.5/source/%{name}-%{version}.tar.gz
# Source0-md5:	62579a9814ccb39579796cdcc1560067
Patch0:		%{name}-gcc4.patch
URL:		http://opendap.org/
BuildRequires:	curl-devel >= 7.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.6.16
Requires:	curl >= 7.12.0
Requires:	libxml2 >= 2.6.16
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

%description -l pl
Ten pakiet zawiera OPeNDAP - implementacjê w C++ protoko³u dostêpu do
danych Data Access Protocol w wersji 2 (DAP2) z pewnymi
rozszerzeniami, które bêd± czê¶ci± DAP3.

DAP2 ma za zadanie udostêpnienie jednolitego sposobu dostêpu do wielu
ró¿nych rodzajów danych w Internecie. By³ oryginalnie czê¶ci±
projektów DODS, a nastêpnie NVODS. Projekty te skupia³y siê na
dostêpie do danych Earth-Science, wiêc wiêkszo¶æ programów
tworzonych przy u¿yciu DAP2 by³a zwi±zana z t± dyscyplin± nauki.
Jednak model danych DAP2 jest bardzo ogólny (i podobny do
wspó³czesnych strukturalnych jêzyków programowania), wiêc mo¿e
dotyczyæ wielu ró¿nych dziedzin.

%package devel
Summary:	Header files for OPeNDAP library
Summary(pl):	Pliki nag³ówkowe biblioteki OPeNDAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.12.0
Requires:	libstdc++-devel

%description devel
Header files for OPeNDAP library.

%description devel -l pl
Pliki nag³ówkowe biblioteki OPeNDAP.

%package static
Summary:	Static OPeNDAP library
Summary(pl):	Statyczna biblioteka OPeNDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OPeNDAP library.

%description static -l pl
Statyczna biblioteka OPeNDAP.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT_* NEWS README*
%attr(755,root,root) %{_bindir}/getdap
%attr(755,root,root) %{_sbindir}/deflate
%attr(755,root,root) %{_libdir}/libdap.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dap-config
%attr(755,root,root) %{_libdir}/libdap.so
%{_libdir}/libdap.la
%{_includedir}/libdap
%{_aclocaldir}/libdap.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libdap.a
