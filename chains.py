# chains.py

"""
Configuration et implémentation des chaînes LangChain pour l'agent Reflexion.

Ce module met en place un système de "first responder chain" (chaîne de premier répondant)
qui génère une réponse structurée à partir d'une requête utilisateur, incluant:
- Une réponse détaillée à la question
- Une auto-critique de la réponse
- Des suggestions de requêtes de recherche pour améliorer la réponse

Le module utilise des techniques avancées de LangChain telles que:
- Les prompts structurés
- Le function calling via des schémas Pydantic
- Le chaînage d'opérations (piping)

Dépendances:
- langchain_core: Pour les composants de base de LangChain
- langchain_openai: Pour l'intégration avec les modèles OpenAI
- schemas: Pour les modèles Pydantic définissant la structure des sorties
"""

# Imports des bibliothèques standard
import datetime
from dotenv import load_dotenv

# Chargement des variables d'environnement (clés API, etc.)
load_dotenv()

# Imports des parseurs de sortie pour traiter les réponses structurées des LLMs
from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,  # Pour transformer les réponses en dictionnaires JSON
    PydanticToolsParser,    # Pour transformer les réponses en objets Pydantic
)

# Import pour créer des messages à envoyer au LLM
from langchain_core.messages import HumanMessage

# Imports pour créer des templates de prompts structurés
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Import pour interagir avec les modèles OpenAI
from langchain_openai import ChatOpenAI

# Import du schéma Pydantic qui définit la structure de sortie attendue
from schemas import AnswerQuestion

# Initialisation du modèle de langage (LLM)
# o4-mini est une référence à un modèle OpenAI spécifique (ici probablement GPT-4 mini)
llm = ChatOpenAI(model="o4-mini")

# Initialisation des parseurs pour traiter la sortie du LLM
# Ce parseur retourne le résultat brut du function calling sous forme de dictionnaire
parser = JsonOutputToolsParser(return_id=True)

# Ce parseur transforme la réponse en une instance de la classe AnswerQuestion
parser_pydantic = PydanticToolsParser(tools=[AnswerQuestion])

# Création du template de prompt principal pour l'agent
# Ce template définit la structure des messages envoyés au LLM
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        # Message système définissant le rôle et les tâches de l'agent
        (
            "system",
            """You are expert researcher.
Current time: {time}

1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. Recommend search queries to research information and improve your answer.""",
        ),
        # Placeholder pour les messages précédents dans la conversation
        # Cela permet de maintenir un contexte entre les interactions
        MessagesPlaceholder(variable_name="messages"),
        
        # Message système final pour rappeler le format attendu
        ("system", "Answer the user's question above using the required format."),
    ]
# Pré-remplissage de certaines variables du template
# Ici, le timestamp actuel est injecté dynamiquement à chaque appel
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

# Spécialisation du template pour le "first responder"
# L'instruction principale est définie: générer une réponse détaillée d'environ 250 mots
first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~250 word answer."
)

# Création de la chaîne de premier répondant
# Cette chaîne connecte le template de prompt au LLM et force l'utilisation
# de la classe AnswerQuestion pour structurer la sortie
first_responder = first_responder_prompt_template | llm.bind_tools(
    tools=[AnswerQuestion], tool_choice="AnswerQuestion"
)

# Section de test - s'exécute uniquement si ce fichier est lancé directement
if __name__ == "__main__":
    # Création d'un message utilisateur pour tester la chaîne
    human_message = HumanMessage(
        content="Write about AI-Powered SOC / autonomous soc problem domain,"
        " list startups that do that and raised capital."
    )
    
    # Construction de la chaîne complète pour le test
    # Cette chaîne:
    # 1. Utilise le template de prompt du premier répondant
    # 2. Passe la sortie au LLM configuré pour utiliser la classe AnswerQuestion
    # 3. Parse le résultat en objet Pydantic
    chain = (
        first_responder_prompt_template
        | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
        | parser_pydantic
    )
    
    # Exécution de la chaîne avec le message utilisateur
    # Le résultat sera un objet structuré selon le schéma AnswerQuestion
    res = chain.invoke(input={"messages": [human_message]})
    
    # Affichage du résultat pour vérification
    print(res)