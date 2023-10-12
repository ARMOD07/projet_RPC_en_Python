# projet_RPC_en_Python


Ce projet propose une démonstration d'un mini serveur de gestion de fichiers à distance, basé sur NFS (Network File System), en utilisant un Middleware RPC (Remote Procedure Call) implémenté en Python. L'objectif principal est de permettre la gestion des fichiers et des répertoires à distance, offrant des fonctionnalités telles que la liste des fichiers/répertoires, la création et la suppression de fichiers, ainsi que la création et la suppression de répertoires.

Le serveur de fichiers est mis en œuvre en tant que classe Python exposant des méthodes via le module Pyro4, permettant l'accès et la manipulation des fichiers à partir d'un client distant. Les fonctionnalités incluent la liste des fichiers/répertoires, la création de fichiers et de répertoires, la suppression de fichiers et de répertoires, ainsi que l'ajout de données à un fichier existant.

Le client se connecte au serveur à l'aide de l'URI (Uniform Resource Identifier) fournie par le serveur, puis offre un menu interactif permettant à l'utilisateur d'effectuer diverses opérations sur les fichiers et répertoires distants.

Ce projet offre un exemple concret de communication client-serveur à distance, utilisant un middleware RPC pour permettre la gestion des fichiers à distance. Il peut servir de base pour des applications plus complexes de gestion de fichiers à distance, avec des fonctionnalités étendues et des mesures de sécurité renforcées.

Sur GitHub, ce projet peut être publié en tant que référence d'utilisation d'un middleware RPC pour la gestion de fichiers distants, avec des instructions claires sur son utilisation et son déploiement. Les utilisateurs pourront ainsi étudier le code, le tester et le personnaliser selon leurs besoins spécifiques.
 
