from random import randint

nb_allumettes_restante = 21
joueur_un = input("Entrez votre Pseudo (Joueur 1) :")
bot ="Bot"
joueur = joueur_un
print("====================================================================================")
print("Bienvenue,", joueur_un," ! :)" )
print("Il y a 21 allumettes.")

while True:
    if joueur == joueur_un :
        print("====================================================================================")
        nb_allumettes_enleve = int(input("Entrez un nombre d'allumette à retirer (3,2 ou 1) :"))

        if nb_allumettes_enleve != 3 and nb_allumettes_enleve != 2 and nb_allumettes_enleve != 1:
            print("====================================================================================")
            print("⚠ Erreur, vous n'avez pas entré un chiffre égal à 3, 2 ou 1 !")
            print("====================================================================================")
            break

        else :
            nb_allumettes_restante = nb_allumettes_restante - nb_allumettes_enleve
            print("Il reste", nb_allumettes_restante,"allumettes après votre tour.")

        if nb_allumettes_restante < 1:
            print("====================================================================================")
            print("Désolé mais", joueur, ", vous avez perdu (vous êtes descendu en bas de 1)...... Ressayez !")
            print("====================================================================================")
            break

        elif nb_allumettes_restante == 1:
            print("====================================================================================")
            print("Bravo à vous", joueur,",vous avez gagné ! :)")
            print("====================================================================================")
            break

        joueur = bot


    else:

        if nb_allumettes_restante == 4:
            nb_allumettes_enleve = 3
            nb_allumettes_restante -= nb_allumettes_enleve
            print("====================================================================================")
            print("Désolé mais", joueur_un, ", vous avez perdu, le BOT a gagné en retirant", nb_allumettes_enleve, "allumettes......... Ressayez !")
            print("====================================================================================")
            break


        elif nb_allumettes_restante == 3:
            nb_allumettes_enleve = 2
            nb_allumettes_restante -= nb_allumettes_enleve
            print("====================================================================================")
            print("Désolé mais", joueur_un, ", vous avez perdu, le BOT a gagné en retirant", nb_allumettes_enleve, "allumettes......... Ressayez !")
            print("====================================================================================")
            break

        elif nb_allumettes_restante == 2:
            nb_allumettes_enleve = 1
            nb_allumettes_restante -= nb_allumettes_enleve
            print("====================================================================================")
            print("Désolé mais", joueur_un, ", vous avez perdu, le BOT a gagné en retirant", nb_allumettes_enleve, "allumettes......... Ressayez !")
            print("====================================================================================")
            break
        
        elif nb_allumettes_restante > 4:
            nb_allumettes_enleve = randint(1,3)
            nb_allumettes_restante -= nb_allumettes_enleve
            print("====================================================================================")
            print("Le BOT a retiré", nb_allumettes_enleve,"allumettes, donc il reste", nb_allumettes_restante, "allumettes")
            


        joueur = joueur_un