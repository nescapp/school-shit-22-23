"""
Objectif
Programme simulant un distributeur de boissons
Consignes
➢ Réaliser un Distributeur de boissons
➢ La solution devra se présenter comme l’exemple de sortie ci-dessous.
➢ Sauvegarder sous le nom CS_Fevrier_Nom_Prenom_Classe_groupe
Données
- Un montant entré par l’utilisateur
- Un numéro d’article entré par l’utilisateur
Indications
Le distributeur comporte :
- Eau à 1.90 €
- Coca-cola à 2.90 €
- Fanta à 2.00 €
- Ice Tea à 3.30 €
- Chips paprika à 1.20 €
- Fromage à 1.90 €
Résultats
- Un message confirmant ou annulant la transaction
- Un message indiquant la monnaie rendue si existante
- Un message indiquant le produit vendu et souhaitant un une bonne santé/appétit !
"""


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