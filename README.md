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
To run the FastAPI application, you need to use uvicorn. In the terminal or command prompt, navigate to the directory where your main.py file is located and run:uvicorn main:app --reload

Access the API
Once the server is running, you can access the API at http://127.0.0.1:8000. You can use tools like Postman, curl, or even a web browser to interact with your API.

Using curl
Open a terminal and run:
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{
    "url": "https://example.com",
    "query": "your query here"
}'
Replace "https://example.com" with the URL you want to load and "your query here" with your query string.
