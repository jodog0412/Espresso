'''1. Prepare'''
# pip install --upgrade diffusers accelerate transformers openai xformers
from image_func import *
from text_func import *
openai.api_key="" #여러분의 openai api key를 입력해주세요.

''' 2. Initialize '''
inputs='Europe tour package'
writer, painter = text_gen(inputs), image_gen(inputs)

''' 3. Strategy&Design '''
plan_txt, plan_key =writer.strategy()
design_txt=writer.design(plan_key)
logo=painter.design()

''' 4. Ad '''
ad_txt, ad_key=writer.ad(plan_key)
ad_img=painter.ad()

