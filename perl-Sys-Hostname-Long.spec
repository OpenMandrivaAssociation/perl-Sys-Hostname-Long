%define module	Sys-Hostname-Long
%define name	perl-%{module}
%define version	1.4
%define	release	%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Try every conceivable way to get full hostname
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	%{module}-%{version}.tar.bz2
Patch0:		Sys-Hostname-Long-1.4-no_win32.diff
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
How to get the host full name in perl on multiple operating systems.

%prep

%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sys/Hostname/*
%{_mandir}/*/*


