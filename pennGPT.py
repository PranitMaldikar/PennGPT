import os 
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import streamlit as st 
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

persist_directory = "./storage"
pdf_path = "./edited_mergedData.pdf"

loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=texts, 
                                 embedding=embeddings,
                                 persist_directory=persist_directory)
vectordb.persist()

retriever = vectordb.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model_name='gpt-4')

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

logo_path = "./logo.jpg"

st.image(logo_path, width=100)
st.title('PennGPT')

user_input = st.text_input("Enter a query: ")
if user_input:
    query = f"###Prompt {user_input}"
    try:
        llm_response = qa(query)
        st.write(llm_response["result"])
    except Exception as err:
        print('Exception occurred. Please try again', str(err))
