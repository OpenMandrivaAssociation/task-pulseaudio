Name:    task-pulseaudio
Version: 2008.1
Release: %mkrel 1
Summary: Metapackage for Pulse Audio
Group:   Sound
License: GPL
#
Requires: pulseaudio
Requires: pulseaudio-utils
Requires: pulseaudio-module-x11
Requires: paman
Requires: paprefs
Requires: pavucontrol
Requires: pavumeter
Requires: padevchooser
#
Suggests: pulseaudio-module-zeroconf
#
Suggests: xine-pulse
Suggests: gstreamer0.10-pulse
Suggests: libflashsupport

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies and recommended additions for running pulse audio.

%files
