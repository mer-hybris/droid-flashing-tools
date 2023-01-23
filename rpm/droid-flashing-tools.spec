%define __find_provides %{nil}
%define __find_requires %{nil}
%define __strip /bin/true
%define __requires_exclude ^.*$
%global debug_package %{nil}

Name:    droid-flashing-tools
Version: 29.0.5
Release: 1
Summary: Some flashing tools
Group:   System
License: BSD-2-Clause AND Apache-2.0
Source:	 %{name}-%{version}.tar.bz2

%description
%{summary}

%prep
%setup -q

%build

%install
install -Dm644 AdbWinApi.dll AdbWinUsbApi.dll fastboot.exe \
        --target-directory %{buildroot}%{_datadir}/%{name}/

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/*
%license LICENSE.APACHE
%license LICENSE.BSD2
