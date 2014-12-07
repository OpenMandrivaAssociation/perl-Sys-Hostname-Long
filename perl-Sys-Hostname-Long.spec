%define module	Sys-Hostname-Long

Summary:	Try every conceivable way to get full hostname
Name:		perl-%{module}
Version:	1.4
Release:	19
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	%{module}-%{version}.tar.bz2
Patch0:		Sys-Hostname-Long-1.4-no_win32.diff
BuildArch:	noarch
BuildRequires:	perl-devel

%description
How to get the host full name in perl on multiple operating systems.

%prep
%setup -qn %{module}-%{version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Sys/Hostname/*
%{_mandir}/man3/*

