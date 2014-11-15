__author__ = 'kylejablon'
#This code scrapes for song lyrics


#xpath ipmorts
from lxml import html
import requests

#This is our test lyrics page, we will use azlyrics.com
lyricspage = 'http://www.azlyrics.com/lyrics/taylorswift/blankspace.html'
page = request.get(lyricspage)
tree = html.fromstring(page.text)

unmodifiedlyrics = tree.xpath('//')