import xbmc
#xbmc.executebuiltin('XBMC.ActivateWindow(videofiles,C:\)')
#xbmc.executebuiltin('XBMC.RunScript(script.audio.spotimc)')
#xbmc.executebuiltin('XBMC.ActivateWindow(myvideolibrary,movietitles)')
#xbmc.executebuiltin('XBMC.ActivateWindow(videofiles,x:\downloads\)')


# Clean cache
import os
import xbmc
path = xbmc.translatePath( "special://temp" )
filenames = next(os.walk(path))[2]
for i in filenames:
    if ".fi" in i:
        os.remove(os.path.join(path, i))

