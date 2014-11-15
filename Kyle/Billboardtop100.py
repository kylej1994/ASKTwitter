__author__ = 'kylejablon'
#This code scrapes the billboard top 100 using xpath and returns an array of the names of the top 100 songs

#xpath ipmorts
from lxml import html
import requests

##test code courtesy of http://docs.python-guide.org/en/latest/scenarios/scrape/
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.text)
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span/@class')
# print buyers
# print prices



def billboardscrape(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)


    #Collect array of song number in format of "row-#{songnumber}"
    songsnumber = tree.xpath('//article/@id')
    #Collect array of song names in format of "Song Hover-#{SongName}"
    songhovernames = tree.xpath('//article/@data-hovertracklabel')
    #Because our collection of song names is in an incoherent format, we must fix it to just be an array of song names


    #Now create the final array of the songs. First create an empty array, then add the concatenate dversion of the new songs
    songs = []
    i = 0
    for song in songhovernames:
        songs.append(song[11:])
        i += 1

    return songs

#The current billboard web page we will access is going to be the week of October 5, 2013. This can be modified later.
billboardwebpage = 'http://www.billboard.com/charts/hot-100/2013-10-05'
print billboardscrape(billboardwebpage)
