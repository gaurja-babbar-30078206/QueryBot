from datetime import datetime

# path list for testing documents
doc_path_list = {
    'pdf' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf",
    'txt' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\alice_in_wonderland.txt",
}

# path list of local embedding models
embedding_model_map = {
    "gte_base": r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\gte-base",
    "all-mpnet-base-v2": "sentence-transformers/all-mpnet-base-v2",        
}


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
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\mistral_7B_v0.3", 
        file_name= "Mistral-7B-Instruct-v0.3.Q4_K_M.gguf",
        ),
    
    LLModelSpecs(
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "capybarahermes-2.5-mistral-7b.Q3_K_M.gguf"
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


# custom logger
def blog(input:str):
    print(f"⏲️  ⏲️  ⏲️   {datetime.now()} 🟢 🟢 🟢 ----> {input}")


'''
Configurables
- document loaders
- splitters
- embedding models
- Vector Stores
- Retrievers
- LLModels
- Chains

'''