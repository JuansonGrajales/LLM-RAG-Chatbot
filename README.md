# LLM-RAG-Chatbot

## Description
This project implements a chatbot powered by Large Language Models (LLM) through Retrieval-Augmented Generation (RAG). RAG enhances LLM capabilities by retrieving relevant information from a database, enabling the generation of contextually relevant responses. Specifically, this chatbot is designed for use within a hospital system, capable of retrieving and providing information on patients, patient experiences, visits, insurance payers, and physicians.

## Installation and Configuration
Follow these steps to set up the LLM-RAG-Chatbot:

### 1. Configure OpenAI API Key
Ensure you have an OpenAI account and a valid API key. Set up environment variables for OpenAI as follows:

### 2. Sign Up for Neo4j AuraDB
Create a free account on [Neo4j AuraDB](https://neo4j.com/cloud/aura-free/) by clicking the **Start Free** button, followed by **New Instance**. After selecting **Download and Continue**, your instance will be created and should be up and running.

### 3. Create a .env File
In the project's root directory, create a `.env` file with the necessary configurations:
```env
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
NEO4J_URI=YOUR_NEO4J_URI
NEO4J_USERNAME=YOUR_NEO4J_USERNAME
NEO4J_PASSWORD=YOUR_NEO4J_PASSWORD
HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/JuansonGrajales/LLM-RAG-Chatbot/main/data/reviews.csv
HOSPITAL_AGENT_MODEL=gpt-3.5-turbo-1106
HOSPITAL_CYPHER_MODEL=gpt-3.5-turbo-1106
HOSPITAL_QA_MODEL=gpt-3.5-turbo-0125
CHATBOT_URL=http://host.docker.internal:8000/hospital-rag-agent
```

### 4. Start the Application
Open a terminal and execute the following command:
```sh
docker-compose up --build
```
After the build and run process completes, access the chatbot UI at `http://localhost:8501/` to start interacting with the chatbot.

## Source
The tutorial for building this chatbot is available at [Real Python by Harrison Hoffmam](https://realpython.com/build-llm-rag-chatbot-with-langchain/#step-5-deploy-the-langchain-agent)