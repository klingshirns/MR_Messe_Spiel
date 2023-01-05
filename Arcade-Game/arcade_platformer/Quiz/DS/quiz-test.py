"""
Messe-Quiz
"""

score = 0
print("Herzlich Wilkommen zum Maschinenfabrik Reinhausen Quiz")

print("Zuerst kommen ein paar Fragen über die Maschinenfabrik Reinhausen:\n")

answer1 = input("1. Frage: Wann wurde die Maschinenfabrik Reinhausen gegründet?\n \n a) 1929\n b) 1986\n c) 1999\n Anwort:")
if answer1 == "a" or answer1 == "1929":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist 1929\n")

answer2 = input("2. Frage: Wer waren die Erfinder des Laststufenschalters?\n \n a) Dr.Janson\n b) Scheubeck\n c) die Gebrüder Scheubeck\n Anwort:")
if answer2 == "c" or answer2 == "die Gebrüder Scheubeck":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist die Gebrüder Scheubeck\n")

answer3 = input("3. Frage: Wann wurde der erste Laststufnschalter erfunden?\n \n a) 1903\n b) 1929\n c) 1856\n Anwort")
if answer3 == "b" or answer3 == "1929":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist 1929\n")

print("Schätzfrage: \n")
answer4 = input("In wie vielen Ländern sind wir vertreten?\n \n a) 36\n b) 19\n c) 28\n d) 40\n Anwort:")
if answer4 == "c" or answer4 == "28":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist 28\n\n")

print("Als nächstes kommen ein paar Fragen zur Ausbildung/ duales Studium\n")

answer5 = input("1. Frage: Wie viele Ausbildungsangebote gibt es?\n \n a) 14\n b) 9\n c) 20\n d) 4\n Antwort:")
if answer5 == "b" or answer5 == "9":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist 9\n ")

answer6 = input("2. Frage: Was sind deine Belohnungen während der Ausbildung?\n \n Mehrfachauswahl!!\n \na) attraktive Vergütungen\n b) 40 Stunden-Woche\n c) iPad oder Laptop\n d) feste Arbeitszeiten\n e) 35 Stunden-Woche\n f) flexible Arbeitszeiten\n Antwort:")
if answer6 == "a" and answer6 == "c"and answer6 == "e" and answer6 == "f":
    print("Richtig")
    score += 1
else:
    print("Falsch!! Richtig sind attraktive Vergütungen, iPad oder Laptop, 35 Stunden-Woche, flexible Arebitszeiten\n")

print("Schätzfrage:\n")
answer7= input("Wie viele Auszubildende werden derzeit in der MR auf die späteren Unternehmensaufgaben vorbereitet?\n \n a) 130\n b) 82\n c) 90\n d) 111,5\n e) 98\n Anwort:")
if answer7 == "e" or answer7 == "1929":
    print("Richtig\n")
    score += 1
else: 
    print("Falsch!! Richig ist 1929\n")

print("Du hast " + str(score/7 * 100) + "%" + " der Fragen richtig beantwortet!!")