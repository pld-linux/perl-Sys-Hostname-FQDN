#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	Hostname-FQDN
Summary:	Sys::Hostname::FQDN - extract full host name
Summary(pl):	Sys::Hostname::FQDN - uzyskiwanie pe³nej nazwy hosta
Name:		perl-Sys-Hostname-FQDN
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b7ffa6e39156f8d519903f7e487d09d
Patch0:		%{name}-segv.patch
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Hostname::FQDN uses the host C library to discover the (usually)
short host name, then uses (perl) gethostbyname to extract the real
hostname.

The results from gethostbyname are exported as gethostinfo and
asciihostinfo as a convenience since they are available. Similarly,
the C library functions inet_ntoa and inet_aton are exported.

%description -l pl
Sys::Hostname::FQDN u¿ywa biblioteki C do uzyskania (zwykle) krótkiej
nazwy hosta, a nastêpnie u¿ywa (perlowej) funkcji gethostbyname aby
uzyskaæ prawdziw± nazwê hosta.

Wyniki z gethostbyname s± dla wygody eksportowane jako gethostinfo i
asciihostinfo, poniewa¿ s± dostêpne. Podobnie s± wyeksportowane
funkcje biblioteki C inet_ntoa i inet_aton.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

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
%dir %{perl_vendorarch}/Sys/Hostname
%{perl_vendorarch}/Sys/Hostname/FQDN.pm
%dir %{perl_vendorarch}/auto/Sys/Hostname
%dir %{perl_vendorarch}/auto/Sys/Hostname/FQDN
%{perl_vendorarch}/auto/Sys/Hostname/FQDN/autosplit.ix
%{perl_vendorarch}/auto/Sys/Hostname/FQDN/FQDN.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Hostname/FQDN/FQDN.so
%{_mandir}/man3/*
