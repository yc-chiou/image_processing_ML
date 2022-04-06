import cv2
import numpy as np
from matplotlib import pyplot as plt
import myMath


def main(path1, path2):
    path1 = path1 + '.jpg'
    path2 = path2 + '.jpg'
    resolution1, hist1 = calculateHist(path1)
    plotHist(path1, hist1)
    resolution2, hist2 = calculateHist(path2)
    plotHist(path2, hist2)

    # Normalize hist
    for i in range(0, 3):
        hist1[i] = hist1[i] / resolution1
        hist2[i] = hist2[i] / resolution2
   
    color = ['b', 'g', 'r']
    for channel, col in enumerate(color):
        similarity = myMath.similarity(hist1[channel], hist2[channel])
        print('Simiarity of channel ' + col + ' is ' + str(similarity))

def calculateHist(path):
    img = cv2.imread(path, -1)
    height, width, channels = img.shape
    resolution  = height * width
   
    color = ['b', 'g', 'r']
    hist = []
    for channel, col in enumerate(color):
        hist.append(cv2.calcHist([img], [channel], None, [256], [0, 256]))
    
    return (resolution, hist)

def plotHist(path, hist):
    color = ['b', 'g', 'r']
    for channel, col in enumerate(color):
        plt.plot(hist[channel], color = col)    
        plt.xlim([0, 256])
    plt.title('Histogram for color scale picture of ' + path)
    plt.show()

if __name__ == "__main__":
    print('*********************************')
    print('*                               *')
    print('* Only jpg extension is allowed *')
    print('* Enter file name only          *')
    print('*                               *')
    print('*********************************')
    path1 = raw_input('Name of Sample 1 : ')
    path2 = raw_input('Name of Sample 2 : ')
    
    main(path1, path2)
