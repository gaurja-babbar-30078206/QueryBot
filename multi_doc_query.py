"""
Building a multidoc reader and chatbot with Langchain
- the best part is that the chatbot will remember your chat history


Definition:
Embedding - An embedding organises and categorises a text based on its semantic meaning
- OpenAI embeddings transformer with cosine similarity to calculate similarity between dcouments and 
question.
- Document loaders-- output --- Document
- load_qa_chain
- RetrievalQA chain
- setting persist_directory
- adding chat history
- passing in all the info each time
- ConversationalRetrievalChain: chat history
- return_source_documents = True

Interacting with Multiple Documents
[+] APPROACH 1 :-
LINK:
- adding more documents to the list
- adding them to the document list
- add the documents to a single document list, containing 
all the documents of all the uploaded files
- LIMITATIONS :
- openAI token limit, we cannot send more than 6-7 chunks of text from the vectorDB
- smart prompt engineering
- Agents for recursive lookups


[+] APPROACH 2 :-
LINK:
- Coverinig - Multiple files | ChromaDB | Source info | 
- RetrievalQA chain
- Directory loader


IMPLEMENTING --->
File Directory: How to load all documents in a directory
glob: to control which files to load



"""

from langchain_huggingface import HuggingFaceEmbeddings

embed_llm_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\snowflake-arctic-embed-m"
embed_llm =  HuggingFaceEmbeddings(
            model_name = embed_llm_path,
            show_progress = True,
            model_kwargs = {"trust_remote_code": True})
