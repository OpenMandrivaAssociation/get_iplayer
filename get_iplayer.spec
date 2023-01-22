%define debug_package %{nil}
%define __requires_exclude perl\\(Programme|Streamer

Summary:	iPlayer TV, Radio, Podcase, Programmes stream tool
Name:		get_iplayer
Version:	3.31
Release:	1
License:	GPL
Group:		Networking/File transfer
Url:		http://www.infradead.org/get_iplayer/html/get_iplayer.html
Source:		https://github.com/get-iplayer/get_iplayer/archive/v%{version}.tar.gz
BuildRequires:	xz
Requires:	perl-XML-LibXML
Suggests:	rtmpdump

%description
Lists, searches and records BBC iPlayer TV/Radio, BBC Podcast
and ITVplayer TV programmes

Note: This is the version from:
  http://www.infradead.org/get_iplayer/html/get_iplayer.html
which is a fork/continuation of the original from:
  http://linuxcentre.net/getiplayer
which was discontinued as outlined here:
  http://linuxcentre.net/get_iplayer-dropped-in-response-to-bbcs
-lack-of-support-for-open-source


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 755 get_iplayer %{buildroot}%{_bindir}
install -m 644 get_iplayer.1  %{buildroot}/%{_mandir}/man1
xz  %{buildroot}/%{_mandir}/man1/*
%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/get_iplayer
%{_mandir}/man1/get_iplayer.1*
%doc README.md
