#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	EasyOBJ
Summary:	XML::EasyOBJ - easy XML object navigation
Summary(pl.UTF-8):   XML::EasyOBJ - łatwa nawigacja po obiekcie XML
Name:		perl-XML-EasyOBJ
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	875e4331ba2b8eebfee1ea15f4437992
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is designed to make accessing an XML document rather
trivial. You don't need to understand the DOM, you don't need to even
know what SAX is, all you need to know is how an XML document is
structured and how to program with objects (OOP).

%description -l pl.UTF-8
Ten moduł został zaprojektowany aby uczynić dostęp do dokumentów XML
w miarę prostym. Nie trzeba rozumieć DOM, nie trzeba nawet wiedzieć
czym jest SAX, wystarczy znać tylko strukturę dokumentu XML i
programowanie z użyciem obiektów (OOP).

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
%{perl_vendorlib}/XML/EasyOBJ.pm
%{_mandir}/man3/*
