import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with gpt-3.5")
    parser.add_argument("--personality", type=str, help="A brief summary about chatbot personality", default= "Friendly and helpful chatbot")

    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role": "system","content": initial_prompt}]
    
    while True:
        try:
            user_input = input("You: ")

            messages.append({"role": "user","content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            
            messages.append(response["choices"][0]["message"].to_dict())
            print("Assistant: ", response["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(response)

if __name__ == "__main__":
    main()