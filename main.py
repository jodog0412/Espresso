#1. Prepare
# pip install --upgrade diffusers accelerate transformers openai xformers
from function import *
openai.api_key="" #여러분의 openai api key를 입력해주세요.

input='making vegan burger'

#2. text generation
## [method 1]
# inputs=text_generation(input)
# idea_text=inputs.idea_text()
# stp_text=inputs.stp_text()
# content_text,keyword=inputs.content_text()

## [method 2]
idea_text,stp_text,(content_text,keyword)=text_generation(input).returns()

#3. image generation
images=image_generation(keyword).implement()

# #4. Show Output
grid,sentence=output_process(images,content_text).returns() #Return output
output_process(images,content_text).show() #Show output
