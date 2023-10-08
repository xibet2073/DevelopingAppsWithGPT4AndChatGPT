import openai
import os

def chat_with_gpt3():
    # Read the OpenAI API key from a file
    with open('api_key.txt', 'r') as f:
        api_key = f.read().strip()

    # Set the OpenAI API key
    openai.api_key = api_key

    # Call the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello World!"}],
    )

    # Extract the response
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    chat_with_gpt3()