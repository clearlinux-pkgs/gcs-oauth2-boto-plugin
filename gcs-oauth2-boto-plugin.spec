#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gcs-oauth2-boto-plugin
Version  : 2.5
Release  : 32
URL      : https://files.pythonhosted.org/packages/11/d0/45b69da0d40365fa8ecdf4f93d7847dc2079845c821edcf183675db0e77a/gcs-oauth2-boto-plugin-2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/d0/45b69da0d40365fa8ecdf4f93d7847dc2079845c821edcf183675db0e77a/gcs-oauth2-boto-plugin-2.5.tar.gz
Summary  : Auth plugin allowing use the use of OAuth 2.0 credentials for Google Cloud Storage in the Boto library.
Group    : Development/Tools
License  : Apache-2.0
Requires: gcs-oauth2-boto-plugin-python = %{version}-%{release}
Requires: gcs-oauth2-boto-plugin-python3 = %{version}-%{release}
Requires: PySocks
Requires: boto
Requires: google-reauth
Requires: httplib2
Requires: oauth2client
Requires: pyOpenSSL
Requires: retry_decorator
Requires: six
BuildRequires : PySocks
BuildRequires : boto
BuildRequires : buildreq-distutils3
BuildRequires : google-reauth
BuildRequires : httplib2
BuildRequires : oauth2client
BuildRequires : pyOpenSSL
BuildRequires : retry
BuildRequires : retry_decorator
BuildRequires : six
Patch1: 0001-Switch-to-PySocks.patch

%description
# gcs-oauth2-boto-plugin
gcs-oauth2-boto-plugin is a Python application whose purpose is to behave as
an auth plugin for the [boto] auth plugin framework for use with [OAuth 2.0]
credentials for the Google Cloud Platform. This plugin is compatible with
both [user accounts] and [service accounts], and its functionality is
essentially a wrapper around [oauth2client]
with the addition of automatically caching tokens
for the machine in a thread- and process-safe fashion.

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
Provides: pypi(gcs-oauth2-boto-plugin)

%description python3
python3 components for the gcs-oauth2-boto-plugin package.


%prep
%setup -q -n gcs-oauth2-boto-plugin-2.5
cd %{_builddir}/gcs-oauth2-boto-plugin-2.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582929053
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
