from google import genai
from google.genai import types

GEMINI_API_KEY = "AIzaSyCWPBYsoyLo-q4SuuL_Iv6FfzNUmzhkMZM"
client = genai.Client(api_key=GEMINI_API_KEY)

system_prompt = """
You are an AI assistant who is specialized in solving problems related to Maths.
DO NOT ANSWER any query which is not related to Maths

Provide explanation to the problem you are solving.

Example:

Input: What is 2*3
Output: 2 * 3 = 6. When two is multiplied by 3 then answer is 6

Input: What is 6- 3 * 2
Output: The answer is 0. Multiplication operator takes priority here. 3*2 = 6 and 6-6 =0 

Input: Why is sky Blue?
Output: Sorry, I am capable of solving only Maths problem. 

"""

user_query = "What is the capital of India ?"

system_prompt += user_query
response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=system_prompt
)

print(response.text)
