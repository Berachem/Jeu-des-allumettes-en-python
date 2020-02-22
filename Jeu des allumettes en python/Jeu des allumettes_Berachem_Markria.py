nb_allumettes_restante = 21
joueur_un = input("Entrez votre Pseudo (Joueur 1) :")
joueur_deux = input("Entrez votre Pseudo (Joueur 2) :")
joueur = joueur_un
print("===============================================================================================")
print("Bienvenue,", joueur_un,"et" ,joueur_deux, "! :)" )
print("Il y a 21 allumettes.")

while True:
  print("========================================Tour de", joueur, "========================================")
  nb_allumettes_enleve = int(input("Entrez un nombre d'allumette à retirer (3,2 ou 1) :"))

  if nb_allumettes_enleve != 3 and nb_allumettes_enleve != 2 and nb_allumettes_enleve != 1:
    print("====================================================================================================")
    print(" ⚠ Erreur, vous n'avez pas entré un chiffre égal à 3, 2 ou 1 !")
    print("===============================================================================================")
    break

  else :
    nb_allumettes_restante = nb_allumettes_restante - nb_allumettes_enleve
    

    if nb_allumettes_restante < 1:
      print("====================================================================================================")
      print("Désolé mais", joueur, ", vous avez perdu (vous êtes descendu en bas de 1)...... Ressayez !")
      print("====================================================================================================")
      break

    elif nb_allumettes_restante == 1:
      print("====================================================================================================")
      print("Bravo à vous", joueur,",vous avez gagné ! :)")
      print("====================================================================================================")
      break

    print("Il reste", nb_allumettes_restante,"allumettes")

    if joueur == joueur_un:
      joueur = joueur_deux

    else:
      joueur = joueur_un
