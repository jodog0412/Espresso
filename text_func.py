import openai
import torch

def answer(prompt:str):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", 
                "content": prompt}
                ]
        )
        result=completion.choices[0].message["content"]
        return result

class text_generation:
    def __init__(self,input:str):
        self.input=input
        self.roleplay=f"You're a marketing assistant.\
        Your task is to assist and make marketing contents from idea.\
        Given the idea delimated by '''.\
        Idea : '''{self.input}'''"

class idea(text_generation):
    def keyword(self):
        request=f"Extract 3 keywords from the idea.\
        Write keywords using ',' symbol only. Using other symbols is not allowed."
        
        return answer(self.roleplay+request)

    def introduction(self):
        request="Perform the following actions:\
        1 - Create name for idea.\
        2 - Write catchphrase for idea.\
        Use the following format:\
        Name: <idea name>\
        Catchphrase: <idea catchphrase>"

        return answer(self.roleplay+request)
    
    def returns(self):
        inputs=idea(self.input)

        return inputs.introduction(), inputs.keyword()

class content(text_generation):
    def strategy(self):
        request="Write the STP strategy for idea using macro and micro environment analysis.\
        Use the following format:\
        -Segmentation\
        ∙ Demographic: <demographic segmentation strategy>\
        ∙ Psychographic: <Psychographic segmentation strategy>\
        ∙ Behavioral: <Behavioral segmentation strategy>\
        -Targeting\
        <Targeting strategy>\
        -Positioning\
        <Positioning strategy>"

        return answer(self.roleplay+request)
    
    def introduction(self):
        request="I want to make a picture for advertising idea, but I don't know what scene is suitable for marketing.\
        You can imagine a picture for idea. \
        Please describe the scene of photo for advertising idea in 4 lines."
        sentence=answer(self.roleplay+request)
        
        keyword=answer(f"I write the description for photo.\
        description is {sentence}.\
        Please extract and list 8 keywords for the scene of photo. \
        You should write keywords using ',' symbol only. Other symbols are not allowed.")

        return sentence, keyword
    
    def returns(self):
        inputs=content(self.input)
