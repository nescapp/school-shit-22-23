"""

1. Écrire une application demandant à l'utilisateur de répondre aux différentes questions par

un oui ou par un non.

Vous devez dès lors, créer une seule fonction permettant de renvoyer la réponse à l'écran à

chaque question demandée à l'utilisateur.

Les questions sont les suivantes :

Partez-vous en vacance cet été ?

Partez-vous en avion ?

Avez-vous des enfants ?

Avez-vous des animaux domestiques ?


2. Créer une application dans laquelle la fonction renvoie la multiplication de cinq nombres

fournis en argument.

Les nombres devront être fournis par l'utilisateur dans le programme principal.


3. Créer une application dans laquelle la fonction renvoie le nombre de consonnes contenues

dans une chaîne de caractères passée en argument.

Les consonnes devront être fournies par l'utilisateur dans le programme principal.
"""


def question(prompt:str):

    while True:
        rep = input(f"{prompt} (Oui/Non) : ")
        if rep.lower() in ("oui", "non"):

            break
    return rep
    

def multiplication(n1, n2, n3, n4, n5):

    print("Le résultat de la multiplication est :", n1 * n2 * n3 * n4 * n5)


def consonnes(mot:str):
    consonnes = 0
    for letter in mot:
        if letter not in "aeiouy":
            consonnes += 1

    print("Le nombre de consonnes est :", consonnes)


question("Partez-vous en vacance cet été ?")
question("Partez-vous en avion ?")
question("Avez-vous des enfants ?")
question("Avez-vous des animaux domestiques ?")

multiplication(
    int(input("Entrez nombre n°1 : ")), 
    int(input("Entrez nombre n°2 : ")), 
    int(input("Entrez nombre n°3 : ")), 
    int(input("Entrez nombre n°4 : ")), 
    int(input("Entrez nombre n°5 : ")))

consonnes(input("Entrez un mot : "))

