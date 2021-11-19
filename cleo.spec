#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cleo
Version  : 0.8.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/a5/36/943c12bc9b56f5fc83661558c576a3d95df0d0f9c153f87ee4c19647025b/cleo-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/36/943c12bc9b56f5fc83661558c576a3d95df0d0f9c153f87ee4c19647025b/cleo-0.8.1.tar.gz
Summary  : Cleo allows you to create beautiful and testable command-line interfaces.
Group    : Development/Tools
License  : MIT
Requires: cleo-python = %{version}-%{release}
Requires: cleo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
Cleo
####
.. image:: https://travis-ci.org/sdispater/cleo.png
:alt: Cleo Build status
:target: https://travis-ci.org/sdispater/cleo

%package python
Summary: python components for the cleo package.
Group: Default
Requires: cleo-python3 = %{version}-%{release}

%description python
python components for the cleo package.


%package python3
Summary: python3 components for the cleo package.
Group: Default
Requires: python3-core
Provides: pypi(cleo)
Requires: pypi(clikit)

%description python3
python3 components for the cleo package.


%prep
%setup -q -n cleo-0.8.1
cd %{_builddir}/cleo-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637362946
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
