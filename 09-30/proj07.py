age = int(input("Quelle est votre age: "))
sexe = input("Quelle est votre sexe (M-F): ").lower()
fumeur = input("Fumez vous? ").lower() == "oui"
sport = input("Faites vous du sport? ").lower() == "oui"

niveau = 0

if fumeur:
    niveau += 2
if sport:
    niveau -= 1
if sexe == "m" and age > 50:
    niveau += 1
if sexe == "f" and age > 60:
    niveau += 1

if niveau <= 1:
    print(f"Le niveau de risque est faible : ({niveau})")
else:
    print(f"Le niveau de risque est élevé : ({niveau})")