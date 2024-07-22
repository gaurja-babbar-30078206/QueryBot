## Inbuilt imports
import os ## use for doc extension, if already using
import pathlib # creates single var
# text and pdf covered, also covers Images(jpg, png), have to see how??
from langchain_community.document_loaders import UnstructuredFileLoader , UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from constant import blog


from llama_index.core.storage.storage_context import StorageContext
from llama_index.core import SimpleDirectoryReader, KnowledgeGraphIndex
from llama_index.core.graph_stores import SimpleGraphStore

   
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
            case '.docx':
                loader = UnstructuredWordDocumentLoader(self.path)
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
    
    
    def load_doc_llama(self, embeddings, path):
        self.path = path
        docs = self.split_documents()
        graph_store = SimpleGraphStore()
        storage_context = StorageContext.from_defaults(graph_store=graph_store)

        index_graph = KnowledgeGraphIndex.from_documents(documents=docs,
                                           max_triplets_per_chunk=3,
                                           storage_context=storage_context,
                                           embed_model=embeddings,
                                          include_embeddings=True)        



                    
        
         