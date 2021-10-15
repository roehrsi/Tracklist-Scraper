'''
Created on 04.01.2020

@author: Daniel
'''

from _datetime import date, timedelta
from requests_html import HTML, HTMLSession
from src import printer

rawurl = "{}?date={}&hour={}&search_submit=Anzeigen"

ndr2 = "NDR2", "https://www.ndr.de/ndr2/programm/titelliste1202.html"
ndr1NDS = "NDR1 Niedersachsen", "https://www.ndr.de/ndr1niedersachsen/programm/titelliste1210.html"
ndr903 = "NDR90.3", "https://www.ndr.de/903/programm/titelliste1208.html"
ndr1WN = "NDR1 Welle Nord", "https://www.ndr.de/wellenord/programm/titelliste1204.html"
ndrRMV = "NDR Radio MW", "https://www.ndr.de/radiomv/programm/titelliste1206.html"
ndrkultur = "NDR Kultur", "https://www.ndr.de/ndrkultur/programm/titelliste1212.html"
ndrblue = "NDR blue", "https://www.ndr.de/ndrblue/programm/titelliste1214.html"

njoy = "N-JOY", "https://www.n-joy.de/radio/titelsuche118"

def run(station):
    
    tuple = None
    if station=="ndr2":
        tuple = ndr2
    elif station=="ndr1nds":
        tuple = ndr1NDS
    elif station=="ndr903":
        tuple = ndr903
    elif station=="ndr1WN":
        tuple = ndr1WN 
    elif station=="ndrRMV":
        tuple = ndrRMV
    elif station=="ndrkultur":
        tuple = ndrkultur
    elif station=="ndrblue":
        tuple = ndrblue
    elif station=="njoy":
        tuple = njoy
        rawurl = "{}_date-{}_hour-{}.html"
    
    scrape_url(tuple)

    
def scrape_url(station):
    print("working... This may take a while")
    tracks = []
    today = date.today()
    delta = timedelta(days=1)    

    i = 0    
    for daynum in range(0, 14):
        day = today - delta * daynum
        for hour in range(0, 24):
            #use the url of the specified station from the above list
            url = rawurl.format(station[1], day, hour)
            session = HTMLSession()
            r = session.get(url)
            
            for e in r.html.find(".details"):
                i += 1
                if i % 500 == 0 :
                    print("still working... (I've found {} tracks so far!)".format(i))
                artist = e.find(".artist", first=True)
                title = e.find(".title", first=True)
                tracks.append((artist.text, title.text))
    
    #use the name of the specified station
    printer.to_file(station[0], tracks)
