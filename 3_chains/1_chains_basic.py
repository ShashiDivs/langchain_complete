from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert on {topic}."),
        ("human", "Tell me {Analytical} philosophy"),
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"philosophy","Analytical":"philosophy"})

print(result)