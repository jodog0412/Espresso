"""1. Prepare"""
# pip install --upgrade diffusers accelerate transformers openai xformers
from image_func import *
from text_func import *
openai.api_key="" #여러분의 openai api key를 입력해주세요.

inputs='making vegan burger'

"""2. text generation"""
template=content(inputs)
stp_txt, stp_key=template.strategy()
idea_txt=template.idea(stp_key)
logo=image_generation(inputs).idea_image()

"""3. content generation"""
content_txt, content_key=template.content(stp_key)
content_img=image_generation(content_key).content_image()

