"""1. Prepare"""
# pip install --upgrade diffusers accelerate transformers openai xformers
from image_func import *
from text_func import *
openai.api_key="" #여러분의 openai api key를 입력해주세요.

input='making vegan burger'

"""2. idea introduction"""
idea_txt,idea_key=idea(input).returns()
logo=image_generation(idea_key).idea_image()

"""3. content generation"""
stp,(content_txt,content_key)=content(input).returns()
content_img=image_generation(content_key).content_image()

"""4. Output"""
idea_output=post_process(logo,idea_txt)
idea_grid=idea_output.returns() #Returns output image
# idea_output.show() #Print output image and text

content_output=post_process(content_img,content_txt)
content_grid=content_output.returns()
# content_output.show()
