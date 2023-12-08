import os
import click
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

_prompt= """
Input: List all the files in the current directory
Output: ls -l

Input: List all the files in the current directory, including hidden files
Output: ls -la

Input: Delete all the files in the current directory
Output: rm *

Input: Count the number of occurrences of the word "sun" in the file "test.txt"
Output: grep -o "sun" test.txt | wc -l

Input: {}
Output:"""

while True:
    #request= input(click.style("Input", fg="green"))
    #prompt= _prompt.format(request)
    #result= client.completions.create(
    #    model="text-davinci-002",
    #    prompt=prompt,
    #    temperature=0.0,
    #    max_tokens=100,
    #    stop=["\n"],
    #)
    #
    #command= result.choices[0].text.strip()
    #click.echo(click.style("Output: ", fg="yellow") + command)
    #click.echo()

    request= input(click.style("Input (type 'exit' to quit): ", fg="green"))
    
    if request == "exit":
        break
    
    prompt= _prompt.format(request)
    
    try:
         
        result= client.completions.create(
                model="text-davinci-002",
                prompt=prompt,
                temperature=0,
                max_tokens=100,
                stop=["\n"],
        )

        command= result.choices[0].text.strip()
        
        click.echo(click.style("Output: ", fg="yellow") + command)
        click.echo(click.style("Execute? (y/n): ", fg="yellow"), nl=False)
        
        choice= input()

        if choice == "y":
            os.system(command)
        elif choice == "n":
            continue
        else:
            click.echo(click.style("Invalid choice. Please enter 'y' or 'n'.", fg="red"))
    
    except Exception as e:
        click.echo(click.style("The command could not be executed. {}".format(e), fg="red"))
            
    click.echo()
    

#result= client.completions.create(
#    model="text-davinci-002",
#    prompt=prompt.format("Count the number of files in the current directory"),
#    max_tokens=200,
#    temperature=0,
#)

#print(result.choices[0].text.strip())

