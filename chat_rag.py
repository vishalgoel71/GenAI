# from google import genai
# from google.genai import types

# client = genai.Client(api_key=GEMINI_API_KEY)   

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

pdf_path = Path(__file__).parent / "VishalGoel-BloodProfileReport.pdf"
GEMINI_API_KEY = "AIzaSyBj6dIh5MGaJ9ItMcuCw8ChQPex3hYmcjE"

# if not os.getenv("GOOGLE_API_KEY"):
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass(GEMINI_API_KEY)

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
print(docs[0])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
)

split_docs = text_splitter.split_documents(documents=docs)

print("Docs" , len(docs))
print("SPLIT",len(split_docs))

embedder = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07",google_api_key= GEMINI_API_KEY)

vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embedder
)

vector_store.add_documents(documents=split_docs)
print("ingestion done")

print('end')