import openai
import sys

openai.api_key = "YOUR KEY"

try:
    openai.Completion.create(
        engine="davinci",
        prompt="Hello, world!",
        max_tokens=5
    )
    print("API key is valid.")
except Exception as e:
    print("API key is not valid.")
    sys.exit()
