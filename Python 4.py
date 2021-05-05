Aufgabe Python 5
# Aufgabe: erweitern sie das Wörterbuchbeispiel um die Möglichkeit, Einträge zu ergänzen bzw. zu löschen

woerterbuch_deutsch = ['Apfel','Birne','Kirsche','Melone','Marille','Pfirsich']
woerterbuch_english = ['apple','pear','cherry','melon','apricot','peach']
Max = len(woerterbuch_deutsch)

index = 0

answer = (input('Möchtest du etwas [E]rgänzen, [L]öschen oder [A]bfragen? Gib das zutreffende Element in den eckigen Klammer ein: '))

if answer in ['e', 'E']:
    Deutsch = input('Gib das Wort in Deutsch ein: ')
    woerterbuch_deutsch.append(Deutsch)
    Englisch = input('Gib das Wort in Englisch ein: ')
    woerterbuch_english.append(Englisch)
    
    print(woerterbuch_deutsch)
    print(woerterbuch_english)

elif answer in ['L','l']:
    
    print (woerterbuch_deutsch)
    print(woerterbuch_english)
    D = input('Gib das zu löschende Wort aus der Liste ein: ')

    while index < Max:

        if woerterbuch_deutsch[index].lower() == D.lower():
            woerterbuch_deutsch.remove(woerterbuch_deutsch[index])
            woerterbuch_english.remove(woerterbuch_english[index])
            break
        
        if woerterbuch_english[index].lower() == D.lower():
            woerterbuch_deutsch.remove(woerterbuch_deutsch[index])
            woerterbuch_english.remove(woerterbuch_english[index])
            break
        
        index += 1
        
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
    
    if index == Max:
        print ('Wort wurde nicht gefunden!')
    
elif answer in ['A', 'a']:
    Eingabe = (input('Gib das zu übersetzende Wort ein: '))

    while index < Max:
    
        if woerterbuch_deutsch[index].lower() == Eingabe.lower(): 
            print('Übersetzung: ',woerterbuch_english[index], '(EN)') 
            break
    
        if woerterbuch_english[index].lower() == Eingabe.lower():
            print('Übersetzung: ',woerterbuch_deutsch[index], '(DE)')
            break
    
        index +=1
    
    if index == Max:
        print('Übersetzung konnte nicht gefunden werden!')   

else:
    print('Falsche Eingabe!')



  




