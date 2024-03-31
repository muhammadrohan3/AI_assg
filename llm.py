# tag::llm[]
from langchain_openai import OpenAIEmbeddings
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
import getpass
import os
from langchain_community.llms import EdenAI
from langchain_community.embeddings.edenai import EdenAiEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings
# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = "AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac"

# llm = ChatOpenAI(
#     openai_api_key=st.secrets["OPENAI_API_KEY"],
#     model=st.secrets["OPENAI_MODEL"],
# )
# llm = EdenAI(edenai_api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTIwNTUwNjAtZmY2Yy00NDZiLWExNjctOTA4Y2U3N2NmZWMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.LFC2hFeYGwOKBjqcbMfQWU50GIkqAHiC62TzhH0Sma4", provider="openai", temperature=0.2, max_tokens=250)
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac")
# end::llm[]

# tag::embedding[]
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyBj6QnDxwNSqrK-003OKbvrKY7ctNqReac", dimensionality=1536)
embeddings = EdenAiEmbeddings(edenai_api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTIwNTUwNjAtZmY2Yy00NDZiLWExNjctOTA4Y2U3N2NmZWMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.LFC2hFeYGwOKBjqcbMfQWU50GIkqAHiC62TzhH0Sma4", provider="openai")




# model_name = "sangmini/msmarco-cotmae-MiniLM-L12_en-ko-ja"
# model_kwargs = {'device': 'cpu'}
# encode_kwargs = {'normalize_embeddings': False}
# embeddings = HuggingFaceEmbeddings(
#     model_name=model_name,
#     model_kwargs=model_kwargs,
#     encode_kwargs=encode_kwargs,
# )
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

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTIwNTUwNjAtZmY2Yy00NDZiLWExNjctOTA4Y2U3N2NmZWMwIiwidHlwZSI6ImFwaV90b2tlbiJ9.LFC2hFeYGwOKBjqcbMfQWU50GIkqAHiC62TzhH0Sma4"