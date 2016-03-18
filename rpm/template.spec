Name:           ros-indigo-dynamic-reconfigure
Version:        1.5.42
Release:        0%{?dist}
Summary:        ROS dynamic_reconfigure package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/dynamic_reconfigure
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin >= 0.5.87
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

%description
This unary stack contains the dynamic_reconfigure package which provides a means
to change node parameters at any time without having to restart the node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 18 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.5.42-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Esteve Fernandez <esteve@osrfoundation.org> - 1.5.38-0
- Autogenerated by Bloom

