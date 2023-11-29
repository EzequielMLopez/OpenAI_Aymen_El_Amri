import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

my_song= client.completions.create(
    model="text-davinci-002",
    prompt="Write a rap song:\n\n",
    max_tokens=200,
    temperature=1.0,
)

print(my_song.choices[0].text.strip())
