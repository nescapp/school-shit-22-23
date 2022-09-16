"""
Dans ce projet, on se propose de créer un calculateur de trajet, permettant de savoir si un trajet ou une
série de trajet sont réalisables par rapport au réservoir d’essence d’une voiture.Pour ce faire, il faut
spécifier une distance en kilomètres et un nombre de passagers à bord (sans compter le conducteur).
Au départ, la voiture fait un plein d’essence de 32,5 Litres.
Indications :
- Le véhicule a les caractéristiques suivantes :
o Au départ, la voiture fait un plein d’essence de 32,5 litres
o Une consommation fixe de 5.0 litres pour 100 km
o Pour chaque personne ajoutée (le conducteur ne compte pas), l’essence
utilisée augmente de 30 % en rapport à la consommation normale.
o Exemple :
 Pour 1 personne en plus du conducteur, la consommation vaut 1.3 fois
la consommation normale.
 Pour 2 personnes en plus du conducteur, la consommation vaut 1.6 fois
la consommation normale.

o Lors de la saisie de la distance, si l’utilisateur met 0, le programme rempli le
réservoir d’essence du véhicule.
o Lorsque qu’un voyage est réalisable, un message affiche le nombre de litres
restants
o Le programme se termine uniquement si une panne d’essence se produit.
Si cela arrive, un message affiche que la panne arrivera lors de ce trajet.
Un second message affichera la distance parcourue avec tous les trajets (avant
celui de la panne).
"""
essance = 32.5
consommation = 5.0
distance = int(input("Entrer la distance de votre destination ou entrer 0 pour faire le plain : "))

if distance == 0:
    print("Vous avez fait le plein")
    print(f"Vous avez {essance} litres d'essance")
else:
    personne = int(input("Entrer le nombre de personne : "))

    # Calcul de la consommation
    consommation = consommation + (consommation * (personne * 0.3))

    # Calcul de la distance
    distance = distance * consommation

    # Calcul de la distance
    if distance > essance:
        print("Panne d'essence")
        print(f"Distance parcourue {essance / consommation}")
    else:
        print(f"Distance parcourue {distance / consommation}")


