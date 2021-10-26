Summary:	Common classes and functionality used by finance applications for the KDE SC
Summary(pl.UTF-8):	Wspólne klasy i funkcje wykorzystywane przez aplikacje finansowe dla KDE SC
Name:		libalkimia
Version:	7.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.kde.org/stable/alkimia/%{version}/src/alkimia-%{version}.tar.xz
# Source0-md5:	a495c100910f4602cc3e77c0e1c61bc3
URL:		http://community.kde.org/Alkimia/libalkimia
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	doxygen
BuildRequires:	gmp-c++-devel
BuildRequires:	kf5-extra-cmake-modules
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libalkimia5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libalkimia5.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalkimia5.so
%{_includedir}/alkimia
%{_pkgconfigdir}/libalkimia5.pc
%{_libdir}/cmake/LibAlkimia5*
