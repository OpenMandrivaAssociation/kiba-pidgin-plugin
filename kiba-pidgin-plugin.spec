%define svn	722
%define release 0.%{svn}.4
%define fname	kiba-gaim-plugin

Name:		kiba-pidgin-plugin
Version:	0.1
Release:	%{release}
Summary:	Pidgin plugin for Kiba-Dock
Group:		System/X11
URL:		http://www.kiba-dock.org/
Source0:	%{fname}-%{svn}.tar.lzma
patch0:		kiba-pidgin-plugin.kiba-dock-version.patch
License:	GPLv2+
BuildRequires:	kiba-dock-devel = %{version}
BuildRequires:	intltool
BuildRequires:	pidgin-devel
BuildRequires:	librsvg-devel
BuildRequires:	startup-notification-devel
Requires:	kiba-dock
Requires:	pidgin

%description
Pidgin plugin for Kiba-Dock.

%prep
%setup -q -n %{fname}
%patch0 -p1 -b .kiba-dock-version

%build
sh autogen.sh -V
%configure2_5x
%make

%install
%makeinstall_std
%find_lang pidgin-kiba-plugin

%files -f pidgin-kiba-plugin.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/pidgin/libkiba.*
