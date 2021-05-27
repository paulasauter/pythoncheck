#pythoncheck

n = input("Eine ganze Zahl zwischen 0 und 100: ")

#auf , oder . prüfen
if "," in n or "." in n:
    
    n = input ("Bitte geben Sie Ihre Zahl ohne Dezimalstellen ein: ")

#einstellige Zahlen
if len(n) == 1:

        dict = {"0" : "null", "1" : "eins", "2" : "zwei", "3" : "drei", "4" : "vier", "5" : "fünf", "6" : "sechs", "7" : "sieben", "8" : "acht", "9" : "neun"}
        print(dict[n])

#zweistellige Zahlen
if len(n) == 2:
        
        #Ausnahmen
        if n == "11" or n == "12" or n == "16" or n == "17":
            
            dict = {"11":"elf", "12":"zwölf", "16":"sechzehn", "17" : "siebzehn"}
            
            print(dict[n])
       
        #regelmäßige Zahlen    
        else:
            z = n[0]
            e = n[1]
           
            #Wort für Einerziffer
            dict_e = {"0" : "", "1" : "ein", "2" : "zwei", "3" : "drei", "4" : "vier", "5" : "fünf", "6" : "sechs", "7" : "sieben", "8" : "acht", "9" : "neun"}
            e_out = dict_e[e]
            
            zus_1 = ""
            
            #Füllwort "und" für Zahlen die größer als 20 und keine Zehnerzahlen sind
            if e != "0" and z != "1":
                zus_1 = "und"
            
            #Wort für Zehnerziffer
            dict_z = {"1":"zehn", "2": "zwanzig", "3":"dreißig", "4":"vierzig", "5":"fünfzig", "6":"sechzig", "7": "siebzig", "8":"achtzig", "9":"neunzig"}
            z_out = dict_z[z]
            
            #output-Wort zusammensetzen
            output = e_out + zus_1 + z_out
            print(output)
        
#dreistellige Zahlen
if len(n) == 3:
        if n == "100":
            print("einhundert")
        else:
            print("Die Zahl liegt nicht zwischen 0 und 100")