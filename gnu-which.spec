%global _name which
Summary: Displays where a particular program in your path is located
Name: gnu-which
Version: 2.21
Release: 1
License: GPLv3
Source0: http://ftp.gnu.org/gnu/which/%{_name}-%{version}.tar.gz
Source1: which2.sh
Source2: which2.csh
Patch0: which-2.21-coverity-fixes.patch
Url: https://savannah.gnu.org/projects/which/
Requires: coreutils
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig(readline)
BuildRequires: autoconf

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%license COPYING
%doc EXAMPLES README AUTHORS NEWS
%attr(0644,root,root) %{_sysconfdir}/profile.d/which2.*
%{_bindir}/which
%{_infodir}/which.info*
%{_mandir}/man1/which.1*
