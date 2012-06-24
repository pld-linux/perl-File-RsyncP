#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	RsyncP
Summary:	File::RsyncP - Perl implementation of an rsync client
Summary(pl):	File::RsyncP - implementacja klienta rsync w Perlu
Name:		perl-%{pdir}-%{pnam}
Version:	0.50
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e444b1b5f0981043e3b462fc4178f0b0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::RsyncP is a Perl implementation of an rsync client. It can send
or receive files, either by running rsync on the remote machine, or
connecting to an rsyncd deamon on the remote machine.

File::RsyncP seperates all file system I/O into a seperate module
(File::RsyncP::FileIO), which can be replaced by any module of your
own design. This allows rsync interfaces to non-filesystem data types
(eg: databases) to be developed with relative ease.

File::RsyncP does not yet provide a command-line interface that mimics
native rsync. Instead it provides an API that makes it possible to
write simple scripts that talk to rsync or rsyncd.

%description -l pl
File::RsyncP jest implementacj� klienta rsync w Perlu. Umo�liwia
wysy�anie i pobieranie plik�w, zar�wno przez uruchomionego zdalnie
klienta rsync jak i przez po��czenie z demonem rsyncd na zdalnej
maszynie.

Wszystkie operacje wej�cia/wyj�cia na systemie plik�w zosta�y
wyodr�bnione do oddzielnego modu�u (File::RsyncP::FileIO), kt�ry mo�e
by� zast�piony przez inny modu� w�asnego projektu. Umo�liwia to w
miar� proste tworzenie interfejs�w do rsynca, kt�re nie operuj� na
systemie plik�w a np. na bazach danych.

File::RsyncP nie udost�pnia jeszcze interaktywnego interfejsu
na�laduj�cego lini� polece� programu rsync. W zamian udost�pnia API,
umo�liwiaj�ce pisanie prostych skrypt�w do komunikacji z rsync
i rsyncd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorarch}/%{pdir}/%{pnam}
%{perl_vendorarch}/%{pdir}/%{pnam}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}/Digest
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}/FileList
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*/*.so
%{_mandir}/man3/*
