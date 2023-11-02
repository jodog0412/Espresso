'''1. Prepare'''
# pip install --upgrade diffusers accelerate transformers openai xformers
from image_func import *
from text_func import *
openai.api_key="" #여러분의 openai api key를 입력해주세요.

''' 2. Initialize '''
inputs='Europe tour package'
writer, painter = textGen(inputs), imageGen(inputs)

''' 3. Marketing '''
marketing_text, marketing_keywrd = writer.marketing()

''' 4. Design '''
design_text, logo = writer.design(marketing_keywrd), painter.design(marketing_keywrd)

''' 4. Ad '''
ad_text, ad_keywrd = writer.ad(marketing_keywrd)
ad_img=painter.ad(ad_keywrd)

