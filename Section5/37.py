from langchain.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

load_dotenv()
embeddings= OpenAIEmbeddings()

text_splitter= CharacterTextSplitter(
    chunk_size= 200,
    separator = "\n",
    chunk_overlap= 0
)

loader= TextLoader("facts.txt")
docs= loader.load_and_split(
    text_splitter= text_splitter
)

db = Chroma.from_documents(
    documents=docs,
    embedding= embeddings,
    persist_directory="emb"
)

result = db.similarity_search("Who is Neil Armstrong")
print(result[0].page_content)

