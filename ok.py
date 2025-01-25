from dotenv import load_dotenv
# Ensure your VertexAI credentials are configured

from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model="gemini-1.5-flash")

load_dotenv()

def generate_pet_name():
    llm = model(temperature = 0.5)  # Set the temperature to 0.5 for a balance between creativity and coherence
    name = llm("i have a pet dog suggest me some cool name for my pet!!")

    return name

if __name__ == "__main__":
    print(generate_pet_name())




