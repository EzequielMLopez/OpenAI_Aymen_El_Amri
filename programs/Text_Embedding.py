import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

response= client.embeddings.create(
    model="text-embedding-ada-002",
    input=["I am a progammer", "I am a writer"],
)

for data in response.data:
    print(data.embedding)
