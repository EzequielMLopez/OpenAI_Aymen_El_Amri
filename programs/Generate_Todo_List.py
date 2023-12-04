import os
from openai import OpenAI


client= OpenAI(
    api_key=os.environ["API_KEY"]
)

next= client.completions.create(
    model="text-davinci-002",
    prompt="Todo list to create a company in US\n\n1.",
    temperature=0.3,
    max_tokens=64,
    top_p=0.1,
    frequency_penalty=0,
    presence_penalty=0.5,
    stop=["6."]
)

print(next.choices[0].text)


