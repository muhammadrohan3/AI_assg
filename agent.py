from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from yelp import yelp_qa  # Adjust import based on your Yelp database interaction module
from llm import llm

# Define tools for the agent
tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not include querying data from the database",
        func=llm.invoke,
        return_direct=True,
    ),
    Tool.from_function(
        name="Yelp Business Search",
        description="Provides information about Yelp businesses",
        func=yelp_qa.invoke,  # Adjust function based on your Yelp database interaction
        return_direct=True,
    )
]

# Initialize conversation memory
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)

# Create a prompt template for the agent
agent_prompt = PromptTemplate.from_template("""
As an expert on Yelp reviews and a business analyst, your primary objective is to provide valuable insights and recommendations to our clients regarding their businesses and how they can improve based on Yelp data.

Your role involves analyzing reviews and businesses on Yelp to gather meaningful information that can help our clients make informed decisions and develop effective strategies for their businesses.

When interacting with the LLM, ensure that you focus solely on queries related to businesses, categories, cities, reviews, or users. Avoid addressing any topics outside of these areas.

Your responses should be aimed at being as helpful and informative as possible, providing detailed insights and recommendations whenever necessary.

Remember, your goal is to assist our clients in understanding their businesses better and leveraging Yelp data to drive growth and success.

Now, proceed with confidence and utilize your expertise to deliver valuable insights and recommendations to our clients.

Do not answer anything that is not in your domain.


TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:
```

Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```
When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:
```
Thought: Do I need to use a tool? No
Final Answer: your response here
```
                                            
Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
""")

# Create the agent using LLM and tools
agent = create_react_agent(llm, tools, agent_prompt)

# Create an executor for the agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
)

# Define a function to generate responses
def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """
    response = agent_executor.invoke({"input": prompt})
    return response['output']
