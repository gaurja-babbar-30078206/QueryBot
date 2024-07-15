from utils import blog
from llmodel import get_llm, get_embed_llm
from document_reader import DocumentReader
from contanst import doc_path_list
from question_answering import QuestionAnswering
import time
import itertools
import threading
import time
import sys
from contanst import available_docs
from chat_history import add_chat_history



done = False    
def animate():
    start_time = time.time()
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f"\rloading {c} {time.time() - start_time }")
        sys.stdout.flush()
        time.sleep(0.1)
        
        
    sys.stdout.write('\rDone!     ') 


if __name__ == "__main__":
    
    keep_asking = True
    chainge_model = False
    
    # how to do this parallely
    # Initialise LLModel
    llm = get_llm()
    
    # Initialise Embeddings model
    embed_llm = get_embed_llm()
    blog(f"Embedding Model: {embed_llm}")
    
    # Document loading and vector store creation
    doc_loading = DocumentReader()
    
    vector_store = doc_loading.load_document(embeddings=embed_llm)
    blog(f"Vector store created {vector_store}")
    
    # Initializing retriever
    qa_retriever = vector_store.as_retriever()
    blog(f"Retriever created ---------->{qa_retriever}")
    
    # Querying
    
    store = {}
    while keep_asking:
        choice = str(input("Want to ask a query? Enter Y for yes, N for no: \n")).strip().lower()
        
        if choice == 'y':
            keep_asking = True
            query = input("Enter your query:")
 
            start_time = time.time()
            print("Generating ...")
            response = add_chat_history(llm= llm, retriever= qa_retriever, store= store, query=query)
            blog(f"Context Used -----> {response['context']}")
            blog(f"Answer -----> ${response['answer']}")
            end_time = time.time()
            print('\n')
            blog(f"Response time: {end_time - start_time}")
            print('\n')            
        elif choice == 'n':
            keep_asking = False
            blog("Following is the Chat History ---->")
            print(store)
            blog("Chat Ended")
        
        
            
                
        
    
    