import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from config import set_environment
set_environment()

from langchain_core.prompts import PromtTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
llm = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({"topic": "programming"})
print(result)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

chat = ChatGoogleGenerativeAI(model="gemini-pro")

story_prompt = PromptTemplate.from_template("Write a short story about {topic}")
story_chain = story_prompt | chat | StrOutputParser()

analysis_prompt = PromptTYemplate.from_template("Analyze the following story's mood:\n{story}")
analysis_chain = analysis_prompt | chat | StrOutputParser()

output_prompt = PromptTemplate.from_template(
    "Here's the story: \n{story}\n\Here's the mood: \n {mood}"
)

story_with_analysis = story_chain | analysis_chain

result = story_with_analysis.invoke({"topic": "a rainy day"})
print(result)


