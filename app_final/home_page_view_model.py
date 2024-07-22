import streamlit as st
from constant import llm_path_list, embed_llm_path_list
from langchain_community.llms.ctransformers import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_huggingface import HuggingFaceEmbeddings
from constant import blog
import tempfile
import os
from document_reader import DocumentReader
from langchain_huggingface import HuggingFaceEmbeddings
import random
import time
from stream_handler_model import StreamHandler

@st.cache_resource
def initialise_llm(index: int):
    if index is not None:
        print(f"Initialising LLM ... {index}")
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
        return CTransformers( model= dir, model_file = llm_path_list[index].model_file, config = {"context_length": 16000, "max_new_tokens": 3000})

@st.cache_resource
def initialise_embed_llm(index: int):
    if index is not None:
        print(f"Initializing Embed LLM ...{index}")
        return HuggingFaceEmbeddings(
            model_name = embed_llm_path_list[index].model_dir,
            show_progress = True,
            model_kwargs = {"trust_remote_code": True})


## Hashing the unhashable parameters
        
def hash_func(obj: HuggingFaceEmbeddings):
    return obj.model_name

@st.cache_resource(hash_funcs= {HuggingFaceEmbeddings: hash_func})
def create_vector_store(embed_llm,uploaded_file ):
    if uploaded_file is not None and embed_llm is not None:
        blog("Creating Vector Store ...")
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir,uploaded_file.name)
        path = rf"{path}"
        blog(path)
        with open(path,"wb") as f:
            f.write(uploaded_file.getvalue())
        
        doc_reader = DocumentReader()
        vectore_store = doc_reader.load_document(embeddings= embed_llm ,path = path)
        blog(f"Vectore Store created ---> {vectore_store}") 
        return vectore_store
    

def response_generator():
        response =random.choice(
            [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?", 
            ]
        )
        
        for word in response.split():
            yield word + " "
            time.sleep(0.05) 
            
