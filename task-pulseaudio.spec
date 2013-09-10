Name:		task-pulseaudio
Version:	2011.0
Release:	4
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


%changelog
* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1mdv2011.0
+ Revision: 655952
- bump to 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-5mdv2011.0
+ Revision: 607980
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-4mdv2010.1
+ Revision: 524168
- rebuilt for 2010.1

* Thu Oct 01 2009 Colin Guthrie <cguthrie@mandriva.org> 2010.0-3mdv2010.0
+ Revision: 452396
- Don't obsolete libflashsupport here as it will install task-pulseaudio when not strictly needed.

* Tue Sep 29 2009 Colin Guthrie <cguthrie@mandriva.org> 2010.0-2mdv2010.0
+ Revision: 450807
- Obsolete libfashsupport

* Wed Sep 16 2009 Colin Guthrie <cguthrie@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 443690
- Do not suggest libflashsupport anymore - it's not needed with flash 10

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-3mdv2010.0
+ Revision: 423764
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-2mdv2009.1
+ Revision: 351485
- rebuild

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 282558
- bump version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-5mdv2009.0
+ Revision: 225638
- rebuild

* Tue Mar 04 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-4mdv2008.1
+ Revision: 178289
- Don't suggest xine pulseaudio plugin, it isn't very stable ATM

* Tue Jan 08 2008 Frederic Crozat <fcrozat@mandriva.com> 2008.1-3mdv2008.1
+ Revision: 146749
- Remove suggests on paman, pavumeter and padevchooser, they aren't useful for most users, we shouldn't install them by default

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2008.1-2mdv2008.1
+ Revision: 116296
- Add suggest on alsa PulseAudio plugin

* Wed Dec 05 2007 Frederic Crozat <fcrozat@mandriva.com> 2008.1-1mdv2008.1
+ Revision: 115612
- Replace some requires by suggests
- Fix PA naming in description

  + Colin Guthrie <cguthrie@mandriva.org>
    - import task-pulseaudio


