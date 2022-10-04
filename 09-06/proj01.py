# articles (article, prix)
articles = [
    ["Eau", 1.90],
    ["Coca-cola", 2.90],
    ["Fanta", 2.00],
    ["Ice Tea", 3.30],
    ["Chips paprika", 1.20],
    ["Fromage", 1.90]
]

print("Bienvenue, Voici notre selection de produits : ")
print("- - - - - - - - - - - - - - - - -")
# affichage des articles
for group in articles:
    # affiche 2 décimales après la virgule
    print(
        f"{articles.index(group) + 1}. {group[0]} : {'{:.2f}'.format(group[1])} €")

print("- - - - - - - - - - - - - - - - -")
monnaie = float(input("Veuillez introduire votre monnaie : "))
produit = int(input("Veuillez selectionner un produit : "))
# calcul de la monnaie à rendre avec arrondis
monnaierendue = round(monnaie-articles[produit-1][1], 2)
if monnaierendue < 0:
    print("monnaie insuffisante")  # vérifie si la monnaie est suffisante
    print(f"Monnaie à rendre : {'{:.2f}'.format(monnaie)} €")
else:
    print(f"Produit sélectionné : {articles[produit - 1][0]}")
    if monnaierendue != 0:
        # n'affiche pas la monnaie à rendre si elle est nulle
        print(f"Monnaie à rendre : {'{:.2f}'.format(monnaierendue)} €")
    print("Servi, bonne santé")
