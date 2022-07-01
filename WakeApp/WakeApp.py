import datetime
import json
import os.path
from datetime import timedelta
from pickle import TRUE

while True:
    # Funktionen
    def HHMMtoM(hhmm):
        minuten = int(hhmm[:-3]) * 60 + int(hhmm[-2:])
        return minuten

    def MtoHHMM(minuten):
        hhmm = str(timedelta(minutes=minuten))[:-3]
        return hhmm

    def CheckTime(hhmm):
        hhmm = int(hhmm)
        if(hhmm > 24 and hhmm < 0):
            while hhmm > 24 or hhmm < 0:      
                print('Richtige Zahl eintragen')
                hhmm = input()
                if(hhmm < 24 and hhmm > 0):
                    return hhmm
    
    def is_json(myjson):
        try:
            json.loads(myjson)
        except ValueError as e:
            return False
        return True
           

    # Inhalt
    print('Herzlich Willkommen zur WakeApp Terminal App')
    print('--------------')

    # Checken ob Datei existiert und ob die Datei eine valide JSON ist
    if(os.path.isfile('data.json')):
        jsonString = json.dumps('data.json')
        if(is_json(jsonString)):
            load = open('data.json', "r")
            jobj = json.load(load)
            print('letzte Eingaben: \nAnkunftszeit: ', jobj['Ankunftszeit'], 'Uhr', '\nLaenge der Fahrt: ', jobj['Fahrzeit'],'Minuten', '\nZeit am Morgen: ', jobj['Zeit am Morgen'],'Minuten', '\nvorgeschlagene Weckzeit: ', jobj['vorgeschlagener Wecker'], 'Uhr\n')
    else:
        new = open("data.json", "w")

    print('Geben Sie die Ankunftszeit ein')
    try:
        hhmm = input()
    except:
        print('Die Eingabe ist fehlgeschlagen, bitte erneut probieren')
        break

    # Ueberpruefung von Doppelpunkt
    try:
        if(hhmm.find(':') != -1):
            hhmm = HHMMtoM(hhmm)
        else:
            hhmm = int(hhmm) * 60
    except:
        print('Der Doppelpunkt-Check ist fehlgeschlagen')
    
    try:
        CheckTime(hhmm)
    except:
        print('Das Checken der Uhrzeit ist fehlgeschlagen')
        break
    print('Wie lange benoetigen Sie fuer die Fahrt?')
    fahrzeit = input()
    
    if(':' in fahrzeit):
        fahrzeit = HHMMtoM(fahrzeit)

    print('Wie lange brauchst du um dich am morgen fertig zu machen?')

    morgenzeit = input()

    if(':' in morgenzeit):
        morgenzeit = HHMMtoM(morgenzeit)

    UhrzeitWecker = int(hhmm) - int(fahrzeit) - int(morgenzeit)
    heute = str(datetime.datetime.today())

    json1 = {
        "Erstellungsdatum": heute,
        "Ankunftszeit": MtoHHMM(hhmm),
        "Fahrzeit": fahrzeit,
        "Zeit am Morgen": morgenzeit,
        "vorgeschlagener Wecker": MtoHHMM(UhrzeitWecker)
    }
    write = open('data.json', "w")
    json2 = json.dumps(json1)
    write.write(json2)
    write.close()
    
    print('------------------------------')
    print('Deine vorraussichtliche Aufbruchzeit: ', MtoHHMM(UhrzeitWecker), '\n\n\n')


    