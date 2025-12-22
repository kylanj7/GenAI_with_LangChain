## Working with Prompts

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from config import set_environment
set_environment()

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

llm = GoogleGenerativeAI(model="gemini-1.5-pro")

story_prompt = PromptTemplate("Write a short story about {topic}")
story_chain = story_prompt | llm | StrOutputParser()

analysis_prompt = PromptTemplate.from_template(
    "Analyze the following stoy's mood:\n{story}"
)
analysis_chain = analysis_prompt | llm | StrOutputParser()

story_with_analysis = story_chain | analysis_chain

story_analysis = story_chain | analysis_chain

story_analysis = story_with_analysis.invoke({"topic": "a rainy day"})
print("\nAnalysis:", story_analysis)

## LLM's and Prompts

from lang_chain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

template = """
summarize this text in one sentence:

{test}
"""
llm = GoogleGenerativeAI(model"gemini-1.5-pro")

prompt = PromptTemplate.from_template(template)

formatted_prompt = prompt.format(tezt="Some long story about AI...")

result = llm.invoke(formatted_prompt)
print(result)
