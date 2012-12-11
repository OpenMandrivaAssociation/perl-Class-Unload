%define upstream_name    Class-Unload
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Unload a class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Unload a class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 656892
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1
+ Revision: 634213
- update to new version 0.07

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 553073
- update to 0.06

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401703
- rebuild using %%perl_convert_version
- fixed license field

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2009.1
+ Revision: 309626
- update to new version 0.05

* Tue Dec 02 2008 Jérôme Quelin <jquelin@mandriva.org> 0.03-1mdv2009.1
+ Revision: 309265
- import perl-Class-Unload


* Tue Dec 02 2008 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist

