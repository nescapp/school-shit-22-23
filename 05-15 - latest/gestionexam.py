import json
import os

def ConnectUser(mode):
    print('\033c')
    print('connecter utilisateur (l: login, s: signup, q: quitter): ', end='')
    action = input()
    if action == 'l':
        print('\033c')
        print('login')
        Login(mode)
    elif action == 's':
        print('\033c')
        print('signup')
        Signup(mode)
    elif action == 'q':
        print('\033c')
        exit()
    else:
        print('\033c')
        print('action inconnue')
        ConnectUser(mode)

def DefineMode():
    print('\033c')
    print('choisiser mode de gestion des examens (e: élève, p: prof, q: quitter): ', end='')
    action = input()
    if action == 'e':
        print('\033c')
        print('mode élève')
        return action
    elif action == 'p':
        print('\033c')
        print('mode prof')
        return action
    elif action == 'q':
        print('\033c')
        exit()
    else:
        print('\033c')
        print('mode inconnu')
        DefineMode()

def Login(mode):
    # check if users.json exists
    print('fuck you')
    Signup(mode)
    # try:
    #     users = json.load(open('users.json'))
    # except FileNotFoundError:
    #     users = {}
    #     print('erreur: pas de fichier users.json, créer un compte')
    #     Signup(mode)
    

def Signup(mode):

    if mode == 'e':
        print('créer compte élève')
    elif mode == 'p':
        print('créer compte prof')

    print('nom d\'utilisateur: ', end='')
    username = input()
    print('mot de passe: ', end='')
    password = input()
    with open(db, 'a') as f:
        # append username and password$
        

current_dir = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(current_dir, 'users.json')
mode = DefineMode()
ConnectUser(mode)
    