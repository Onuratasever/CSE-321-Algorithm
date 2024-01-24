def findBrightestPixel(image):
    if(isIncrease(image)):
        return helperIncrease_findBrightestPixel(image, 0)
    else:
        return helperDecrease_findBrightestPixel(image, 0)

def helperIncrease_findBrightestPixel(image, column): # her şey artan sıraya göreymiş gibi yapıyorum
    for numOfrows in range(len(image)):
        #print("numOfRows: ", numOfrows)
        if(column + 1 < len(image[0])):
            # print(image[numOfrows][column], image[numOfrows][column+1])
            if(image[numOfrows][column] > image[numOfrows][column+1]):
                return numOfrows, column, image[numOfrows][column]
        elif (numOfrows == len(image) - 1):
             return numOfrows, column, image[numOfrows][column]
    return helperIncrease_findBrightestPixel(image, column + 1)

def helperDecrease_findBrightestPixel(image, column): # her şey azalan sıraya göreymiş gibi yapıyorum
    for numOfrows in range(len(image)):
        if(column + 1 < len(image[0])):
            # print(image[numOfrows][column], image[numOfrows][column+1])
            if(image[numOfrows][column] < image[numOfrows][column+1]):
                return numOfrows, column+1, image[numOfrows][column+1]
        elif (numOfrows == len(image) - 1):
             return numOfrows, len(image[0])-1-column, image[numOfrows][0]
    return helperDecrease_findBrightestPixel(image, column + 1)

def isIncrease(image):
    count = 0
    for numOfrows in range(len(image)):
        if(1 < len (image[0])):
            if(image[numOfrows][0] > image[numOfrows][1]):
                count = count - 1
            if(image[numOfrows][0] < image[numOfrows][1]):
                count = count + 1
    if (count < 0):
        return False
    return True

def main():
    image = [
        [6, 4, 3, 1],
        [12, 10, 4, 2],
        [14, 19, 12, 3],
        [18, 8, 6, 4]
    ]

    print(findBrightestPixel(image))

main()