import getpass
import os

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools


from langchain.agents import initialize_agent
from langchain.agents import AgentType


# model = ChatGroq(model="llama3-8b-8192", temperature=0.5)
# response = model.invoke("Who is pradip?")
# print(response)

def generate_pet_name(animal_type, pet_colour):
  llm = ChatGroq(model="llama3-8b-8192", temperature=0.5)  # Set the temperature to 0.5 for a balance between creativity and coherence

  prompt_template_name = PromptTemplate(
  input_variables = ["animal_type", "pet_colour"], 
  template = "i have a pet {animal_type} and it is {pet_colour} in colour. Suggest me 5 cool name for my pet!!"
  )

  name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key = "pet_name")
  response = name_chain({'animal_type': animal_type, 'pet_colour': pet_colour})
  return response

def langchain_agent():
  llm = ChatGroq(model="llama3-8b-8192", temperature=0.5)
  tools = load_tools(["wikipedia", "llm-math"])

  agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
  )

  result = agent.run(
    "what is the average age of the dog? Multiply the age by 2"
  )

if __name__ == "__main__":
  print(langchain_agent)
#   print(generate_pet_name("dog", "black"))


