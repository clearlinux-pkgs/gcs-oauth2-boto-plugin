#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gcs-oauth2-boto-plugin
Version  : 3.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/05/e5/3162be0abab32f152f331423426471935f286dd4ad70fa704f2a34ea3c1e/gcs-oauth2-boto-plugin-3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/e5/3162be0abab32f152f331423426471935f286dd4ad70fa704f2a34ea3c1e/gcs-oauth2-boto-plugin-3.0.tar.gz
Summary  : Auth plugin allowing use the use of OAuth 2.0 credentials for Google Cloud Storage in the Boto library.
Group    : Development/Tools
License  : Apache-2.0
Requires: gcs-oauth2-boto-plugin-license = %{version}-%{release}
Requires: gcs-oauth2-boto-plugin-python = %{version}-%{release}
Requires: gcs-oauth2-boto-plugin-python3 = %{version}-%{release}
Requires: PySocks
BuildRequires : PySocks
BuildRequires : buildreq-distutils3
BuildRequires : pypi(boto)
BuildRequires : pypi(google_reauth)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(oauth2client)
BuildRequires : pypi(pyopenssl)
BuildRequires : pypi(retry_decorator)
BuildRequires : pypi(rsa)
BuildRequires : pypi(six)
BuildRequires : retry
BuildRequires : retry_decorator

%description
gcs-oauth2-boto-plugin is a Python application whose purpose is to behave as an
        auth plugin for the boto auth plugin framework for use with OAuth 2.0
        credentials for the Google Cloud Platform. This plugin is compatible with both
        user accounts and service accounts, and its functionality is essentially a
        wrapper around oauth2client with the addition of automatically caching tokens
        for the machine in a thread- and process-safe fashion.

%package license
Summary: license components for the gcs-oauth2-boto-plugin package.
Group: Default

%description license
license components for the gcs-oauth2-boto-plugin package.


%package python
Summary: python components for the gcs-oauth2-boto-plugin package.
Group: Default
Requires: gcs-oauth2-boto-plugin-python3 = %{version}-%{release}

%description python
python components for the gcs-oauth2-boto-plugin package.


%package python3
Summary: python3 components for the gcs-oauth2-boto-plugin package.
Group: Default
Requires: python3-core
Provides: pypi(gcs_oauth2_boto_plugin)
Requires: pypi(boto)
Requires: pypi(google_reauth)
Requires: pypi(httplib2)
Requires: pypi(oauth2client)
Requires: pypi(pyopenssl)
Requires: pypi(retry_decorator)
Requires: pypi(rsa)
Requires: pypi(six)

%description python3
python3 components for the gcs-oauth2-boto-plugin package.


%prep
%setup -q -n gcs-oauth2-boto-plugin-3.0
cd %{_builddir}/gcs-oauth2-boto-plugin-3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637779070
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . rsa
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gcs-oauth2-boto-plugin
cp %{_builddir}/gcs-oauth2-boto-plugin-3.0/LICENSE %{buildroot}/usr/share/package-licenses/gcs-oauth2-boto-plugin/5a7d7df655ba40478fae80a6abafc6afc36f9b6a
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} rsa
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gcs-oauth2-boto-plugin/5a7d7df655ba40478fae80a6abafc6afc36f9b6a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
