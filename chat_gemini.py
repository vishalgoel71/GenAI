from google import genai
from google.genai import types

GEMINI_API_KEY = "AIzaSyCWPBYsoyLo-q4SuuL_Iv6FfzNUmzhkMZM"
client = genai.Client(api_key=GEMINI_API_KEY)

system_prompt = """
You are an AI assistant. You are an expert in breaking down complex problems and then resolve user query.
For the given user input, analyse the input and break down the problem step by step.
Atleast think 5 6 steps on how to solve the problem before solving it down.

The steps are you get a user query, you think, you analyze, you think , you again think for several times and then return an output with explanation and finally you validate the output as well before giving final result

Follow the steps in sequence that is "analyze", "think", "output","validate", "result"

Example: 
Input: What is 2 + 2
Output : {{step: "analyze", content: "Alright! user is interested in solving a maths query and he is asking a basic mathematic operation."}}
Output : {{step: "think", content: "To perform arithmatic operation, i must go from left to right and following all the operands"}}
Output : {{step: "output", content: "4"}}
Output : {{step: "validate", content: "Seems like 4 is correct output"}}
Output : {{step: "result", content: "2+2 = 4. That is hy summing all numbers"}}

Rules:

1. Follow the strict json output as per output schema
2. Always perform one step at a time and wait  for next input
3. carefully analyze the user query.

Output format:
{{step: "string", content : "string"}}

"""

user_query = "What is 3+4 *5"
system_prompt += user_query
system_prompt += '{{step: "analyze", content: "The user is asking to evaluate an arithmetic expression: 3 + 4 * 5. I need to remember the order of operations (PEMDAS/BODMAS) to solve this correctly."}}'
system_prompt += '{{step: "think", content: "I must apply the order of operations. Multiplication comes before addition. So, I need to multiply 4 and 5 first, and then add the result to 3."}}'
system_prompt += '{{step: "output", content: "First, calculate 4 * 5 which equals 20."}}'
system_prompt += '{{step: "validate", content: "4 multiplied by 5 is indeed 20. The multiplication step is validated."}}'

response = client.models.generate_content(model="gemini-2.0-flash-001", contents=system_prompt)
print(response.text)