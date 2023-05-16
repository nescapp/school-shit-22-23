import json
import os
import getpass
import msvcrt

def ResetUsers():
    """Fonction qui permet de réinitialiser le fichier users.json"""
    open(db, 'w').close()
    CreateNewUser('eleve', 'eleve', 'e')
    CreateNewUser('prof', 'prof', 'p')
    print('utilisateurs réinitialisés')
    DefineMode()

def UserList():
    """Fonction qui permet d'afficher la liste des utilisateurs"""
    if os.stat(db).st_size != 0:
        # Si le fichier n'est pas vide
        for user in users:
            # Afficher le nom d'utilisateur et le type
            print(f'{user} - ', end='')
            if users[user]['type'] == 'e':
                print('\033[93mélève\033[0m')
            elif users[user]['type'] == 'p':
                print('\033[94mprof\033[0m')
        DefineMode() # retourner au menu principal
    else:
        print('aucun utilisateur')
        DefineMode() # retourner au menu principal

def GetPassword():
    password = ""
    print('\033[2m', end='')
    while True:
        ch = msvcrt.getch().decode('utf-8')
        if ch == '\r' or ch == '\n':
            print('\033[0m\n', end='')
            break
        elif ch == '\b' and len(password) > 0:
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += ch
            print('*', end='', flush=True)
    return password

def VerifyUserExistance(username):
    """Fonction qui permet de vérifier si un utilisateur existe"""
    # vérifier si le fichier est vide
    if os.stat(db).st_size != 0:
        # vérifier si l'utilisateur existe déjà
        with open(db, 'r') as file:
            users = json.load(file)
        if username in users:
            return True
        else:
            return False
    else:
        return False

def VerifyPassword(username, password):
    """Fonction qui permet de vérifier si le mot de passe est correct"""
    with open(db, 'r') as file:
        users = json.load(file)
    if username in users:
        if password == users[username]['password']:
            return True
        else:
            return False
    else:
        return False
    

def CreateNewUser(username, password, type):
    # vérifier si le fichier est vide
    if os.stat(db).st_size == 0:
        # si oui, créer le dictionnaire
        users = {}
    else:
        # vérifier si l'utilisateur existe déjà
        with open(db, 'r') as file:
            users = json.load(file)
        if username in users:
            print("erreur: Ce nom d'utilisateur existe déjà.")
            return
    
    users[username] = {
        "password": password,
        "type": type
    }

    with open(db, 'w') as file:
        json.dump(users, file, indent=4)

    print("Compte créé avec succès")

def ConnectUser(mode):
    """Fonction qui permet de connecter un utilisateur soit par un login soit par un signup"""
    # titre: connecter utilisateur
    if mode == 'e':
        print('connecter utilisateur \033[93mélève\033[0m (\'l\': login, \'s\': signup, \'r\': retour, \'q\': quitter): ', end='')
    elif mode == 'p':
        print('connecter utilisateur \033[94mprof\033[0m (\'l\': login, \'s\': signup, \'r\': retour, \'q\': quitter): ', end='')

    action = input().lower() # récupérer l'action de l'utilisateur
    
    if action == 'l':
        Login(mode)
    elif action == 's':
        Signup(mode)
    elif action == 'r':
        mode = DefineMode()
    elif action == 'q':
        # nettoyer l'écran et quitter le programme
        print('\033c')
        exit()
    else:
        # action inconnue, tentative de connexion à nouveau
        print('\033c')
        print('action inconnue')
        ConnectUser(mode)

def DefineMode():
    """Fonction qui permet de définir le mode de gestion des examens"""
    # titre: choisir mode de gestion des examens
    print('choisiser mode de gestion des examens (\'e\': élève, \'p\': prof, \'x\':reset, \'l\':liste, \'q\': quitter): ', end='')
    action = input().lower() # récupérer l'action de l'utilisateur
    
    if action == 'e':
        print('\033[93m[mode élève]\033[0m')
        ConnectUser(action)
    elif action == 'p':
        print('\033[94m[mode prof]\033[0m')
        ConnectUser(action)
    elif action == 'x':
        ResetUsers()
    elif action == 'l':
        UserList()
    elif action == 'q':
        # nettoyer l'écran et quitter le programme
        print('\033c')
        exit()
    else:
        # action inconnue, tentative de sélection de mode à nouveau
        DefineMode()


def Login(mode):
    """Fonction qui permet de connecter un utilisateur à son compte"""
    # titre: se connecter à son compte
    if mode == 'e':
        print('\033[93m[se connecter à son compte élève]\033[0m')
    elif mode == 'p':
        print('\033[94m[se connecter à son compte prof]\033[0m')

    print('\'r\': retour')

    # vérifier si le fichier est vide
    if os.stat(db).st_size == 0:
        print('aucun utilisateur n\'existe')
        ConnectUser(mode)

    # saisie du nom d'utilisateur
    while True:
        print('nom d\'utilisateur: ', end='')
        username = input().lower()
        # had an error here once, not sure why
        if username == 'r':
            ConnectUser(mode)
        elif not VerifyUserExistance(username):
            print('erreur: ce nom d\'utilisateur n\'existe pas')
        else:
            break

    # saisie du mot de passe, problème ici quelque part
    while True:
        action = None

        print('mot de passe: ', end='')
        password = GetPassword()
        if VerifyPassword(username, password):
            break
        else:
            print('\033[95merreur: mot de passe incorrect\033[0m')
            while True:
                print('(\'r\': réessayer, \'m\': menu principal): ', end='')
                action = input().lower()

                if action == 'r' or action == 'm':
                    break

        if action == 'r':
            # rester dans la boucle si l'utilisateur veut réessayer
            continue
        elif action == 'm':
            # retourner au menu principal si l'utilisateur veut retourner au menu principal
                ConnectUser(mode)
        else:
            # peut être inutile
            break
            
def Signup(mode):
    """Fonction qui permet de créer un compte"""
    # titre: créer un compte
    if mode == 'e':
        print('\033[93m[créer compte élève]\033[0m')
    elif mode == 'p':
        print('\033[94m[créer compte prof]\033[0m')

    print('\'r\': retour')
    # procédure de création de compte

    # saisie du nom d'utilisateur
    while True:
        print('nom d\'utilisateur: ', end='')
        username = input().lower()
        if username == 'r':
            ConnectUser(mode)
        elif len(username) < 4:
            print('erreur: le nom d\'utilisateur doit faire au moins 4 caractères')
        elif VerifyUserExistance(username):
            print('erreur: ce nom d\'utilisateur existe déjà')
            ConnectUser(mode)
        else:
            break

    # saisie du mot de passe
    while True:
        password = None
        password_confirm = None
        action = None

        while True:
            # demander le mot de passe tant qu'il ne correspond pas aux critères
            print('mot de passe: ', end='')
            password = GetPassword()
            if len(password) < 4:
                print('erreur: le mot de passe doit faire au moins 4 caractères')
            else:
                break

        while True:
            # demander la confirmation du mot de passe tant qu'il ne correspond pas au mot de passe
            print('confirmer mot de passe: ', end='')
            password_confirm = GetPassword()
            if password_confirm != password:
                print('\033[95mles mots de passe ne correspondent pas!\033[0m')
                while True:
                    print('(\'r\': réessayer, \'d\': redéfinir, \'m\': menu principal): ', end='')
                    action = input().lower()

                    if action == 'r' or action == 'd' or action == 'm':
                        break

                if action == 'r':
                    # rester dans la boucle si l'utilisateur veut réessayer
                    continue
                elif action == 'd':
                    # sortir de la boucle si l'utilisateur veut redéfinir le mot de passe
                    break
                elif action == 'm':
                    # retourner au menu principal si l'utilisateur veut retourner au menu principal
                    ConnectUser(mode)
            else:
                # Les mots de passe correspondent, sortir de la boucle de confirmation
                break

        if action == 'd':
            # rester si l'utilisateur veut redéfinir le mot de passe
            continue
        else:
            # sortir si aucune action n'a été prise et donc les mots de passe correspondent
            break

    CreateNewUser(username, password, mode)

    
# nettoyer l'écran
print('\033c') 

# définir le chemin du fichier users.json
current_dir = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(current_dir, 'users.json')

# s'assurer que le fichier users.json existe
if not os.path.exists(db):
    # créer le fichier s'il n'existe pas
    open(db, 'w').close()
else:
    # s'assurer que le fichier n'est pas vide
    if not os.stat(db).st_size == 0:
        # organiser le fichier en mettant tous les utilisateurs de type prof en premier
        with open(db, 'r') as file:
            users = json.load(file)
        users = dict(sorted(users.items(), key=lambda item: item[1]['type'], reverse=True))
        with open(db, 'w') as file:
            json.dump(users, file, indent=4)
    else:
        # si le fichier est vide, le remplir avec un dictionnaire vide
        open(db, 'w').close()

# définir le mode de gestion des examens
mode = DefineMode()
