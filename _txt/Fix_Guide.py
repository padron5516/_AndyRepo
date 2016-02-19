#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import xbmcplugin
import xbmcgui
import xbmc
import xbmcaddon
import os
import sys
import time
import xbmcvfs
import glob
import shutil
import subprocess
dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()

mainurl_epg = \
    'https://raw.githubusercontent.com/halikus/_AndyRepo/master/_txt/'
url_EPG_ADDONINI = mainurl_epg + 'addons.ini'

addon1 = 'plugin.video.stalker'
addon2 = 'plugin.video.dnatv'
addon3 = 'Andy.plugin.ufo'
addon4 = 'Andy.plugin.video'
addon5 = '-'
addon6 = '-'
addon7 = '-'
addon8 = ''
addon9 = '-'
addon10 = '-'

TVGuide1 = 'Andy.plugin.program.Guide'
TVGuide2 = 'Andy.plugin.program.Guide.Extra'
TVGuide3 = 'Andy.plugin.program.Guide.UK'
TVGuide4 = 'Andy.plugin.program.Guide.Sports'
TVGuide5 = 'Andy.plugin.program.Guide.Stalker'
TVGuide6 = 'script.tvguidetecbox'
TVGuide7 = 'script.ivueguide'
TVGuide8 = '-'
TVGuide9 = '-'
TVGuide10 = '-'

mode = 'Maintenance_Guide_TVGuide'
mode = 'Guide_TVGuide'


################################
###    Fix Maintenance Main      ###
################################

def Maintenance_Guide_TVGuide():

    Wipe_Cache()

    Delete_Packages()

    # TVGuide_Delete_addon_data_cache_file()

    TVGuide_Delete_addon_data_cache_file_prompt()

    # TVGuide_Delete_userdata_files()

    TVGuide_Delete_userdata_files_prompt()

    # Clean_KODI_thumbnails()

    Clean_KODI_thumbnails_prompt()


################################
###    Fix TVGuide Main      ###
################################

def Guide_TVGuide():

    Wipe_Cache()

    Delete_Packages()

    # TVGuide_Delete_addon_data_cache_file()

    TVGuide_Delete_addon_data_cache_file_prompt()


    # TVGuide_Delete_userdata_files()
    # TVGuide_Delete_userdata_files_prompt()

    # Clean_KODI_thumbnails()
    # Clean_KODI_thumbnails_prompt()

################################
###    Delete TVGuide cache     ###
################################

def TVGuide_Delete_addon_data_cache_file():
    addon_data_TVGuide_cache_file_delete(addon1)
    addon_data_TVGuide_cache_file_delete(addon2)
    addon_data_TVGuide_cache_file_delete(addon3)
    addon_data_TVGuide_cache_file_delete(addon4)
    addon_data_TVGuide_cache_file_delete(addon5)
    addon_data_TVGuide_cache_file_delete(addon6)
    addon_data_TVGuide_cache_file_delete(addon7)
    addon_data_TVGuide_cache_file_delete(addon8)
    addon_data_TVGuide_cache_file_delete(addon9)
    addon_data_TVGuide_cache_file_delete(addon10)


#
################################
###    Delete TVGuide cache     ###
################################

def TVGuide_Delete_addon_data_cache_file_prompt():
    choice = xbmcgui.Dialog().yesno(
        'Main cache cleared.  Clear plugins Cache?',
        'This will clear :',
        'http_portal_iptvprivateserver_tv',
        'http_mw1_iptv66_tv',
        nolabel='Cancel',
        yeslabel='Delete',
        )
    if choice == 1:
        addon_data_TVGuide_cache_file_delete(addon1)
        addon_data_TVGuide_cache_file_delete(addon2)
        addon_data_TVGuide_cache_file_delete(addon3)
        addon_data_TVGuide_cache_file_delete(addon4)
        addon_data_TVGuide_cache_file_delete(addon5)
        addon_data_TVGuide_cache_file_delete(addon6)
        addon_data_TVGuide_cache_file_delete(addon7)
        addon_data_TVGuide_cache_file_delete(addon8)
        addon_data_TVGuide_cache_file_delete(addon9)
        addon_data_TVGuide_cache_file_delete(addon10)


#

def addon_data_TVGuide_cache_file_delete(addon):
    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib11 = os.path.join(path, 'http_mw1_iptv66_tv')
    lib12 = os.path.join(path, 'http_mw1_iptv66_tv-genres')
    lib13 = os.path.join(path, 'http_portal_iptvprivateserver_tv')
    lib14 = os.path.join(path, 'http_portal_iptvprivateserver_tv-genres'
                         )
    lib15 = os.path.join(path, 'http_iptv66_stalkerclone_network')
    lib16 = os.path.join(path, 'http_iptv66_stalkerclone_network-genres'
                         )
    lib17 = os.path.join(path, 'http_nfps_stalkerclone_network')
    lib18 = os.path.join(path, 'http_nfps_stalkerclone_network-genres')
    lib19 = os.path.join(path, 'http_nfps_stalkerclone_network.1')
    lib110 = os.path.join(path,
                          'http_nfps_stalkerclone_network-genres.1')
    try:
        os.remove(lib11)
        os.remove(lib12)
        os.remove(lib13)
        os.remove(lib14)
        os.remove(lib15)
        os.remove(lib16)
        os.remove(lib17)
        os.remove(lib18)
        os.remove(lib19)
        os.remove(lib110)
    except:
        pass


################################
###    TVGuide Delete userdata files
################################

def TVGuide_Delete_userdata_files_prompt():
    choice = xbmcgui.Dialog().yesno(
        'Reset EPG?',
        'This will reset your EPG and addons.ini',
        'This cannot run inside TV Guide',
        'ReDownloaded upon next start',
        nolabel='Cancel',
        yeslabel='Delete',
        )
    if choice == 1:
        TVGuide_Delete_userdata(TVGuide1)
        TVGuide_Delete_userdata(TVGuide2)
        TVGuide_Delete_userdata(TVGuide3)
        TVGuide_Delete_userdata(TVGuide4)
        TVGuide_Delete_userdata(TVGuide5)
        TVGuide_Delete_userdata(TVGuide6)
        TVGuide_Delete_userdata(TVGuide7)
        TVGuide_Delete_userdata(TVGuide8)
        TVGuide_Delete_userdata(TVGuide9)
        TVGuide_Delete_userdata(TVGuide10)


#

def TVGuide_Delete_userdata_files():
    TVGuide_Delete_userdata(TVGuide1)
    TVGuide_Delete_userdata(TVGuide2)
    TVGuide_Delete_userdata(TVGuide3)
    TVGuide_Delete_userdata(TVGuide4)
    TVGuide_Delete_userdata(TVGuide5)
    TVGuide_Delete_userdata(TVGuide6)
    TVGuide_Delete_userdata(TVGuide7)
    TVGuide_Delete_userdata(TVGuide8)
    TVGuide_Delete_userdata(TVGuide9)
    TVGuide_Delete_userdata(TVGuide10)


#

def TVGuide_Delete_userdata(addon):
    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib1 = os.path.join(path, 'source5.db')
    lib2 = os.path.join(path, 'guide.xml')
    lib3 = os.path.join(path, 'master.xml')
    lib4 = os.path.join(path, 'Sports.xml')
    lib5 = os.path.join(path, 'Networks.xml')
    lib6 = os.path.join(path, 'Stalker.xml')
    lib7 = os.path.join(path, '0.xml')
    lib8 = os.path.join(path, '1.xml')
    lib9 = os.path.join(path, '2.xml')
    lib10 = os.path.join(path, '3.xml')
    lib11 = os.path.join(path, '4.xml')
    lib12 = os.path.join(path, '5.xml')
    try:
        os.remove(lib1)
        os.remove(lib2)
        os.remove(lib3)
        os.remove(lib4)
        os.remove(lib5)
        os.remove(lib6)
        os.remove(lib7)
        os.remove(lib8)
        os.remove(lib9)
        os.remove(lib10)
        os.remove(lib11)
        os.remove(lib12)
    except:
        pass


       #

################################
###    TVGuide Delete addons.ini files
################################

def TVGuide_Delete_addonsini_files():
    TVGuide_Delete_addonsini(TVGuide1)
    TVGuide_Delete_addonsini(TVGuide2)
    TVGuide_Delete_addonsini(TVGuide3)
    TVGuide_Delete_addonsini(TVGuide4)
    TVGuide_Delete_addonsini(TVGuide5)
    TVGuide_Delete_addonsini(TVGuide6)
    TVGuide_Delete_addonsini(TVGuide7)
    TVGuide_Delete_addonsini(TVGuide8)
    TVGuide_Delete_addonsini(TVGuide9)
    TVGuide_Delete_addonsini(TVGuide10)


#

def TVGuide_Delete_addonsini(addon):
    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib = os.path.join(path, 'addons.ini')
    try:
        os.remove(lib)
    except:
        pass

       #

    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib = os.path.join(path, 'addons.ini')
    try:

       # DownloaderClass9(url_EPG_ADDONINI,lib,addon)

        time.sleep(1)
    except:
        pass


#

def TVGuide_Delete_addonsini_files_prompt():
    choice = xbmcgui.Dialog().yesno(
        'Delete addonsini?',
        'This will reset your addons.ini',
        'This cannot run inside TV Guide',
        'ReDownloaded upon next start',
        nolabel='Cancel',
        yeslabel='Delete',
        )
    if choice == 1:
        TVGuide_Delete_addonsini2(TVGuide1)
        TVGuide_Delete_addonsini2(TVGuide2)
        TVGuide_Delete_addonsini2(TVGuide3)
        TVGuide_Delete_addonsini2(TVGuide4)
        TVGuide_Delete_addonsini2(TVGuide5)
        TVGuide_Delete_addonsini2(TVGuide6)
        TVGuide_Delete_addonsini2(TVGuide7)
        TVGuide_Delete_addonsini2(TVGuide8)
        TVGuide_Delete_addonsini2(TVGuide9)
        TVGuide_Delete_addonsini2(TVGuide10)


#

def TVGuide_Delete_addonsini2(addon):
    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib = os.path.join(path, 'addons.ini')
    try:
        os.remove(lib)
    except:
        pass

       #

    path = \
        xbmc.translatePath(os.path.join('special://home/userdata/addon_data'
                           , addon))
    lib = os.path.join(path, 'addons.ini')
    try:

       # DownloaderClass9(url_EPG_ADDONINI,lib,addon)

        time.sleep(1)
    except:
        pass


#

################################
###    Delete Packages       ###
################################

def Delete_Packages():
    packages_cache_path = \
        xbmc.translatePath(os.path.join('special://home/addons/packages'
                           , ''))
    for (root, dirs, files) in os.walk(packages_cache_path):
        file_count = 0
        file_count += len(files)

    # Count files and give option to delete

        if file_count > 0:
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))


#

################################
###    Delete Cache          ###
################################

def Wipe_Cache():
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'
                                   ), 'cache')
    if os.path.exists(xbmc_cache_path) == True:
        for (root, dirs, files) in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)

        # Count files and give option to delete

            if file_count > 0:
                for f in files:
                    try:
                        os.unlink(os.path.join(root, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d))
                    except:
                        pass


################################
###     Function to clear the thumbnails folder
################################

def Clean_KODI_thumbnails():
    Remove_Textures()

    #

    THUMBNAILS = \
        xbmc.translatePath(os.path.join('special://home/userdata',
                           'Thumbnails'))
    Destroy_Path(THUMBNAILS)


    # Destroy_Path('special://home/userdata/Thumbnails')
#
################################
###     Function to clear the thumbnails folder with a prompt
################################

def Clean_KODI_thumbnails_prompt():
    choice = xbmcgui.Dialog().yesno(
        'Clear Cached Images?',
        'This will clear your textures13.db file and remove',
        'your Thumbnails folder. These will automatically be',
        'repopulated after a restart.',
        nolabel='Cancel',
        yeslabel='Delete',
        )
    if choice == 1:
        Remove_Textures()

        #

        THUMBNAILS = \
            xbmc.translatePath(os.path.join('special://home/userdata',
                               'Thumbnails'))
        Destroy_Path(THUMBNAILS)


        # Destroy_Path('special://home/userdata/Thumbnails')
#
# Function to remove textures13.db and thumbnails folder

def Remove_Textures():
    textures = \
        xbmc.translatePath('special://home/userdata/Database/Textures13.db'
                           )
    try:
        dbcon = database.connect(textures)
        dbcur = dbcon.cursor()
        dbcur.execute('DROP TABLE IF EXISTS path')
        dbcur.execute('VACUUM')
        dbcon.commit()
        dbcur.execute('DROP TABLE IF EXISTS sizes')
        dbcur.execute('VACUUM')
        dbcon.commit()
        dbcur.execute('DROP TABLE IF EXISTS texture')
        dbcur.execute('VACUUM')
        dbcon.commit()
        dbcur.execute("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))"""
                      )
        dbcon.commit()
        dbcur.execute("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)"""
                      )
        dbcon.commit()
        dbcur.execute("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))"""
                      )
        dbcon.commit()
    except:
        pass


#
# Function to do a full wipe.

def Destroy_Path(path):
    dp.create(path, 'Wiping...', '', 'Please Wait')
    shutil.rmtree(path, ignore_errors=True)


#

def DownloaderClass9(
    url,
    dest,
    dlfile,
    useReq=False,
    ):
    dp = xbmcgui.DialogProgress()
    dp.create('TVGuide', 'Downloading & Copying ' + dlfile, '')
    if useReq:
        import urllib2
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://wallpaperswide.com/')
        f = open(dest, mode='wb')
        resp = urllib2.urlopen(req)
        content = int(resp.headers['Content-Length'])
        size = content / 100
        total = 0
        while True:
            if dp.iscanceled():
                raise Exception('Canceled')
                dp.close()
            chunk = resp.read(size)
            if not chunk:
                f.close()
                break
            f.write(chunk)
            total += len(chunk)
            percent = min(100 * total / content, 100)
            dp.update(percent)
    else:
        urllib.urlretrieve(url, dest, lambda nb, bs, fs, url=url: \
                           _pbhook(nb, bs, fs, url, dp))


#

def _pbhook(
    numblocks,
    blocksize,
    filesize,
    url=None,
    dp=None,
    ):
    try:
        percent = min(numblocks * blocksize * 100 / filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled():
        raise Exception('Canceled')
        dp.close()


if mode == 'Guide_TVGuide':
    Guide_TVGuide()
if mode == 'Maintenance_Guide_TVGuide':
    Maintenance_Guide_TVGuide()
