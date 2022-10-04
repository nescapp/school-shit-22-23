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
    print(f"{articles.index(group) + 1}. {group[0]} : {'{:.2f}'.format(group[1])} €")  # affiche 2 décimales après la virgule

print("- - - - - - - - - - - - - - - - -")
monnaie = float(input("Veuillez introduire votre monnaie : "))
produit = int(input("Veuillez selectionner un produit : "))
monnaierendue = round(monnaie-articles[produit-1][1], 2)  # calcul de la monnaie à rendre avec arrondis
if monnaierendue < 0:
    print("monnaie insuffisante")  # vérifie si la monnaie est suffisante
    print(f"Monnaie à rendre : {'{:.2f}'.format(monnaie)} €")
else:
    print(f"Produit sélectionné : {articles[produit - 1][0]}")
    if monnaierendue != 0:
        print(f"Monnaie à rendre : {'{:.2f}'.format(monnaierendue)} €")  # n'affiche pas la monnaie à rendre si elle est nulle
    print("Servi, bonne santé")