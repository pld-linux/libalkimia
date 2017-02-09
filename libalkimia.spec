Summary:	Common classes and functionality used by finance applications for the KDE SC
Summary(pl.UTF-8):	Wspólne klasy i funkcje wykorzystywane przez aplikacje finansowe dla KDE SC
Name:		libalkimia
Version:	4.3.1
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	73d7f1365118019030b2045d95c92456
Patch0:		link.patch
URL:		http://community.kde.org/Alkimia/libalkimia
BuildRequires:	QtCore-devel >= 4
BuildRequires:	cmake >= 2.6.4
BuildRequires:	doxygen
BuildRequires:	gmp-c++-devel
BuildRequires:	kde4-kdelibs-devel >= 4
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
Requires:	QtCore-devel >= 4
Requires:	gmp-c++-devel
Requires:	kde4-kdelibs-devel >= 4
Requires:	libstdc++-devel

%description devel
Header files for alkimia library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki alkimia.

%prep
%setup -q
%patch0 -p1

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
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libalkimia.so.4.3.1
%attr(755,root,root) %ghost %{_libdir}/libalkimia.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalkimia.so
%{_includedir}/alkimia
%{_pkgconfigdir}/libalkimia.pc
%{_datadir}/apps/cmake/modules/FindLibAlkimia.cmake
