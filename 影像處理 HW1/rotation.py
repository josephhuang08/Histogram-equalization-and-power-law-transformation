#Program by 黃書垣.
import cv2
from math import sin, cos, radians, ceil, floor
import numpy as np

#Rotate image using nearest neighbor interpolation
def nearest_neighbor(img):
     #Construct blank output image
     outImg = np.zeros((outImgSize, outImgSize, 3), dtype=int)

     #rotate image
     for x in range(0, outImgSize):
          for y in range(0, outImgSize):
               #round new coordinates (nearest neighbor method)
               X = round(float(x*m[0][0] + (y-256)*m[0][1]))
               Y = round(float(x*m[1][0] + (y-256)*m[1][1]))

               #Check if X,Y is in img 
               if X<512 and Y<512 and X>=0 and Y>=0:
                    outImg[x][y] = img[X][Y]
                                     
     return outImg

#Rotate image using bilinear interpolation.​
def bilinear(img):
     #Construct blank output image
     outImg = np.zeros((outImgSize, outImgSize, 3), dtype=int)
     
     #rotate image
     for x in range(0, outImgSize):
          for y in range(0, outImgSize):
               X = float(x*m[0][0] + (y-256)*m[0][1])
               Y = float(x*m[1][0] + (y-256)*m[1][1])

               #Check if X,Y is in img 
               if X<=511 and Y<=511 and X>=0 and Y>=0:
                    #Calculate new RGB level using bilinear method
                    X1, X2, Y1, Y2 = floor(X), ceil(X), floor(Y), ceil(Y)
                    R1 = (X2 - X) * img[X1][Y1] + (X-X1) * img[X2][Y1]
                    R2 = (X2 - X) * img[X1][Y2] + (X-X1) * img[X2][Y2]
                    outImg[x][y] = (Y2-Y) * R1 + (Y-Y1) * R2

     return outImg


#choose to input letter or nature scene 
chooseImg = input('Enter 1 for letter image, 2 for nature image: ')
if(chooseImg == '1'):
     img = cv2.imread('letter_E.png')
if(chooseImg == '2'):
     img = cv2.imread('nature.png')
     
print('rotating image...')

#Get output image size
outImgSize = round(512 * (sin(radians(30)) + sin(radians(60))))

#Define transform matrix for clockwise rotation 30 degrees
m = [[cos(radians(-30)), -sin(radians(-30))],
      [sin(radians(-30)), cos(radians(-30))]]
m = np.linalg.inv(m)

#create images
outImg1 = nearest_neighbor(img)
outImg2 = bilinear(img)

#output images
cv2.imwrite('nearest_neighbor.png', outImg1)
cv2.imwrite('bilinear.png', outImg2)

