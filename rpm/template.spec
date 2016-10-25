Name:           ros-jade-dynamic-reconfigure
Version:        1.5.45
Release:        0%{?dist}
Summary:        ROS dynamic_reconfigure package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/dynamic_reconfigure
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-rospy
Requires:       ros-jade-rosservice
Requires:       ros-jade-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-jade-catkin >= 0.5.87
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roscpp-serialization
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-std-msgs

%description
This unary stack contains the dynamic_reconfigure package which provides a means
to change node parameters at any time without having to restart the node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.45-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.44-0
- Autogenerated by Bloom

* Sat Mar 19 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.43-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.42-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.39-2
- Autogenerated by Bloom

* Wed Apr 22 2015 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.39-1
- Autogenerated by Bloom

* Wed Apr 22 2015 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.39-0
- Autogenerated by Bloom

* Wed Dec 31 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.38-1
- Autogenerated by Bloom

* Wed Dec 31 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.38-0
- Autogenerated by Bloom

