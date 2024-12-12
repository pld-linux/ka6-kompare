#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kompare
Summary:	kompare
Name:		ka6-%{kaname}
Version:	24.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	206b68627a4ddef7c27d219c33e7ca05
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkomparediff2-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-ktexteditor-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kompare is a GUI front-end program that enables differences between
source files to be viewed and merged. It can be used to compare
differences on files or the contents of folders, and it supports a
variety of diff formats and provide many options to customize the
information level displayed.

%description -l pl.UTF-8
Kompare jest programem GUI, który pokazuje różnice między plikami kodu
źródłowego, które mogą być złączone. Może być użyty do porównania
plików, lub zawartości folderów. Wspiera różne formaty diffa i
dostarcza wielu opcji do zmieniania zakresu wyświetlanej informacji.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%dir %{_includedir}/kompare
%{_includedir}/kompare/kompareinterface.h
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so.?
%{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkompareinterface.so.?
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/komparenavtreepart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/komparepart.so
%{_desktopdir}/org.kde.kompare.desktop
%{_iconsdir}/hicolor/*x*/apps/kompare.png
%{_iconsdir}/hicolor/scalable/apps/kompare.svgz
%{_datadir}/metainfo/org.kde.kompare.appdata.xml
%{_datadir}/qlogging-categories6/kompare.categories
%{_datadir}/kio/servicemenus/kompare.desktop
