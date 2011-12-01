%define major 2
%define libname %mklibname dmapsharing %major
%define develname %mklibname -d dmapsharing

Name: libdmapsharing
Version: 2.1.9
Release: %mkrel 3
License: LGPLv2+
Source: http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.flyn.org/projects/libdmapsharing/index.html
Summary: A DMAP client and server library
Group: System/Libraries
BuildRequires: glib2-devel
BuildRequires: libsoup-devel
BuildRequires: avahi-glib-devel
BuildRequires: avahi-client-devel
BuildRequires: avahi-common-devel
BuildRequires: gstreamer0.10-devel

%description
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package -n %libname
Summary: A DMAP client and server library
Group: System/Libraries

%description -n %libname
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%files -n %libname
%defattr(-, root, root, -)
%{_libdir}/libdmapsharing.so.%{major}
%{_libdir}/libdmapsharing.so.%{major}.*

%package -n %develname
Summary: Files needed to develop applications using libdmapsharing
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%files -n %develname
%defattr(-, root, root, -)
%{_libdir}/pkgconfig/libdmapsharing-*.pc
%{_includedir}/libdmapsharing-*
%{_libdir}/libdmapsharing.so
%{_libdir}/libdmapsharing.la
%{_datadir}/gtk-doc/html/libdmapsharing

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
