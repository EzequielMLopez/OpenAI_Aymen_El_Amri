import os
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)

#next= client.completions.create(
#    model="text-davinci-002",
#    #prompt="Write a JSON containing primary numbers between 0 and 9 \n\n{\n\t\"prim\
#    #    es\": [",
#    prompt="Write a JSON containing primary numbers between 0 and 9 \n\n{\n\t\"prim\
#        es\": [",
#    suffix= "]\n}",
#)

#prompt= "The first programming language to be invented was Plankalkül, which was de\
#signed by Konrad Zuse in the 1940s, but not publicly known until 1972 (and not imple\
#mented until 1998). \
#The first widely known and successful high-level programming l \
#anguage was Fortran, \
#developed from 1954 to 1957 by a team of IBM researchers led \
#by John Backus. \
#The success of FORTRAN led to the formation of a committee of scie\
#ntists to develop a universal computer language; \
#the result of their effort was AL\
#GOL 58. Separately, John McCarthy of MIT developed Lisp, the first language with o\
#rigins in academia to be successful. With the success of these initial efforts, prog\
#ramming languages became an active topic of research in the 1960s and beyond\n\nKeyw\
#ords:\n-"

prompt= "The first programming language to be invented was Plankalkül, which was de\
signed by Konrad Zuse in the 1940s, but not publicly known until 1972 (and not imple\
mented until 1998). \
The first widely known and successful high-level programming l \
anguage was Fortran, \
developed from 1954 to 1957 by a team of IBM researchers led \
by John Backus. \
The success of FORTRAN led to the formation of a committee of scie\
ntists to develop a universal computer language; \
the result of their effort was AL\
GOL 58. Separately, John McCarthy of MIT developed Lisp, the first language with o\
rigins in academia to be successful. With the success of these initial efforts, prog\
ramming languages became an active topic of research in the 1960s and beyond\n\nTweet\
with hashtags:"

tweet= client.completions.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=300,
)

print(tweet)

