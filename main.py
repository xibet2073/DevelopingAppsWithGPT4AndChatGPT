from dotenv import load_dotenv
load_dotenv()
import openai
import os

def chat_with_gpt3():

    # Load the .env file to get OpenAI key
    load_dotenv("api_key.env")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Call the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello World!"}],
    )

    # Extract the response
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    chat_with_gpt3()