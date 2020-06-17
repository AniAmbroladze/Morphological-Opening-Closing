import csv
import numpy as np
import cv2
import os
import sys

class  Dil_Ero:
    def dilation(self,imgFile,l,k,seFile, n, m,):
        """
            The method performs dilation of a binary image with 
            respect to a structuring element 'SE'

            :param imgFile: Matrix of the image
            :param l: Number of rows of the image matrix
            :param k: Number of columns of the image matrix
            :param seFile: Maxtrix of SE
            :param n: Number of rows of SE matrix
            :param m: Number of columns of SE matrix
            :return: Dilated matrix
        """
        matrix = [[0 for x in range(k)] for y in range(l)] 
        if(m%2 != 0 and n%2 != 0):
            col = int((m/2)-1/2)
            row = int((n/2)-1/2)
            seRow = row
            seCol = col
        else:
            col = m-1
            row = n-1
            seRow = 0
            seCol = 0
        breaker = False
        v = 0
        while v != l:
            h = 0
            while h != k:
                i = 0
                while i <= row:
                    j = -1
                    while j < col:
                        j = j + 1
                        if(seFile[seRow+i][seCol+j]!= 0 and (v+i < l) and (h+j < k)):
                            if(imgFile[v+i][h+j] == 1):
                                matrix[v][h] =1
                                breaker = True
                                break

                        if(seFile[seRow+i][seCol-j]!= 0 and (v+i < l) and (h-j >= 0)):
                            if(imgFile[v+i][h-j] == 1):
                                matrix[v][h] = 1
                                breaker = True
                                breakil

                        if(seFile[seRow-i][seCol+j]!= 0 and (v-i >= 0) and (h+j < k)):
                            if(imgFile[v-i][h+j] == 1):
                                matrix[v][h] = 1
                                breaker = True
                                break
                        
                        if(seFile[seRow-i][seCol-j]!= 0 and (v-i >= 0) and (h-j >= 0)):
                            if(imgFile[v-i][h-j] == 1):
                                matrix[v][h] = 1
                                breaker = True
                                break
                    i = i+1
                    if(breaker == True):
                        breaker = False
                        break                  
                h = h+1
            v = v+1
        return matrix

    def erosion(self,imgFile,l,k,seFile,n,m):
        """
            The method performs erosion of a binary image with 
            respect to a structuring element 'SE'
            
            :param imgFile: Matrix of the image
            :param l: Number of rows of the image matrix
            :param k: Number of columns of the image matrix
            :param seFile: Maxtrix of SE
            :param n: Number of rows of SE matrix
            :param m: Number of columns of SE matrix
            :return: Eroded matrix
        """
        matrix = [[0 for x in range(k)] for y in range(l)] 
        if(m%2 != 0 and n%2 != 0):
            col = int((m/2)-1/2)
            row = int((n/2)-1/2)
            seRow = row
            seCol = col
        else:
            col = m-1
            row = n-1
            seRow = 0
            seCol = 0
        breaker = False
        v = 0
        while v != l:
            h = 0
            while h != k:
                i = 0
                while i <= row:
                    j = -1
                    while j < col:
                        j = j + 1
                        if(seFile[seRow+i][seCol+j]!=0 and (v+i < l) and (h+j < k)):
                            if(imgFile[v+i][h+j] == 1):
                                breaker = True
                                matrix[v][h] = 1
                            else:
                                breaker = False
                                matrix[v][h] = 0
                                break

                        if(seFile[seRow+i][seCol-j]!=0 and (v+i < l) and (h-j >= 0)):
                            if(imgFile[v+i][h-j] == 1):
                                breaker = True
                                matrix[v][h] = 1
                            else:
                                breaker = False
                                matrix[v][h] = 0
                                break

                        if(seFile[seRow-i][seCol+j]!=0 and (v-i >= 0) and (h+j < k)):
                            if(imgFile[v-i][h+j] == 1):
                                breaker = True
                                matrix[v][h] = 1
                            else:
                                breaker = False
                                matrix[v][h] = 0
                                break
                        
                        if(seFile[seRow-i][seCol-j]!=0 and (v-i >= 0) and (h-j >= 0)):
                            if(imgFile[v-i][h-j] == 1):
                                breaker = True
                                matrix[v][h] = 1
                            else:
                                breaker = False
                                matrix[v][h] = 0 
                                break
                    i = i+1
                    if(breaker == False):
                        break
                h = h+1
            v = v+1
        return matrix

    def eroDil_Gray(self,imgFile,l,k,seFile,n,m,word):
        """
            The method performs erosion and dilation of a grayscale image with 
            respect to a structuring element 'SE'
            
            :param imgFile: Matrix of the image
            :param l: Number of rows of the image matrix
            :param k: Number of columns of the image matrix
            :param seFile: Maxtrix of SE
            :param n: Number of rows of SE matrix
            :param m: Number of columns of SE matrix
            :param word: Character that indicates to the operation ('d'/'e')
            :return: Eroded matrix/Dilated Matrix
        """
        matrix = [[0 for x in range(k)] for y in range(l)] 
        if(m%2 != 0 and n%2 != 0):
            col = int((m/2)-1/2)
            row = int((n/2)-1/2)
            seRow = row
            seCol = col
        else:
            col = m-1
            row = n-1
            seRow = 0
            seCol = 0
        greyArr = list()
        v = 0
        while v != l:
            h = 0
            while h != k:
                i = 0
                while i <= row:
                    j = -1
                    while j < col:
                        j = j + 1
                        if(seFile[seRow+i][seCol+j]!=0 and (v+i < l) and (h+j < k)):
                            greyArr.append(imgFile[v+i][h+j])

                        if(seFile[seRow+i][seCol-j]!=0 and (v+i < l) and (h-j >= 0)):
                            greyArr.append(imgFile[v+i][h-j])

                        if(seFile[seRow-i][seCol+j]!=0 and (v-i >= 0) and (h+j < k)):
                            greyArr.append(imgFile[v-i][h+j])
                        
                        if(seFile[seRow-i][seCol-j]!=0 and (v-i >= 0) and (h-j >= 0)):
                            greyArr.append(imgFile[v-i][h-j])
                    i = i+1
                if(word == 'd'):
                    matrix[v][h] =  max(greyArr)
                else:
                    matrix[v][h] =  min(greyArr)
                greyArr[:] = []
                h = h+1
            v = v+1
        return matrix
    
    def getCSVandPNG(self, word, result):
        """
            The method writes resulted matrix into CSV style file 
            and PNG file
            :param word: Name of the TXT file
            :param word: Resulted matrix
        """
        with open('../output/'+ word,"w+") as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',') 
            csvWriter.writerows(result)
        name = word.split('.')
        cv2.imwrite("../output/"+name[0]+".png",np.array(result))
    
class img:
    def __init__(self,file):
        """
            The method reads csv file and writes it as a list 
            :param file: Path to the file
        """
        with open(file, 'r')as f:
           csv_file = csv.reader(f,delimiter=',')
           self.data_as_list = list(csv_file)
    
    def getArray(self):
        """
            The method returns a matrix of the list data 
        """
        seFile = [list(map(int,x)) for x in self.data_as_list]
        return seFile

    def getSize(self):
        """
            The method returns the size of the matrix
        """
        return np.shape(self.data_as_list)

    def checkImg(self,array):
        """
            The method checks if the image is binary or not
        """
        for x  in array:
            for val in x:
                if val > 1:
                    return True

userInput = input()
words = userInput.split()
sePath = '../input/' + words[2]
imgPath = '../input/' + words[3]

imgObj = img(imgPath)
l = imgObj.getSize()[0]
k = imgObj.getSize()[1]
imgArray = imgObj.getArray()

seObj = img(sePath)
n = seObj.getSize()[0]
m = seObj.getSize()[1]
seArray = seObj.getArray()

dilObj = Dil_Ero()
if(words[1] == 'e'):
    if(imgObj.checkImg(imgArray)):
        result = dilObj.eroDil_Gray(imgArray,l,k,seArray,n,m,'e')
    else:
        result = dilObj.erosion(imgArray,l,k,seArray,n,m)
    dilObj.getCSVandPNG(words[4],result)
elif(words[1] == 'd'):
    if(imgObj.checkImg(imgArray)):
        result = dilObj.eroDil_Gray(imgArray,l,k,seArray,n,m,'d')
    else:
        result = dilObj.dilation(imgArray,l,k,seArray,n,m)
    dilObj.getCSVandPNG(words[4],result)
else:
    print("There is no such operation!")
    exit