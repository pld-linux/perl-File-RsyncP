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
File::RsyncP jest implementacj± klienta rsync w Perlu. Umo¿liwia
wysy³anie i pobieranie plików, zarówno przez uruchomionego zdalnie
klienta rsync jak i przez po³±czenie z demonem rsyncd na zdalnej
maszynie.

Wszystkie operacje wej¶cia/wyj¶cia na systemie plików zosta³y
wyodrêbnione do oddzielnego modu³u (File::RsyncP::FileIO), który mo¿e
byæ zast±piony przez inny modu³ w³asnego projektu. Umo¿liwia to w
miarê proste tworzenie interfejsów do rsynca, które nie operuj± na
systemie plików a np. na bazach danych.

File::RsyncP nie udostêpnia jeszcze interaktywnego interfejsu
na¶laduj±cego liniê poleceñ programu rsync. W zamian udostêpnia API,
umo¿liwiaj±ce pisanie prostych skryptów do komunikacji z rsync
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
