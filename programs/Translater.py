import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

#response= client.edits.create(
#    model="text-davinci-edit-001",
#    input="Hallo Welt",
#    instruction="Translate to Spanish",
#)

#response= client.edits.create(
#    model="text-davinci-edit-001",
#    instruction="Translate the following sentence to Spanish: 'Hallo Welt'",
#)

#response = client.edits.create(
#model="text-davinci-edit-001",
#instruction="Translate from English to French, Arabic, and Spanish.",
#input="The cat sat on the mat."
#)

# next= client.completions.create( ESTA ES LA FORMA CORRECTA
#    model="text-davinci-003",
#    prompt="""
#    Translate the following sentence from English to French, Arabic, and Spanish.
#    English: The cat sat on the mat.
#    French:
#    Arabic:
#    Spanish:
#    """,
#    max_tokens=60,
#    temperature=0
#)

#response = client.edits.create(
#    model="text-davinci-edit-001",
#    instruction="Complete the story",
#    input="Once upon a time",
#)

next= client.completions.create(
    model="text-davinci-003",
    prompt="""
    Explain the following Golang code in Spanish:
    package main

    import (
        "io/ioutil"
        "log"
        "net/http"
    )

    func main() {
        resp, err := http.Get("https://website.com")
        if err != nil {
            log.Fatalln(err)
    }
    
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        log.Fatalln(err)
    }
     
    sb := string(body)
    log.Printf(sb)      
}""",
    max_tokens=100,
    temperature=0,
)

response= client.edits.create(
    model="text-davinci-edit-001",
    instruction="Explain the following Golang code:",
    input="""
package main
import (
    "io/ioutil"
    "log"
    "net/http"
)

func main() {
    resp, err := http.Get("https://website.com")
    if err != nil {
        log.Fatalln(err)
    }

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        log.Fatalln(err)
    }
 
    sb := string(body)
    log.Printf(sb) 
}
""",
)

print(response.choices[0].text)
#print(next.choices[0].text)