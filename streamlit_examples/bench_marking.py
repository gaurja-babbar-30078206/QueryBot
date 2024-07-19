"""
Control Environment:

LLM: 
Embedding LLM:
Vector Store:
Retriever:
Contextual Prompt:
Prompt:
Questions = [] 
"""



from langchain_openai import AzureChatOpenAI
from langchain_openai import OpenAIEmbeddings
from utils import blog 
from document_reader import DocumentReader
from chat_history import add_chat_history
from llmodel import get_embed_llm
from contanst import llm_path_list, LLModelSpecs
from time import time
import pandas as pd
from langchain_community.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def print_llm_list(llm_list: list[LLModelSpecs]):
    print("List of available models:")
    for count in range(len(llm_list)):
        print(f"[{count}] {llm_list[count].model_file}")
        
def get_llm_local(): 

    #print llm list
    print_llm_list(llm_list= llm_path_list)
    
    # choose LLM
    llm_opn = int(input("Enter index of chosen model: "))
    
    dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
    
    if (llm_opn < 0 or llm_opn >= len(llm_path_list)):
        blog("Invalid input")
        return
    else:    
        blog(f"Chosen Model: {llm_path_list[llm_opn].model_file}")
        file_name = llm_path_list[llm_opn].model_file    
    
     
    start_time = time()
    llm =  CTransformers( model= dir, model_file = file_name, callbacks=[StreamingStdOutCallbackHandler()], config = {"context_length": 16000, "max_new_tokens": 3000})
    blog(f"LLM Initialisation time ----->{time() - start_time}")
    return llm

def get_llm(): 
    
    OPENAI_API_BASE="https://ailabazopenaise.openai.azure.com"
    GPT_DEPLOYMENT_NAME="ailabgpt35turbo"
    OPENAI_API_KEY="07a2db3305d14f619202c549ca81b0d2"

    model = AzureChatOpenAI(
    azure_endpoint=OPENAI_API_BASE,
    openai_api_version="2023-09-15-preview",
    deployment_name =GPT_DEPLOYMENT_NAME,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure",
    )    
    
    blog(f"Created Model ----> {model}")
    return model


if __name__ == "__main__":
    
    keep_asking = True
    chainge_model = False
    
    # how to do this parallely
    # Initialise LLModel
    llm = get_llm_local()
    
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
            # query = input("Enter your query:")
            print("Generating ...")
            answers = []
            ## take a list of queries
            queries = [
                "What are the different types of leave mentioned in the document?",
                "Who is the sanctioning authority for granting leave to employees?",
                "What is the objective of providing leave to employees?",
                "How is leave earning calculated for employees?",
                "What is the Leave Year defined as in the document?",
                "Can employees avail leave without having leave credit?",
                "What are the conditions for employees to be entitled to leave?",
                "Can employees carry forward unused leave to the next year?",
                "How many public holidays are declared by businesses each year?",
                "What happens if employees do not choose optional holidays?",
                "What is the purpose of Exit Leave?",
                "Who can approve deviations from the leave rules?",
                "Are employees encouraged to work from home?",
                "What is the consequence of absence from work without sanctioned leave?",
                "Are employees entitled to special leave for parental benefits?",
                "What is the policy for employees joining or leaving in the middle of a Leave Year?",
                "Can employees encash their leave?",
                "Can employees choose their preferred holidays from the list of optional holidays?",
                "Who determines the list of optional holidays for employees to choose from?",
                "Are there any restrictions on the maximum leave balance that employees can accumulate?",
                ]
            for index in range(len(queries)):    
                response = add_chat_history(llm= llm, retriever= qa_retriever, store= store, query=queries[index])
                # blog(f"Answer -----> ${response['answer']}")
                answers.append(f"{response['answer']}")
                print('\n')            
            df = pd.DataFrame({"Questions": queries, "Answers": answers})
            blog(f"Pandas dataframe --> {df}")
            df.to_excel("bench_mark.xlsx",sheet_name=f"{llm}+{embed_llm}")
            blog(f"Excel created...")
        
        elif choice == 'n':
            keep_asking = False
            blog("Following is the Chat History ---->")
            print(store)
            blog("Chat Ended")
        
        
            
                    
    
            