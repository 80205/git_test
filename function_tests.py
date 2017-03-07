# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:20:24 2017

@author: 王晓涛
"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://localhost:8000")
assert "Django" in browser.title