"""
Crée un programme qui ouvre le fichier animeaux.txt et qui affiche le mot le plus court et le plus long.

"""

with open('animeaux.txt', 'r') as f:
    liste = f.readlines()
    liste.sort(key=len)

print(f"Le mot le plus court est: {liste[0]}")
print(f"Le mot le plus long est: {liste[-1]}")