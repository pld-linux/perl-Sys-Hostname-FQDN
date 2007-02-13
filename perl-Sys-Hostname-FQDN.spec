#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sys
%define		pnam	Hostname-FQDN
Summary:	Sys::Hostname::FQDN - extract full host name
Summary(pl.UTF-8):	Sys::Hostname::FQDN - uzyskiwanie pełnej nazwy hosta
Name:		perl-Sys-Hostname-FQDN
Version:	0.07
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab6b00e3f0781b3e074daa53160d1815
Patch0:		%{name}-segv.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Hostname::FQDN uses the host C library to discover the (usually)
short host name, then uses (perl) gethostbyname to extract the real
hostname.

The results from gethostbyname are exported as gethostinfo and
asciihostinfo as a convenience since they are available. Similarly,
the C library functions inet_ntoa and inet_aton are exported.

%description -l pl.UTF-8
Sys::Hostname::FQDN używa biblioteki C do uzyskania (zwykle) krótkiej
nazwy hosta, a następnie używa (perlowej) funkcji gethostbyname aby
uzyskać prawdziwą nazwę hosta.

Wyniki z gethostbyname są dla wygody eksportowane jako gethostinfo i
asciihostinfo, ponieważ są dostępne. Podobnie są wyeksportowane
funkcje biblioteki C inet_ntoa i inet_aton.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Sys/Hostname/FQDN/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Sys/Hostname
%{perl_vendorarch}/Sys/Hostname/FQDN.pm
%dir %{perl_vendorarch}/auto/Sys/Hostname
%dir %{perl_vendorarch}/auto/Sys/Hostname/FQDN
%{perl_vendorarch}/auto/Sys/Hostname/FQDN/FQDN.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Hostname/FQDN/FQDN.so
%{_mandir}/man3/*
