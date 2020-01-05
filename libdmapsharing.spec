%define gstapi	1.0
%define api	3.0
%define major	2
%define libname	%mklibname dmapsharing %{api} %{major}
%define devname	%mklibname -d dmapsharing

Summary:	A DMAP client and server library
Name:		libdmapsharing
Version:	2.9.39
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.flyn.org/projects/libdmapsharing/index.html
Source0:	http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz

BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(howl)
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

%package -n %{devname}
Summary:	Files needed to develop applications using libdmapsharing
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%prep
%setup -q
%autopatch -p1

%build
%configure LIBS=-lm
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libdmapsharing-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libdmapsharing-%{api}.pc
%{_includedir}/libdmapsharing-%{api}
%{_libdir}/libdmapsharing-%{api}.so
%{_datadir}/gtk-doc/html/libdmapsharing-%{api}
%{_datadir}/vala/vapi/%{name}-%{api}.vapi
