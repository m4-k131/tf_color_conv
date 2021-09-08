# tf_color_conv
Colorspace conversion functions for Tensorflow.
Rescale & shift the build-in conversion functions' outputs to range([0,1],[-1,1],[-1,1]) for easy usage
in e.g a colorization-model.

RGB inputs must be in range[0,1] to work properly.
Outputs of RGB2Colorspace functions are in range[0,1] for the L/Y/V (lightness)-channel and [-1,1] for the color channels.

Outputs of Colorspace2RGB are in range[0,1]

H & V channel for HSV in- and outputs are swapped, so that the Lightness-channel is always the first channel regardless of colorspace.

All functions work with a single image or image batch.

