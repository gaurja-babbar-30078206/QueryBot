from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains.combine_documents import create_stuff_documents_chain
from contanst import blog
from time import time


class QuestionAnswering:
    
    def __init__(self, retriever, llm) -> None:
        
        template = """
    You are an assistant for question-answering tasks. \
    Use the following pieces of retrieved context to answer the question. \
    If you don't know the answer, just say that you don't know. \
    Use three sentences maximum and keep the answer concise.\

    {context}"""           

        self.prompt = ChatPromptTemplate.from_template(template)
        self.retriever = retriever
        self.llm = llm
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)    
        
    def answerQuery(self, query):
        chain = (
        {"context": self.retriever, "question": RunnablePassthrough()}
        | self.prompt
        | self.llm
        )
        return chain.invoke(query)
    
    def answerQuery_test(self, query):
        start_time = time()
        selected_documents = self.retriever.invoke(query)
        blog(f"Document retrieval time ---->{time() - start_time }")
        blog(f"Retrieved Documents ----> {selected_documents}")
        start_time = time()
        document_chain = create_stuff_documents_chain(self.llm, self.prompt)
        response = document_chain.invoke({"context":selected_documents, "question": query})
        blog(f"LLM reponse time ---->{time() - start_time }")
        return response
                        
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
                    
def get_response(llm, retriever, query):
    qa_system_prompt = """
    You must answer the user's questions. \
    Use the following pieces of retrieved context to answer the question :{context} \
    If you don't know the answer, just say that you don't know. \
    Do not make up fake information. \
    Keep the answer concise.\

    Answer: """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            ("human", "{input}"),
        ]
    )
            
    rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | qa_prompt
    | llm)
        
    return rag_chain.invoke(query)    
    
                
        
        
            