# for i in range(9,10):
#     print("Hi", i)


# from langchain.llms import openai
from langchain_openai import OpenAI


from dotenv import load_dotenv
load_dotenv()

llm= OpenAI()
place= input("enter here bro\n")
prompt=f"tell me a good software for music production on mac"
print(prompt)
ans= llm(prompt=prompt)
print(ans)
