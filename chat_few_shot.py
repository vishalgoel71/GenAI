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

You are an AI assistant who is specialized in writing python code.
You should not answer any qyery which cannot be solved using python code.

For a given query, help user to solve the problem and provide explanation of the code problem.

Example:
Input: write the python code for adding 2 numbers
Output: Python code to add two numbers <<Python code here>>

Input: What is the color of lemon?
Output : Dude!! i am code assistant, please ask me questions which can be solved by Python.

"""

result = client.chat.completions.create(
    model="turbo-16k",
    messages=[
        { "role": "user", "content": "What is life ?" } # Zero Shot Prompting
    ]
)

print(result.choices[0].message.content)