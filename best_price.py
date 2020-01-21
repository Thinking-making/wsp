#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:49:40 2020

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

# =============================================================================
# while True:
#     info = html.read(8192)
#     print(info)
#     if len(info) < 1: break
# =============================================================================

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup.findAll("span", {"class": "price-standard"})
tags = soup.findAll("div", {"itemprop": "offers"})

for tag in tags:
    print(tag)
    howmany = howmany + 1

print("We found " + str(howmany) + " anchors")