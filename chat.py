import openai
from openai import AzureOpenAI

# Specify the deployment name (not the model name)
deployment_name = "turbo-16k"


# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key="",
    api_version="",  # Use the version matching your deployment
    azure_endpoint=""
)

# Send chat completion request
response = client.chat.completions.create(
    model="turbo-16k",  # This is the deployment name, NOT the model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
    ],
    temperature=0.7,
    max_tokens=100
)

# Print the response
print(response.choices[0].message.content)
