Summary:	Unicode Text Segmentation Package
Name:		sombok
Version:	2011.4
Release:	1
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR Artistic-1.0-Perl)
Group:		System/Libraries
URL:		https://github.com/hatukanezumi/sombok
Source0:	https://github.com/hatukanezumi/sombok/archive/%{name}-%{version}.tar.gz
# A multilib-safe wrapper, bug #1853260
#Source1:	sombok.h

BuildRequires:	pkgconfig(libthai)
BuildRequires:	libtool

%description
Sombok library package performs Line Breaking Algorithm described in Unicode
Standards Annex #14 (UAX #14). East_Asian_Width informative properties defined
by Annex #11 (UAX #11) may be concerned to determine breaking positions. This
package also implements "default" Grapheme Cluster segmentation described in
Annex #29 (UAX #29).

%files
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.REL1 NEWS README README.ja_JP
%{_libdir}/libsombok.so.*

#---------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%{_includedir}/sombok*.h
%{_libdir}/libsombok.so
%{_libdir}/pkgconfig/sombok.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
autoreconf -fiv
%configure --disable-doc
%make_build

%install
#make_install DESTDIR=%{buildroot}
make install DESTDIR=%{buildroot}

# remove statuc stuff
find %{buildroot} -name '*.la' -delete

# Rename sombok.h to sombok-ARCH.h and install a sombok.h wrapper to avoid
# a file conflict on multilib systems, bug #1853260
#mv %{buildroot}/%{_includedir}/sombok.h %{buildroot}/%{_includedir}/sombok-%{_arch}.h
#install -m 0644 %{SOURCE1} %{buildroot}/%{_includedir}/sombok.h

