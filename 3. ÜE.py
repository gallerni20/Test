print ('Hallo User!')


n = int(input('Gib die Anzahl deiner Iterationen ein: ')) #Anzahl der wiederholungen
k = 0 #Variable der Formel
Summe = 0

while n >= k+1: #Bedingung für Abbruch
    Formel = 4*((-1)**k/(2*k+1))
    Summe += Formel
    k +=1 #Zählt von 0 hoch

print ('Ergebnis: ', Summe)