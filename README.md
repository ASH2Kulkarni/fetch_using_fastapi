# fetch_using_fastapi

This FastAPI application provides an API endpoint to retrieve relevant content from a specified URL based on a user query. The application performs the following steps:
1)Load Content from the Web
1)Split Documents into Chunks
3)Store and Retrieve Document Embeddings

Dependencies
The application relies on several external libraries, including:

FastAPI for creating the API.
Pydantic for data validation and parsing.
bs4 (BeautifulSoup) for web content parsing.
langchain_community.document_loaders for loading web content.
langchain_text_splitters for splitting text into chunks.
langchain_huggingface for generating text embeddings.
langchain_chroma for storing and retrieving document embeddings.

you can change the url and query in request.py according to your needs and also the class you want to fetch data from in FASTAPI.py
