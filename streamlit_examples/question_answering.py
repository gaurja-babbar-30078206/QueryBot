from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


class QuestionAnswering:
    
    def __init__(self) -> None:
        # creating prompt
        template = """Answer the question based ONLY on the following context:
                    {context}
                    Question: {question}
                    """

        self.prompt = ChatPromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)    
        
    def answerQuery(self,retriever, llm, query):
        chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | self.prompt
        | llm
        | StrOutputParser()
        )

        return chain.invoke(query)
    
    
                
        
        
            