essance = 32.5
consommation = 5.0
distance = int(input("Entrer la distance de votre destination ou entrer 0 pour faire le plain : "))

if distance == 0:
    print("Vous avez fait le plein")
    print(f"Vous avez {essance} litres d'essance")
else:
    personne = int(input("Entrer le nombre de personne : "))

    # Calcul de la consommation
    consommation = consommation + (consommation * (personne * 0.3))

    # Calcul de la distance
    distance = distance * consommation

    # Calcul de la distance
    if distance > essance:
        print("Panne d'essence")
        print(f"Distance parcourue {essance / consommation}")
    else:
        print(f"Distance parcourue {distance / consommation}")


