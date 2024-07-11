from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

app = FastAPI()

# Function to load, split, and store content
def load_split_store(url):
    # Load content from the web
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("abtsdm-homosecwptinfo leadership-msg")
            )
        ),
    )
    docs = loader.load()
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    
    # Store embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=embeddings)
    
    return vectorstore

# Function to retrieve documents based on a query
def retrieve_documents(vectorstore, query):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    retrieved_docs = retriever.invoke(query)
    if retrieved_docs:
        return retrieved_docs[0].page_content
    return "No documents found matching the query."

# Pydantic model for request
class QueryRequest(BaseModel):
    url: str
    query: str

# Pydantic model for response
class QueryResponse(BaseModel):
    result: str

# Endpoint to handle query
@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    vectorstore = load_split_store(request.url)
    result = retrieve_documents(vectorstore, request.query)
    return QueryResponse(result=result)


