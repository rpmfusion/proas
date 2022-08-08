Summary: Planning of astronomical observations
Name: proas
Version: 2.2.0
Release: 16%{?dist}
License: GPL+
Group: Applications/Engineering
URL: https://guaix.fis.ucm.es/projects/proas/wiki
Source0: ftp://astrax.fis.ucm.es/pub/software/proas/%{name}-%{version}.tar.gz
BuildRequires: pgplot-devel gcc-gfortran

%description
Proas is a program devoted to the computation of the visibility conditions of 
astronomical objects. The initial data are the observatory location, observing
date, and the target coordinates. The program computes the object altitude as 
a function of the universal time (UT).

%prep
%setup -q

%build
%configure FFLAGS="${FFLAGS} -fbackslash"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc COPYING README manual.ps
%{_bindir}/*

%changelog
* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Oct 10 2012 Sergio Pascual <sergiopr@fis.ucm.es> - 2.2.0-2
- Enable -fbackslash (fixes bz #2517)

* Thu Mar 22 2012 Sergio Pascual <sergiopr@fis.ucm.es> - 2.2.0-1
- New upstream source

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

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

* Thu Jan 10 2002 Sergio Pascual <sergiopr@astrax.fis.ucm.es> 2.0-1
- Initial RPM file.
