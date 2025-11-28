import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Command line prompt
    try:
        user_prompt = sys.argv[1]
    except IndexError:
        print("No prompt provided")
        sys.exit(1)

    is_verbose = "--verbose" in sys.argv

    # Init api client
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )
    print(response.text)
    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {getattr(response.usage_metadata, 'prompt_token_count', None)}")
        print(f"Response tokens: {getattr(response.usage_metadata, 'candidates_token_count', None)}")



if __name__ == "__main__":
    main()
