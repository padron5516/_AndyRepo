## <a href="http://tinypic.com?ref=2iuw5ck" target="_blank"><img src="http://i66.tinypic.com/2iuw5ck.png" border="0" alt="Image and video hosting by TinyPic"></a> Andy Repository Public
------------


Repo Main Page (This page) https://github.com/halikus/_AndyRepo

Repo Zip https://raw.githubusercontent.com/halikus/_AndyRepo/master/Andy.repository.zip

Maintenance Program https://raw.githubusercontent.com/halikus/_AndyRepo/master/_repo/Andy.plugin.program.Maintenance/Andy.plugin.program.Maintenance-1.0.1.zip


Install http://kodi.tv/download/

ARM cpu (Most):  http://mirrors.kodi.tv/releases/android/arm/old/kodi-14.2-Helix-armeabi-v7a.apk

***Android - AceStreams and Sopcast can optionally be downloaded via Playstore


AceStream-3.0.6-2in1.apk   https://raw.githubusercontent.com/halikus/_AndyRepo/master/_android/AceStream-3.0.6-2in1.apk


org.sopcast.android_124.apk   https://raw.githubusercontent.com/halikus/_AndyRepo/master/_android/org.sopcast.android_124.apk



Windows  https://github.com/halikus/_AndyRepo/tree/master/_windows


## Repo Installation
------------

Simply download the Repo ZIP file to your device and install through the menu via:

System -> Settings -> Add-ons -> Install from zip file. 


Once the repository ZIP file is installed, you can install the individual add-ons through my repository:

System -> Settings -> Add-ons -> Install From Repository -> Select "Andy Repository" -> Program Add-Ons --> "Andy Maintenance Tool" --> Install


You can install Repositories (source of addons), Addons (the extra applications), preconfigured addon settings (Addon_data), and xmls.  The xml files are the sources of your media files.


IPTV Plugins are not installed with the AIO bundles.  You must install seperatly from repo.


## Comman Paths :

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




## Portable CMD

(Make a cmd file in main directory located anywhere)



@echo off

TASKKILL /im pulsar.exe /f

tskill pulsar.exe

TASKKILL /im Kodi.exe /f

tskill Kodi.exe

TASKKILL /im XBMC.exe /f

tskill XBMC.exe

start Kodi.exe -p



*This repo is a constant WIP by a simple hobbyist that knows python.  Modded\original work is tagged "Andy.".  Mostly acts as my backup and as a P.O.C.

kodithrowaway@gmail.com