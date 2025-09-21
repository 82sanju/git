# main.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- 1. INITIAL SETUP ---

# Load environment variables (your OPENAI_API_KEY)
load_dotenv()

# Check if the API key is loaded
if os.getenv("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY is not set in the .env file")

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

# --- 2. DATA LOADING AND PROCESSING (The RAG Pipeline) ---

# Load the PDF document from the data directory
loader = PyPDFLoader("./data/document.pdf")
docs = loader.load()

# Split the document into smaller chunks for processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Create a vector store using OpenAI embeddings and ChromaDB
# This will embed the document chunks and store them locally
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Create a retriever to fetch relevant documents
retriever = vectorstore.as_retriever()

# --- 3. PROMPT AND CHAIN DEFINITION ---

# Define the prompt template
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Initialize the Language Model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Create the RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 4. API ENDPOINT ---

# Define the request body model
class Query(BaseModel):
    text: str

@app.post("/query")
async def handle_query(query: Query):
    """
    Receives a user query, processes it through the RAG chain,
    and returns the model's answer.
    """
    try:
        question = query.text
        answer = rag_chain.invoke(question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

# A simple root endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"status": "Server is running"}