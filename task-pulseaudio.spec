Name:		task-pulseaudio
Version:	%distro_release
# Ugly, but needed for 2015.0 -> 3.0 transition
Epoch:          1
Release:	11
Summary:	Metapackage for PulseAudio
Group:		Sound
License:	GPL
Requires:	pulseaudio
Requires:	pulseaudio-utils
Requires:	pulseaudio-module-x11
#
# don't suggest those, they aren't useful for most users
# we don't want to get those installed by default
#Suggests:	paman
#Suggests:	pavumeter
#Suggests:	padevchooser
#
Recomends:	pulseaudio-module-zeroconf
#
# don't suggest xine-pulse, plugin is not in a good shape ATM
#Suggests:	xine-pulse
Recommends:	gstreamer1.0-pulse
Recomemnds:	alsa-plugins-pulseaudio

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies and recommended additions for running PulseAudio.

%files
