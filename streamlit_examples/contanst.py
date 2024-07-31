from models.app_models import DocItems
    
from datetime import datetime
# custom logger
def blog(input:str):
    print(f"⏲️  ⏲️  ⏲️   {datetime.now()} 🟢 🟢 🟢 ----> {input}")
    print("\n")

    
# path list for testing documents
doc_path_list = {
    'pdf' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf",
    'txt' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\alice_in_wonderland/.txt",
}

available_docs = [
    DocItems(file_name = "Leave policy.pdf -- 139 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf"),
    DocItems(file_name = "Alice in Wonderland.txt -- 140 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\alice_in_wonderland/.txt"),
    DocItems(file_name = "Hunger Games book.pdf -- 809 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\(The Hunger Games 2) Collins, Suzanne - Catching Fire.pdf"),
    DocItems(file_name = "biology_general_knowledge -- 1848 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\biology_general_knowledge.pdf"),
    DocItems(file_name = "ncert-textbook-for-class-8-social-science-geography-chapter-2 -- 3577 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\ncert-textbook-for-class-8-social-science-geography-chapter-2.pdf"),
]
    
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
    # LLModelSpecs(
    #     dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
    #     file_name= "Meta-Llama-3-8B-Instruct-Q2_K.gguf",
    #     ),
    
    LLModelSpecs(
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
        file_name= "capybarahermes-2.5-mistral-7b.Q3_K_M.gguf",
        ),
    
    # LLModelSpecs(
    #     dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
    #     file_name= "capybarahermes-2.5-mistral-7b.Q4_K_M.gguf"
    # ),
    
    # LLModelSpecs(
    #     dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
    #     file_name= "Mistral-7B-Instruct-v0.3.Q4_K_M.gguf",
    #     ),
    
    
    # LLModelSpecs(
    #     dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
    #     file_name= "llama-2-7b-chat.Q4_K_M.gguf"
    # ),

    # LLModelSpecs(
    #     dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models", 
    #     file_name= "llama-2-7b-chat.Q6_K.gguf"
    # ),
]    

# from smaller to larger memory size
embed_llm_path_list = [
    LLModelSpecs(
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\snowflake-arctic-embed-m",
        file_name= "snowflake-arctic-embed-m" 
        ),
    LLModelSpecs(
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\bge-base-en-v1.5",
        file_name= "bge-base-en-v1.5"
        ),
    LLModelSpecs(
        dir= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\gte-base-en-v1.5", 
        file_name= "gte-base-en-v1.5"),
    
]

# predictions_list = 