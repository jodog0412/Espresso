from django.shortcuts import render, redirect
import re
from func.text_func import *
from func.image_func import *

# Create your views here.
openai.api_key="" #Enter your OPENAI api key.

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
        writer=text_gen(inputs)        
        plan_txt, plan_key =writer.strategy()
        design_txt=writer.design(plan_key)
        ad_txt, ad_key=writer.ad(plan_key)
        ad_txt=ad_txt.replace('.','.\n').replace('!','.\n')
        context={'plan_txt':'\n'+plan_txt,
                 'design_txt':'\n'+design_txt,
                 'ad_txt':'\n'+ad_txt}
        return render(request, 'espresso/output.html', context)