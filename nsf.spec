%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          nsf
Summary:       Next Scripting Framework (NSF): Object orientation for Tcl
Version:       2.1.0
Release:       0
License:       MIT
Group:         Development/Libraries/Tcl
Source:        %{name}%{version}.tar.gz
Patch0:        makefile.patch
URL:           https://next-scripting.org/xowiki/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
The Next Scripting Framework (for short: NSF) is an infrastructure
for creating object-oriented scripting languages based on Tcl.
This package provides two ready-made object-orientated extensions
for Tcl based on NSF: Next Scripting Language (NX, pronounced "next")
and Extended Object Tcl version 2 (XOTcl2, pronounced "exotickle").

%package devel
Summary:        Development package for NSF
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
This package contains development files for NSF.

%prep
%setup -q -n %{name}%{version}
%patch0

%build
%{__autoconf}
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make

%install
make DESTDIR=%{buildroot} pkglibdir=%tcl_noarchdir/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/bin/nxsh
/usr/bin/nxwish
/usr/bin/xotclsh
/usr/bin/xowish
/usr/lib64/libnsf2.1.0.so
%tcl_noarchdir/%{name}%{version}
/usr/share/man/man1
/usr/share/man/man3

%files devel
%defattr(-,root,root)
/usr/lib64/nsfConfig.sh
/usr/lib64/libnsfstub2.1.0.a
/usr/include/nsf.h
/usr/include/nsfDecls.h
/usr/include/nsfInt.h
/usr/include/nsfIntDecls.h

%changelog

