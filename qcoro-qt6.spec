#
# Conditional build:
%bcond_with	tests		# build with tests
%define		qtver		6.6.1
%define		kfname	qcoro
Summary:	QCoro - Coroutines for Qt5 and Qt6
Name:		qcoro-qt6
Version:	0.10.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://github.com/danvratil/qcoro/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	2af4e86cd77493cd41ba5ffcac33d5f4
URL:		https://qt-widgets.github.io/qcoro-Coroutines-for-Qt/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 5.15.9
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6WebSockets-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20.0
BuildRequires:	ninja
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The QCoro library provides set of tools to make use of C++20
coroutines with Qt.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	-DUSE_QT_VERSION=6 \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libQCoro6Core.so.0
%attr(755,root,root) %{_libdir}/libQCoro6Core.so.*.*.*
%ghost %{_libdir}/libQCoro6DBus.so.0
%attr(755,root,root) %{_libdir}/libQCoro6DBus.so.*.*.*
%ghost %{_libdir}/libQCoro6Network.so.0
%attr(755,root,root) %{_libdir}/libQCoro6Network.so.*.*.*
%ghost %{_libdir}/libQCoro6Qml.so.0
%attr(755,root,root) %{_libdir}/libQCoro6Qml.so.*.*.*
%ghost %{_libdir}/libQCoro6Quick.so.0
%attr(755,root,root) %{_libdir}/libQCoro6Quick.so.*.*.*
%ghost %{_libdir}/libQCoro6WebSockets.so.0
%attr(755,root,root) %{_libdir}/libQCoro6WebSockets.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/qcoro6
%{_libdir}/cmake/QCoro6
%{_libdir}/cmake/QCoro6Core
%{_libdir}/cmake/QCoro6Coro
%{_libdir}/cmake/QCoro6DBus
%{_libdir}/cmake/QCoro6Network
%{_libdir}/cmake/QCoro6Qml
%{_libdir}/cmake/QCoro6Quick
%{_libdir}/cmake/QCoro6Test
%{_libdir}/cmake/QCoro6WebSockets
%{_libdir}/libQCoro6Core.so
%{_libdir}/libQCoro6DBus.so
%{_libdir}/libQCoro6Network.so
%{_libdir}/libQCoro6Qml.so
%{_libdir}/libQCoro6Quick.so
%{_libdir}/libQCoro6WebSockets.so
%{_libdir}/qt6/mkspecs/modules/qt_QCoroCore.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroCoro.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroDBus.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroNetwork.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroQml.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroQuick.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroTest.pri
%{_libdir}/qt6/mkspecs/modules/qt_QCoroWebSockets.pri
