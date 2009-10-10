Summary: Planning of astronomical observations
Name: proas
Version: 2.1.2
Release: 2%{?dist}
License: GPL+
Group: Applications/Engineering
URL: https://guaix.fis.ucm.es/projects/proas/wiki
Source0: ftp://astrax.fis.ucm.es/pub/users/spr/proas/%{name}-%{version}.tar.gz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: pgplot-devel gcc-gfortran

%description
Proas is a program devoted to the computation of the visibility conditions of 
astronomical objects. The initial data are the observatory location, observing
date, and the target coordinates. The program computes the object altitude as 
a function of the universal time (UT).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README manual.ps
%{_bindir}/*

%changelog
* Wed Sep 30 2009 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.2-2
- Changed licence to GPL+

* Wed Sep 16 2009 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.2-1
- Submitted to rpmfusion

* Fri Jun 27 2008 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.1-3
- Rebuilt for el5

* Thu Jun 19 2008 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.1-2
- Patch to set the default equinox in 2000.0

* Fri Jan 18 2008 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.1-1
- New upstream sources

* Sun Jul 22 2007 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.1.0-1
- New upstream sources

* Fri Oct 28 2005 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.0-3
- Rebuilt for pgplot-5.2.2-8.

* Mon Oct 10 2005 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.0-2
- Updated spec file.

* Tue Jan 10 2002 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.0-1
- Initial RPM file.
