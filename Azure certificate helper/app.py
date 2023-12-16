import argparse
import os

import openai

def main():
    parser = argparse.ArgumentParser(description="Simple command line utility")
    parser.add_argument("-p", type=str, help="The prompt")

    args = parser.parse_args()
    openai.api_key = os.environ["OPENAI_API_KEY"]

    while True:
        try:
            print("\n\n")
            print("Your Question:")
            user_input = input()
            answer = get_answer(user_input)
            print(answer)
        except KeyboardInterrupt:
            print("Exiting...")
            break

def get_answer(prompt):
    messages = [
        {"role": "system", "content": """You are an expert Azure Developer with a broad knowlage of the azure platform 
        and azure ecosystem, i will ask you some questions that i have for the azure 204 exam, you will provide me with answer(s) and explanation on those questions. 
        Response should be in format: 
         Answer: 
		 <assistant_answer>
		 Explanation:
         <assistant_explanation> 
        """   
        },
        {"role": "user", "content": f"{prompt}"},
    ]

    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-4"
    )

    answer = response["choices"][0]["message"]["content"]
    return answer

if __name__ == "__main__":
    main()
