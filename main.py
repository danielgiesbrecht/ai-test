from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

#llm =GoogleGenerativeAI(model="gemini-pro")
# print(
#     llm.invoke(
#         "qual é o maior peixe do mundo?"
#     )
# )

llm =ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

prompt=ChatPromptTemplate.from_template("crie um mapa mental para aprender {input}")
model=prompt|llm

st.set_page_config(page_title='Teste de Gemini')
st.header ('Teste de Gemini')
entrada=st.text_input(label='prompt')
botao=st.button(label='Enviar')

if(botao):
    res=model.invoke({'input':entrada})
    st.write(res.content)

# para rodar com o streamlit
# streamlit run main.py