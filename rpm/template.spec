# template of .spec
# full description http://www.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html
# GPL
# 2016, Maxim I, newmocart@gmail.com
# version 0.1
#

################
# The Preamble #
################

Summary: 
Name: 
Version: 
Release: 
Copyright: 
Group: 
# Source - link to .tar.gz source code
Source: 
# URL - usually link to documentation
URL: 
Distribution: 
Vendor: 
Packager: 

#
# Text description of package. You can see it by run 'rpm -qi' 
#
%description


##########################
# I. build-time scripts. #
##########################

#
# It Prepares for the build. Usually
# 1) Delete all files from the previous build
# 2) untar sources from SOURCES into BUILD folders 
#
%prep

#
# build the package. It is similar to 'make' command
#
%build

#
# install. like 'make install'. put files in destination folder
#
%install

#
# it contains a list of the files that are part of the package. 
# Always remember — if it isn't in the file list, it won't be put in the package!
#
# can be derictives: %doc %condif %dir %attr %doc...
# Directives For the %files list -  http://www.rpm.org/max-rpm/s1-rpm-inside-files-list-directives.htm
#
%files

# Clean up the software's build directory tree
# rm -rf $RPM_BUILD_ROOT
#
%clean


##############################
# Install/Erase-time Scripts #
##############################

