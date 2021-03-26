Name= input('Bitte gib deinen Namen ein: ')
print ('Hello', Name,'!')

zahl1= int(input('Gib die erste Zahl ein: '))

zahl2= int(input('Gib eine zweite Zahl ein: '))

print ('Deine Ergebnisse: ')
#Summe

print ('Summe = ', zahl1+zahl2)

#Differenz

if zahl1 > zahl2:
    Differenz= zahl1-zahl2
else:
    Differenz= zahl2-zahl1
print('Differenz = ',Differenz)

#Produkt

print ('Produkt = ', zahl1*zahl2)

#Quotient

if zahl1 > zahl2:
    Quotient= (zahl1/zahl2)
else:
    Quotient= (zahl2/zahl1)
print ('Quotient = ',Quotient)


