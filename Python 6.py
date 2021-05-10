# Erweitern des Wörterbuch Programmes
#
# 1) Funktion zur Eingabe des Befehls
# 2) Funktion zur Eingabe des Suchbegriffs bzw. Wortes
# 3) Funktion zur Suche
# 4) Funktion zur Ausgabe

woerterbuch_deutsch = ['Apfel','Birne','Kirsche','Melone','Marille','Pfirsich']
woerterbuch_englisch = ['apple','pear','cherry','melon','apricot','peach']

# Schleife für eine richtige Eingabe (E; L; A)


def eingabe_befehl():
    korrekt = False
    while korrekt == False:
        
        answer = input('Möchtest du etwas [E]rgänzen, [L]öschen oder [A]bfragen? Gib das zutreffende Element in den eckigen Klammer ein: ')
        answer = answer.upper()
    
        if answer == 'E':
            korrekt = True 
            return answer
    
        elif answer == 'L':
            korrekt = True
            return answer
    
        elif answer == 'A':
            korrekt = True
            return answer

def Übersetzung():
    
    index = 0
    korrekt_Ü = False
    
    while korrekt_Ü == False:
        Eingabe = input('Gib das zu übersetzende Wort ein: ')
        
        if woerterbuch_deutsch[index].lower() == Eingabe.lower(): 
            korrekt_Ü = True
            print ('Übersetzung: ',woerterbuch_englisch[index],' [EN]')
            
        elif woerterbuch_englisch[index].lower() == Eingabe.lower():
            korrekt_Ü = True
            print ('Übersetzung: ',woerterbuch_deutsch[index],' [DE]')
        
        else:
            print ('Falsche Eingabe oder Wort nicht vorhanden -> erneuter Versuch')
def Ergänzung():
    
    index = 0
    korrekt_e = False
    max = len(woerterbuch_deutsch)
    while korrekt_e == False:
        
        if len(woerterbuch_deutsch) <= max:
            Deutsch = input('Gib das Wort in Deutsch ein: ')
            woerterbuch_deutsch.append(Deutsch)
            Englisch = input('Gib das Wort in Englisch ein: ')
            woerterbuch_englisch.append(Englisch)
    
            print('Liste [DE]: ',woerterbuch_deutsch)
            print('Liste [EN]:',woerterbuch_englisch)
        
        else:
            korrekt_e = True

def Löschen():
    
    index = 0
    korrekt_l = False

    while korrekt_l == False:
        
        print (woerterbuch_deutsch)
        print(woerterbuch_englisch)
        D = input('Gib das zu löschende Wort aus der Liste ein: ')

        if woerterbuch_deutsch[index].lower() == D.lower():
            korrekt_l = True
            woerterbuch_deutsch.remove(woerterbuch_deutsch[index])
            woerterbuch_englisch.remove(woerterbuch_englisch[index])
        
        elif woerterbuch_englisch[index].lower() == D.lower():
            korrekt_l = True
            woerterbuch_deutsch.remove(woerterbuch_deutsch[index])
            woerterbuch_englisch.remove(woerterbuch_englisch[index])
        
    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)
    
# Hauptkommando

Befehl = eingabe_befehl()

if Befehl == 'A':
    Übersetzung()
if Befehl == 'E':
    Ergänzung()
if Befehl == 'L':
    Löschen()

print ('Ende des Programms!')