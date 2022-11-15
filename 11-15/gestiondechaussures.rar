stock = [
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
    2 : Afficher les articles présents plusieurs fois
    3 : Afficher les articles pour chaque pointure
    4 : Afficher la pointure la plus présente
    5 : Afficher le nombre de fois la pointure la plus présente
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
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
    elif choix == 2:
        # print all articles with more than one size
        for i in range(1, len(stock)):
            if stock[i][0] == stock[i-1][0]:
                print(f"{stock[i][0]} ({stock[i][1]}) \t {stock[i][2]}€")
            if stock[i][0] == stock[i-1][0] and stock[i][0] != stock[i-2][0]:
                print(f"{stock[i-1][0]} ({stock[i-1][1]}) \t {stock[i-1][2]}€")
        
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
    elif choix == 3:
        print(" - - - - - - - - - - - - - - - - - - - ")
        j = 1
        for i in range(1, len(stock)):
            print(f"{j}. {stock[i][0]} ({stock[i][1]}) \t {stock[i][2]}€")
            j += 1
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
    elif choix == 4:
        print("Afficher la pointure la plus présente")
        print(" - - - - - - - - - - - - - - - - - - - ")
        frequence_pointure = []
        for i in range(1, len(stock)):
            frequence_pointure.append(stock[i][1])
        print("La pointure la plus présente est la pointure", max(set(frequence_pointure), key=frequence_pointure.count))
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
    elif choix == 5:
        frequence_article = []
        for i in range(1, len(stock)):
            frequence_article.append(stock[i][0])
        print(f"L'article le plus présent ('{max(set(frequence_article), key=frequence_article.count)}') apparait {frequence_article.count(max(set(frequence_article), key=frequence_article.count))} fois")
        
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
        
        input("\nAppuyez sur [Entrée] pour continuer...")
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
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()
    elif choix == 0:
        print("Quitter le programme")
    else:
        print("Choix inexistant")
        input("\nAppuyez sur [Entrée] pour continuer...")
        main()

main()