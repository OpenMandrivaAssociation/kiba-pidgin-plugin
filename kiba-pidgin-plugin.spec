%define svn	722
%define release %mkrel 0.%{svn}.1
%define fname	kiba-gaim-plugin

Name:		kiba-pidgin-plugin
Version:	0.1
Release:	%{release}
Summary:	Pidgin plugin for Kiba-Dock
Group:		System/X11
URL:		http://www.kiba-dock.org/
Source0:	%{fname}-%{svn}.tar.lzma
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-root
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

%build
sh autogen.sh -V
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang pidgin-kiba-plugin

%clean
rm -rf %{buildroot}

%files -f pidgin-kiba-plugin.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/pidgin/libkiba.*

