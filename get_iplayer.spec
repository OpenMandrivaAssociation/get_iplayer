%define name 	get_iplayer
%define version 2.80
%define release 2

Summary:	iPlayer TV, Radio, Podcase, Programmes stream tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
Url:		http://www.infradead.org/get_iplayer/html/get_iplayer.html
Source:		ftp://ftp.infradead.org/pub/get_iplayer/get_iplayer-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Suggests:	flvstreamer

%description
Lists, searches and records BBC iPlayer TV/Radio, BBC Podcast and ITVplayer TV programmes

Note: This is the version from:
  http://www.infradead.org/get_iplayer/html/get_iplayer.html
which is a fork/continuation of the original from:
  http://linuxcentre.net/getiplayer
which was discontinued as outlined here:
  http://linuxcentre.net/get_iplayer-dropped-in-response-to-bbcs-lack-of-support-for-open-source


%prep
%setup -q

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/%{name}/plugins

install -m 755 get_iplayer %{buildroot}%{_bindir}
install -m 644 plugins/*.plugin %{buildroot}%{_datadir}/%{name}/plugins/

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/get_iplayer
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/*.plugin
%doc README.txt
