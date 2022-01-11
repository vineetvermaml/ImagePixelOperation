import cv2
import numpy as np
import os


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

def HSIYCbCr(img):
    img = img
    height, width, channels = img.shape
    for i in range(0, height):
        for j in range(0, width):
            (b, g, r) = img[i, j]



