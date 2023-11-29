import os
from openai import OpenAI
from openai.types import Model
import openai
from openai import OpenAI

def init_api():
    client = OpenAI(api_key=os.environ.get("API_KEY"))
    return client
# Reading variables from .env file, namely API_KEY and ORG_ID
#with open(".env") as env:
#    for line in env:
#        key, value= line.strip().split("=")
#        os.environ[key]= value
        
# Initializing the API key and organization ID

# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=os.environ.get("ORG_ID"))'
# openai.organization= os.environ.get("ORG_ID")

# Calling the API and listing models
client= init_api()
models = client.models.list()

i = 0
while(i < len(models.data)):
    print(models.data[i].id)
    i += 1
