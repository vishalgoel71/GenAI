from google import genai
from google.genai import types
import json

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

user_query = "What came first? Egg or chicken "
# user_query = "What is Greater ? 9.8 or 9.11 "

system_prompt += user_query

while True :
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=system_prompt)
    print(response.text)
    clean_data = response.text.strip('{}')  # Remove the outer double braces
    clean_data = '{' + clean_data + '}'  # Add single JSON-compatible braces
    # Step 2: Replace unquoted keys with quoted ones (if needed)
    clean_data = clean_data.replace('step:', '"step":').replace('content:', '"content":').replace('}\n}','').replace('\n','').replace('}{','')
    
    parsed_response = json.loads(clean_data)
    if parsed_response.get("step") == "result" :
        break
    system_prompt += response.text
