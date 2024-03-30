# tag::llm[]
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
import getpass
import os

# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = "AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac"

# llm = ChatOpenAI(
#     openai_api_key=st.secrets["OPENAI_API_KEY"],
#     model=st.secrets["OPENAI_MODEL"],
# )
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac")
# end::llm[]

# tag::embedding[]
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac")

# import streamlit as st
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(
#     openai_api_key="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",
#     model="gpt-3.5-turbo",
# )
# from langchain_openai import OpenAIEmbeddings

# embeddings = OpenAIEmbeddings(
#     openai_api_key="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"
# )
# end::embedding[]
