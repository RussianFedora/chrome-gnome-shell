Name:           chrome-gnome-shell
Version:        6.1
Release:        2%{?dist}
Summary:        GNOME Shell integration for Chrome

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  cmake
Requires:       gnome-shell
Requires:       python-gobject-base
Requires:       python2

%description
Web extension for Google Chrome browser and native connector that provides
integration with GNOME Shell and the corresponding extensions repository
https://extensions.gnome.org.
                                                                         
%prep
%autosetup

%build
mkdir build
pushd build
  %cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%{_bindir}/gs-chrome-connector
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%{_datadir}/chromium/extensions/gphhapmejobijbbhgpjhcjognlahblep.json
%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%{_datadir}/google-chrome/extensions/gphhapmejobijbbhgpjhcjognlahblep.json
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json

%changelog
* Sun Jul 31 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-2.R
- Add missing Requires: python-gobject-base

* Tue Jun 07 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-1.R
- Update to Ver.6.1

* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1.R
- Update to Ver.6
- Fix "orphaned directory"

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1.R
- Initial package.
