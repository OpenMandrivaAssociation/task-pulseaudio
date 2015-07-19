Name:		task-pulseaudio
Version:	%distro_release
Release:	5
Summary:	Metapackage for PulseAudio
Group:		Sound
License:	GPL
Requires:	pulseaudio
Requires:	pulseaudio-utils
Requires:	pulseaudio-module-x11
Requires:	paprefs
Requires:	pavucontrol
#
# don't suggest those, they aren't useful for most users
# we don't want to get those installed by default
#Suggests:	paman
#Suggests:	pavumeter
#Suggests:	padevchooser
#
Suggests:	pulseaudio-module-zeroconf
#
# don't suggest xine-pulse, plugin is not in a good shape ATM
#Suggests:	xine-pulse
Suggests:	gstreamer0.10-pulse
Suggests:	gstreamer1.0-pulse
Suggests:	alsa-plugins-pulseaudio

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies and recommended additions for running PulseAudio.

%files
