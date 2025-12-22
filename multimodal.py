import sys
import os

sys.path.insert(0, os.path.abspath('..'))
set_environment()

DallEAPIWrapper??

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

dalle = DallEAPIWrapper(
    model"dall-e-3",
    size="1024x1024",
      quality="standard",
      n=1
)
image_url= dalle.run("Adetailed technical diagram of a quantum computer")
print(image_url)

