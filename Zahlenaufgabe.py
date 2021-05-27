# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:43:19 2021

@author: paula
"""

n = input("Eine ganze Zahl zwischen 0 und 100: ")

#einstellige Zahlen
if len(n) == 1:

        dict = {"0" : "null", "1" : "eins", "2" : "zwei", "3" : "drei", "4" : "vier", "5" : "fünf", "6" : "sechs", "7" : "sieben", "8" : "acht", "9" : "neun"}
        print(dict[n])

#zweistellige Zahlen
if len(n) == 2:
        
        if n == "11" or n == "12" or n == "16":
            
            dict = {"11":"elf", "12":"zwölf", "16":"sechzehn"}
            
            print(dict[n])
            
        else:
            z = n[0]
            e = n[1]
            
            #Wort für Einerziffer
            dict_e = {"0" : "", "1" : "ein", "2" : "zwei", "3" : "drei", "4" : "vier", "5" : "fünf", "6" : "sechs", "7" : "sieben", "8" : "acht", "9" : "neun"}
            e_out = dict_e[e]
            
            zus_1 = ""
            
            #falls keine "Zehnerzahl", definiere Füllwort als "und"
            if e != "0":
                zus_1 = "und"
            
            #Wort für Zehnerziffer
            dict_z = {"1":"zehn", "2": "zwanzig", "3":"dreißig", "4":"vierzig", "5":"fünfzig", "6":"sechzig", "7": "siebzig", "8":"achtzig", "9":"neunzig"}
            z_out = dict_z[z]
            
            #output-Wort zusammensetzen
            output = e_out + zus_1 + z_out
            print(output)
        
#dreistellige Zahlen (100)
if len(n) == 3:
        print("einhundert")