## Inbuilt imports
import os ## use for doc extension, if already using
import pathlib # creates single var
# text and pdf covered, also covers Images(jpg, png), have to see how??
from langchain_community.document_loaders import UnstructuredFileLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from constant import blog

   
class DocumentReader:
    
    def __init__(self):
        # Initialising text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.path = ""          
              
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
    def load_document(self,embeddings, path):
        self.path = path
        docs = self.split_documents()
        return Chroma.from_documents(documents=docs, embedding = embeddings)            
        
         