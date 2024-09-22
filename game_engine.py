import random
with open ('word_list.txt') as file:
    words_list = file.read()
    words_list = words_list.split(",\n")

# Je récupère un mot aléatoire dans mon fichier word_list.txt
my_word = random.choice(words_list).upper() 

# Crée une liste de "_" de la longueur de word
def hidden_word(word): 
    hidden_word =[]
    for i in my_word:
        if len(my_word) != len(hidden_word):
            hidden_word.append("_")   
    return hidden_word


mot_cache = hidden_word(my_word)
print(' '.join(mot_cache))


def game():
    mot_trouve = False
    penalite = 0
    attempts = 0

    # Récupère le meilleur score 
    f = open("scores.txt", "r")
    best_score = int(f.read(2))
    f.close()

    while mot_trouve != True:
        enter = (input("rentre une lettre ou le mot : "))
        enter = enter.upper()
        attempts+=1
        print("Tu es à {} esssais".format(attempts))

        if len(enter)==1:
            if enter in my_word:
                for position,lettre in enumerate(my_word):
                    if lettre == enter:
                        mot_cache[position] = enter
                        penalite += 1
                        print(f"{enter} est bien dans le mot, pénalité = {penalite}")
                        print(' '.join(mot_cache))
            else:
                penalite+=3
                print(f"{enter} n'est pas dans le mot et pénalité = {penalite}")
                print(' '.join(mot_cache))
        elif len(enter)==len(my_word):
            if enter== my_word :
                mot_trouve = True
                if attempts < best_score:
                    # Je mets à jour le meilleur score
                    f = open("scores.txt", "w")
                    f.write(str(attempts))
                    f.close()
                    print("Best ever!!! Vous avez trouvé {} en {} d'essais.".format(my_word,attempts))
                else:
                    print("Bravo vous avez trouvé {} en {} d'essais. Le record est de {} essais.".format(my_word,attempts,best_score))
            else :
                mot_trouve = False
                penalite+=5
                print(f"{enter} n'est pas le bon mot et pénalité = {penalite}")
                print(' '.join(mot_cache))
        else :
            penalite+=5
            print(f"{enter} est incorrecte et pénalité = {penalite}")
            print(' '.join(mot_cache))

        if "_" not in mot_cache:
            mot_trouve=True
            if attempts < best_score:
                f = open("scores.txt", "w")
                f.write(str(attempts))
                f.close()
                print("Best ever!!! Vous avez trouvé {} en {} d'essais.".format(my_word,attempts))
            else:
                print("Bravo vous avez trouvé {} en {} d'essais. Le record est de {} essais.".format(my_word,attempts,best_score))
    
# Lance le jeu
game()