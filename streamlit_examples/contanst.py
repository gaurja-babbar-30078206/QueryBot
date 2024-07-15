class DocItems:
    file_name = ""
    file_path = ""
    
    def __init__(self, file_name, file_path) -> None:
        self.file_name = file_name
        self.file_path =  file_path
    
# path list for testing documents
doc_path_list = {
    'pdf' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf",
    'txt' : r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\alice_in_wonderland/.txt",
}

available_docs = [
    DocItems(file_name = "Leave policy.pdf -- 139 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf"),
    DocItems(file_name = "Hunger Games book.pdf -- 809 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\(The Hunger Games 2) Collins, Suzanne - Catching Fire.pdf"),
    DocItems(file_name = "Alice in Wonderland.txt -- 140 kb", file_path= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\alice_in_wonderland/.txt")
    # r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\Leave_Policy_2024.pdf",
    # r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\(The Hunger Games 2) Collins, Suzanne - Catching Fire.pdf"
    
]
    
# path list of local embedding models
embedding_model_map = {
    "gte_base": r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models\embedding_models\gte-base",
    "all-mpnet-base-v2": "sentence-transformers/all-mpnet-base-v2",        
}



    
            
        
