from django.shortcuts import render, redirect
import os
import re
from func.text_func import *
from func.image_func import *

# Create your views here.
openai.api_key=os.getenv("OPENAI_API_KEY") #Enter your OPENAI api key.

class Views:
    def index(request):
        if request.method=='POST':
            inputs = request.POST.get('myTextarea')
            request.session['data']=inputs
            return redirect('output')
        return render(request, 'espresso/index.html')
    
    def loading(request):
        if request.method=='POST':
            return redirect('output')
        return render(request, 'espresso/loading.html')

    def output(request):
        inputs=request.session['data']
        writer=textGen(inputs)        
        marketing_text, marketing_keywrd =writer.marketing()
        design_text=writer.design(marketing_keywrd)
        ad_text, ad_keywrd=writer.ad(marketing_keywrd)
        ad_text=ad_text.replace('.','.\n').replace('!','!\n')
        context={'marketing_text':'\n'+marketing_text,
                 'design_text':'\n'+design_text,
                 'ad_text':'\n'+ad_text}
        return render(request, 'espresso/output.html', context)