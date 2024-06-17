from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=50,
)

loader= TextLoader("facts.txt")
docs= loader.load_and_split(
    text_splitter=text_splitter
)
text= loader.load()
print(docs)