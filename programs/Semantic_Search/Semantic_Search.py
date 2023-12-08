import os
import numpy as np
import pandas as pd
from openai import OpenAI

client= OpenAI(
    api_key=os.environ["API_KEY"]
)


