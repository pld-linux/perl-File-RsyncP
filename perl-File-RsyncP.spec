#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	RsyncP
Summary:	File::RsyncP - Perl implementation of an rsync client
Summary(pl.UTF-8):	File::RsyncP - implementacja klienta rsync w Perlu
Name:		perl-File-RsyncP
Version:	0.70
Release:	14
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CB/CBARRATT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f244372d15a2991b8700f62e73ac51e4
URL:		http://search.cpan.org/dist/File-RsyncP/
BuildRequires:	perl-Encode
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

%{__make} -j1

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
%attr(755,root,root) %{perl_vendorarch}/auto/File/RsyncP/*/*.so
%{_mandir}/man3/*
