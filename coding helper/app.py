import argparse
import os
import openai

def main():
    parser = argparse.ArgumentParser(description="Simple command line utility")
    parser.add_argument("-p", type=str, help="The prompt")
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Initialize messages with bot 'system' role message
    messages = [
        {
        "role": "system",
        "content": "The system is expected to function as an expert software developer with a comprehensive understanding across various domains and programing languages gained from 30 years of professional experience. Additionally, it should serve as a helpful assistant, providing prompt and accurate responses to user queries and offering valuable guidance."
        }]

    # Chat loop
    while True:
        try:
            print("\n\n")
            print("Your Question:")
            user_input = input()
            # Appending the user message to conversation
            messages.append({"role": "user", "content": user_input})
            # Get answer function now includes 'messages'
            answer = get_answer(messages)
            # Appending the bot's response to the conversation
            messages.append({"role": "assistant", "content": answer})
            print(answer)
        except KeyboardInterrupt:
            print("Exiting...")
            break

def get_answer(messages):
    response = openai.ChatCompletion.create(messages=messages, model="gpt-4")
    answer = response["choices"][0]["message"]["content"]
    return answer

if __name__ == "__main__":
    main()