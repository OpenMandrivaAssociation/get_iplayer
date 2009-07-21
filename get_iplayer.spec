%define name 	get_iplayer
%define version 2.10
%define release %mkrel 1

Summary: 	iPlayer TV, Radio, Podcase, Programmes stream tool
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Networking/File transfer
Url: 		http://linuxcentre.net/getiplayer/
Source: 	http://linuxcentre.net/get_iplayer/packages/get_iplayer-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root

%description
Lists, searches and records BBC iPlayer TV/Radio, BBC Podcast and ITVplayer TV programmes

%prep
%setup -q

%build

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/%{name}/plugins

install -m 755 get_iplayer %{buildroot}%{_bindir}
install -m 644 get_iplayer.1 %{buildroot}%{_mandir}/man1
install -m 644 plugins/*.plugin %{buildroot}%{_datadir}/%{name}/plugins/

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/get_iplayer
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/*.plugin
%{_mandir}/man1/get_iplayer.1*
%doc README.txt
