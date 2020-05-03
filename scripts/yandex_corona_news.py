#!/usr/bin/env python3

import urllib.request
from urllib.parse import urlsplit, urlunsplit
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        url_list = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "/news/story/" in url:
                url = urlunsplit(urlsplit(url)._replace(query=""))
                url_list.append(base_url + url)
        for url in list(dict.fromkeys(url_list)):
            print(url)


base_url = "https://yandex.ru"
coronovirus_news = "https://yandex.ru/news/rubric/koronavirus"
Scraper(coronovirus_news).scrape()

