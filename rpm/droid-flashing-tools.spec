Name:    droid-flashing-tools
Version: 0.0.1
Release: 1
Summary: Some flashing tools

Group:   System
License: BSD
Source:	 %{name}-%{version}.tar.bz2

%description
%{summary}

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp AdbWinApi.dll AdbWinUsbApi.dll fastboot.exe %{buildroot}%{_datadir}/%{name}/

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/*
