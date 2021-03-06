#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:49:40 2020

@author: jose
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'https://www.shoecarnival.com/womens/sandals/'
howmany = 0

html = urllib.request.urlopen(URL, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup.findAll("span", {"class": "price-standard"})

for tag in tags:
    prices_tags = tag.find_parent('div').findChildren('span')
    print("Price savings : $", format(float(prices_tags[0].text[2:]) - float(prices_tags[1].text[2:]), ',.2f'))
    howmany = howmany + 1

print("We found " + str(howmany) + " anchors")