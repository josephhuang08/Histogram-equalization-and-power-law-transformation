#Histogram Equalization Program by 黃書垣.
import cv2 as cv2

#Creates cdf table and get the minimum non-zero value of the cdf
def createCdfTable(image, height, width):
    table = [0] * 256
    cdfMin = 999999999
    
    #Count the numbers of pixels in each gray level
    for x in range(0, height):
        for y in range(0, width):
            table[image[x][y]] += 1
            
    #Add up the amounts of each Gray level to create a cdf table
    for x in range(1, 256):
        table[x] += table[x-1]
        #Get minimun cdf
        if table[x] != 0:
            cdfMin = min(cdfMin, table[x])
        
    return table, cdfMin

#Construct a Graylevel LUT
def equalization(table, cdfMin):
    count = 0

    #Get the Equalized value for each gray level
    for grayLvl in range (0, 256):
        if table[grayLvl] != 0:
            table[grayLvl] = round((table[grayLvl] - cdfMin)/(table[255] - cdfMin) * 255)

    return table

#Use the LUT to construct a new image
def constructImg(inputImg, table, height, width):
    for x in range(0, height):
        for y in range(0, width):
            #Replace the old Gray level value with the equalized value
            inputImg[x][y] = table[inputImg[x][y]]

    return inputImg

#Combined functions above into one function
def myEqualizeHist(inputImg):
    imageHeight = inputImg.shape[0]
    imageWidth = inputImg.shape[1]
    
    cdfTable, cdfMin = createCdfTable(inputImg, imageHeight, imageWidth)
    histogramTable = equalization(cdfTable, cdfMin)
    outputImg = constructImg(inputImg, histogramTable, imageHeight, imageWidth)

    return outputImg

#Input image
inputImgName = input('Please enter your image name: ')
inputImg = cv2.imread(inputImgName, 0)

#Equalizing
print('Equalizing please wait...')
outputImg = myEqualizeHist(inputImg)
print('Equalization Finished.')

#Output equalized image
outputImgName = input('Please enter output image name: ')
cv2.imwrite(outputImgName, outputImg)

