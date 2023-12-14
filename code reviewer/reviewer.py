import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
You will receive a file's contents as text.
Generatea code review for a file. Indicate what changes should be made to imporve
it's style, pefromance, readability and mentainability. If there are any reputable libraries that could be introduced to imporve the code,
suggest them. Be kind and constructive. For each suggested change, include line numbers to which are you referring
"""

fileContent = """
    def mystery(x,y)
        return x ** y
"""

messages = [
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": f"Code review the following file: {fileContent}"}
]

result = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)

print(result["choices"][0]["message"]["content"])

