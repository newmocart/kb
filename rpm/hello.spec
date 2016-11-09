# disable degug packages creating
%define debug_package %{nil}

Summary: Hello Maks 
Name:  hello
Version: 0.0.0.1 
Release: rl6
License: GPL
Group: Application/Text
Source: %{name}-%{version}.tar.gz
Distribution: RedHat 
Vendor: Angry cats inc.
Packager: yourmail


%description
Print "Hello Maks" and exit. No more effect.

%prep
echo "Untar something, relax...."
%setup -q

%build 
echo "make hello"
make hello

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} $RPM_BUILD_ROOT/tmp 
cp hello $RPM_BUILD_ROOT/tmp


%files
/tmp/hello 

%clean
echo 'rm -rf $RPM_BUILD_ROOT'
rm -rf $RPM_BUILD_ROOT
