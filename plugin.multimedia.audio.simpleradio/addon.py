#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmc

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

addon_handle = int(sys.argv[1])
addon_url = sys.argv[0]

xbmcplugin.setContent(addon_handle, 'audio')

ROOT = 'http://192.168.1.20:8000/'

RADIOS = {'JamFM': {'name': 'JamFM (95.6)', 'thumb': 'logo/jamfm.png', 'url': 'jamfm', 'desc': 'Rock station', 'genre': 'Rock'},
          'ERadio': {'name': 'ЄРадіо', 'url': 'eradio', 'desc': 'Є! Радіо — хвиля справжньої української музики', 'thumb': 'logo/eradio.png', 'genre': 'Rock/Pop'},
          'Hrom': {'name': 'Громадське радіо', 'url': 'hromadske', 'thumb': 'logo/hromadske.png', 'desc': 'слухайте. думайте.', 'fanart': '', 'genre': 'Talk'},
	  'UR1': {'name': 'Українське радіо', 'thumb': 'logo/ur1.png', 'url': 'ur1', 'desc': 'Перший Національний - завжди перший!', 'genre': 'Talk'},
	  'UR2': {'name': 'Радіо Промінь', 'thumb': 'logo/ur2.png', 'url': 'ur2', 'desc': 'Слухай українське!', 'genre': 'Talk'},
          'RadioROKS': {'name': 'Радіо РОКС', 'thumb': 'logo/RadioROKS.jpg', 'url': 'RadioROKS', 'desc': 'Рок, тільки рок', 'genre': 'Talk'},
          'RadioEra': {'name': 'Радіо Ера', 'thumb': 'logo/radioera.png', 'url': 'RadioEra', 'desc': 'Твій медіа навігатор', 'genre': 'Talk'},
          'RadioYes': {'name': 'Радіо ЄС', 'thumb':'logo/radioyes.gif', 'url': 'radioyes', 'desc': 'Радіо європейської столиці', 'genre':'Music'},
          'BusinessRadio': {'name': 'Бізнес радіо', 'thumb': 'logo/businessradio.gif','url': 'BusinessRadio', 'desc':'Новий формат ваших рішень', 'genre': 'Music'},
	  'UR3': {'name': 'Радіо Культура', 'thumb': 'logo/ur3.jpg', 'url': 'ur3', 'desc': 'Канал духовного відродження', 'genre': 'Talk'},
          'FMAristocrats': {'name': 'Aristocrats FM', 'thumb': 'logo/aristocratsFm.png', 'url': 'AristocratsFm', 'genre': 'Misc', 'desc':'Радио Аристократы'},
          'Hvylia': {'name': 'Радіохвиля', 'url': 'radiohvilya', 'thumb': 'logo/radioHvylya.png', 'genre': 'Music', 'desc': 'Слухай серцем'},
          'Molode': {'name': 'Молоде радіо', 'url': 'molode', 'thumb': 'logo/molode.jpg', 'genre': 'Music', 'desc': '100% сучасної української музики онлайн! Contemporary UA music online!'},
          'Radio24': {'name': 'Радіо 24', 'url': 'radio24', 'thumb': 'logo/radio24.png', 'genre': 'Misc', 'desc': 'Будь собою!'},
          'Skovoroda': {'name': 'Радіо Сковорода', 'url': 'radioskovoroda', 'thumb': 'logo/skovoroda.png', 'genre': 'Misc', 'desc': ''}
          }

def get_stations():
	return RADIOS.keys()
	
def get_station(key):
	return RADIOS[key]

def get_action(url):
    return '?action=play&source={0}{1}'.format(ROOT, url)
	
def list_stations():
    playlist = []
    stations = get_stations()
    for station in stations:
        item = get_station(station)
        url = '{0}{1}'.format(addon_url, get_action(item['url']))
        thumburl = '{0}{1}'.format(ROOT, item['thumb'])
        list_item = xbmcgui.ListItem(label=item['name'], label2=item['desc'], thumbnailImage=thumburl)
        list_item.setProperty('IsPlayable', 'true')
        title = '{0}. {1}'.format(item['name'], item['desc'])
        list_item.setInfo(type='music', infoLabels = {'title': title, 'genre': item['genre']})
        playlist.append((url,list_item,False,item['url']))
    xbmcplugin.addDirectoryItems(addon_handle,playlist,1)
    xbmcplugin.addSortMethod(addon_handle,xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(addon_handle)

def play_radio(radio):
    if radio != '':
        play_item = xbmcgui.ListItem(path=radio)
        xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
        #xbmcgui.Dialog().ok(radio)

def router(paramstring):
    params = dict(parse_qsl(paramstring[1:]))
    if params:
        #xbmcgui.Dialog().ok('router',params['source'])
        if params['action'] == 'play':
            play_radio(params['source'])
    else:
        list_stations()

if __name__ == '__main__':
    router(sys.argv[2])
