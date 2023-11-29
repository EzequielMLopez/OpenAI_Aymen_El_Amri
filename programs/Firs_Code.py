import os
from openai import OpenAI
from openai.types import Model
import openai

client = OpenAI(
  api_key=os.environ['API_KEY']  # this is also the default, it can be omitted
)

# Calling the API and listing models
modeles = client.models.list()

i = 0
while(i < len(modeles.data)):
    print(modeles.data[i].id)
    i += 1
