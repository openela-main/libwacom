Name:           libwacom
Version:        1.6
Release:        3%{?dist}
Summary:        Tablet Information Client Library
Requires:       %{name}-data

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/linuxwacom/libwacom

Source0:        https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

Patch001:	0001-data-Add-ISDv4-51c7-Lenovo-IdeaPad-FLEX-14API-304.patch
Patch002:	0002-data-Add-enovo-IdeaPad-Flex-5-14ARE05-ISDv4-5215.patch
Patch003:	0003-data-Add-ISDv4-51e9-Lenovo-ThinkPad-P15-Gen-1-325.patch
Patch004:	0004-data-Add-ISDv4-5202-Lenovo-YOGA-C640-13IML-322.patch
Patch005:	0005-data-Add-Lenovo-X1-Yoga-3-Generation-ISDv4-5148-320.patch

Patch006:	0001-data-Add-multiple-Lenovo-ThinkPad-X1-Yoga-Gen-6-PIDs.patch
Patch007:	0002-data-Add-ISDv4-51f9-Lenovo-ThinkPad-L13-Yoga-358.patch
Patch008:	0003-data-Add-ISDv4-523a-Lenovo-Yoga-9-14ITL5-357.patch
Patch009:	0004-data-Add-ISDv4-5204-Lenovo-YOGA-C640-13IML-356.patch
Patch010:	0005-data-Add-ISDv4-5256-Lenovo-Yoga-7-15ITL5-351.patch
Patch011:	0006-data-Add-ISDv4-5216-Lenovo-IdeaPad-Flex-5-14IIL05-35.patch
Patch012:	0007-data-Add-ISDv4-528e-Lenovo-Yoga-6-13ARE05-346.patch
Patch013:	0008-data-Add-ISDv4-5229-Lenovo-ThinkPad-X1-Yoga-Gen-5-34.patch
Patch014:	0009-data-Add-Lenovo-ThinkPad-X13-Yoga-Gen-1-ISDv4-5220-3.patch
Patch015:	0010-data-Add-ISDv4-5072-Lenovo-ThinkPad-Yoga-11e-3rd-Gen.patch


BuildRequires:  meson gcc
BuildRequires:  glib2-devel libgudev1-devel
BuildRequires:  systemd systemd-devel
BuildRequires:  git
BuildRequires:  libxml2-devel

Requires:       %{name}-data = %{version}-%{release}

%description
%{name} is a library that provides information about Wacom tablets and
tools. This information can then be used by drivers or applications to tweak
the UI or general settings to match the physical tablet.

%package devel
Summary:        Tablet Information Client Library Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Tablet information client library library development package.

%package data
Summary:        Tablet Information Client Library Library Data Files
BuildArch:      noarch

# 65-libwacom.rules moved from libwacom to libwacom-data. Conflict here
# because there's no real use-case for having old libwacom and new
# libwacom-data installed. libwacom-data doesn't require libwacom but it
# does require the same version, so let's conflict with any older version
# here.
Conflicts:      %{name} < %{version}

%description data
Tablet information client library library data files.

%prep
%autosetup -S git

%build
%meson -Dtests=enabled -Ddocumentation=disabled
%meson_build

%install
%meson_install
install -d ${RPM_BUILD_ROOT}/%{_udevrulesdir}

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/libwacom.so.*
%{_bindir}/libwacom-list-local-devices
%{_mandir}/man1/libwacom-list-local-devices.1*

%files devel
%dir %{_includedir}/libwacom-1.0/
%dir %{_includedir}/libwacom-1.0/libwacom
%{_includedir}/libwacom-1.0/libwacom/libwacom.h
%{_libdir}/libwacom.so
%{_libdir}/pkgconfig/libwacom.pc

%files data
%doc COPYING
%{_udevrulesdir}/65-libwacom.rules
%{_udevhwdbdir}/65-libwacom.hwdb
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%dir %{_datadir}/libwacom/layouts
%{_datadir}/libwacom/layouts/*.svg

%changelog
* Wed May 26 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.6-3
- Add Lenovo tablet files from upstream (#1940874)

* Wed Jan 13 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.6-2
- Add Lenovo tablet files from upstream (#1914411)

* Tue Nov 03 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.6-1
- libwacom 1.6 (#1878160)

* Thu Jun 25 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.1-3
- Add a set of Lenovo tablets and styli (#1850319)

* Thu Nov 07 2019 Peter Hutterer <peter.hutterer@redhat.com> 1.1-2
- Conflict with older libwacom

* Thu Nov 07 2019 Peter Hutterer <peter.hutterer@redhat.com> 1.1-1
- libwacom 1.1 (#1741423)

* Thu Aug 09 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.31-1
- libwacom 0.31 (#1612758)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.30-1
- libwacom 0.30

* Wed Mar 07 2018 Peter Hutterer <peter.hutterer@redhat.com>
- Switch URLs to github

* Mon Mar 05 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.29-1
- libwacom 0.29

* Tue Feb 13 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.28-3
- Fix PairedID entry causing a debug message in the udev rules

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28-2
- Escape macros in %%changelog

* Thu Feb 08 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.28-1
- libwacom 0.28
- use autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26-3
- Switch to %%ldconfig_scriptlets

* Tue Oct 17 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.26-2
- run make check as part of the build (#1502637)

*  Fri Aug 25 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.26-1
- libwacom 0.26

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.25-1
- libwacom 0.25

* Wed Feb 15 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.24-1
- libwacom 0.24

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.23-2
- Upload the sources too...

* Fri Jan 20 2017 Peter Hutterer <peter.hutterer@redhat.com> 0.23-1
- libwacom 0.23

* Fri Nov 11 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.22-2
- Add Lenovo X1 Yoga data file (#1389849)

* Wed Jul 20 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.22-1
- libwacom 0.22

* Fri Jun 17 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.21-1
- libwacom 0.21

* Wed Jun 08 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.20-1
- libwacom 0.20

* Tue Apr 26 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.19-1
- libwacom 0.19

* Fri Apr 01 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.18-2
- Add a custom quirk for HUION Consumer Control devices (#1314955)

* Fri Apr 01 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.18-1
- libwacom 0.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.17-1
- libwacom 0.17

* Fri Nov 13 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.16-1
- libwacom 0.16

* Sun Jul 12 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-3
- fix %%{_udevrulesdir} harder

* Sat Jul 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-2
- Use %%{_udevrulesdir} so rule.d doesn't inadvertantly end up in /
- Use %%license

* Wed Jul 08 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.15-1
- libwacom 0.15

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.13-2
- Don't label touchscreens as touchpads (#1208685)

* Mon Apr 20 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.13-1
- libwacom 0.13

* Tue Mar 10 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.12-1
- libwacom 0.12

* Thu Nov 06 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.11-1
- libwacom 0.11

* Wed Aug 20 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.10-1
- libwacom 0.10

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.9-2
- Generate the rules file from the database

* Tue Mar 04 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.9-1
- libwacom 0.9

* Mon Jan 20 2014 Peter Hutterer <peter.hutterer@redhat.com> - 0.8-2
- Update rules file to current database

* Mon Oct 07 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.8-1
- libwacom 0.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.7.1-3
- Disable silent rules

* Wed May 01 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.7.1-2
- Use stdout, not stdin for printing

* Tue Apr 16 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.7.1-1
- libwacom 0.7.1

* Fri Feb 22 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.7-3
- Install into correct udev rules directory (#913723)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.7-1
- libwacom 0.7

* Fri Nov 09 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.6.1-1
- libwacom 0.6.1
- update udev.rules files for new tablet descriptions

* Fri Aug 17 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.6-5
- remove %%defattr, not necessary anymore

* Mon Jul 30 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.6-4
- ... and install the rules in %%libdir

* Mon Jul 30 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.6-3
- udev rules can go into %%libdir now

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.6-1
- libwacom 0.6

* Tue May 08 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.5-3
- Fix crash with WACf* serial devices (if not inputattach'd) (#819191)

* Thu May 03 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.5-2
- Fix gnome-control-center crash for Bamboo Pen & Touch
- Generic styli needs to have erasers, default to two tools.

* Wed May 02 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.5-1
- Update to 0.5
- Fix sources again - as long as Source0 points to sourceforge this is a bz2

* Tue Mar 27 2012 Matthias Clasen <mclasen@redhat.com> 0.4-1
- Update to 0.4

* Thu Mar 22 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.3-6
- Fix udev rules generator patch to apply ENV{ID_INPUT_TOUCHPAD} correctly
  (#803314)

* Thu Mar 08 2012 Olivier Fourdan <ofourdan@redhat.com> 0.3-5
- Mark data subpackage as noarch and make it a requirement for libwacom
- Use generated udev rule file to list only known devices from libwacom
  database

* Tue Mar 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.3-4
- libwacom-0.3-add-list-devices.patch: add API to list devices
- libwacom-0.3-add-udev-generator.patch: add a udev rules generater tool
- libwacom-0.3-add-bamboo-one.patch: add Bamboo One definition

* Tue Feb 21 2012 Olivier Fourdan <ofourdan@redhat.com> - 0.3-2
- Add udev rules to identify Wacom as tablets for libwacom

* Tue Feb 21 2012 Peter Hutterer <peter.hutterer@redhat.com>
- Source file is .bz2, not .xz

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 0.3-1
- Update to 0.3

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 0.2-1
- Update to 0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.1-1
- Initial import (#768800)
