# Construction des chaînes d'exécution pour Langgraph

## Introduction
Dans cet article, nous allons explorer la mise en œuvre des chaînes (chains) qui s'exécuteront dans notre graphe (graph) Langgraph. Nous nous concentrerons sur la création de deux composants essentiels : la chaîne de génération et la chaîne de réflexion, qui travailleront ensemble pour produire et améliorer des tweets.

## Comprendre l'architecture
Avant de construire le graphe complet, nous devons d'abord développer ses composants internes. Notre système comportera deux chaînes principales :

1. **La chaîne de génération** (generation chain) : chargée de créer et réviser des tweets jusqu'à obtenir un résultat optimal.
2. **La chaîne de réflexion** (reflection chain) : responsable d'analyser chaque tweet, de le critiquer et de fournir des suggestions d'amélioration.

Ces deux chaînes fonctionneront de manière cyclique dans notre graphe, la critique produite par la chaîne de réflexion alimentant la chaîne de génération pour réviser progressivement le tweet.

## Implémentation du code

Commençons par créer un nouveau fichier nommé `chains.py` qui contiendra toutes les invites (prompts) et les chaînes utilisées dans notre graphe Langgraph.

### Importations nécessaires

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
```

Nous importons :
- `ChatPromptTemplate` : permet de structurer le contenu envoyé au modèle de langage (LM)
- `MessagesPlaceholder` : permet de créer un emplacement pour les futurs messages
- `ChatOpenAI` : interface pour interagir avec les modèles OpenAI

### Création des prompts

#### Prompt de réflexion

```python
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
```

Ce prompt joue le rôle de critique. Il examine le tweet généré et fournit des commentaires détaillés sur la façon de l'améliorer. Le `MessagesPlaceholder` crée un espace où seront placés les messages historiques que notre agent analysera.

#### Prompt de génération

```python
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            " Generate the best twitter post possible for the user's request."
            " If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
```

Ce prompt est responsable de la génération des tweets. Il produit une première version puis la révise en fonction des critiques reçues jusqu'à obtenir un tweet parfait. Le `MessagesPlaceholder` stockera l'historique des réflexions et révisions précédentes.

### Initialisation du modèle et création des chaînes

```python
llm = ChatOpenAI(model="o4-mini")
generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm
```

Nous initialisons d'abord un modèle de langage (par défaut GPT-3.5 Turbo, mais ici configuré pour utiliser o4-mini). Ensuite, nous créons deux chaînes simples en utilisant la syntaxe de chaînage (pipe) :

1. `generate_chain` : connecte le prompt de génération au modèle de langage
2. `reflect_chain` : connecte le prompt de réflexion au modèle de langage

## Conclusion

Nous avons maintenant implémenté les deux chaînes principales qui formeront notre graphe Langgraph. La chaîne de génération créera les tweets, tandis que la chaîne de réflexion les évaluera et fournira des suggestions d'amélioration.

Dans la prochaine étape, nous implémenterons le graphe Langgraph lui-même, qui orchestrera ces chaînes pour créer un cycle d'amélioration continue des tweets.