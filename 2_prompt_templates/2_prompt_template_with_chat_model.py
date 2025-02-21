from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

# print("----------Prompt from template----------")
# template = "Tell me a joke about {topic}."
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({"topic":"cats"})
# result = model.invoke(prompt)
# print(result.content)


# template_multiple = """You are a helful assistant
# Human: Tell me a {adjective} story about a {animal}
# Assistant:"""

# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective":"funny","animal":"pandas"})
# print("\n--------Prompt with multiple placeholders-----------------\n")
# response = model.invoke(prompt)
# print(response.content)



# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}"),
#     ("human","tell me {joke_count} jokes"),

# ]

# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic":"lawyers","joke_count":3})
# print("\n--------Prompt with System and Human Messsages-----------------\n")
# response = model.invoke(prompt)
# print(response.content)



messages = [
    ("system","You are a comedian whho tells jokes about {topic}"),
    HumanMessage(content="Tell me 3 jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"lawyers"})
print("\n--------Prompt with System and Human Messsages (Tuple)-----------------\n")
response = model.invoke(prompt)
print(response.content)