"""
ISSUES:
1) Caching the Vector Store 
I want that type writer effect from my project
Advance concepts of Streamlit
Session state
Caching allows you to save the outputs

session state lets you save information for each user
that is perserved between reruns. 
This not only allows you to avoid unecessary recalculation,
but also allows you to create dynamic pages and handle progressisve
processes.

## so my embeddings were not hashable, so I can prolly save them in a variable
## Caching my embeddings or vector store that has been created

## Session state  

The hash_funcs parameter
- cachin decorators hash the input parameters and

- Initialising the Embedding model choosing embedding model
- To create a vector store --> it needs the embedding llm and the path
- so Vector store should not be created if, embedding llm and path remain the same


q) What is a session state?

a dictionary like interface where you can save information that is preserved
between script reruns

- Now we have to take the user input
- pass on this query to the chains created
- get the response
- add both the messages to the chat history
- View this in Scrollable container


## Now onto the input and output


## The Answer was there all along ....

// TODO
[0] Add a timer to record the response time

"""

import streamlit as st
from constant import llm_path_list, embed_llm_path_list
from home_page_view_model import *
from constant import blog
from chat_history import add_chat_history, get_response
from home_page_view_model import initialise_embed_llm 
from time import time




st.title("Document Query Bot 📔+🤖")
with st.sidebar:
    
    left_col,right_col = st.columns(2)
    
    
    llm = initialise_llm(left_col.selectbox(
        "LLM",placeholder = "Choose an LLM",
        options= range(len(llm_path_list)), index= None,
        format_func= lambda x: llm_path_list[x].model_file,
        ))

    embed_llm = initialise_embed_llm(right_col.selectbox(
        "Embed LLM",placeholder = "Choose an Embed LLM",
        options= range(len(embed_llm_path_list)), index= None,
        format_func= lambda x: embed_llm_path_list[x].model_file ))

    
    if "retriever" not in st.session_state:
        st.session_state.retriever = None
            
    with st.form("my_form"):
        blog("build")
        uploaded_file= st.file_uploader("Choose a Document")
        submitted = st.form_submit_button("Submit")
        if submitted:
            vector_store = create_vector_store(uploaded_file= uploaded_file, embed_llm=embed_llm)
            st.session_state.retriever = vector_store.as_retriever()
        else:
            st.empty()
            
            

if "store" not in st.session_state:
    st.session_state.store = {}
    
    
# initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])    


# react to user input
if prompt:= st.chat_input("Enter your questions..."):
    # display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role":"user", "content":prompt})


    # Display assistant response in chat message container
    with st.chat_message("ai"):
        chat_box = st.empty()
        stream_handler = StreamHandler(chat_box,display_method='write')
        config ={"callbacks": [stream_handler, StreamingStdOutCallbackHandler()]}
        start_time = time()
        response = get_response(llm=llm,retriever=st.session_state.retriever,query=prompt, config= config )
        st.write(f"Total Response time ---> {time() - start_time}")
    st.session_state.messages.append({"role":"ai", "content": response})            
    