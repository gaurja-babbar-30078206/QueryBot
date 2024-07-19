from langchain_community.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from contanst import llm_path_list, embed_llm_path_list, LLModelSpecs
from langchain_huggingface import HuggingFaceEmbeddings
from utils import blog
from time import time
from utils import blog

def print_llm_list(llm_list: list[LLModelSpecs]):
    print("List of available models:")
    for count in range(len(llm_list)):
        print(f"[{count}] {llm_list[count].model_file}")
        

def get_llm(): 

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
 
 

def get_embed_llm():
    print_llm_list(llm_list= embed_llm_path_list)
    
    llm_opn = int(input("Enter index of chosen model: "))
    
    if (llm_opn < 0 or llm_opn >= len(embed_llm_path_list)):
        blog("Invalid input")
        return
    else:    
        blog(f"Chosen Model: {embed_llm_path_list[llm_opn].model_file}")
        file_name = embed_llm_path_list[llm_opn].model_dir   
    
    start_time = time()
    embed_llm =  HuggingFaceEmbeddings(
            model_name = file_name,
            show_progress = True,
            model_kwargs = {"trust_remote_code": True})
    blog(f"Embed LLM Initialisation time ----->{time() - start_time}")
    return embed_llm    
        
    

                