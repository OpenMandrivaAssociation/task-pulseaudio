Name:    task-pulseaudio
Version: 2008.1
Release: %mkrel 2
Summary: Metapackage for PulseAudio
Group:   Sound
License: GPL
#
Requires: pulseaudio
Requires: pulseaudio-utils
Requires: pulseaudio-module-x11
Requires: paprefs
Requires: pavucontrol
#
Suggests: paman
Suggests: pavumeter
Suggests: padevchooser
#
Suggests: pulseaudio-module-zeroconf
#
Suggests: xine-pulse
Suggests: gstreamer0.10-pulse
Suggests: libflashsupport
Suggests: alsa-plugins-pulseaudio

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies and recommended additions for running PulseAudio.

%files
