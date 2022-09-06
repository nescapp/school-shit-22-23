"""
Dans ce mini-projet nous voulons réaliser un programme de calcul du prix du billet de
cinéma selon plusieurs rabais possibles :
Prix normal d’un billet : 10 €
Rabais étudiant : 2 €
Rabais membre : 3 €
Forfait famille : 1 €
Carte mensuelle : L’entrée est gratuite

Indications :
- Il est possible de bénéficier d’un rabais membre et étudiant en même temps.
- Il n’est pas possible de bénéficier d’un rabais famille et étudiant.
- Il est possible de bénéficier d’un rabais membre et famille.
- Il est possible d’avoir une carte mensuelle offrant l’accès gratuitement à ce film.
- Si une personne possède la carte membre et étudiante ainsi que le rabais famille, le
rabais membre et étudiant s’applique (car le rabais étudiant est plus grand).
Contraintes :
- Si la personne possède la carte mensuelle, il ne faut pas lui demander d’autres
informations.

Données à saisir par l’utilisateur :
L’utilisateur doit spécifier au programme les informations suivantes pour qu’il puisse
calculer le rabais qu’il va lui appliquer :
- Possession d’une carte mensuelle (Oui/Non)
- Possession d’une carte membre (Oui/Non)
- Possession d’une carte étudiante (Oui/Non)
- Forfait famille applicable (Oui/Non)
-
Résultats : Un message à afficher spécifiant le prix à payer.
"""

# variables
carte_mensuelle = False
carte_membre = False
carte_etudiant = False
forfait_famille = False
# prix_billet = 10

# demande des informations
carte_mensuelle = input("Possédez-vous une carte mensuelle ? (Oui/Non) ").lower() == "oui"
if not carte_mensuelle:
    carte_membre = input("Possédez-vous une carte membre ? (Oui/Non) ").lower() == "oui"
    carte_etudiant = input("Possédez-vous une carte étudiante ? (Oui/Non) ").lower() == "oui"
    forfait_famille = input("Possédez-vous un forfait famille ? (Oui/Non) ").lower() == "oui"

# calcul du prix
if carte_mensuelle:
    print("Le prix est de 0€")
elif carte_membre and carte_etudiant and forfait_famille:
    print("Le prix est de 5€")
elif carte_membre and carte_etudiant:
    print("Le prix est de 5€")
elif carte_membre and forfait_famille:
    print("Le prix est de 6€")
elif carte_etudiant and forfait_famille:
    print("Le prix est de 8€")
elif carte_membre:
    print("Le prix est de 7€")
elif carte_etudiant:
    print("Le prix est de 8€")
elif forfait_famille:
    print("Le prix est de 9€")
else:
    print("Le prix est de 10€")
