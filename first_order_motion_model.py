# -*- coding: utf-8 -*-
"""first_order_motion_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bVReQlgJQNo-uR8b1jkhVaOevBwW5aG9

**Preparation**

First we setup the repository first-order-motion model by cloning the repository. Please make sure that your runting setting is set as GPU which can be set up from the top menu (Runtime → change runtime type), and make sure to click Connect on the top right-hand side of the screen before you start.
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/AliaksandrSiarohin/first-order-model.git
# %cd first-order-model

!pip install -r requirements.txt

"""First let's download the driving videos from fashion datset from : https://vision.cs.ubc.ca/datasets/fashion/"""

!wget -c https://vision.cs.ubc.ca/datasets/fashion/resources/fashion_dataset/fashion_train.txt
!wget -c https://vision.cs.ubc.ca/datasets/fashion/resources/fashion_dataset/fashion_test.txt

import requests
import os

f_train = open('fashion_train.txt', "r")
f_test = open('fashion_test.txt', "r")

train_files = f_train.readlines()
test_files = f_test.readlines()

os.mkdir('train')
os.mkdir('test')

for video_url in train_files:
    r = requests.get(video_url[:-1])
    file_name = video_url[:-1].split("/")[-1]
    with open("train/"+file_name,'wb') as f:
        f.write(r.content)

for video_url in test_files:
    r = requests.get(video_url[:-1])
    file_name = video_url[:-1].split("/")[-1]
    with open("test/"+file_name,'wb') as f:
        f.write(r.content)

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/first-order-model

"""To Train the model run the following code."""

!CUDA_VISIBLE_DEVICES=0,1,2,3 python run.py --config config/fashion-256.yaml --device_ids 0,1,2,3

"""Copy the driving video files from : https://drive.google.com/drive/folders/1JM8ZjI7YO8WXGpUi5XAzqrvrWN9Z2KSo?usp=sharing to your drive.

Copy the source files from link: https://drive.google.com/drive/folders/1Wu-3q8XvAb8QD4yqeCUmTDXf1HQ3lUvB?usp=sharing to your own drive.
"""

from google.colab import drive
drive.mount('/content/drive')

import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Source image path
source_image = imageio.imread('/content/drive/MyDrive/Colab Notebooks/FINAL PROJECT/source_files/source_25.png')
# Driving image video
driving_video = imageio.mimread('/content/drive/MyDrive/Colab Notebooks/FINAL PROJECT/driving_files/fashion-demo-5.mp4', memtest=False)


# Resize video to 256x256

source_image = resize(source_image, (256, 256))[..., :3]
driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

def display(source, driving, generated=None):
    fig = plt.figure(figsize=(8 + 4 * (generated is not None), 6))

    ims = []
    for i in range(len(driving)):
        cols = [source]
        cols.append(driving[i])
        if generated is not None:
            cols.append(generated[i])
        im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    plt.close()
    return ani
    
# Mostramos el resultado de la carga de ambos recursos
HTML(display(source_image, driving_video).to_html5_video())

"""Copy the fashion.pth.tar file from link :  https://drive.google.com/file/d/1W7qunHxacXC8tdkHjMyLF43nTbIf8HwX/view?usp=sharing to your drive."""

from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/fashion-256.yaml', 
                            checkpoint_path='/content/drive/MyDrive/fashion.pth.tar')

from demo import make_animation
from skimage import img_as_ubyte

predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

# Generate video results
imageio.mimsave('../generated.mp4', [img_as_ubyte(frame) for frame in predictions])

# Render video on colab
HTML(display(source_image, driving_video, predictions).to_html5_video())