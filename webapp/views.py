from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from text_func import *
from image_func import *
from forms import InputForm
# Create your views here.
class ResultView:
    def __init__(self, request):
        if request.method=='POST':
            form=InputForm(request.POST)
            if form.is_valid():
                input_txt=form.cleaned_data['input_txt']
                template=content(input_txt)
                self.input_txt=input_txt
                self.stp_txt, self.stp_key=template.strategy()
                self.idea_txt=template.idea(self.stp_key)
                self.content_txt, self.content_key=template.content(self.stp_key)
        else: 
            form=InputForm()
            return render(request, 'input.html', {'form':form})

    def idea_introduction(self, request):
        return (request, 'webapp\output.html', {'idea_txt':self.idea_txt})
    
    def idea_logo(self, request):
        logo=image_generation(self.input_txt).idea_image()
        grid=image_grid(logo)
        return (request, 'webapp\output.html', {'idea_logo':grid})

    def marketing_strategy(self, request):
        return (request, 'webapp\output.html', {'strategy':self.stp_txt})
    
    def content_introduction(self, request):
        return (request, 'webapp\output.html', {'content_txt':self.content_txt})
    
    def content_image(self, request):
        img=image_generation(self.content_key).content_image()
        grid=image_grid(img)
        return (request, 'webapp\output.html', {'content_img':grid})
