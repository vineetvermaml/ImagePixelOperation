import cv2
import numpy as np
import os
import math


def readimage():
    img = cv2.imread('Images/bostondynamics.jpg', cv2.IMREAD_COLOR)

    #cv2.imshow('IMAGE', img)
    return img


def reduceimageBy2(img):
    img = img
    height, width, channels = img.shape
    print(height, width)
    for i in range(0, height):
        for j in range(0, width):
            #img[i, j] = img[i, j]-2
            (b, g, r) = img[i, j]
            #print((b, g, r))
            b= b/2
            g = g/2
            r = r/2
            img[i, j] = (b, g, r)
            #(b, g, r) = img[i, j]
            #print((b, g, r))
    #filename = 'savedImage.jpg'
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
    os.chdir(directory)
    cv2.imwrite('savedImage.jpg', img)

def imageresize():
    img = cv2.imread('Images/bostondynamics.jpg', cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    width = 600
    height = 800
    dim = (width, height)
    resized = cv2.resize(gray_image, dim, interpolation=cv2.INTER_AREA)
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
    os.chdir(directory)
    cv2.imwrite('grayscaleImageresized.jpg', resized)
    cv2.imshow("Resized image", resized)


def changeintensities(img):
    img = img
    height, width, channels = img.shape
    for i in range(0, height):
        for j in range(0, width):
            #img[i, j] = img[i, j]-2
            (b, g, r) = img[i, j]
            img[i, j] = (b, g, 0)# Removed the red intensity of pixel
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
    os.chdir(directory)
    cv2.imwrite('noredImage.jpg', img)

def swapintensities(img):
    img = img
    height, width, channels = img.shape
    for i in range(0, height):
        for j in range(0, width):
            #img[i, j] = img[i, j]-2
            (b, g, r) = img[i, j]
            img[i, j] = (r, b, g)#swapped the intensity of the pixel
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
    os.chdir(directory)
    cv2.imwrite('swapedintensityimage.jpg', img)


def RGB_TO_HSI(img):

    with np.errstate(divide='ignore', invalid='ignore'):

        #Load image with 32 bit floats as variable type
        bgr = np.float32(img)/255

        #Separate color channels
        blue = bgr[:,:,0]
        green = bgr[:,:,1]
        red = bgr[:,:,2]

        #Calculate Intensity
        def calc_intensity(red, blue, green):
            return np.divide(blue + green + red, 3)

        #Calculate Saturation
        def calc_saturation(red, blue, green):
            minimum = np.minimum(np.minimum(red, green), blue)
            saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)

            return saturation

        #Calculate Hue
        def calc_hue(red, blue, green):
            hue = np.copy(red)

            for i in range(0, blue.shape[0]):
                for j in range(0, blue.shape[1]):
                    hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                                math.sqrt((red[i][j] - green[i][j])**2 +
                                        ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                    hue[i][j] = math.acos(hue[i][j])

                    if blue[i][j] <= green[i][j]:
                        hue[i][j] = hue[i][j]
                    else:
                        hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

            return hue

        #Merge channels into picture and return image
        hsi = cv2.merge((calc_hue(red, blue, green), calc_saturation(red, blue, green), calc_intensity(red, blue, green)))
        directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
        os.chdir(directory)
        """ we need convert your buffer to uint8 (and make sure the values are in the range 0-255) before calling imwrite """
        hsi = (hsi * 255).astype('uint8')
        cv2.imwrite('RGB_TO_HSI.jpg', hsi)
        #cv2.imshow("Resized image", img)
        #cv2.imshow("Resized image1", hsi)

def YCrCbImage(img):
    img = img
    YCrCbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images'
    os.chdir(directory)
    cv2.imwrite('YCrCbImage.jpg', YCrCbImage)


def halves(img):
    img = img
    height, width, channels = img.shape

    # cv2.imread() -> takes an image as an input
    h, w, channels = img.shape

    quarter = w // 4

    # this will be the first column
    first_part = img[:, :quarter]
    second_quarter = (quarter*2)
    second_part = img[:, quarter:second_quarter]
    third_quarter = (quarter*3)
    third_part = img[:, second_quarter:third_quarter]
    fourth_quarter = (quarter*4)
    fourth_part = img[:, third_quarter:fourth_quarter]

    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages'
    os.chdir(directory)

    cv2.imwrite("Resized_image.jpg", first_part)
    cv2.imwrite("Resized_image1.jpg", second_part)
    cv2.imwrite("Resized_image2.jpg", third_part)
    cv2.imwrite("Resized_image3.jpg", fourth_part)

    cv2.waitKey(0)

def hconcat_resize():
    img1 = cv2.imread(r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages\Resized_image.jpg')
    img2 = cv2.imread(r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages\Resized_image1.jpg')
    img3 = cv2.imread(r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages\Resized_image2.jpg')
    img4 = cv2.imread(r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages\Resized_image3.jpg')
    im_v = cv2.hconcat([img1, img2, img3, img4])
    directory = r'C:\Users\Nagraj\PycharmProjects\ComputerVision01\Images\cropImages'
    os.chdir(directory)
    cv2.imwrite("Complete_image.jpg", im_v)





