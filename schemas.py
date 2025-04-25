# schemas.py

"""
Schémas Pydantic pour structurer les sorties des modèles de langage.

Ce module définit les structures de données utilisées pour formater et valider 
les réponses générées par les LLMs via le mécanisme de function calling.

Les classes définies servent à:
1. Standardiser le format des réponses
2. Guider le LLM vers un format de sortie précis
3. Valider automatiquement les données reçues

Dépendances:
- pydantic: Pour la définition et validation des modèles de données
- typing: Pour les annotations de type
"""
from typing import List
from pydantic import BaseModel, Field


class Reflection(BaseModel):
    """
    Modèle pour structurer une auto-critique d'une réponse.
    
    Cette classe permet au LLM de fournir une analyse critique de sa propre réponse
    en identifiant les informations manquantes et superflues.
    """
    missing: str = Field(
        description="Critique of what is missing.", 
        # Cette description guide le LLM à identifier ce qui manque dans la réponse initiale
    )
    superfluous: str = Field(
        description="Critique of what is superfluous",
        # Cette description guide le LLM à identifier les informations non nécessaires
    )


class AnswerQuestion(BaseModel):
    """
    Modèle principal pour structurer la réponse complète à une question.
    
    Cette classe définit le format attendu pour une réponse élaborée, incluant:
    - La réponse principale
    - Une auto-critique 
    - Des suggestions de requêtes de recherche pour amélioration
    """
    
    answer: str = Field(
        description="~250 word detailed answer to the question.",
        # Guide le LLM à produire une réponse détaillée d'environ 250 mots
    )
    reflection: Reflection = Field(
        description="Your reflection on the initial answer.",
        # Demande une auto-critique structurée via le modèle Reflection
    )
    search_queries: List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer.",
        # Guide le LLM à proposer des requêtes de recherche pertinentes pour améliorer la réponse
    )