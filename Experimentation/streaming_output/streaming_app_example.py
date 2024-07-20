from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import HumanMessage
import streamlit as st
from langchain_community.llms.ctransformers import CTransformers


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text="", display_method='markdown'):
        self.container = container
        self.text = initial_text
        self.display_method = display_method

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # self.text += token + "/"
        self.text += token + ""
        display_function = getattr(self.container, self.display_method, None)
        if display_function is not None:
            display_function(self.text)
        else:
            raise ValueError(f"Invalid display_method: {self.display_method}")

query = st.text_input("input your query", value="Tell me a joke")
ask_button = st.button("ask")

st.markdown("### streaming box")
chat_box = st.empty()
stream_handler = StreamHandler(chat_box, display_method='write')
chat = CTransformers( 
              model= r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models",
              model_file = "capybarahermes-2.5-mistral-7b.Q3_K_M.gguf",
              callbacks=[stream_handler],
              config = {"context_length": 16000, "max_new_tokens": 3000})

st.markdown("### together box")

if query and ask_button:
    response = chat.invoke(query)
    st.markdown(response)