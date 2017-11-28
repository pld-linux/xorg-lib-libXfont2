Summary:	X font library version 2
Summary(pl.UTF-8):	Biblioteka fontów X w wersji 2
Name:		xorg-lib-libXfont2
Version:	2.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXfont2-%{version}.tar.bz2
# Source0-md5:	b7ca87dfafeb5205b28a1e91ac3efe85
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	docbook-dtd44-xml
BuildRequires:	freetype-devel >= 2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontsproto-devel >= 2.1.3
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.7
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font
file formats, and rasterizing them. It is used by the X servers, the X
Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients. X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%description -l pl.UTF-8
libXfont udostępnia główną część starego systemu fontów X11,
obsługującą pliki indeksów (fonts.dir, fonts.alias, fonts.scale),
różne formaty plików fontów oraz rasteryzację ich. Jest używana przez
serwer X, serwer fontów X (xfs - X Font Server) i różne narzędzia
związane z fontami (np. bdftopcf), ale nie powinna być używana przez
normalne aplikacje klienckie X11. Te ostatnie powinny odwoływać się do
fontów przez nowe API w libXft lub stare API w libX11.

%package devel
Summary:	Header files for libXfont2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXfont2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	freetype-devel >= 2
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-xtrans-devel
Requires:	xorg-proto-fontsproto-devel >= 2.1.3
Requires:	xorg-proto-xproto-devel
Requires:	zlib-devel

%description devel
X font library version 2.

This package contains the header files needed to develop programs that
use libXfont2.

%description devel -l pl.UTF-8
Biblioteka fontów X w wersji 2.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXfont2.

%package static
Summary:	Static libXfont2 library
Summary(pl.UTF-8):	Biblioteka statyczna libXfont2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
X font library version 2.

This package contains the static libXfont2 library.

%description static -l pl.UTF-8
Biblioteka fontów X w wersji 2.

Pakiet zawiera statyczną bibliotekę libXfont2.

%prep
%setup -q -n libXfont2-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-bzip2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXfont2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXfont2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXfont2.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libXfont2.so
%{_includedir}/X11/fonts/libxfont2.h
%{_pkgconfigdir}/xfont2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXfont2.a
