"""
Module chains.py - Implémentation de chaînes LangChain pour la génération et l'évaluation de tweets

Ce module définit deux chaînes LangChain distinctes qui travaillent ensemble pour générer et améliorer des tweets:
1. Une chaîne de génération qui crée des tweets basés sur les demandes de l'utilisateur
2. Une chaîne de réflexion qui évalue les tweets générés et fournit des critiques

Ces chaînes utilisent le modèle OpenAI pour interagir avec l'utilisateur dans un processus itératif
d'amélioration de contenu pour Twitter.
"""

# Importation des modules nécessaires
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# =============================================================================
# Configuration des prompts (instructions) pour les modèles de langage
# =============================================================================

# Prompt pour la chaîne de réflexion (évaluation de tweets)
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Vous êtes un influenceur viral sur Twitter évaluant un tweet. Générez une critique et des recommandations pour le tweet de l'utilisateur."
            "Fournissez toujours des recommandations détaillées, y compris des demandes concernant la longueur, la viralité, le style, etc.",
        ),
        # Emplacement réservé pour stocker l'historique des messages de la conversation
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Prompt pour la chaîne de génération (création de tweets)
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Vous êtes un assistant influenceur technique sur Twitter chargé de rédiger d'excellents posts Twitter."
            " Générez le meilleur post Twitter possible pour la demande de l'utilisateur."
            " Si l'utilisateur fournit une critique, répondez avec une version révisée de vos tentatives précédentes.",
        ),
        # Emplacement réservé pour stocker l'historique des messages de la conversation
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# =============================================================================
# Initialisation du modèle de langage et des chaînes
# =============================================================================

# Initialisation du modèle de langage OpenAI (o4-mini)
llm = ChatOpenAI(model="o4-mini")

# Création de la chaîne de génération: combine le prompt de génération avec le LLM
# L'opérateur | (pipe) en LangChain permet de connecter des composants pour créer un flux de traitement
generate_chain = generation_prompt | llm

# Création de la chaîne de réflexion: combine le prompt de réflexion avec le LLM
reflect_chain = reflection_prompt | llm

# Note d'utilisation:
# Ces chaînes sont conçues pour être utilisées ensemble dans un workflow où:
# 1. generate_chain crée un tweet initial basé sur la demande de l'utilisateur
# 2. reflect_chain évalue ce tweet et fournit des recommandations
# 3. generate_chain utilise ces recommandations pour améliorer le tweet
# Ce cycle peut être répété pour affiner le tweet jusqu'à satisfaction.