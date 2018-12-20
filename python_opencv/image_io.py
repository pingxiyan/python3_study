
import cv2 as cv
import sys

if __name__ == '__main__':

    fname = "../cat.jpg"
    im = cv.imread(fname)
    if im is None:
        print('Failed to load image file:', fname)
        sys.exit(1)

    gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)

    cv.imshow('im',im)
    cv.imshow('gray',gray)
    cv.waitKey(0)

