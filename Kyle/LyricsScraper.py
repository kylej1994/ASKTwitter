__author__ = 'kylejablon'
#This code scrapes for song lyrics


#xpath ipmorts
from lxml import html
import requests



def lyricsscraper(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    unmodifiedlyrics = tree.xpath('//*[@id="main"]/div[3]/text()')
    print unmodifiedlyrics

    blocklyrics = ''
    blocklyrics = ''.join(unmodifiedlyrics)
    print blocklyrics
    return blocklyrics


#This is our test lyrics page, we will use azlyrics.com
lyricspage = 'http://www.azlyrics.com/lyrics/taylorswift/blankspace.html'
print lyricsscraper(lyricspage)