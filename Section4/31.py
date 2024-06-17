from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader

loader= TextLoader("facts.txt")
text= loader.load()
print(text)