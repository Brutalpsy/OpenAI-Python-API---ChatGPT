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

def code_review(file_path, model):
    with open(file_path,"r") as file:
        content = file.read()
    generated_code_review = make_code_review_request(content, model)
    print(generated_code_review)


def make_code_review_request(fileContent, model):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"Code review the following file: {fileContent}"}
    ]

    result = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return result["choices"][0]["message"]["content"]


code_review("./sample/tree.py","gpt-4")

