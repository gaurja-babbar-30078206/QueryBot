from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory


class QuestionAnswering:
    
    def __init__(self, retriever, llm) -> None:
        # creating prompt
        template = """Answer the question based ONLY on the following context:
                    {context}
                    Question: {question}
                    """

        self.prompt = ChatPromptTemplate.from_template(template)
        self.retriever = retriever
        self.llm = llm
        memory = ConversationBufferMemory(memory_key= "chat_history")
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)    
        
    def answerQuery(self, query):
        chain = (
        {"context": self.retriever, "question": RunnablePassthrough()}
        | self.prompt
        | self.llm
        | StrOutputParser()
        )
        
        return chain.invoke(query)
    
    def add_chat_history(self,query):
        chain =  self.answerQuery()
        chain_with_history = RunnableWithMessageHistory(
            chain,
            lambda session_id: SQLChatMessageHistory(
                session_id= session_id,
                connection= "sqlite:///sqlite.db"
            ),
            input_messages_key= "question",
            history_messages_key= "history"
        )
        config = {
            "configurable":{
                "session_id": "100"
            }
        }
    
        return chain_with_history.invoke({"question":query}, config=config)
        
    
    
                
        
        
            