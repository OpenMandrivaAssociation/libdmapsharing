%define api 3.0
%define major 2
%define libname %mklibname dmapsharing %{api} %{major}
%define develname %mklibname -d dmapsharing

Summary:	A DMAP client and server library
Name:		libdmapsharing
Version:	2.9.15
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.flyn.org/projects/libdmapsharing/index.html
Source0:	http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz
Patch0:		libdmapsharing-2.9.14-link.patch

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libsoup-2.4)

%description
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package -n %{libname}
Summary:	A DMAP client and server library
Group:		System/Libraries

%description -n %{libname}
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package -n %{develname}
Summary:	Files needed to develop applications using libdmapsharing
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%prep
%setup -q
%apply_patches
NOCONFIGURE=yes gnome-autogen.sh

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

%changelog
* Wed May 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.9.15-1
+ Revision: 797775
- new version 2.9.15
- cleaned up spec
- new api 3.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.9-3
+ Revision: 662363
- mass rebuild

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 2.1.9-2
+ Revision: 650922
- rebuild for updated libsoup libtool archive

* Wed Nov 17 2010 Götz Waschk <waschk@mandriva.org> 2.1.9-1mdv2011.0
+ Revision: 598140
- update to new version 2.1.9

* Sun Oct 31 2010 Götz Waschk <waschk@mandriva.org> 2.1.7-1mdv2011.0
+ Revision: 591179
- update to new version 2.1.7

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 571652
- import libdmapsharing

