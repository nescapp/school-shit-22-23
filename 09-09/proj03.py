"""
Mini projet 6 : Compagnie d’assurance

Dans ce mini-projet, une compagnie d’assurance automobile propose à ses clients quatre
familles de tarifs identifiables par une couleur, du moins au plus onéreux :
Tarifs bleu, vert, orange et rouge.

Le tarif dépend de la situation du conducteur :

o   Un conducteur de moins de 25 ans et titulaire du permis depuis moins de
    deux ans, se voit attribuer le tarif rouge, si toutefois il n’a jamais été
    responsable d’accident. Sinon, la compagnie refuse de l’assurer.
o   Un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux
    ans, ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a
    le droit au tarif orange s’il n’a jamais provoqué d’accident, au tarif rouge pour
    un accident, sinon il est refusé.
o   Un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans
    bénéficie du tarif vert s’il n’est à l’origine d’aucun accident et du tarif orange
    pour un accident, du tarif rouge pour deux accidents, et refusé au-delà.
o   De plus, pour encourager la fidélité des clients acceptés, la compagnie
    propose un contrat de la couleur immédiatement la plus avantageuse s’il est
    entré dans la maison depuis plus de cinq ans. Ainsi, s’il satisfait à cette
    exigence, un client normalement « vert » devient « bleu », un client
    normalement « orange » devient « vert », et le « rouge » devient « orange ».

Écrire le programme permettant de saisir les données nécessaires et de calculer le tarif
d’assurance automobile selon quatre familles de tarifs identifiables par une couleur, du
moins au plus onéreux.

Les informations à entrer par l’utilisateur sont les suivantes :

- L’Age du conducteur
- Le nombre d’années de permis
- Le nombre d’accidents
- Le nombre d’années d’assurance

A l’issue de traitement de ces informations, le programme doit afficher un message
spécifiant la situation du client (bleu, vert, orange et rouge).
"""

def getinfo(Prompt): # Fonction qui permet de récupérer une information
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
