%global qt_module qtcanvas3d

%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define _qt5_prefix %{_libdir}/qt%{api}

Summary:	Qt5 - Canvas3d component
Version:	5.12.1
Name:		qt5-qtcanvas3d
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtcanvas3d-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%(echo %{beta} |sed -e "s,1$,,")/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtcanvas3d-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Source1:	qt5-qtcanvas3d.rpmlintrc

License:	LGPLv2 with exceptions or GPLv3 with exceptions
Url:		http://www.qt.io
Group:		Development/KDE and Qt

BuildRequires:	qmake5 = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	qt5-qtqml-private-devel
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt5 Canvas3D component.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}  = %{version}-%{release}
%description examples
%{summary}.

%prep
%autosetup -n %qttarballdir -p1

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_qt5_prefix}/qml/QtCanvas3D/

%files examples
%doc LICENSE.*
%{_qt5_prefix}/examples/canvas3d/
