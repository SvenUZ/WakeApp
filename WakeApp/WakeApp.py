import datetime
import json
import os.path
from datetime import timedelta

while True:
    # Funktionen
    def HHMMtoM(hhmm):
        minuten = int(hhmm[:-3]) * 60 + int(hhmm[-2:])
        return minuten

    def MtoHHMM(minuten):
        hhmm = str(timedelta(minutes=minuten))[:-3]
        return hhmm

    def checkTime(hhmm):
        while hhmm > 24 or hhmm < 0:
            print('Richtige Zahl eintragen')
            hhmm = input()
            return hhmm


    
    # Inhalt
    print('Herzlich Willkommen zur WakeApp Terminal App')
    print('--------------')

    # Checken ob Datei existiert
    if(os.path.isfile('data.json')):
        load = open('data.json', "r")
        jobj = json.load(load)
        print('letzte Eingaben: \nAnkunftszeit: ', jobj['Ankunftszeit'], '\nLaenge der Fahrt: ', jobj['Fahrzeit'],'Minuten', '\nZeit am Morgen: ', jobj['Zeit am Morgen'],'Minuten \n')
        
        #jsonP = json.load(load)
        #print('Daten wurden geladen \n', jsonP)
    else:
        jsonFile = open("data.json", "w")

    print('Geben Sie die Ankunftszeit ein')
    hhmm = input()

    # Überprüfung von Doppelpunkt
    if(hhmm.find(':') != -1):
        hhmm = HHMMtoM(hhmm)
    else:
        hhmm = int(hhmm) * 60

    print('Wie lange benoetigen Sie fuer die Fahrt?')
    fahrzeit = input()

    if(':' in fahrzeit):
        fahrzeit = HHMMtoM(fahrzeit)

    print('Wie lange brauchst du um dich am morgen fertig zu machen?')

    morgenzeit = input()

    if(':' in morgenzeit):
        morgenzeit = HHMMtoM(morgenzeit)

    UhrzeitWecker = int(hhmm) - int(fahrzeit) - int(morgenzeit)


    json1 = {
        "Ankunftszeit": MtoHHMM(hhmm),
        "Fahrzeit": fahrzeit,
        "Zeit am Morgen": morgenzeit
    }
    write = open('data.json', "w")
    json2 = json.dumps(json1)
    write.write(json2)
    write.close()
    
    print('Deine vorraussichtliche Aufbruchzeit: ', MtoHHMM(UhrzeitWecker), '\n')
    print('------------------------------\n\n\n')

    