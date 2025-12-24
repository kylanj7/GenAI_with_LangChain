import sys
import os

sys.path.insert(0, os.path.abspath('..'))
set_environment()

DallEAPIWrapper??

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

dalle = DallEAPIWrapper(
   model="dall-e-3",  # Options: "dall-e-2" (default) or "dall-e-3"
   size="1024x1024",       # Image dimensions
    quality="standard",     # "standard" or "hd" for DALL-E 3
    n=1                     # Number of images to generate (only for DALL-E 2)
)
image_url= dalle.run("Adetailed technical diagram of a quantum computer")
print(image_url)

from langchain_community.llms import Replicate

text2image = Replicate(
    model="stability-ai/stable-diffusion-3.5-large",
    model_kwargs={
        prompt_strength": 0.85,
        "cfg": 4.5,
        "steps": 40,
        "aspect_ratio": "1:1",
        "output_format": "webp",
        "output_quality": 90
    }
)

image_url = text2image.invoke(
   "A detailed techinical diagram of an AI Agent"
)

orint(image_url)

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

def analyze_image(image_url: str, question: str) -> str:
   chat = ChatOpenAI(model="gpt-40-mini", max_tokens=256)



