%define debug_package %{nil}

Name:           chrome-gnome-shell
Version:        8.2.1
Release:        2%{?dist}
Summary:        GNOME Shell integration for Chrome

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://github.com/nE0sIghT/%{name}-mirror/archive/v8.2.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  python2-devel
BuildRequires:  jq

Requires:       gnome-shell
Requires:       python-gobject-base
Requires:       python2-requests

Provides:       %{name}-mirror = %{version}-%{release}

%description
Web extension for Google Chrome/Chromium, Vivaldi, Opera and native host
messaging connector that provides integration with GNOME Shell and the
corresponding extensions repository https://extensions.gnome.org.
                                                                         
%prep
%autosetup -n %{name}-mirror-%{version}

%build
mkdir build
pushd build
  %cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DBUILD_EXTENSION=OFF
  %make_build
popd

%install
pushd build
  %make_install
popd

%files
%doc README.md
%license LICENSE
%{_bindir}/chrome-gnome-shell
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/chromium/policies/managed/chrome-gnome-shell.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/managed
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/opt/chrome/policies/managed/chrome-gnome-shell.json
%{_libdir}/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/icons/gnome/*/apps/org.gnome.ChromeGnomeShell.png
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{python2_sitelib}/chrome_gnome_shell-*.egg-info

%changelog
* Thu Apr 13 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 8.2.1-2
- added R: python2-requests

* Wed Apr 12 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 8.2.1-1
- update to Ver.8.2.1

* Mon Sep 26 2016 Maxim Orlov <murmansksity@gmail.com> - 7.1-1.R
- Update to Ver.7.1

* Thu Sep 08 2016 Maxim Orlov <murmansksity@gmail.com> - 7-1.R
- Update to Ver.7

* Sat Aug 06 2016 Maxim Orlov <murmansksity@gmail.com> - 6.2-1.R
- Update to Ver.6.2

* Sun Jul 31 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-2.R
- Add missing Requires: python-gobject-base

* Tue Jun 07 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-1.R
- Update to Ver.6.1

* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1.R
- Update to Ver.6
- Fix "orphaned directory"

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1.R
- Initial package.
