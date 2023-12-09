import os
import openai
from dotenv import load_dotenv
import argparse

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def main():
    parser = argparse.ArgumentParser(description="Simple command line utility")
    parser.add_argument("--personality", type=str, help="A brief summary about chatbot personality", default= "Friendly and helpful chatbot")
    parser.add_argument("--envfile", type=str, default=".env", required=False, help='A dotenv file with your environment variables: "OPENAI_API_KEY" ')

    args = parser.parse_args()
    
    load_dotenv(args.envfile)

    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("Error: missing OPENAI_API_KEY fro menvironment. Please check your env file.")
    
    openai.api_key = os.environ["OPENAI_API_KEY"]

    personality = args.personality

    prompt_message = "You are a conversational chatbot."
    if personality:
        prompt_message+= f"Your personality is: {personality}"
    else:
        prompt_message += "Your personality is: friendly and helpful."

    messages = [{"role": "system", "content": prompt_message}]

    print("Type a message. Hit <Enter> to submit or <CTRL+C> to exit")

    while True:
        try:
            user_input = input(bold(blue("You: ")))

            messages.append({"role": "user","content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages)
            
            messages.append(response["choices"][0]["message"].to_dict())
            print(bold(red("Assistant: ")), response["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("Exiting...")
            break

    print(response)

if __name__ == "__main__":
    main()