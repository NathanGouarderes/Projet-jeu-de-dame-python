jsonJoueurs = open("TableauJoueurs.json", "r")
print(jsonJoueurs.read())
jsonJoueurs.close()
jsonJoueurs = open("TableauJoueurs.json", "w")
jsonJoueurs.write('')
jsonJoueurs.close()
print('Ta race est finie, tu peux passer à la suivante !')