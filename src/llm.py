import os
from dotenv import load_dotenv
from google import genai


def get_llm():
    """Return a client that can talk to Gemini."""
    load_dotenv()                      # reads the .env file
    api_key = os.getenv("GOOGLE_API_KEY")         # which name did you use in .env?
    return genai.Client(api_key=api_key)


if __name__ == "__main__":
    client = get_llm()
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="what is revenue",                # your question
    )
    print(response.text)                # which part holds the answer text?