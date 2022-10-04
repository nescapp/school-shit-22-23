def getinfo(Prompt):  # Fonction qui permet de récupérer une information
    while True:
        try:
            return int(input(Prompt))
        except ValueError:
            print("Erreur - Veuillez entrer un nombre entier")


age = getinfo("Entrer l'age : ")
anne_permis = getinfo("Entrer le nombre d'annees de permis : ")
accidents = getinfo("Entrer le nombre d'accidents : ")
anne_assurance = getinfo("Entrer le nombre d'annees d'assurance : ")

# Calcul du tarif
if age < 25 and anne_permis < 2:
    if accidents == 0:
        tarif = "rouge"
    else:
        tarif = "refusé"
elif age < 25 and anne_permis >= 2 or age >= 25 and anne_permis < 2:
    if accidents == 0:
        tarif = "orange"
    elif accidents == 1:
        tarif = "rouge"
    else:
        tarif = "refusé"
elif age >= 25 and anne_permis >= 2:
    if accidents == 0:
        tarif = "vert"
    elif accidents == 1:
        tarif = "orange"
    elif accidents == 2:
        tarif = "rouge"
    else:
        tarif = "refusé"

# Calcul du tarif en fonction de la fidélité
if anne_assurance >= 5:
    if tarif == "rouge":
        tarif = "orange"
    elif tarif == "orange":
        tarif = "vert"
    elif tarif == "vert":
        tarif = "bleu"

# Affichage du tarif
print("-----------------------------")
print(f"Tarif {tarif}")
