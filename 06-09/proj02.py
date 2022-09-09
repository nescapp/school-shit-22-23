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
# Début du programme
carte_mensuelle = False
carte_membre = False
carte_etudiant = False
forfait_famille = False

# Verification des données saisies par l'utilisateur
def verify_input(user_input):
    while not user_input == "oui" and not user_input == "non":
        user_input = input("Veuillez entrer oui ou non : ").lower()
    return user_input

# Verification de la carte mensuelle
carte_mensuelle = input("Possédez-vous une carte mensuelle ? (Oui/Non) ").lower()
carte_mensuelle = verify_input(carte_mensuelle) # On vérifie que l'utilisateur a bien entré oui ou non

if carte_mensuelle == "non": # Si l'utilisateur n'a pas de carte mensuelle, on lui demande les autres informations
    carte_membre = input("Possédez-vous une carte membre ? (Oui/Non) ").lower()
    carte_membre = verify_input(carte_membre)
    carte_etudiant = input("Possédez-vous une carte étudiante ? (Oui/Non) ").lower()
    carte_etudiant = verify_input(carte_etudiant)
    forfait_famille = input("Possédez-vous un forfait famille ? (Oui/Non) ").lower()
    forfait_famille = verify_input(forfait_famille)

# calcul du prix
if carte_mensuelle == "oui":
    print("Le prix est de 0€") # Si l'utilisateur a une carte mensuelle, le prix est de 0€
elif carte_membre and carte_etudiant and forfait_famille:
    print("Le prix est de 5€") # Si l'utilisateur a une carte membre, une carte étudiante et un forfait famille, le prix est de 5€
elif carte_membre and carte_etudiant:
    print("Le prix est de 5€") # Si l'utilisateur a une carte membre et une carte étudiante, le prix est de 5€
elif carte_membre and forfait_famille:
    print("Le prix est de 6€") # Si l'utilisateur a une carte membre et un forfait famille, le prix est de 6€
elif carte_etudiant and forfait_famille:
    print("Le prix est de 8€") # Si l'utilisateur a une carte étudiante et un forfait famille, le prix est de 8€
elif carte_membre:
    print("Le prix est de 7€") # Si l'utilisateur a une carte membre, le prix est de 7€
elif carte_etudiant:
    print("Le prix est de 8€") # Si l'utilisateur a une carte étudiante, le prix est de 8€
elif forfait_famille:
    print("Le prix est de 9€") # Si l'utilisateur a un forfait famille, le prix est de 9€
else:
    print("Le prix est de 10€") # Si l'utilisateur n'a rien, le prix est de 10€
