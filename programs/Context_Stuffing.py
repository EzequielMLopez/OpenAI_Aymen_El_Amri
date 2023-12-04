import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

#prompt_a= "The light is red. Determine the part of speech of the word 'light'.\n\n"
#prompt_b= "This desk is very light. Determine the part of speech of the word 'light'.\n\n"
#prompt_c= "You light up my life. Determine the part of speech of the word 'light'.\n\n"
#
#for prompt in [prompt_a, prompt_b, prompt_c]:
#    result= client.completions.create(
#        model="text-davinci-002",
#        prompt=prompt,
#        max_tokens=20,
#        temperature=0,
#    )
#    print(result.choices[0].text)
    
prompt = "Huawei:\ncompany\n\nGoogle:\ncompany\n\nMicrosoft:\ncompany\n\nApple:\n"
prompt = "Huawei:\ncompany\n\nGoogle:\ncompany\n\nMicrosoft:\ncompany\n\nApricot:\nF\
ruit\n\nApple:\n"

result= client.completions.create(
    model="text-davinci-002",
    prompt=prompt,
    max_tokens=20,
    temperature=0,
    stop=["\n", " "],
)
print(result.choices[0].text.strip())