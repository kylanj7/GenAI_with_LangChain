
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
from langgraph.pregel import RetryPolicy
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
    job_description: str
    is_suitable: bool
    application: str
    actions: Annotated[list[str], add]

def generate_applications(state):                             
    print("...Generating Application...")
    return {"application": "some_fake_application", "actions": ["action2"]}

def is_suitable_condition)state: JobApplicationState) -> Literal["generate_application", END]:
        if state.get("is_suitable"):
            return "generate_application"
        return END

llms = {
    "fake": fake_llm,
    "Google": llm
}

def analyze_job_description(state, config: RunnableConfig):
    try:
        print("here")
        llm = config["configurable"].get("model_provider", "Google")
        analyze_chain = llm | parser
        prompt = prompt_template_enum.format(job_description=job_description)
        result = analyze_chain.invoke(prompt)
        return {is_suitable": result}
    except Exception as e:
        logger.error(f"Exception {e} occured while executing analyze_job_description")
        return {"is_suitable": False}

builder = StateGraph(JobApplicationState)
builder.add_node("analyze_job_description", analyze_job_description)
builder.add_node("generate_application", generate_application)
builder.add_edge(START, "analyze_job_description")
builder.add_conditional_edges(
    "analyze_job_description", is_suitable_condition)
builder.add_edge("generate_application", END)

graph = builder.complile()

from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()

res = graph.invoke({job_description":"fake_jd"}, config={"configurable": {model_provider": "fake"}})
print(res)

res = graph.invoke({"job_description": job_description}, config={"configurable": {"model_provider": "fake"}})
print(res)

res = graph.invoke({"job_description":"fake_jd"}, config={"configurable": {"model_provider": "fake"}})
print(res)

fake_llm.invoke("test")

chain_fallback = RunnableLambda(lambda _: print("running fallback"))
chain = fake_llm | RunnableLambda(lambda _: print("running main chain"))
chain_with_fb = chain.with_fallbacks([chain_fallback])

chain_with_fb.invoke("test")
chain_with_fb.invoke("test")

fake_llm_retry = fake_llm.with_retry(
    retry_if_exception_type=(ValueError,),
    wait_exponential_jitter=True,
    stop_after_attept=2,
)

analyze_chain_fake_retries.invoke("test")

def analyze_job_description(state, config: RunnableConfig):
    model_provider = config["configurable"].get("model_provider", "Google")
    llm = llms[model_provider]
    analyze_chain = llm | parser
    prompt = prompt_template_enum.format(job_description=job_description)
    result = analyze_chain.invoke(prompt)
    return {is_suitable": result}

builder = StateGraph(JobApplicationState)
builder.add_node("analyze_job_description", analyze_job_description, retry=RetryPolicy(retry_on=ValueError, max_attempts=2))
builder.add_node("generate_application", generate_application)
builder.add_edge(START, "analyze_job_description")
builder.add_conditional_edges(
    "analyze_job_description", is_suitable_condition)
builder.add_edge("generate_application", END)

graph = builder.compile()

from IPython.display import Image, display
display(Image(graph.get_graph().graw_mermaid_png()))





