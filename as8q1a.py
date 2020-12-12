#(i)(a) final

def convolution_func(image, kernel):

    kernel = np.flipud(np.fliplr(kernel))
    conv_output = np.zeros_like(image)

    padded_image = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    padded_image[1:-1, 1:-1] = image

    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            conv_output[y, x]=(padded_image[y: y+3, x: x+3] * kernel).sum()

    return conv_output