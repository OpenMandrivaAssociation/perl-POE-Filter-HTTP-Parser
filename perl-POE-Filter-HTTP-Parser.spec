%define upstream_name    POE-Filter-HTTP-Parser
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A HTTP POE filter for HTTP clients or servers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Parser)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(POE)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::POE::Client::TCP)
BuildRequires: perl(Test::POE::Server::TCP)
Requires: perl(HTTP::Parser)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


