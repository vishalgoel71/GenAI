from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key="",
    api_version="",  # Use the version matching your deployment
    azure_endpoint=""
)

text = "Eifil Tower is famous in Paris and its a great landmark which is 324m tall"

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small",

)

print("Vector Embeddings", response.data[0].embedding)