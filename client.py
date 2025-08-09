from openai import OpenAI

client = OpenAI(
  api_key="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"
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named google skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)