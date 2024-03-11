from django.shortcuts import render, redirect
from openai_func import *

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
        generator=ContentGenerator(inputs)
        marketingText=generator.getMarketingText()
        designText=generator.getDesignText()
        adText=generator.getAdText()
        logoImg=generator.getLogoImage()
        adImg=generator.getAdImage()
        
        context={'marketingText':'\n'+marketingText,
                 'designText':'\n'+designText,
                 'adText':'\n'+adText,
                 'logoImg':logoImg,
                 'adImg':adImg
                 }
        return render(request, 'espresso/output.html', context)