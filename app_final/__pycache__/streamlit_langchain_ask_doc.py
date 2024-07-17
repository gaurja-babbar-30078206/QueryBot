"""
LANGCHAIN + STREAMLIT TUTORIAL :
LINK: https://blog.streamlit.io/langchain-tutorial-4-build-an-ask-the-doc-app/
Previous Langchain tutorials
LLM model + prompt templates
Data connection (document loader and text splitting)
Chains

1) Set up Coding Environment
2) Build the App
3) Deploy the App 

A) Ingestion
Ingestion transforms it into index, the most common
being the vector store.
- loading the document
- splitting the document
- creating the embeddings
- Storing the Embeddings in dB (a vector store)


B) Generation
- with the index or vector store , we can use the formatted data
to generate an answer 
- by accepting the user's question
- identify the most relevant document for the question
- Pass the quesion and the document as input to the LLM to generate answer



- User uploads 
"""
