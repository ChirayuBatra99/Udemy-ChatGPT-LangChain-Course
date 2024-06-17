from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate
from  langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

llm= OpenAI()

prompt = PromptTemplate(
    input_variables=["foo"], template="Tell me about {foo}"
)

code_chain= LLMChain(
    llm=llm,
    prompt= prompt,
    output_key= "code"
)

result= code_chain({
    "foo": "Molecule"
})

print(result)



#Left argparser and sequential chain.