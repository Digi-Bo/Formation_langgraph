# main.py
"""
Point d'entrée principal de l'application Reflexion.

Ce fichier sert de point de démarrage pour l'application d'agent réflexif.
Pour l'instant, il contient uniquement un message de bienvenue mais il pourrait
être étendu pour orchestrer les différents composants de l'application.

Dépendances:
- dotenv: Pour charger les variables d'environnement
"""

# Importe la fonction load_dotenv du module dotenv
# Cette fonction permet de charger les variables d'environnement depuis un fichier .env
from dotenv import load_dotenv

# Charge les variables d'environnement à partir du fichier .env
# Ces variables peuvent inclure des clés API, des configurations, etc.
load_dotenv()

# Point d'entrée du programme
# Le bloc suivant ne s'exécute que si ce fichier est exécuté directement (pas importé)
if __name__ == "__main__":
    # Affiche un simple message pour confirmer que l'application a démarré
    # Cette ligne sera remplacée par du code plus substantiel dans le futur
    print("Hello Reflexion")
