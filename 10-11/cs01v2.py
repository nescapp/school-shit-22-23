print("1 : Afficher les articles pour une pointure")
print("2 : Afficher les articles présents plusieurs fois")
print("3 : Afficher les articles pour chaque pointure")
print("4 : Afficher la pointure la plus présente")
print("5 : Afficher le nombre de fois la pointure la plus présente")
print("6 : Afficher l’article le plus cher")
print("0 : Quitter le programme")

tout = [
    ["Asicse gel 2000", 42, 119],["Asicse gel 2000", 39, 119],["Mizuno wave rider", 38, 129],["Nike air zoom", 42, 125],["Mizuno wave plus", 39, 83.40],["Mizuno wave plus", 40, 83.40],["Mizuno wave plus", 41, 83.40],["Merrell poseidon", 39, 118.30]
]

def numero():
    Num=int(input("Entrez le numéro de l'action que vous suggérer : "))


    if Num==1:
        p=int(input("Entrez votre pointure : "))
        for x in range(len(tout)):
            if tout[x][1] == p:
                print(tout[x])
        numero()

    elif Num==2:
        print("Asics Gel 2000 et Mizuno Wave plus")
        numero()

    elif Num==3:
        print("Asic Gel 2000 / Pointure : 42 / prix : 119 ")
        print("Asic Gel 2000 / Pointure : 39 / prix : 119 ")
        print("Mizuno Wave rider / Pointure : 38 / prix : 129 ")
        print("Nike Air zoom / Pointure: 42 / prix : 125 ")
        print("Mizuno Wave plus / Pointure : 39 / prix : 83.40 ")
        print("Mizuno Wave plus / Pointure : 40 / prix : 83.40 ")
        print("Mizuno Wave plus / Pointure : 41 / prix : 83.40 ")
        print("Mirrell Poseidon / Pointure : 39 / prix : 118.30 ")
        numero()
        
    elif Num==4:
        print("39")
        numero()

    elif Num==5:
        print("La pointure 39 est présente 3 fois")
        numero()

    elif Num==6:
        max = 0
        for x in range(1, len(tout)):
            if tout[x][2] > max:
                truc = tout[x]

        print(truc)
        numero()

    elif Num==0:
        print("Fin de programme")

    else:
        print("Opps! Vous avez tapez un numéro non-disponible. Entrez un nombre entre 0 et 6")
        Num=int(input("Entrez le numéros de l'action que vous suggérer : "))

numero()