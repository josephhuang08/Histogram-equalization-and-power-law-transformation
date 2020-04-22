#Power law program by 黃書垣
import cv2 as cv2

#Consruct LUT
def constructLUT(gamma):
    lut = []

    #Normalize gray level 0~255 to 0~1. Power each gray level by gamma. Restore normalized value
    for x in range (0,256):
        lut.append((x / 255.0) ** gamma * 255.0)
    
    return lut

#Construct the image using LUT
def constructImg(inputImg, gamma):
    #Construct LUT and get image size
    table = constructLUT(gamma)
    imageHeight = inputImg.shape[0]
    imageWidth = inputImg.shape[1]

    #Construct new image
    for x in range(0, imageHeight):
        for y in range(0, imageWidth):
            #Replace the old Gray level value with new value
            inputImg[x][y] = table[inputImg[x][y]]

    return inputImg
    
#Enter you input image
inputImgName = input('Please enter your image name: ')

#Equalize image using 5 gamma levels
for gamma in [0.1, 0.5, 1.5, 2.5, 5]:
    #Input image
    inputImg = cv2.imread(inputImgName, 0)
    #Equalize
    outputImg = constructImg(inputImg, gamma)
    #Name and output image
    outputImageName = "gamma="+str(gamma)+'_'+inputImgName
    cv2.imwrite(outputImageName, outputImg)
    print('Output image:', outputImageName, 'complete.')

