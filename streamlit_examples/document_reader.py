## Inbuilt imports
import os ## use for doc extension, if already using
import pathlib # creates single var


# text and pdf covered, also covers Images(jpg, png), have to see how??
from langchain_community.document_loaders import UnstructuredFileLoader 
# pdf

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from contanst import available_docs
from utils import blog

def print_doc_list():
    print("List of available documents:")
    for count in range(len(available_docs)):
        print(f"[{count}] {available_docs[count].file_name}")
   
class DocumentReader:
    
    def __init__(self):
        # Initialising text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        print_doc_list()
        chosen_doc = int(input("Enter index of chosen document: "))
        self.path = available_docs[chosen_doc].file_path
        blog(f"File chosen -----> {self.path}")
                  
              
    # get the file extension
    def get_file_extension(self):
        return pathlib.Path(self.path).suffix
    
    # returns loaded document
    def get_document(self):
        file_ext = self.get_file_extension()
        match file_ext:
            case '.pdf':
                loader = UnstructuredFileLoader(self.path)               
            case '.txt':
                loader = UnstructuredFileLoader(self.path)
            case _:
                print('Format of the document is not supported')    
        return loader.load()
     
    # Splitting documents
    def split_documents(self):
        docs = self.get_document()
        return self.text_splitter.split_documents(docs)
        
            
    # creates vector embeddings and stores in vector store    
    def load_document(self,embeddings):
        docs = self.split_documents()
        return Chroma.from_documents(documents=docs, embedding = embeddings)            
        
         