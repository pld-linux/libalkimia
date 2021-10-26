Summary:	Common classes and functionality used by finance applications for the KDE SC
Summary(pl.UTF-8):	Wspólne klasy i funkcje wykorzystywane przez aplikacje finansowe dla KDE SC
Name:		libalkimia
Version:	8.1.0
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz
# Source0-md5:	8e7a4693995b1e0d3d0f3f19e96cd83c
URL:		https://community.kde.org/Alkimia/libalkimia
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	doxygen
BuildRequires:	gmp-c++-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libalkimia is a library with common classes and functionality used by
finance applications for the KDE SC.

%description -l pl.UTF-8
libalkimia to biblioteka ze wspólnymi klasami i funkcjami
wykorzystywanymi przez aplikacje finansowe dla KDE SC.

%package devel
Summary:	Header files for alkimia library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki alkimia
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel
Requires:	Qt5DBus-devel
Requires:	gmp-c++-devel
Requires:	kf5-extra-cmake-modules
Requires:	libstdc++-devel

%description devel
Header files for alkimia library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki alkimia.

%prep
%setup -q -n alkimia-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang --with-kde --all-name alkimia.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f alkimia.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/onlinequoteseditor5
%attr(755,root,root) %{_libdir}/libalkimia5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libalkimia5.so.8
%attr(755,root,root) %{_libdir}/qml/org/kde/alkimia/libqmlalkimia.so
%{_libdir}/qml/org/kde/alkimia/qmldir
%{_desktopdir}/org.kde.onlinequoteseditor5.desktop
%{_iconsdir}/hicolor/*x*/apps/onlinequoteseditor5.png
%{_iconsdir}/hicolor/scalable/apps/onlinequoteseditor5.svgz
%{_datadir}/knsrcfiles/alkimia-quotes.knsrc
%{_datadir}/knsrcfiles/kmymoney-quotes.knsrc
%{_datadir}/knsrcfiles/skrooge-quotes.knsrc
%{_datadir}/metainfo/org.wincak.foreigncurrencies2.appdata.xml
%{_datadir}/plasma/plasmoids/org.wincak.foreigncurrencies2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalkimia5.so
%{_includedir}/alkimia
%{_pkgconfigdir}/libalkimia5.pc
%{_libdir}/cmake/LibAlkimia5*
