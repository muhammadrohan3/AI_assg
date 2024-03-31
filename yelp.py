from langchain.chains import GraphCypherQAChain
from langchain.prompts.prompt import PromptTemplate

from llm import llm
from graph import graph  # Assuming you have a graph file where the database connection is established

# Define the Cypher generation template
CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about businesses and reviews on Yelp.
Convert the user's question based on the schema. Return the answer in the parsed form string or list of strings.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Fine Tuning:

For business names that begin with "The", move "the" to the end. For example "The Best Cafe" becomes "Best Cafe, The" or "the restaurant" becomes "Restaurant, The".

Example Cypher Statements:

1. How to find how many degrees of separation there are between two users who are friends:

```
MATCH path = shortestPath(
(u1:User {{name: "User 1"}})-[:FRIENDS*]-(u2:User {{name: "User 2"}})
)
RETURN length(path) AS degrees_of_separation
```
2. Give me businesses in the same category as a business with a specific name:
    
```
    MATCH (b1:Business {{name: "Business 1"}})-[:IN_CATEGORY]->(category:Category)<-[:IN_CATEGORY]-(b2:Business)
    RETURN b2
```
Use the neo4J query to answer the question.

Schema:
{schema}

Question:
{question}

"""

# Create a Cypher prompt template
cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)

# Create a GraphCypherQAChain
yelp_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    cypher_prompt=cypher_prompt
)

