from random import choice
studySet = [["s1","d11","d12"],["s2", "d21"],["s3","d31","d32"]]
while len(studySet) > 0:
    vyber = choice(studySet)
    #print(vyber)
    studySet.remove(vyber)
    #print(studySet)

    verze = choice(vyber)
    print("Zadání:",verze)

    odpoved = ""
    if verze == vyber[0]:
        odpoved = vyber[1:]
    else:
        odpoved = vyber[0]
    print("Odpověď:", odpoved)

    vstup = input("Zadej svou odpověď:")

    if (vstup.lower() in odpoved and type(odpoved) == list) or (vstup.lower() == odpoved):
        print("Správně")
    else:
        print("To je ale chybááááá")    
print("Konec zkoušení, není co zkoušet.")