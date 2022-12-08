print ("Herzlich Wilkommen zum Maschinenfabrik Reinhausen Quiz")

playing = input ("Willst du spielen?")

if playing !="Ja": 
    quit()

score = 0

print ("OK!! Lass uns spielen")

print("Zuerst kommen ein paar Fragen über die Maschinenfabri Reinhausen:")

answer = input ("1. Frage: Wann wurde die Maschinenfabrik Reinhausen gegründet?")
print("a) 1929\n b) 1986\n c) 1999")
if answer == "1929":
    print("Richtig")
    score += 1


print("Du hast " + str(score/4 * 100) + "%" + " der Fragen richtig beantwortet!!")