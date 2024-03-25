# Chatbot API

## Description
The Chatbot API leverages FastAPI to serve the chatbot REST endpoint, which is the core deliverable of this project. The `chatbot_api/src/agents` and `chatbot_api/src/chains` subdirectories house the LangChain objects that constitute the chatbot.

## Agents
The agent `hospital_rag_agent` acts as a central coordination point, intelligently determining which tools or resources are best suited to handle a given query based on the context and the question's nature. Currently, we have four tools: `hospital_review_chain`, `hospital_cypher_chain`, the function `wait_times.py`, and the function `get_most_available_hospital`. Many of the tools' descriptions include few-shot prompts, advising the agent on when to utilize the tool and providing examples of what inputs to pass.

## Chains
There are multiple chains, one for reviews and another for generating Cypher queries for the Neo4j database. These chains represent a sequence of steps:
1. **Understand the Query:** Interpret the user's question or command within a specific context. For example, the chains include system messages with detailed prompts on what they should and should not respond to. In `hospital_cypher_chain.py`, it provides a few-shot examples of how it might generate a Cypher query.
2. **Access and Process Data:** Retrieve data from the identified sources and process it to extract relevant information.
3. **Generate an Answer:** Use the processed data to formulate a response that effectively addresses the user's query.
