# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:31:49 2019

@author: TeesMaarKhan
"""

import whois
site = input('Enter Your Site : ')
w = whois.whois(site)
print (w)
