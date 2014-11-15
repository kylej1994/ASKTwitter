__author__ = 'kylejablon'
#This code scrapes for song lyrics


#xpath ipmorts
from lxml import html
import requests

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
    finalLyrics = tempLyrics.replace('\n', "")
    return finalLyrics


#This is our test lyrics page, we will use azlyrics.com
lyricspage = 'http://www.azlyrics.com/lyrics/taylorswift/blankspace.html'
print lyricsscraper(lyricspage)

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
        driver.find_element_by_link_text(song).click()
        currentUrl = driver.current_url
        songDb[song] = lyricsscraper(currentUrl) #map song + return to dictionary
        driver.get(baseurl) #return to baseurl for next song

    driver.quit()
    print songDb #print keys for testing purposes

testsongs = ["Blank Space", "Turn Down For What"]
lyricSearcher(testsongs)