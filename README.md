# tf_color_conv
Colorspace conversion functions for Tensorflow.

RGB inputs must be in range[0,1] to work properly.

Outputs are in range[0,1] for the L/Y/V (lightness)-channel and [-1,1] for the color channels.

H & V channel for HSV in- and outputs are swapped, so that the Lightness-channel is always the first channel regardless of colorspace.


Colorspace2RGB functions expect a Tensor (yuv/lab2rgb also can take a NumPy-array), while RGB2Colorspace functions can take a NumPy-arrays or Tensors. All functions return a NumPy-array.


get_conversion_fn(colorspace):
param str colorspace: lab, yuv or hsv
Returns the corrosponding rgb2cs and cs2rgb function
