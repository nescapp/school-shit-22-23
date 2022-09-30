essance = 32.5
distance = int(input("Entrer la distance de votre destination ou entrer 0 pour faire le plain : "))
consommation = 5 * distance / 100

if distance == 0:
    print("- - - Vous avez fait le plein - - -")
    print(f"Vous avez {essance} litres d'essance")
else:
    personne = int(input("Entrer le nombre de personnes : "))
    consommation += (consommation * (personne * 0.3))
    distance *= consommation

    if distance > essance:
        print("- - - Panne d'essence - - -")
        print(f"Distance parcourue {essance / consommation}")
    else:
        print(f"Distance parcourue {distance / consommation}")

