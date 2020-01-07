#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-htmlhelp
Version  : 1.0.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/f1/f2/88e9d6dc4a17f1e95871f8b634adefcc5d691334f7a121e9f384d1dc06fd/sphinxcontrib-htmlhelp-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/f2/88e9d6dc4a17f1e95871f8b634adefcc5d691334f7a121e9f384d1dc06fd/sphinxcontrib-htmlhelp-1.0.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/f1/f2/88e9d6dc4a17f1e95871f8b634adefcc5d691334f7a121e9f384d1dc06fd/sphinxcontrib-htmlhelp-1.0.2.tar.gz.asc
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-htmlhelp-license = %{version}-%{release}
Requires: sphinxcontrib-htmlhelp-python = %{version}-%{release}
Requires: sphinxcontrib-htmlhelp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
======================
sphinxcontrib-htmlhelp
======================
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.

%package license
Summary: license components for the sphinxcontrib-htmlhelp package.
Group: Default

%description license
license components for the sphinxcontrib-htmlhelp package.


%package python
Summary: python components for the sphinxcontrib-htmlhelp package.
Group: Default
Requires: sphinxcontrib-htmlhelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-htmlhelp package.


%package python3
Summary: python3 components for the sphinxcontrib-htmlhelp package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-htmlhelp package.


%prep
%setup -q -n sphinxcontrib-htmlhelp-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555006322
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-htmlhelp
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-htmlhelp/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-htmlhelp/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
