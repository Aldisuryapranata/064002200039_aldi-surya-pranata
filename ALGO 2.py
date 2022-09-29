# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:15:24 2022

@author: ALDI SURYA PRANATA
"""

import math

At = float(input("Masukkan lattitude kota pertama = "))
Ag = float(input("Masukkan longitude kota pertama = "))

Ab = float(input("Masukkan lattitude kota kedua = "))
Aa = float(input("Masukkan longitude kota kedua = "))

dlat = Ab - At
dlon = Aa - Ag

a = math.sin(math.radians(dlat/2)) * 2 + math.cos(math.radians(At)) * math.cos(math.radians(Ab)) * math.sin(math.radians(dlon/2)) * 2

# Versi Arc sinus
s = 2 * math.asin(math.sqrt(a))
    
# Versi Arc tangen 2
t = 6371.01

print("jarak antara dua titik adalah" , s*t, "kilometer")