from llmodel import get_llm, get_embed_llm
from document_reader import DocumentReader
from contanst import doc_path_list,blog
from question_answering import QuestionAnswering
import threading
import time
import itertools
import threading
import time
import sys


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
    
    # how to do this parallely
    # Initialise LLModel
    llm = get_llm()
    blog(f"LLModel: {llm}")
    
    
    # Initialise Embeddings model
    embed_llm = get_embed_llm()
    blog(f"Embedding Model: {embed_llm}")
    
    # Document loading and vector store creation
    doc_loading = DocumentReader()
    vector_store = doc_loading.load_document(path = doc_path_list['pdf'], embeddings=embed_llm)
    blog(f"Vector store created {vector_store}")
    
    # Initializing retriever
    qa_retriever = vector_store.as_retriever()
    blog(f"Retriever created ---------->{qa_retriever}")
    
    # Querying
    qa = QuestionAnswering()
    # t = threading.Thread(target=animate)
    # t.start()
    # query = str(input("Please enter your query"))
    query = "Summarize the given document in 5 bullet points only"
    response = qa.answerQuery(retriever= qa_retriever, llm = llm, query= query)
    
   
 