# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2

import imageRead
import os


if __name__ == '__main__':

    img = imageRead.readimage()
    #imageRead.reduceimageBy2(img)
    #imageRead.imageresize()
    #imageRead.changeintensities(img)
    #imageRead.swapintensities(img)
    #imageRead.RGB_TO_HSI(img)
    imageRead.YCrCbImage(img)
    #imageRead.imagecropinto4(img)
    #imageRead.hconcat_resize()
    #imageRead.halves(img)
    #imageRead.hconcat_resize()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
