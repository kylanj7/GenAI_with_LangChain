## Basic Examples

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from config import set_environment
set_environment()

from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI

gemini_pro = GoogleGenerativeAI(model="gemini-2.0-flash")

openai_llm = OpenAI()

response = gemini_pro.invoke("Tell me a joke about light bulbs!")
print(response)

