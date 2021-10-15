'''
Created on 15.01.2020

@author: Daniel
'''
from _datetime import datetime
from requests_html import HTML, HTMLSession, HTMLResponse
from src import printer

days = ["today", "yesterday", "daybefore"]
name = "harmonyfm"
URL = f"https://www.{name}.de/musik/playlist.html?tx_ffhonair_pi1[action]=showhitfinder&tx_ffhonair_pi1[controller]=Onair&cHash=b6be3742e906131204d28e286870e9ea"


def run():
    scrape(URL)


def scrape(url):
    tracks = []
    print("working... This may take a while")
    i = 0
    for day in days:
        for hour in range(0, 24):
            payload = {"tx_ffhonair_pi1[__referrer][@extension]": "FfhOnair",
                       "tx_ffhonair_pi1[__referrer][@vendor]": "RTFFH",
                       "tx_ffhonair_pi1[__referrer][@controller]": "Onair",
                       "tx_ffhonair_pi1[__referrer][@action]": "showhitfinder",
                       "tx_ffhonair_pi1[__referrer][arguments]": "YTo2OntzOjY6ImFjdGlvbiI7czoxMzoic2hvd2hpdGZpbmRlciI7czoxMDoiY29udHJvbGxlciI7czo1OiJPbmFpciI7czoxMDoic29uZ0luZm9EYiI7czo3OiJoYXJtb255IjtzOjc6ImZvcm1kYXkiO3M6NToidG9kYXkiO3M6NDoiaG91ciI7czoyOiIxNyI7czo2OiJzdWJtaXQiO3M6NjoiU3VjaGVuIjt9080baeed414c69a4eb44c51d8717847975d5903f",
                       "tx_ffhonair_pi1[__referrer][@request]": '{"@extension":"FfhOnair","@controller":"Onair","@action":"showhitfinder"}157095b799c3b5bd431658a279f156717af157db',
                       "tx_ffhonair_pi1[__trustedProperties]": '{"songInfoDb":1,"formday":1,"submit":1}6c6c7e56fcb35bb4378bd04f5c4e6a1e2c56566e',
                       "tx_ffhonair_pi1[songInfoDb]": "harmony",
                       "tx_ffhonair_pi1[formday]": day,
                       "tx_ffhonair_pi1[hour]": f"{hour}",
                       "tx_ffhonair_pi1[submit]": "Suchen"}

            session = HTMLSession()
            r = session.post(url, params=payload)

            for e in r.html.find(".song"):
                i += 1
                if i % 500 == 0:
                    print("still working... (I've found {} tracks so far!)".format(i))
                artist = e.find(".artist", first=True)
                title = e.find(".title", first=True)
                tracks.append((artist.text, title.text))

    printer.to_file(name, tracks)
