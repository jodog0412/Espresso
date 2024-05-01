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
        agent=MarketingAgent(inputs)
        marketing_text=agent.write_marketing_strategy()
        design_text=agent.write_idea_description()
        ad_text=agent.write_advertisement()
        logo_img=agent.draw_logo()
        ad_img=agent.draw_ad_image()
        
        context={'marketingText':'\n'+marketing_text,
                 'designText':'\n'+design_text,
                 'adText':'\n'+ad_text,
                 'logoImg':logo_img,
                 'adImg':ad_img
                 }
        return render(request, 'espresso/output.html', context)