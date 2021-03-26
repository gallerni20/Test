# Schleifen/Zählvariable: i, j, k
counter = 10

while counter >=0:
    print(counter) # 1. Möglichkeit (geht bis 0)
    counter = counter - 1 # alt.: counter -=1
    #print (counter) # Reihenfolge kann Auswirkungen auf das Programm haben. (geht bis -1)
    
#Addieren Sie in einer Schleife die Zahlen von 1 - 100 + Ausgabe des Ergebnisses

Summe = 0
Ergebnis = 0
while Summe <= 100:
    Summe +=1 # Zählt bei Summe + 1 dazu
    Ergebnis += Summe # Zählt jede Summe auf das vorherige Ergebnis

print ("Ergebnis: ", Ergebnis)
    