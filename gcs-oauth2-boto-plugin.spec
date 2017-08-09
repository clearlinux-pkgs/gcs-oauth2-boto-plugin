#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gcs-oauth2-boto-plugin
Version  : 1.14
Release  : 1
URL      : http://pypi.debian.net/gcs-oauth2-boto-plugin/gcs-oauth2-boto-plugin-1.14.tar.gz
Source0  : http://pypi.debian.net/gcs-oauth2-boto-plugin/gcs-oauth2-boto-plugin-1.14.tar.gz
Summary  : Auth plugin allowing use the use of OAuth 2.0 credentials for Google Cloud Storage in the Boto library.
Group    : Development/Tools
License  : Apache-2.0
Requires: gcs-oauth2-boto-plugin-python
Requires: boto
Requires: httplib2
Requires: oauth2client
Requires: pyOpenSSL
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
gcs-oauth2-boto-plugin is a Python application whose purpose is to behave as an
        auth plugin for the boto auth plugin framework for use with OAuth 2.0
        credentials for the Google Cloud Platform. This plugin is compatible with both
        user accounts and service accounts, and its functionality is essentially a
        wrapper around oauth2client with the addition of automatically caching tokens
        for the machine in a thread- and process-safe fashion.

%package python
Summary: python components for the gcs-oauth2-boto-plugin package.
Group: Default

%description python
python components for the gcs-oauth2-boto-plugin package.


%prep
%setup -q -n gcs-oauth2-boto-plugin-1.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502288463
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1502288463
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
