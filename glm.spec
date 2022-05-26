# The library consists of headers only
%global debug_package %{nil}


Name:           glm
Version:        0.9.9.8
Release:        1%{?dist}
Summary:        C++ mathematics library for graphics programming

License:        MIT
URL:            http://glm.g-truc.net/
Source0:        https://github.com/g-truc/glm/releases/download/%{version}/%{name}-%{version}.zip

Source1:	glm.pc.in
Source2:	glmConfigVersion.cmake.in
Source3:	glmConfig.cmake.in
Source4:	glmTargets.cmake


%description
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%package        devel
Summary:        C++ mathematics library for graphics programming
BuildArch:      noarch

# As required in
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Static_Libraries_2
Provides:       %{name}-static = %{version}-%{release}

%description    devel
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%{name}-devel is only required for building software that uses
the GLM library. Because GLM currently is a header-only library,
there is no matching run time package.

%package        doc
Summary:        Documentation for %{name}-devel
BuildArch:      noarch

%description    doc
The %{name}-doc package contains reference documentation and
a programming manual for the %{name}-devel package.

%prep
%autosetup -n glm
    sed -i 's|/usr/lib/cmake|/usr/share/cmake|g' %{S:4}
    
%build



%install
   mkdir -p %{buildroot}/usr/include/
    cp -r glm %{buildroot}/usr/include/

    # For some stupid reason, glm upstream removed the CMake install target here:
    # https://github.com/g-truc/glm/commit/5f352ecce21bb1ab37fa56fac0f383c779b351a3
    # There is no reasoning for it. Discussion here: https://github.com/g-truc/glm/issues/947
    mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
    sed "s/@VERSION@/%{version}/" %{S:1} > %{buildroot}/%{_libdir}/pkgconfig/glm.pc

    mkdir -p %{buildroot}/%{_datadir}/cmake/glm/
    sed "s/@VERSION@/%{version}/" %{S:2} > %{buildroot}/%{_datadir}/cmake/glm/glmConfigVersion.cmake
    sed "s/@VERSION@/%{version}/" %{S:3} > %{buildroot}/%{_datadir}/cmake/glm/glmConfig.cmake
    install -Dm644 %{S:4} %{buildroot}/%{_datadir}/cmake/glm/glmTargets.cmake
    
    
    
%files devel
%doc readme.md
%{_includedir}/%{name}
%{_datadir}/cmake
%{_libdir}/pkgconfig/

%files doc
%doc doc


%changelog
* Wed May 25 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.9.9.8-1 
- Updated to 0.9.9.8

* Sat May 02 2020 Joonas Sarajärvi <muep@iki.fi> - 0.9.9.6-3
- Remove arch check from glmConfigVersion.cmake, fix #1758009
