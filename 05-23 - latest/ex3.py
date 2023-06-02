with open('animeaux.txt', 'w') as f:
    f.write('chien\ncheval\nchat\nsouris\nrat\nlapin\ncochon\nmouton\nvache\npoule\ncoq\ncanard\noie\nchevre\nelephant\nhippopotame\nrhinoceros\nlion\ntigre\nours\nloup\nrenard\nsinge\npanda\nkangourou\ngirafe\nzebre\nantilope\nmarmotte\nchameau\nlama\nalpaga\nchinchilla\nfuret\nherisson\necureuil\nbelette\nblaireau\nraton-laveur\nparesseux\nkoala\nornithorynque\nperroquet\nperruche\ngeai\npie\nmerle\nmoineau\npigeon\nhibou\naigle\nfaucon\nvautour\npoussin\npoulet\ncoquelet')

with open('animeaux.txt', 'r') as f:
    liste = f.readlines()
    liste.sort(key=len)

print(f"Le mot le plus court est: {liste[0]}")
print(f"Le mot le plus long est: {liste[-1]}")