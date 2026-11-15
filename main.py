taches = []

def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("La liste des tâches est vide.")
    else:
        print("Liste des tâches :")
        numero = 1

        for titre in taches:
            print(numero, "-", titre)
            numero = numero + 1


def rechercher_tache():
    mot_cle = input("Mot-clé à rechercher : ").strip().lower()

    if mot_cle == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
        return

    trouve = False
    numero = 1

    for titre in taches:
        if mot_cle in titre.lower():
            print(numero, "-", titre)
            trouve = True
        numero = numero + 1

    if not trouve:
        print("Aucune tâche ne contient ce mot-clé.")


def main():
    choix = ""

    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir, à bientôt !")
        else:
            print("Option invalide, veuillez choisir 1, 2, 3 ou 0.")


main()



