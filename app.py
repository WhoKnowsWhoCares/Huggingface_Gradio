# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['repo_id', 'learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_cat', 'classify_image']

# %% app.ipynb 2
from fastai.vision.all import *
from huggingface_hub import from_pretrained_fastai
import gradio as gr

repo_id = "asFrants/photo_enhancement"
def is_cat(x): return x[0].isupper() 

# %% app.ipynb 5
# learn = load_learner('../models/model.pkl')
learn = from_pretrained_fastai(repo_id)

# %% app.ipynb 8
# categories = ('Dog','Cat')
categories = learn.dls.vocab
def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% app.ipynb 10
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['./examples/dog.jpg','./examples/cats.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)

