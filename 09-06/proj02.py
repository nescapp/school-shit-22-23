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
carte_mensuelle = input(
    "Possédez-vous une carte mensuelle ? (Oui/Non) ").lower()
# On vérifie que l'utilisateur a bien entré oui ou non
carte_mensuelle = verify_input(carte_mensuelle)

if carte_mensuelle == "non":  # Si l'utilisateur n'a pas de carte mensuelle, on lui demande les autres informations
    carte_membre = input("Possédez-vous une carte membre ? (Oui/Non) ").lower()
    carte_membre = verify_input(carte_membre)
    carte_etudiant = input(
        "Possédez-vous une carte étudiante ? (Oui/Non) ").lower()
    carte_etudiant = verify_input(carte_etudiant)
    forfait_famille = input(
        "Possédez-vous un forfait famille ? (Oui/Non) ").lower()
    forfait_famille = verify_input(forfait_famille)

# calcul du prix
if carte_mensuelle == "oui":
    # Si l'utilisateur a une carte mensuelle, le prix est de 0€
    print("Le prix est de 0€")
elif carte_membre and carte_etudiant and forfait_famille:
    # Si l'utilisateur a une carte membre, une carte étudiante et un forfait famille, le prix est de 5€
    print("Le prix est de 5€")
elif carte_membre and carte_etudiant:
    # Si l'utilisateur a une carte membre et une carte étudiante, le prix est de 5€
    print("Le prix est de 5€")
elif carte_membre and forfait_famille:
    # Si l'utilisateur a une carte membre et un forfait famille, le prix est de 6€
    print("Le prix est de 6€")
elif carte_etudiant and forfait_famille:
    # Si l'utilisateur a une carte étudiante et un forfait famille, le prix est de 8€
    print("Le prix est de 8€")
elif carte_membre:
    # Si l'utilisateur a une carte membre, le prix est de 7€
    print("Le prix est de 7€")
elif carte_etudiant:
    # Si l'utilisateur a une carte étudiante, le prix est de 8€
    print("Le prix est de 8€")
elif forfait_famille:
    # Si l'utilisateur a un forfait famille, le prix est de 9€
    print("Le prix est de 9€")
else:
    # Si l'utilisateur n'a rien, le prix est de 10€
    print("Le prix est de 10€")
