__author__ = 'kylejablon'
#This code scrapes for song lyrics


#xpath ipmorts
from lxml import html
import requests
import Billboardtop100 as bb
import sys

#selenium imports
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

#This function takes in a azlyrics.com URL, and returns a string of song lyrics
def lyricsscraper(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    unmodifiedlyrics = tree.xpath('//*[@id="main"]/div[3]/text()')
    #print unmodifiedlyrics

    blocklyrics = ''.join(unmodifiedlyrics) #You know have a huge block of lyrics including weird spaces
    tempLyrics = blocklyrics.replace('\r', "") #replace '\r' with a space
    finalLyrics = tempLyrics.replace('\n', " ")
    return finalLyrics


#This is our test lyrics page, we will use azlyrics.com
#lyricspage = 'http://www.azlyrics.com/lyrics/taylorswift/blankspace.html'
#print lyricsscraper(lyricspage)

#The following function searches given an array of song names will search azlyrics, and return a dictionary of lyrics
def lyricSearcher(songs):
    baseurl = "http://www.azlyrics.com/"
    driver = webdriver.Firefox()
    driver.get(baseurl)

#create a dictionary to map song names -> song lyrics
    songDb = {}

#for each song, add its values to the dictionary
    for song in songs:
        inputElement = driver.find_element_by_name("q") #find the search element
        inputElement.send_keys(song) #send a qeury for the song name
        inputElement.submit() #submit queury
        #click on song.
        try:
            songLink = driver.find_element_by_link_text(song)
            songLink.click()
        except(Exception):
            driver.get(baseurl)
            continue
        currentUrl = driver.current_url
        songDb[song] = lyricsscraper(currentUrl) #map song + return to dictionary
        driver.get(baseurl) #return to baseurl for next song

    driver.quit()
    return songDb

#Testcases
#testsongs = ["Blank Space", "Turn Down For What"]
#print lyricSearcher(testsongs)



#Four arbitrarily chosen weeks for billboard database building
top2011 = "http://www.billboard.com/charts/hot-100/2011-02-19"
top2012 = "http://www.billboard.com/charts/hot-100/2012-04-28"
top2013 = "http://www.billboard.com/charts/hot-100/2013-10-05"
top2014 = "http://www.billboard.com/charts/hot-100/2014-02-22"
dict2011 = lyricSearcher(bb.billboardscrape(top2011))
dict2012 = lyricSearcher(bb.billboardscrape(top2012))
dict2013 = lyricSearcher(bb.billboardscrape(top2013))
dict2014 = lyricSearcher(bb.billboardscrape(top2014))
songdatabase = dict(dict2011.items() + dict2012.items() + dict2013.items() + dict2014.items())
#songdatabase = lyricSearcher(["Blank Space", "Turn Down For What"])
sys.stdout = open('file.txt', 'w')
for key in songdatabase.keys():
    print key + ' ' + songdatabase[key] + '\n'
sys.stdout.close()