# -*- coding: utf-8 -*-
#@author: Malte Kleine

"""
Colorspace conversion functions for Tensorflow.

RGB inputs must be in range[0,1] to work properly.
Outputs are in range[0,1] for the L/Y/V (lightness)-channel and [-1,1] for the color channels.
H & V channel for HSV in- and outputs are swapped, so that the Lightness-channel is always the first channel regardless of colorspace.

Colorspace2RGB functions expect a Tensor (yuv/lab2rgb also can take a NumPy-array), while RGB2Colorspace functions can take a NumPy-arrays or Tensors. All functions return a NumPy-array.

"""


from tensorflow import image 
try:
    from tensorflow_io import experimental
except:
    print('Warning: tensorflow_io not installed. This package is needed for rgb->lab and lab->rgb conversion. Install tensorflow_io or use YUV and HSV colorspaces')
import numpy as np



lab_array=np.array([100., 128., 128.])
yh_array=np.array([1., 2., 2.])



def rgb2lab(img):
    img=experimental.color.rgb_to_lab(img).numpy()
    img/=lab_array
    return img

def lab2rgb(image):
    img=image*lab_array
    img=experimental.color.lab_to_rgb(img).numpy()
    return img


def rgb2yuv(img):
    img=image.rgb_to_yuv(img).numpy()
    img*=yh_array
    return img
    
def yuv2rgb(img):
    img/=yh_array
    img=image.yuv_to_rgb(img).numpy()
    return img


def rgb2hsv(img):
    img=image.rgb_to_hsv(img).numpy()
    v_channel=img[...,2].copy()
    img[...,2]=img[...,0]
    img[...,0]=v_channel
    img*=yh_array
    img[...,1:]-=1
    return img

def hsv2rgb(img):
    img=img.numpy()
    img[...,1:]+=1
    img/=yh_array
    v_channel=img[...,0].copy()
    img[...,0]=img[...,2]
    img[...,2]=v_channel
    img=image.hsv_to_rgb(img).numpy()
    return img

