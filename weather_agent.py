from google import genai
from google.genai import types
import json
import re

GEMINI_API_KEY = "AIzaSyCWPBYsoyLo-q4SuuL_Iv6FfzNUmzhkMZM"
client = genai.Client(api_key=GEMINI_API_KEY)

def get_weather(city: str) :
    print('Tool called for fetching weather of ' + city)
    return f"32 degree celcius"  

available_tools = {
    'get_weather' : {
        'fn': get_weather,
        'description': "Takes the city name as input and return weather as output "
    }
}

system_prompt = """
You are an helpful AI assistant who is specialized in resolving user query.
You work on start, plan, identify tool, action, observe mode.
For the given user query and available tools, plan the step by step execution based on the planning, 
select the relevant tool from the available tools and based on the tool selection you perform an action to call the tool.
Wait for the observation and based on the observation from the tool call, return the final output to the user.
Perform only one step at a time. DO NOT perform more than one step in single iteration.

Rules:

1. Follow the Output Json Format
2. Always perform single step at a time and wait for next input
3. carefully analyze the user query.

Output format:
{{step: "string", content : "string", "function" : "Name of the function in case of action", "input" :"Input parameter for the function"}}

Available Tools: get_weather to get the weather using external API

Example: 
User Query : What is the weather of New York?
Output : {{"Step": "plan", "content":"The user is interested in knowing the weather of New York" }}
Output : {{"Step": "identify tool", "content":"From the available tools, i should call get_weather" }}
Output : {{"Step": "action", "function":"get_weather" input :"New York " }}
Output : {{"Step": "Observe", "Output":"12 Degree celcius" }}
Output : {{"Step": "Output", "content":"Weather of New york seems to be 12 Degree celcius" }}

"""

user_query = "What is the current weather of Noida"
system_prompt += user_query

while True :
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=system_prompt)
    # print(response.text)

    cleaned_str = re.sub(r'^```json\n|```$', '', response.text.strip(), flags=re.MULTILINE)
    # Step 2: Fix double curly braces (turn `{{ ... }}` into `{ ... }`)
    cleaned_str = cleaned_str.replace('{{', '{').replace('}}', '}')

    data = json.loads(cleaned_str)
    if data['step'] == 'plan' or data['step'] == 'identify tool' or data['step'] == 'Observe':
        print(cleaned_str)
        system_prompt += json.dumps(data)
        continue
    elif data['step'] == 'action':
        function = data['function']
        input = data['input']

        if(available_tools.get(function,False)) != False :
            output = available_tools[function].get('fn')(input)
            system_prompt += json.dumps({"step":"observe","output":output}) 
    elif data['step'] == 'Output':
        print(cleaned_str)
        break
