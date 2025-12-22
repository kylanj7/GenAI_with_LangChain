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

from langchain_community.llms import FakeListLLM

fake_llm = FakeListLLM(responses=["Hello"])

sesult = fake_llm.invoke("Any input will return Hello")
print(Result)

from langchain_anthropic import ChatAnthropic

from langchain_core.messages import SystemMessage, HumanMessage

chat = ChatAnthropic(model="claude3-opus-20240229")

messages = [
    SystemMessage(content="You're a helpful programming assistant")
    HumanMessage(content="Write a Python function to calculate factorial")
]
response = chat.invoke(messages)
print(response.content)
