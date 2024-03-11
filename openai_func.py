import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(verbose=True)
openai_api_key=os.getenv("OPENAI_API_KEY")
class ContentGenerator:
    def __init__(self,inputs):
        client = OpenAI(api_key=openai_api_key)
        client.chat.completions.create(model="gpt-3.5-turbo-1106",
                                       messages=[{"role": "system",
                                                  "content": f"You're a marketing assistant.\
                                                  Your task is to assist and make marketing contents from idea.\
                                                  Given the idea delimated by '''.\
                                                  Idea : '''{inputs}'''"}])
        self.inputs=inputs
        self.client=client


    def getMarketingText(self):
        client =self.client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user",
                 "content": "Write the STP marketing strategy for idea.\
                 Use the following format:\
                 1. Market Segmemtation \
                 - Demographic: <appropriate demographic market segmentation in one line>\
                 - Psychographic: <appropriate psychographic market segmentation in one line>\
                 - Behavioral: <appropriate behavioral market segmentation in one line>\
                 2. Targets \
                 <appropriate target customers for the idea in one line>\
                 3. Positioning \
                 <appropriate positioning for the idea in one line>"},
                ]
            )
        return response.choices[0].message.content

    def getDesignText(self):
        client =self.client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user",
                 "content": f"Given the idea : '''{self.inputs}'''\
                 Perform the following actions from the idea:\
                 1 - Create name for idea.\
                 2 - Write catchphrase for idea.\
                 Use the following format:\
                 Name: <idea name>\
                 Catchphrase: <idea catchphrase>"},
                ]
            )
        return response.choices[0].message.content

    def getAdText(self):
        client =self.client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user",
                 "content": f"Given the idea: '''{self.inputs}'''\
                 You can imagine a photo content to advertise and market the idea.\
                 Introduce photo content in 4 lines.\
                 after the last sentence, write 5 hash tag for photo content.\
                 Number signs are not allowed."},
                ]
            )
        return response.choices[0].message.content

    def getAdImage(self):
        client =self.client
        response = client.images.generate(
            model="dall-e-3",
            prompt=f'advertisement photo, masterpiece, {self.inputs}, realistic',
            size="1024x1024",
            quality="hd",
            n=1,
            )
        image_url=response.data[0].url
        # return Image.open(BytesIO(requests.get(image_url).content))
        return image_url

    def getLogoImage(self):
        client =self.client
        response = client.images.generate(
            model="dall-e-3",
            prompt=f'company logo masterpiece, {self.inputs}, minimalism, white background',
            size="1024x1024",
            quality="hd",
            n=1,
            )
        image_url=response.data[0].url
        # return Image.open(BytesIO(requests.get(image_url).content))
        return image_url


