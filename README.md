# ☕ Espresso
Team project for the lecture `AI융합캡스톤과 창업`.  
Awarded excellence prize in `2023-1 서강융합기술경진대회`.

# Introduction
* __Enterpreneur Assistance Web Application__
* `GPT 3.5`, `Stable-Diffusion`

# Feature
## 🚀 __Efficient Generation__      
Generate marketing contents efficiently.    
(Time consumption : 3m)    
## 📊 __Generation Based on marketing strategy__    
Generate contents based on STP marketing strategy.
  
# ❓ How to use
| Environment | Colab | Local | GCP                   |
|:-----------:|:-----:|:-----:|:---:|
| Completed   | O    | O   | X                        |
| Stabiltiy   | High | Medium(maybe some bugs) | High |
| Web deploy  | X    | O   | O                        |
## Colab    
☕ [espresso_colab](https://colab.research.google.com/drive/1-rpJjPArcVYP5JfD1NIlNdkQx2b9lqxG#scrollTo=nX2KcS3gmlim)    
## Local
1. Download repository to local    
```git
git clone https://github.com/jodog0412/espresso
```
2. Run manage.py in your local repository(espresso)    
```git
python manage.py runserver
```
# Sample
![result](https://github.com/jodog0412/Espresso/assets/83653380/9f9eb07f-b111-4679-a0db-5f186b5cfcb2)  
1. Enter a input.
2. Write business idea.
3. Generate logo, catchphrase, and ad based on marketing strategy.  

# 🛠 Tech-Stack
![image](https://github.com/jodog0412/espresso/assets/83653380/2702f4a3-0a7b-466b-be74-8dc3401d93e8)  
* Stable-diffusion  
  * Checkpoint: [Realistic_Vision_v1.4](https://huggingface.co/SG161222/Realistic_Vision_V1.4)
  * LoRA(Low-Rank Adaption) : [Anylogo_v1.0](https://civitai.com/models/57452/anylogo)

# 🛤 Procedure
![image](https://github.com/jodog0412/espresso/assets/83653380/c2e98be8-25a0-4267-b412-09098708ee78)  
* Done: Colab, Local
* In progress: GCP
# 🙍‍♂️ Member
* 이현성 : 팀장, AI 애플리케이션 개발
* 이해온 : 웹디자인
* 임동준 : UI/UX
* 오홍준 : 공문서 작성, 프레젠테이션
* 오윤진 : 미디어위키
