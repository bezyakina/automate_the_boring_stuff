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
        url_list = list(dict.fromkeys(url_list))
        for url in url_list:
            print(url)
        return url_list

    def save_to_file(self):
        url_list = Scraper.scrape(self)
        new_file = open("file.txt", "a")
        for url in url_list:
            new_file.write(url + "\n")
        new_file.close()


base_url = "https://yandex.ru"
coronovirus_news = "https://yandex.ru/news/rubric/koronavirus"
Scraper(coronovirus_news).save_to_file()
