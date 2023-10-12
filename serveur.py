import os
import Pyro4


# Définit la classe de serveur de fichiers
@Pyro4.expose   # Décorateur pour rendre la méthode accessible via Pyro4
class projet(object):
    # Méthode pour lister les fichiers/répertoires dans un chemin donné
    def list_fichier(self, path):
        # Vérifie si le chemin existe
        if not os.path.exists(path): 
            raise ValueError("Chemin invalide")

        # Liste les fichiers/répertoires et renvoie les noms
        # Si le chemin est valide, la fonction utilise os.listdir(path) pour obtenir une liste des fichiers et des répertoires présents dans le chemin spécifié.
        # Cette fonction renvoie simplement les noms des fichiers et répertoires, sans informations supplémentaires telles que les chemins complets ou les métadonnées des fichiers.
        
        
          # Renvoi des noms :
    # Une fois que la liste des fichiers et répertoires est obtenue, la fonction la renvoie en tant que résultat.
    # Il est important de noter que la fonction ne fait aucune modification ou traitement supplémentaire sur les noms de fichiers, elle se contente de les renvoyer tels quels.
        return os.listdir(path)

    # Méthode pour créer un fichier
    @Pyro4.expose
    def cree_fichier(self, path):
        # Ouvre le fichier en mode écriture avec le context manager 'with' et le nomme 'file'
        with open(path, 'w'):
            pass

    # Méthode pour supprimer un fichier
    @Pyro4.expose
    def supprimer_fichier(self, path):
        os.remove(path)   # Utilise la fonction os.remove pour supprimer le fichier spécifié par 'path'

    # Méthode pour créer un répertoire
    @Pyro4.expose
    def cree_repertoir(self, path):
        os.mkdir(path)  # Utilise la fonction os.mkdir pour créer un nouveau répertoire spécifié par 'path'
           # La fonction os.mkdir crée un nouveau répertoire avec le nom spécifié par 'path'.
    # Si le répertoire existe déjà, une exception FileExistsError sera levée.




    # Méthode pour supprimer un répertoire
    @Pyro4.expose
     # La fonction os.rmdir supprime le répertoire spécifié par 'path'.
    def supprimer_repertoir(self, path):
        os.rmdir(path)

    # Méthode pour ajouter des données à un fichier existant
    @Pyro4.expose
    # La méthode utilise l'instruction `with open` pour ouvrir le fichier spécifié par 'path' en mode d'ajout ('a').
    # Cela signifie que les données seront ajoutées à la fin du fichier sans supprimer son contenu existant.
    def ajouter_des_donnee(self, path, data):
        with open(path, 'a') as f:
            f.write(data)

# Crée un objet de serveur de fichiers
file_server = projet()



#serveur config :
# Configuration du démon Pyro4
daemon = Pyro4.Daemon(host="127.0.10.3", port=5000)
# Démarre le démon Pyro4 et enregistre l'objet de serveur de fichiers

uri = daemon.register(file_server)
print("URI du serveur : ", uri)

# Enregistrer l'URI dans un fichier
with open("uri.txt", "w") as f:
    f.write(str(uri))
 

# Démarrer le serveur Pyro4
daemon.requestLoop()


 
 

 
 
 