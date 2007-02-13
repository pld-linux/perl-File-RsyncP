#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	RsyncP
Summary:	File::RsyncP - Perl implementation of an rsync client
Summary(pl.UTF-8):	File::RsyncP - implementacja klienta rsync w Perlu
Name:		perl-File-RsyncP
Version:	0.62
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16dcbd537d20c7435e1affd09d65a5ce
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::RsyncP is a Perl implementation of an rsync client. It can send
or receive files, either by running rsync on the remote machine, or
connecting to an rsyncd daemon on the remote machine.

File::RsyncP seperates all file system I/O into a seperate module
(File::RsyncP::FileIO), which can be replaced by any module of your
own design. This allows rsync interfaces to non-filesystem data types
(eg: databases) to be developed with relative ease.

File::RsyncP does not yet provide a command-line interface that mimics
native rsync. Instead it provides an API that makes it possible to
write simple scripts that talk to rsync or rsyncd.

%description -l pl.UTF-8
File::RsyncP jest implementacją klienta rsync w Perlu. Umożliwia
wysyłanie i pobieranie plików, zarówno przez uruchomionego zdalnie
klienta rsync jak i przez połączenie z demonem rsyncd na zdalnej
maszynie.

Wszystkie operacje wejścia/wyjścia na systemie plików zostały
wyodrębnione do oddzielnego modułu (File::RsyncP::FileIO), który może
być zastąpiony przez inny moduł własnego projektu. Umożliwia to w
miarę proste tworzenie interfejsów do rsynca, które nie operują na
systemie plików a np. na bazach danych.

File::RsyncP nie udostępnia jeszcze interaktywnego interfejsu
naśladującego linię poleceń programu rsync. W zamian udostępnia API,
umożliwiające pisanie prostych skryptów do komunikacji z rsync
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
%{perl_vendorarch}/File/RsyncP.pm
%dir %{perl_vendorarch}/File/RsyncP
%{perl_vendorarch}/File/RsyncP/*.pm
%dir %{perl_vendorarch}/auto/File/RsyncP
%dir %{perl_vendorarch}/auto/File/RsyncP/Digest
%dir %{perl_vendorarch}/auto/File/RsyncP/FileList
%{perl_vendorarch}/auto/File/RsyncP/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/File/RsyncP/*/*.so
%{_mandir}/man3/*
