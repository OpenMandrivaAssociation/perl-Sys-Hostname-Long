%define module	Sys-Hostname-Long
%define name	perl-%{module}
%define version	1.4
%define release	12

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sys/Hostname/*
%{_mandir}/*/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-11mdv2012.0
+ Revision: 765668
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4-10
+ Revision: 764179
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-9
+ Revision: 667319
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-8mdv2011.0
+ Revision: 426591
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-7mdv2009.1
+ Revision: 351718
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 224060
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-5mdv2008.1
+ Revision: 180574
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4-4mdv2008.0
+ Revision: 67519
- rebuild


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:02:48 (54131)
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:01:27 (54130)
Import perl-Sys-Hostname-Long

* Mon Oct 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdk
- remove win32 calls

* Mon Oct 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.4-1mdk
- Initial Mandriva release.

