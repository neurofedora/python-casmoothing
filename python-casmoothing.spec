%global modname casmoothing
%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$
%global with_python3 0

Name:           python-%{modname}
Version:        0.2
Release:        1%{?dist}
Summary:        Context-aware mesh smoothing for biomedical applications

License:        GPLv2+
URL:            https://github.com/tfmoraes/python-casmoothing
Source0:        https://github.com/tfmoraes/python-casmoothing/archive/v%{version}/%{modname}-%{version}.tar.gz
Patch0:         0001-support-both-py2-py3.patch
Patch1:         0002-install-to-platform-specific-dir.patch

BuildRequires:  git-core
BuildRequires:  cmake gcc-c++
BuildRequires:  vtk-devel
BuildRequires:  swig

%description
This is a implementation of the paper "Context-aware mesh smoothing for
biomedical applications". It can be used to smooth meshes generated by binary
images to remove its staircase artifacts and keep the fine features.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
Requires:       vtk-python

%description -n python2-%{modname}
This is a implementation of the paper "Context-aware mesh smoothing for
biomedical applications". It can be used to smooth meshes generated by binary
images to remove its staircase artifacts and keep the fine features.

Python 2 version

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
Requires:       vtk-python3

%description -n python3-%{modname}
This is a implementation of the paper "Context-aware mesh smoothing for
biomedical applications". It can be used to smooth meshes generated by binary
images to remove its staircase artifacts and keep the fine features.

Python 3 version
%endif

%prep
%autosetup -S git
chmod -x LICENSE.txt AUTHORS.txt

rm -rf python{2,3}/
mkdir python{2,3}/

%build
pushd python2
  %cmake ../ -DPythonLibs_FIND_VERSION=2
  %make_build
popd

%if 0%{?with_python3}
pushd python3
  %cmake ../ -DPythonLibs_FIND_VERSION=3
  %make_build
popd
%endif

%install
pushd python2
  %make_install
popd

%if 0%{?with_python3}
pushd python3
  %make_install
popd
%endif

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.md AUTHORS.txt
%{python2_sitearch}/_ca_smoothing.so
%{python2_sitearch}/ca_smoothing.py*

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE.txt
%doc README.md AUTHORS.txt
%{python3_sitearch}/_ca_smoothing.so
%{python3_sitearch}/ca_smoothing.py
%{python3_sitearch}/__pycache__/ca_smoothing.*
%endif

%changelog
* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1
- Initial package
