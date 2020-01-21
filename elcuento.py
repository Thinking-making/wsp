#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:11:09 2020

@author: jose
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = 'http://www.elcuentorevistadeimaginacion.org/indexcuento.php'
howmany = 0

html = urllib.request.urlopen(URL, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
    howmany = howmany + 1

print("We found " + str(howmany) + " anchors")