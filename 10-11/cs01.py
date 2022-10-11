"""
On souhaite réaliser un simulateur de gestion de stock de chaussures dans un magasin dont
un exemple de la liste des articles est représenté dans le tableau ci-dessous :



Les fonctionnalités du simulateur de gestion de stock de chaussures sont décrites ci-
dessous :

- Afficher sous forme de menu numéroté les actions suivantes proposées à l’utilisateur
;
➢ 1 : Afficher les articles pour une pointure
➢ 2 : Afficher les articles présents plusieurs fois
➢ 3 : Afficher les articles pour chaque pointure
➢ 4 : Afficher la pointure la plus présente
➢ 5 : Afficher le nombre de fois la pointure la plus présente
➢ 6 : Afficher l’article le plus cher
➢ 0 : Quitter le programme
- Le menu s’affiche tant que l’utilisateur ne quitte pas le programme ;
- Afficher un message en cas de choix inexistant ;
- Explications détaillées :
→ L’action 1 demande une pointure à l’utilisateur et lui affiche le nom des
chaussures disponibles dans cette pointure.
→L’action 2 affiche tous les articles (nom du modèle + pointure) présents plusieurs
fois dans le catalogue.
→L’action 3 affiche pour chaque pointure les chaussures disponibles.
→L’action 4 affiche la pointure qui est la plus représentée dans le catalogue.
→L’action 5 affiche le nombre de fois qu’apparait l’article le plus présent dans le
catalogue.

2

Nom
Prénom 11/10/202
→L’action 6 affiche l’article le plus cher et son prix.
→L’action 0 quitte le programme.

Travail à faire :
- Afficher le tableau ci-dessous présentant les articles de chaussures de sport :
- Suggérer les différents tests permettant de vérifier le bon déroulement du
programme.
"""

stock = [
    ["Article", "Pointure", "Prix"],
    ["Asics Gel 2000", 42, 119],
    ["Asics Gel 2000", 39, 119],
    ["Mizuno Wave Rider", 38, 129],
    ["Nike Air Zoom", 42, 125],
    ["Mizuno Wave Plus", 39, 83.40],
    ["Mizuno Wave Plus", 40, 83.40],
    ["Mizuno Wave Plus", 41, 83.40],
    ["Merrell Poseidon", 39, 118.30],
]

def main():
    print("""
    Bienvenue dans le gestionnaire de stock de chaussures
    
    1 : Afficher les articles pour une pointure
    2 : Afficher les articles présents plusieurs fois / pas encore fait
    3 : Afficher les articles pour chaque pointure
    4 : Afficher la pointure la plus présente
    5 : Afficher le nombre de fois la pointure la plus présente / pas encore fait
    6 : Afficher l’article le plus cher
    0 : Quitter le programme

    """)

    choix = int(input("Votre choix : "))
    if choix == 1:
        print(" - - - - - - - - - - - - - - - - - - - ")
        pointure = int(input("Entrez une pointure : "))
        j = 1
        for i in range(1, len(stock)):
            if stock[i][1] == pointure:
                print(f"{j}. {stock[i][0]} ({stock[i][1]}) \t {stock[i][2]}€")
                j += 1
        if j == 1:
            print("Aucun article trouvé")
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 2:
        print("Afficher les articles présents plusieurs fois")
        print(" - pas encore fait")
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 3:
        print(" - - - - - - - - - - - - - - - - - - - ")
        j = 1
        for i in range(1, len(stock)):
            print(f"{j}. {stock[i][0]} ({stock[i][1]}) \t {stock[i][2]}€")
            j += 1
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 4:
        print("Afficher la pointure la plus présente")
        print(" - - - - - - - - - - - - - - - - - - - ")
        # TODO : UTILISER DICTIONNAIRE
        frequence_pointure = []
        for i in range(1, len(stock)):
            frequence_pointure.append(stock[i][1])
        print("La pointure la plus présente est la pointure", max(set(frequence_pointure), key=frequence_pointure.count))
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 5:
        print("Afficher le nombre de fois la pointure la plus présente")
        print(" - pas encore fait")
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 6:
        print(" - - - - - - - - - - - - - - - - - - - ")
        prix_max = 0
        for i in range(1, len(stock)):
            if stock[i][2] > prix_max:
                modele = stock[i][0]
                pointure = stock[i][1]
                prix_max = stock[i][2]
        print(f"Le modèle le plus cher est {modele} ({pointure}) à {prix_max}€")
        input("\nAppuyez sur Entrée pour continuer...")
        main()
    elif choix == 0:
        print("Quitter le programme")
    else:
        print("Choix inexistant")
        input("\nAppuyez sur Entrée pour continuer...")
        main()


main()