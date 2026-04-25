import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

#load the environment API Key + get the connection
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#add a parser for user entry
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str,help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


#check if API key is valid
if api_key == None:
    raise RuntimeError("API Key not found")


def main():
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
    )


    if response.usage_metadata == None:
        raise RuntimeError("failed API request")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)

if __name__ == "__main__":
    main()
