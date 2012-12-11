%define upstream_name    POE-Filter-HTTP-Parser
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A HTTP POE filter for HTTP clients or servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTTP::Parser)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::POE::Client::TCP)
BuildRequires:	perl(Test::POE::Server::TCP)
Requires:	perl(HTTP::Parser)
BuildArch:	noarch

%description
POE::Filter::HTTP::Parser is a the POE::Filter manpage for HTTP which is
based on the HTTP::Parser manpage.

It can be used to easily create the POE manpage based HTTP servers or
clients.

With the 'type' set to 'client', which is the default behaviour, 'get' will
parse the HTTP::Response manpage objects from HTTP streams and 'put' will
accept the HTTP::Request manpage objects and convert them to HTTP streams.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.60.0-4mdv2011.0
+ Revision: 658270
- rebuild

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.60.0-3
+ Revision: 658247
- add runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2
+ Revision: 657460
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.60.0-1
+ Revision: 643455
- update to new version 1.06

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 624757
- import perl-POE-Filter-HTTP-Parser

