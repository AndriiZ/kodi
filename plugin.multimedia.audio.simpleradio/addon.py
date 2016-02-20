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

RADIOS = {'JamFM': {'name': 'JamFM (95.6)', 'thumb': 'http://jamfm.com.ua/i/raw/1/1396270676', 'url': 'http://cast.jamfm.com.ua/jamfm', 'desc': 'Rock station', 'genre': 'Rock'},
          'ERadio': {'name': 'ЄРадіо', 'url': 'http://etoradio.cc.colocall.com:8500/eradio_hi', 'desc': 'Є! Радіо — хвиля справжньої української музики', 'thumb': 'http://eradio.ua/image/logo.png', 'genre': 'Rock/Pop'},
          'Hrom': {'name': 'Громадське радіо', 'url': 'http://193.105.70.76:8000/stream', 'thumb': 'http://hromadskeradio.org/sites/default/files/media/brending/hromadskeradio-logo-250x45.png', 'desc': 'слухайте. думайте.', 'fanart': '', 'genre': 'Talk'},
		  'UR1': {'name': 'Українське радіо', 'thumb': 'http://proradio.org.ua/logos/ur1big.jpg', 'url': 'http://nrcu.gov.ua:8000/ur1-mp3', 'desc': 'Перший Національний - завжди перший!', 'genre': 'Talk'},
		  'UR2': {'name': 'Радіо Промінь', 'thumb': 'http://proradio.org.ua/logos/prominbig.jpg', 'url': 'http://nrcu.gov.ua:8000/ur2-mp3', 'desc': 'Слухай українське!', 'genre': 'Talk'},
          'RadioROKS': {'name': 'Радіо РОКС', 'thumb': 'http://www.proradio.org.ua/logos/roksbig.jpg', 'url': 'http://online-radioroks.tavrmedia.ua/RadioROKS', 'desc': 'Рок, тільки рок', 'genre': 'Talk'},
          'RadioEra': {'name': 'Радіо Ера', 'thumb': 'http://eramedia.com.ua/images/logo_3.png?ua', 'url': 'http://212.26.129.2:8000/era96', 'desc': 'Твій медіа навігатор', 'genre': 'Talk'},
          'RadioEra': {'name': 'Радіо Ера', 'thumb': 'http://eramedia.com.ua/images/logo_3.png?ua', 'url': 'http://212.26.129.2:8000/era96', 'desc': 'Твій медіа навігатор', 'genre': 'Talk'},
          'RadioYes': {'name': 'Радіо ЄС', 'thumb':'http://www.proradio.org.ua/logos/biges.gif', 'url': 'http://185.65.245.34:8000/kiev', 'desc': 'Радіо європейської столиці', 'genre':'Music'},
          'BusinessRadio': {'name': 'Бізнес радіо', 'thumb': 'http://www.proradio.org.ua/logos/business938big.gif','url': 'http://217.20.164.163:8018', 'desc':'Новий формат ваших рішень', 'genre': 'Music'},
          'UR3': {'name': 'Радіо Культура', 'thumb': 'http://proradio.org.ua/logos/ur3big.jpg', 'url': 'http://nrcu.gov.ua:8000/ur3-mp3', 'desc': 'Канал духовного відродження', 'genre': 'Talk'},
          'FMAristocrats': {'name': 'Aristocrats FM', 'thumb': 'https://scontent-frt3-1.xx.fbcdn.net/hprofile-xap1/v/t1.0-1/12119090_1705753319656877_247773860828234647_n.png?oh=d8496086fa3e4b5b696bfcdc75fe6a11&oe=568C7D4B', 'url': 'htt\
p://air.aristocrats.fm:8000/live2', 'genre': 'Misc', 'desc':'Радио Аристократы'},
          'Hvylia': {'name': 'Радіохвиля', 'url': 'http://radiohvilya.com.ua:8000/radiohvilya?type=.mp3', 'thumb': 'https://scontent-fra3-1.xx.fbcdn.net/hphotos-xta1/t31.0-8/11899777_1457239817916758_8834705431766478969_o.png', 'genre':\
 'Music', 'desc': 'Слухай серцем'},
          'Molode': {'name': 'Молоде радіо', 'url': 'http://molode.com.ua:8128/', 'thumb': 'http://molode.com.ua/pics/r01.jpg', 'genre': 'Music', 'desc': '100% сучасної української музики онлайн! Contemporary UA music online!'},
          'Radio24': {'name': 'Радіо 24', 'url': 'http://icecast.luxnet.ua/radio24', 'thumb': 'http://staticcdn.luxnet.ua/radio24/assets/img/logo-r24.png', 'genre': 'Misc', 'desc': 'Будь собою!'},
          'Skovoroda': {'name': 'Радіо Сковорода', 'url': 'http://195.248.234.62:8000/radioskovoroda', 'thumb': 'http://radioskovoroda.com/templates/skovoroda/images/logo-smal.png', 'genre': 'Misc', 'desc': ''}
          }

def get_stations():
	return RADIOS.keys()
	
def get_station(key):
	return RADIOS[key]

def get_action(url):
    return '?action=play&source={0}'.format(url)
	
def list_stations():
    playlist = []
    stations = get_stations()
    for station in stations:
        item = get_station(station)
        url = '{0}{1}'.format(addon_url, get_action(item['url']))
        list_item = xbmcgui.ListItem(label=item['name'], label2=item['desc'], thumbnailImage=item['thumb'])
        list_item.setProperty('IsPlayable', 'true')
        title = '{0}. {1}'.format(item['name'], item['desc'])
        list_item.setInfo(type='music', infoLabels = {'title': title, 'genre': item['genre']})
        playlist.append((url,list_item,False,item['url']))
    xbmcplugin.addDirectoryItems(addon_handle,playlist,1)
    xbmcplugin.addSortMethod(addon_handle,xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    if xbmc.Player().isPlaying() != True:
        xbmc.Player().play('http://cast.jamfm.com.ua/jamfm')
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
