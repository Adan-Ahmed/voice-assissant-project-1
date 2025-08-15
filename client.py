from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()  # loads .env from the current working directory

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Is your .env in the project root?")

client = OpenAI(api_key=api_key)

resp = client.chat.completions.create(
    model="gpt-3.5-turbo",  # you can change this later
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Google skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)
print(resp.choices[0].message.content)