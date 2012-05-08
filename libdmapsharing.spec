%define	api 3.0
%define major 2
%define libname %mklibname dmapsharing %api %{major}
%define develname %mklibname -d dmapsharing

Summary: A DMAP client and server library
Name: libdmapsharing
Version: 2.9.15
Release: 1
License: LGPLv2+
Group: System/Libraries
URL: http://www.flyn.org/projects/libdmapsharing/index.html
Source0: http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz

BuildRequires: gnome-common
BuildRequires: gtk-doc
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(avahi-glib)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gee-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(libsoup-2.4)

%description
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package -n %{libname}
Summary: A DMAP client and server library
Group: System/Libraries

%description -n %{libname}
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package -n %{develname}
Summary: Files needed to develop applications using libdmapsharing
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdmapsharing-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/libdmapsharing-*.pc
%{_includedir}/libdmapsharing-*
%{_libdir}/libdmapsharing-%{api}.so
%{_datadir}/gtk-doc/html/libdmapsharing-%{api}

