Name:           chrome-gnome-shell
Version:        6
Release:        1%{?dist}
Summary:        GNOME Shell integration for Chrome

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  cmake
Requires:       gnome-shell
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
%{_datadir}/chromium/extensions/gphhapmejobijbbhgpjhcjognlahblep.json
%{_datadir}/google-chrome/extensions/gphhapmejobijbbhgpjhcjognlahblep.json
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json

%changelog
* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1.R
- Update to Ver.6

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1.R
- Initial package.
