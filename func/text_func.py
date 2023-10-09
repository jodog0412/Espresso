import openai
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

class default_rule:
    def __init__(self,input:str):
        self.input=input
        self.roleplay=f"You're a marketing assistant.\
        Your task is to assist and make marketing contents from idea.\
        Given the idea delimated by '''.\
        Idea : '''{self.input}'''"

class text_gen(default_rule):
    def strategy(self):
        intro_req="Write the STP strategy for the idea.\
        Use the following format:\
        1. Market Segmemtation \
          - Demographic: <appropriate demographic market segmentation in one line>\
          - Psychographic: <appropriate psychographic market segmentation in one line>\
          - Behavioral: <appropriate behavioral market segmentation in one line>\
        2. Targets \
        <appropriate target customers for the idea in one line>\
        3. Positioning \
        <appropriate positioning for the idea in one line>"
        sentence=answer(self.roleplay+intro_req)
        phrase=sentence.split('\n')[-1]

        key_req=f"Extract 2 keywords that indicates the value in the sentence.\
        Write in English and use ',' symbol only. Other symbols are not allowed.\
        Given the sentence : '''{phrase}'''"
        keyword=answer(key_req)

        return sentence, keyword

    def design(self,valuation):
        intro_req=f"Given values of the idea : '''{valuation}'''\
        Perform the following actions from the idea:\
        1 - Create name for idea.\
        2 - Write catchphrase for idea.\
        Use the following format:\
        Name: <idea name>\
        Catchphrase: <idea catchphrase>"
        sentence=answer(self.roleplay+intro_req)
        return sentence

    def ad(self,valuation):
        intro_req=f"Given values of the idea: '''{valuation}'''\
        You can imagine a photo content to advertise and market the idea.\
        Introduce photo content in 4 lines.\
        after the last sentence, write 5 hash tag for photo content.\
        Number signs are not allowed."
        sentence=answer(self.roleplay+intro_req)
        
        key_req=f"Extract 7 keywords by following the instructions for the photo description\
        If there is a person in the photo, \
        1. Extract 1 keyword for the person's gender.\
        2. Extract 2 keywords for the person's appearance.  \
        3. Extract 1 keyword for the person's action.\
        4. Extract 1 keyword for object in the photo.\
        5. Extract 2 keywords for the photo's atmosphere.\
        Else if there isn't a human in the photo, \
        1. Extract 4 keywords for object in the photo.\
        2. Extract 3 keyword for the photo's atmosphere.\
        Given the photo description : '''{sentence}'''\
        Don't extract keywords from hashtag in the photo description.\
        Write keywords using ',' symbol only. Other symbols are not allowed."
        keyword=answer(key_req)

        return sentence, keyword
    
    def returns(self):
        inputs=text_gen(self.input)
        return inputs.strategy(), inputs.design(), inputs.ad()