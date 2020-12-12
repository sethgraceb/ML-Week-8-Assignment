#Q(i)(b)
import numpy as np
from PIL import Image
im = Image.open('image.jpg')
rgb = np.array(im.convert('RGB'))
r=rgb[:, :, 0] #array of R pixels
Image.fromarray(np.uint8(r)).show()

def convolution_func(image, kernel):

    kernel = np.flipud(np.fliplr(kernel))
    conv_output = np.zeros_like(image)

    padded_image = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    padded_image[1:-1, 1:-1] = image

    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            conv_output[y, x]=(padded_image[y: y+3, x: x+3] * kernel).sum()

    return conv_output

kernel1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
conv_output1 = convolution_func(r, kernel = kernel1)
#im.show()
Image.fromarray(np.uint8(conv_output1)).show()

kernel2 = np.array([[0, -1, 0], [-1, 8, -1], [0, -1, 0]])
conv_output2 = convolution_func(r, kernel = kernel2)
#im.show()
Image.fromarray(np.uint8(conv_output2)).show()