Summary: Hello World Demo
Name: hello-world-%{variant}-%{style}
Version: 1.0
Release: 1
BuildRoot: %{_topdir}/BUILD
Prefix: /opt/hello-world
URL: http://www.cg-soft.com
License: GPL
Group: Applications/Demo
Vendor: CG Software Design

%description
This RPM demonstrates the incremental build and packing system

%install
# skip if we already did this before

#include "manifest.spec-inc"

mkdir -p\
  "${RPM_BUILD_ROOT}%{prefix}/%{version}/bin"\
;

cp\
  "%{cook_top}/src/hello_world_1/DO/%{platform}/%{variant}/simplex/hello_world_1"\
  "%{cook_top}/src/hello_world_2/DO/%{platform}/%{variant}/complex/hello_world_2"\
  "%{cook_top}/src/hello_world_3/bin/DO/%{platform}/%{variant}/simplex/hello_world_3"\
  "%{cook_top}/src/hello_world_4/bin/DO/%{platform}/%{variant}/simplex/hello_world_4"\
  "${RPM_BUILD_ROOT}%{prefix}/%{version}/bin"

manifest\
  hello-world\
  %{version}\
  "${RPM_BUILD_ROOT}%{prefix}"

%files -f %{buildroot}%{prefix}/%{version}/rpm/hello-world/MANIFEST
