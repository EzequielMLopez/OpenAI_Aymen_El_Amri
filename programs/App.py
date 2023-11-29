import os
from openai import OpenAI
import openai

client = OpenAI(
  api_key=os.environ['API_KEY'],  # this is also the default, it can be omitted
)

next= client.completions.create(
    model="text-davinci-003",
    prompt="Once upon a time",
    max_tokens=100,
    #temperature=2, # The next parameter we can customize is the temperature. This can be used to make the model more creative, but creativity comes with some risks.
    #logprobs=2, # To increase the possibilities, we can use the “logprobs” parameter. For example, setting logprobs to 2 will return two versions of each token.
    #top_p=.9, # Using 0.5 means only the tokens with the highest probability mass, comprising 50%, are considered
    #stream=True, # It’s possible to instruct the API to return a stream of tokens instead of a block containing all tokens.
    #frequency_penalty=2.0, # it is a number that can be between -2.0 and 2.0. If the number is positive, it makes it more likely for the model to talk about new topics, because it will be penalized if it uses words that have already been used.
    #presence_penalty=2.0, # it is a number between -2.0 and 2.0. Positive values make it less likely for the model to repeat the same line of text that has already been used.
    n=2, # If you want to have more than one result, you can use the n parameter.
    best_of=3, # It is possible to ask the AI model to generate possible completions for a given task on the server side and select the one with the highest probability of being correct
    stop=["\n", "Story", "End", "Once upon a time"], # In this case, we can ask the API to stop completing the text when there is a new line (\n).
)

# This will return <class 'generator'>
#print(type(next))

# * will unpack the generator
#print(*next, sep='\n')

# Read the generator text elements one by one, just I want the text
#for i in next:
#  #print(i['choices'][0]['text']) # OLD
#  print(i.choices[0].text)  # NEW

#print("=== Frequency and presence penalty 2.0 ===")
#print(next.choices[0].text)
#
#next= client.completions.create(
#  model="text-davinci-003",
#  prompt="Once upon a time",
#  max_tokens=100,
#  frequency_penalty=-2.0,
#  presence_penalty=-2.0,
#)
#
#print("=== Frequency and presence penalty -2.0 ===")
#print(next.choices[0].text)

print(next)
  