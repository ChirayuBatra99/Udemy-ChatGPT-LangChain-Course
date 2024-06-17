from langchain_openai import OpenAIEmbeddings

embeddings= OpenAIEmbeddings()
from dotenv import load_dotenv
load_dotenv()

embedded_query = embeddings.embed_query("cold")
print(embedded_query)