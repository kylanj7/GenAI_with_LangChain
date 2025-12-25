
import logging
from enum import Enum
from lanchain_core.language_core.language_models import GenericFakeChatModel
from langchain_core.messages import AIMessage
from langchain.output_parsers import EnumOutputParser
from langchain_google_vertexai import ChatVertexAI
from typing_extensions import TypedDict
from typing import Annotated, Literal
from operator import add
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables.config import RunnableConfig

class IsSuitableJobEnum(Enum):
    YES = "YES"
    NO = "NO"

parser = EnumOutputParser(enum=IsSuitableJobEnum)
    "Given a job description, decide whether it suites a junior Java developer."
    "\nJOB DESCRIPTION:\n{job_description}\n\nAnswer only YES or NO."

job_description = "test job description"

llm = ChatVertexAI(model="gemini-2.0-flash")
analyze_chain = llm | parser

logger = logging.getlogger(__name__)

def analyze_job_description(state):
    try:
      prompt = prompt_template_enum.format(job_description=job__description)
      result = analyze_chain.invoke(prompt)
      return {"is_suitable": result)
    except Exception s e:
      logger.error(f"Exception {e} occured while executing analyze_job_description")
      return {is_suitable": False
    
class MessagesIterator:
    def __init__(self):
        self._count = 0

    def __iter__(self):
        self._count += 1
        if self._count % 2 == 1:
            raise ValueError("Something went 
        return AIMessage(content="YES")

fake_llm = GenericFakeChatModel(messages=MessagesIterator())

class JobApplicationState(TypedDict):
    
                             
