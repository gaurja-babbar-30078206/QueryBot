from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from constant import blog
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import time
        
## DND        
def add_chat_history(llm, retriever, store ,query, config):
    
    contextualize_q_system_prompt = """Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )
    
    

    qa_system_prompt = """
    You are an assistant for question-answering tasks. \
    Use the following pieces of retrieved context to answer the question. \
    If you don't know the answer, just say that you don't know. \
    Use three sentences maximum and keep the answer concise.\

    {context}"""


    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )


    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)


    def get_session_history(session_id:str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
     


    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key= "input",
        history_messages_key= "chat_history",
        output_messages_key= "answer",
    )
    

    return conversational_rag_chain.invoke(
    {"input": query},
    config = config,
    )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def get_response(llm, retriever, query, config):
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
    
    start = time.time()
    retrieved_docs = retriever.invoke(query)
    blog(f"Retrieve Documents ---- Time: {time.time() - start} ----> {retrieved_docs} ")
    
    start = time.time()        
    rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | qa_prompt
    | llm)
    
    ## //TODO Get Intermediate outputs, like what are the documents being returned by the chain ?
    # blog(f"Response time ---->{time.time() - start}")
    
    return rag_chain.invoke(query, config) 