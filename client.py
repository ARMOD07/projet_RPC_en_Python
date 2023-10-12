import Pyro4
import os

# Récupère l'objet de serveur de fichiers à partir de son URI
uri = input("URI du serveur : ").strip()
 
#connecter au serveur
projet = Pyro4.Proxy(uri)

# Boucle principale du programme
while True:
    print("Menu:")
    print("1. Lister les fichiers/répertoires")
    print("2. Créer un fichier")
    print("3. Supprimer un fichier")
    print("4. Créer un répertoire")
    print("5. Supprimer un répertoire")
    print("6. Ajouter des données à un fichier")
    print("0. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        path = input("Entrez un chemin : ")
        
        # Appel à la méthode list_fichier du serveur
        file_list = projet.list_fichier(path)
        
        # Vérifie si le chemin existe
        if os.path.exists(path):
            print(f"Le chemin {path} existe.")
        else:
            print(f"Le chemin {path} n'existe pas.")
        
        # Affiche la liste des fichiers et répertoires
        for file_name in file_list:
            print(file_name)

    elif choix == "2":
        path = input("Chemin pour créer un fichier : ")
        
        # Vérifie si le chemin n'existe pas
        if not os.path.exists(path):
            projet.cree_fichier(path)
        else:
            print(f"Le répertoire {path} existe déjà.")

    elif choix == "3":
        path = input("Chemin pour supprimer un fichier : ")
        
        # Vérifie si le fichier existe
        if not os.path.exists(path):
            print(f"Le fichier {path} n'existe pas.")
        else:
            # Appel à la méthode supprimer_fichier du serveur
            projet.supprimer_fichier(path)

    elif choix == "4":
        path = input("Chemin pour créer un répertoire : ")
        
        # Vérifie si le chemin n'existe pas
        if not os.path.exists(path):
            projet.cree_repertoir(path)
        else:
            print(f"Le répertoire {path} existe déjà.")

    elif choix == "5":
        path = input("Chemin pour supprimer un répertoire : ")
        
        # Vérifie si le répertoire existe
        if not os.path.exists(path):
            print(f"Le répertoire {path} n'existe pas.")
        else:
            # Appel à la méthode supprimer_repertoir du serveur
            projet.supprimer_repertoir(path)

    elif choix == "6":
        path = input("Chemin du fichier pour les données : ")
        
        # Vérifie si le fichier existe
        if not os.path.exists(path):
            print(f"Le fichier {path} n'existe pas.")
        else:
            data = input("Données à ajouter : ")
            # Appel à la méthode ajouter_des_donnee du serveur
            projet.ajouter_des_donnee(path, data)

    elif choix == "0":
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
