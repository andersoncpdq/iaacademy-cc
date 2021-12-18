import os

import cv2
import glob
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os
import numpy as np
import mahotas

def data_augmentation(PATH: str):
    my_images = [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]  # Getting images
    print(my_images)
    alpha = 1.02
    beta = 0.1
    adjusting_images = [cv2.convertScaleAbs(image, alpha=alpha, beta=beta) for image in my_images]  # Changing the contrast and the brightness of the images
    blur_images = [cv2.medianBlur(image, 1) for image in my_images]  # Images with blur
    rotate_image = [cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) for image in my_images]  # Rotate images
    array = [(my_images[pos], adjusting_images[pos], blur_images[pos], rotate_image[pos]) for pos in range(len(my_images))]
    return array


def preprocessing1(PATH: str):
    pass

def preprocessing2(PATH: str):
    pass

def green_channel(img):
    b,g,r = cv2.split(img)
    return g

def preprocessing3(PATH: str):
    # green channel extraction:

    # CLAHE application:

    # Adaptive Thresholding



    pass

def normalize(PATH: str):
    """
    This function will normalize the data between 0 and 1
    :param PATH: Path to files
    :return: image array
    """
    images = [cv2.imread(PATH + '/' + image)/255. for image in os.listdir(PATH)]
    return images

def load_images(PATH: str):
    #images = [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]
    return [cv2.imread(PATH + '\\' + image) for image in sorted(os.listdir(PATH))]



def CLAHE(image, clip=2.0, grid=(8,8)):
    """
    Equalizes the histogram of a grayscale image using
    Contrast Limited Adaptive Histogram Equalization (CLAHE).

    :param image: image array
    :param clip: threshold for contrast limiting
    :param grid:  size of grid for histogram equalization
                  (Input image will be divided into equally
                  sized rectangular tiles).

    :return: image array after CLAHE

    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=grid)
    return clahe.apply(gray)



'''def resize(img, dim=(224, 224)):
    img_resized = np.zeros(dim)
    try:
        img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    except Exception as e:
        print(str(e))
        
    return img_resized'''

def resize(path, dim=(224, 224)):

    #X = [np.array(resize(cv2.imread(path), (224, 224))) for path in X_path]

    try:
        img = cv2.imread(path)
        if(path == "data_especular_crop\test_images\integra\1100.png"):
            pass
        else:
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        #print(path)

    except Exception as e:
        print(path)
        print(str(e))

    return img

    
    

def labeling(data, val):
    return val * np.ones(len(data))

def adaptive_threshold(img, bsize=11, k=2):
    """
    Adaptive threshold is the method where the threshold value is calculated for smaller regions. This leads to
    different threshold values for different regions with regard to the change in lighting. For this, the
    blockSize × blockSize neighborhood was weighted sum of a less constant point.

    :param img: input image matrix (single channel, 8-bit or floating point)
    :param bsize: size of a pixel neighborhood that is used to calculate a threshold value.
    :param k: a constant value that is subtracted from the average or weighted sum of neighborhood pixels.

    :return: adaptive thresholded image array
    """
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, bsize, k)


#data_augmentation('/home/bagriel/IAAcademy/iaacademy-cc/test_app/computer_vision/data_especular_crop/test_images/confluente')





