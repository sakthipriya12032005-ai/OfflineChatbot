import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
llm = ChatOllama(model="gemma:2b")
prompt = ChatPromptTemplate.from_template("you are an helpful chatbot able to respond to the query {query} by relating it with anything")
chain = prompt | llm | StrOutputParser()
st.title("Chatbot :robot_face:")
user_query = st.text_input("I am your chatbot, Feel free to ask anything to me :blush: :")
def get_response(query):
    return chain.invoke({"query": query})
if st.button("Send"):
    bot_response = get_response(user_query)
    st.write(":robot_face::", bot_response)