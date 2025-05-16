from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key="",
    api_version="",  # Use the version matching your deployment
    azure_endpoint=""
)

system_prompt = """
CONTEXT : Current weather in Delhi is sunny 28 degree celcius

"""

system_prompt += "What is the current weather in Delhi"
result = client.chat.completions.create(
    model="turbo-16k",
    messages=[
        { "role": "user", "content": system_prompt } # Zero Shot Prompting
    ]
)

print(result.choices[0].message.content)