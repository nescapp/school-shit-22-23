import random # importe la librairie random pour pouvoir tirer des nombres aléatoires

def Verify_input(prompt, min, max): # vérifie que l'utilisateur rentre bien un nombre entre min et max
    inp = (input(prompt)) # demande à l'utilisateur de rentrer un nombre
    try :
        inp = int(inp) # on transforme la valeur en int
        if inp > max or inp < min: # si l'input est plus grand que le max ou plus petit que le min
            print("Veuillez entrer un nombre entre", min, "et", max) # on affiche un message d'erreur
            return Verify_input(prompt, min, max) # et on relance la fonction
    except ValueError: # si l'input n'est pas un nombre
        print("entrée invalide") # on affiche un message d'erreur
        return Verify_input(prompt, min, max) # et on relance la fonction
    return inp



def Loterie(gain:int): # fonction principale
    global nombre_chiffres, val_max
    if input("Appuyez sur entrée pour jouer ou écrivez 'exit' pour quitter : ").lower() != "exit":
        nombre_chiffres = Verify_input("Entrez le nombre de chiffres à cocher : ", 2, 10) 
        val_max = Verify_input("Entrez la valeur maximum des chiffres à cocher : ", 5, 50)
        ticket_joueur = Tirage_ticket()
        ticket_gagnant = Tirage_ticket()
        print("------------------------------")
        print("Votre ticket :", ticket_joueur)
        print("Ticket gagnant :", ticket_gagnant)
        print("------------------------------")
        if Gagnant(ticket_joueur, ticket_gagnant): # si le joueur gagne
            print("Vous avez remporté le prix de", "{:,}".format(gain), "€ !!! Félicitation !!")
        else: # si le joueur perd on double le gain
            print("Vous n'avez pas remporté le grand prix de", "{:,}".format(gain), f"€. Vous aurez plus de chance la prochaine fois. Vous aviez {Calcul_probabilite()}% de chance de remporter le gros lot.")
            Loterie(gain*2)
            
    else:
        print("Au revoir !")


def Tirage_ticket(): # fonction qui tire un ticket
    ticket = [random.randint(1, val_max) for i in range(nombre_chiffres)] # on tire un nombre aléatoire entre 1 et val_max pour chaque chiffre du ticket        
    ticket.sort()
    return ticket


def Gagnant(ticket_utilisateur:list, ticket_gagnant:list):
    return True if ticket_utilisateur == ticket_gagnant else False

def Calcul_probabilite(): # jsp comment calculer la probabilité
    return 0

Loterie(1000000)