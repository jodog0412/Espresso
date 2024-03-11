import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image

def img_grid(imgs, rows=2, cols=3):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

class imageGen:
    def __init__(self,user_input:str):
        self.user_input=user_input
        repo_id="SG161222/Realistic_Vision_V6.0_B1_noVAE"
        scheduler = DPMSolverMultistepScheduler.from_pretrained(repo_id, subfolder="scheduler")
        pipeline=DiffusionPipeline.from_pretrained(repo_id,
                                                   scheduler=scheduler,
                                                   torch_dtype=torch.float16).to("cuda")
        self.pipeline=pipeline

    def design(self):
        pipeline=self.pipeline
        pipeline.load_lora_weights("logo_v1-000012.safetensors")
        pipeline.fuse_lora(lora_scale=0.5)
        pos="(masterpiece:1.2), best quality, high resolution, logo, 2d, white background, simple background"
        neg="(worst quality, low quality:1.4), 3d"
        imgs = pipeline(num_inference_steps=30,
                        prompt=pos+','+self.user_input,
                        negative_prompt=neg,
                        guidance_scale=8,
                        num_images_per_prompt=6).images
        return imgs

    def ad(self):
        pipeline=self.pipeline
        pos="masterpiece, best quality, raw photo, extremely detailed skin, extremely detailed face, 8k uhd, \
        dslr, soft lighting,  film grain, Fujifilm XT3, instagram, realstic, clothes"
        neg="(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), \
            (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, \
            disconnected limbs, mutation, mutated, ugly, disgusting, amputation,\
            (nsfw:2), (sexual content:2), (nude:2), (topless:2)"
        imgs = pipeline(num_inference_steps=30,
                        prompt=pos+','+self.user_input,
                        negative_prompt=neg,
                        guidance_scale=8,
                        num_images_per_prompt=6).images
        return imgs