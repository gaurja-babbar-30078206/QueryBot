from langchain_community.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from contanst import embedding_model_map
from langchain_huggingface import HuggingFaceEmbeddings


def get_llm(): 
    
    # choose LLM
    llm_opn = str(input("Enter an alphabet to choose the LLM:\n[A] Mistral-7B-Instruct-v0.3.Q4\n[B] capybarahermes-2.5-mistral-7b.Q3_K_M\n[C] llama-2-7b-chat.Q6_K\n[D] llama-2-7b-chat.Q8_0\n")).strip().lower()
    dir = ""
    file_name = ""    
        
    match llm_opn:
        case 'a':
            dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
            file_name= "Mistral-7B-Instruct-v0.3.Q4_K_M.gguf"
        case 'b':
            dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models" 
            file_name= "capybarahermes-2.5-mistral-7b.Q3_K_M.gguf"
        case 'c':
            dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models" 
            file_name= "llama-2-7b-chat.Q6_K.gguf"
        case 'd':
            dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models" 
            file_name= "llama-2-7b-chat.Q8_0.gguf"
        case _:
            print('Invalid Input')
            return 
    
    return CTransformers( model= dir, model_file = file_name, callbacks=[StreamingStdOutCallbackHandler()], config = {"context_length": 16000, "max_new_tokens": 1600})
 
 

def get_embed_llm():
    
    # chose embed llm
    return HuggingFaceEmbeddings(model_name = embedding_model_map["gte_base"])
        