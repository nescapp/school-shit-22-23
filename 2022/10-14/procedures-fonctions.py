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

