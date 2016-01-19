## <a href="http://tinypic.com?ref=2iuw5ck" target="_blank"><img src="http://i66.tinypic.com/2iuw5ck.png" border="0" alt="Image and video hosting by TinyPic"></a> Andy Repository Public
------------

*Ivue appears to be back.  Use theirs.  I was scared of the traffic my guide may have produced.  I'm considering adding it back.

**There is currently a guide but it has a dummy xml for EPG data. I will never, ever, ever ask for money or donations.  I'm just deterring that portion of my repo atm.

***This repo is a constant WIP by a simple hobbyist that knows python.  Modded\original work is tagged "Andy.".  Mostly acts as my backup and as a P.O.C. i rock.



Repo Main Page (This page) https://github.com/halikus/_AndyRepo

Repo Zip https://raw.githubusercontent.com/halikus/_AndyRepo/master/_repo/Andy.repository.Andy/Andy.repository.Andy-0.0.1.zip

Maintenance Program https://raw.githubusercontent.com/halikus/_AndyRepo/master/_repo/Andy.plugin.program.Maintenance/Andy.plugin.program.Maintenance-0.0.1.zip


Install Kodi http://kodi.tv/download/

*Windows
16 Beta 5 is what i use.
 
15.2 suggested for maximum compatability.
15.2 no DX11 - http://mirrors.kodi.tv/releases/win32/kodi-15.2-Isengard.exe


*Android - 15.2 suggested for maximum compatability.  Needs Jailbreak and 4.12 rom

15.2 ARM  http://mirrors.kodi.tv/releases/android/arm/kodi-15.2-Isengard-armeabi-v7a.apk


**Android - 14.2 suggested for 4.11 rom and less or no Jailbreak

ARM cpu (Most):  http://mirrors.kodi.tv/releases/android/arm/old/kodi-14.2-Helix-armeabi-v7a.apk

x86 cpu:  http://mirrors.kodi.tv/releases/android/x86/old/kodi-14.2-Helix-x86.apk


***Android - AceStreams and Sopcast can optionally be downloaded via Playstore



## Repo Installation
------------

Simply download the Repo ZIP file to your device and install through the menu via:

System -> Settings -> Add-ons -> Install from zip file. 


Once the repository ZIP file is installed, you can install the individual add-ons through my repository:

System -> Settings -> Add-ons -> Install From Repository -> Select "Andy Repository" -> Program Add-Ons --> "Andy Maintenance Tool" --> Install


<a href="http://tinypic.com?ref=16c53cm" target="_blank"><img src="http://i63.tinypic.com/16c53cm.png" border="0" alt="Image and video hosting by TinyPic"></a>



You can install Repositories (source of addons), Addons (the extra applications), preconfigured addon settings (Addon_data), and xmls.  The xml files are the sources of your media files.




## Comman Kodi Paths :

Addons (Core app, no settings):  \addons

Master Profile Settings:         \userdata

Master Profile Addon Settings :  \userdata\addon_data

Master Profile Media Database :  \userdata\Database

Master Profile Media\Addon Art : \userdata\Thumbnails

Master Profile Special Tweaks:   \userdata\Advancedsettings.xml

Master Profile Media Paths:      \userdata\sources.xml

Master Profile RSS Feeds:        \userdata\RssFeeds.xml

*Multiple Profiles:              \userdata\profiles.xml

*Multiple Profiles Profile:      \userdata\profiles\ProfileName



## Userdata Locations per device :


Android  /Android/data/org.xbmc.kodi/files/.kodi/userdata/

Windows  %APPDATA%\kodi\userdata  (C:\Users\UserName\AppData\Roaming\Kodi\userdata)

iOS      /private/var/mobile/Library/Preferences/Kodi/userdata/

Linux    ~/.kodi/userdata/

Mac      /Users/<your_user_name>/Library/Application Support/Kodi/userdata/

OpenELEC /storage/.kodi/userdata/

*A full restore will overwrite certain settings*




## Portable Kodi CMD

(Make a cmd file in Kodi directory located anywhere)



@echo off

TASKKILL /im pulsar.exe /f

tskill pulsar.exe

TASKKILL /im Kodi.exe /f

tskill Kodi.exe

TASKKILL /im XBMC.exe /f

tskill XBMC.exe

start Kodi.exe -p



<a href="http://tinypic.com?ref=2u4igxw" target="_blank"><img src="http://i64.tinypic.com/2u4igxw.jpg" border="0" alt="Image and video hosting by TinyPic"></a>
kodithrowaway@gmail.com