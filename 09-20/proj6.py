import random

def Verify_input(prompt, min, max):
    inp = (input(prompt))
    try :
        inp = int(inp)
        if inp > max or inp < min: # ????
            print("Veuillez entrer un nombre entre", min, "et", max)
            return Verify_input(prompt, min, max)
    except ValueError:
        print("entrée invalide")
        return Verify_input(prompt, min, max)
    return inp



def Loterie(gain:int):
    global nombre_chiffres, val_max
    if input("Appuyez sur entrée pour jouer ou écrivez 'exit' pour quitter : ").lower() == "":
        nombre_chiffres = Verify_input("Entrez le nombre de chiffres à cocher : ", 2, 7)
        val_max = Verify_input("Entrez la valeur maximum des chiffres à cocher : ", 10, 50)
        ticket_joueur = Tirage_ticket()
        ticket_gagnant = Tirage_ticket()
        print("------------------------------")
        print("Votre ticket :", ticket_joueur)
        print("Ticket gagnant :", ticket_gagnant)
        print("------------------------------")
        if Gagnant(ticket_joueur, ticket_gagnant):
            print("Vous avez remporté le prix de", "{:,}".format(gain), "€ !!! Félicitation !!")
        else:
            print("Vous n'avez pas remporté le grand prix de", "{:,}".format(gain), f"€. Vous aurez plus de chance la prochaine fois. Vous aviez {Calcul_probabilite()}% de chance de remporter le gros lot.")
            Loterie(gain*2)
            
    else:
        print("Au revoir !")


def Tirage_ticket():
    global nombre_chiffres, val_max
    ticket = []
    for i in range(nombre_chiffres):
        ticket.append(random.randint(1, val_max))
    ticket.sort()
    return ticket


def Gagnant(ticket_utilisateur:list, ticket_gagnant:list):
    if ticket_utilisateur == ticket_gagnant:
        return True
    else:
        return False


def Calcul_probabilite(): # jsp comment calculer la probabilité
    return 0

Loterie(1000000)