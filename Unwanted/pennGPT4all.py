from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


pdf_path = "./mergedData.pdf"
loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings

vectorstore = Chroma.from_documents(documents=texts, embedding=GPT4AllEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

model_path = ("C:\\Users\\prani\\.cache\\gpt4all\\nous-hermes-llama2-13b.ggmlv3.q4_0.bin")
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
# ("./models/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin")

callbacks = [StreamingStdOutCallbackHandler()]
llm = GPT4All(model=model_path, callbacks=callbacks, verbose=True)
llm = GPT4All(model=model_path, backend="gptj", callbacks=callbacks, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.run(question)
# qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# while True:
#         user_input = input("Enter a query: ")
#         if user_input == "exit":
#             break

#         query = f"###Prompt {user_input}"
#         try:
#             llm_response = qa(query)
#             print(llm_response["result"])
#         except Exception as err:
#             print('Exception occurred. Please try again', str(err))