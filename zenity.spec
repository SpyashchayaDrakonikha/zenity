Summary:	The GNOME port of dialog
Summary(pl):	Port dialog dla GNOME
Name:		zenity
Version:	2.7.91
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	a079dce51aaeb7d66707015f1c29399b
Patch0:		%{name}-locale-names.patch
URL:		http://freshmeat.net/projects/zenity/
BuildRequires:	GConf2-devel >= 2.7.91
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomecanvas-devel >= 2.7.91
BuildRequires:	perl-base
BuildRequires:	popt-devel
BuildRequires:	scrollkeeper
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl
zenity jest kontynuacj� programu gdialog, portu dialog dla GNOME.
Umo�liwia on wy�wietlanie okien dialogowych z linii komend i ze
skrypt�w pow�oki.

%prep
%setup -q
%patch0 -p1

rm po/no.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# zenity-0.1.mo but gnome/help/zenity
%find_lang %{name}-0.1 --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
