from langchain_community.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from contanst import embedding_model_map
from langchain_huggingface import HuggingFaceEmbeddings
from utils import blog

class LLModelSpecs:
    model_dir = ""
    model_file = ""
    context_len = 16000,
    max_new_tokens = 1600
    
    def __init__(self, dir, file_name, cont_len = 16000, max_new_token =  16000) -> None:
        self.model_dir = dir
        self.model_file = file_name
        self.context_len = cont_len,
        self.max_new_tokens = max_new_token
        
llm_path_list = [
    LLModelSpecs(
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "Mistral-7B-Instruct-v0.3.Q4_K_M.gguf",
        ),
    
    LLModelSpecs(
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "capybarahermes-2.5-mistral-7b.Q3_K_M.gguf"
    ),
    
    LLModelSpecs(
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "llama-2-7b-chat.Q4_K_M.gguf"
    ),

    LLModelSpecs(
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "llama-2-7b-chat.Q6_K.gguf"
    ),
    LLModelSpecs(
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "llama-2-7b-chat.Q8_0.gguf"
    ),
]    


def print_llm_list():
    print("List of available models:")
    for count in range(len(llm_path_list)):
        print(f"[{count}] {llm_path_list[count].model_file}")
        

def get_llm(): 
    
    #print llm list
    print_llm_list()
    
    # choose LLM
    llm_opn = int(input("Enter index of chosen model: "))
    
    dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
    
    if (llm_opn < 0 or llm_opn >= len(llm_path_list)):
        blog("Invalid input")
        return
    else:    
        blog(f"Chosen Model: {llm_path_list[llm_opn].model_file}")
        file_name = llm_path_list[llm_opn].model_file    
    
     
    
    return CTransformers( model= dir, model_file = file_name, callbacks=[StreamingStdOutCallbackHandler()], config = {"context_length": 16000, "max_new_tokens": 3000})
 
 

def get_embed_llm():
    # chose embed llm
    return HuggingFaceEmbeddings(model_name = embedding_model_map["gte_base"])
        
        
    
            