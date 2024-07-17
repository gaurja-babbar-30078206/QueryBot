import streamlit as st
from constant import llm_path_list, embed_llm_path_list
from home_page_view_model import *
from constant import blog
from chat_history import add_chat_history

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


# left_col.write(llm)
# right_col.write(embed_llm)
vector_store = None
qa_retriever = None
store = {}

with st.form("my_form"):
    blog("build")
    uploaded_file= st.file_uploader("Choose a Document")
    submitted = st.form_submit_button("Submit")
    if submitted:
        vector_store = create_vector_store(uploaded_file= uploaded_file, embed_llm=embed_llm)
        qa_retriever = vector_store.as_retriever()
        blog(f"Retriever Created ------>{qa_retriever}")
        st.write(add_chat_history(llm= llm,
                            retriever=qa_retriever,
                            store= store,
                            query = "Give me summary of the document in only 5 lines")["answer"])
        
        
# if st.button("Generate"):
#     blog(llm)
#     blog(f"Qa retriver ----> {vector_store}")
    # st.write_stream(add_chat_history(llm= llm,
    #                         retriever=qa_retriever,
    #                         store= store,
    #                         query = "Give me summary of the document in only 5 lines"))

st.session_state
# prompt = st.chat_input("Say something")
# st.button("generate", on_click=add_chat_history(llm= llm,
#                             retriever=qa_retriever,
#                             store= store,
#                             query = "Give me summary of the document in only 5 lines") )
# if llm and qa_retriever:
#     add_chat_history(llm= llm,
#                             retriever=qa_retriever,
#                             store= store,
#                             query = "Give me summary of the document in only 5 lines")
# if llm and qa_retriever:
#     response = st.write_stream(add_chat_history(llm= llm, retriever= qa_retriever, store= store, query = "what is the name of the document"))
# blog(type(prompt))
# if prompt:
    # response = add_chat_history(llm= llm, retriever= qa_retriever, store= store, query = prompt)
#     st.chat_message("user",avatar= "🧑‍💻").write(prompt)
#     st.chat_message("assistant", avatar= "🤖").write(response)


    
        
        
    