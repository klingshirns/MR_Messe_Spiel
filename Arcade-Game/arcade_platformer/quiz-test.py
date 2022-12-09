print("Herzlich Wilkommen zum Maschinenfabrik Reinhausen Quiz")

playing = input("Willst du spielen?")

if playing !="Ja": 
    quit()

score = 0

print("OK!! Lass uns spielen")

print("Zuerst kommen ein paar Fragen über die Maschinenfabrik Reinhausen:")

answer1 = input("1. Frage: Wann wurde die Maschinenfabrik Reinhausen gegründet?\n \n a) 1929\n b) 1986\n c) 1999\n ")
if answer1 == "a" or answer1 == "1929":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist 1929")

answer2 = input("2. Frage: Wer war die Erfinder des Laststufenschalters?\n \n a) Dr.Janson\n b) Scheubeck\n c) die Gebrüder Scheubeck")
if answer2 == "c" or answer2 == "die Gebrüder Scheubeck":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist die Gebrüder Scheubeck")

answer3 = input("3. Frage: Wann wurde der erste Laststufnschalter erfunden?\n \n a) 1903\n b) 1929\n c) 1856")
if answer3 == "b" or answer3 == "1929":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist 1929")

print("Schätzfrage: \n")
answer4 = input("In wie vielen Ländern sind wir vertreten?\n \n a) 36\n b) 19\n c) 28\n d) 40")
if answer4 == "c" or answer4 == "28":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist 28")

print("Als nächstes kommen ein paar Fragen zur Ausbildung/ duales Studium")

answer5 = input("1. Frage: Wie viele Ausbildungsangebote gibt es?\n \n a) 14\n b) 9\n c) 20\n d) 4\n")
if answer5 == "b" or answer5 == "9":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist 9")

answer6 = input("2. Frage: Was sind deine Belohnungen während der Ausbildung?\n \n Mehrfachauswahl!!\n \na) attraktive Vergütungen\n b) 40 Stunden-Woche\n c) iPad oder Laptop\n d) feste Arbeitszeiten\n e) 35 Stunden-Woche\n f) flexible Arbeitszeiten\n")
("a) c) e) f)")
if answer6 == "a" and answer6 == "c"and answer6 == "e" and answer6 == "f" or answer6 =="attraktive Vergütungen" and answer6:
    print("Richtig")
    score += 1
else:
    print("Falsch!! Richtig sind ")

print("Schätzfrage:")
answer7= input("Wie viele Auszubildende werden derzeit in der MR auf die späteren Unternehmensaufgaben vorbereitet?")
print("a) 130\n b) 82\n c) 90\n d) 111,5\n e) 98")
("e)")
if answer1 == "a" or answer1 == "1929":
    print("Richtig")
    score += 1
else: 
    print("Falsch!! Richig ist 1929")

print("Du hast " + str(score/4 * 100) + "%" + " der Fragen richtig beantwortet!!")