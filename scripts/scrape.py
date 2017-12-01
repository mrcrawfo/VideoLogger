# python scripts/scrape.py data

import locale
locale.setlocale(locale.LC_ALL, '')

import math
import os
import sys

chapters = []

class Chapter:
    index = None
    
    time = 0
    timeType1 = 0
    timeType2 = 0
    timeType3 = 0
    timeType4 = 0
    timeType5 = 0
    
    def __init__(self, index):
        self.index = index

fd = sys.argv[1]
files = [f for f in os.listdir(fd) if os.path.isfile(os.path.join(fd, f))]

currentChapter = None
currentTime = 0
currentType = 0

totalTime = 0
totalTimeType1 = 0
totalTimeType2 = 0
totalTimeType3 = 0
totalTimeType4 = 0
totalTimeType5 = 0

def zerofill(value, digits):
    output = str(value)
    while len(output) < digits:
        output = '0' + output
    return output

def formatTime(time):
    h = int(math.floor(time / 3600))
    m = int(math.floor((time % 3600) / 60))
    s = time % 60
    return zerofill(h, 2) + ':' + zerofill(m, 2) + ':' + zerofill(s, 2)

def formatPercent(typeTime, totalTime):
    return str(float('{0:.2f}'.format(100.0 * (float(typeTime) / float(totalTime))))) + '%'

def outputChapter(chapter):
    print('')
    print('Chapter ' + str(chapter.index) + ' (' + formatTime(chapter.time) + '):')
    print('    Type 1 :: ' + formatTime(chapter.timeType1) + ' :: ' + formatPercent(chapter.timeType1, chapter.time))
    print('    Type 2 :: ' + formatTime(chapter.timeType2) + ' :: ' + formatPercent(chapter.timeType2, chapter.time))
    print('    Type 3 :: ' + formatTime(chapter.timeType3) + ' :: ' + formatPercent(chapter.timeType3, chapter.time))
    print('    Type 4 :: ' + formatTime(chapter.timeType4) + ' :: ' + formatPercent(chapter.timeType4, chapter.time))
    print('    Type 5 :: ' + formatTime(chapter.timeType5) + ' :: ' + formatPercent(chapter.timeType5, chapter.time))
    
for fn in files:
    if os.path.exists(os.path.join(fd, fn)) and fn != '.DS_Store':
#        print(fn)
        with open(os.path.join(fd, fn)) as file:
            for line in file:
                if not line.startswith('index'):
                    markerType = int(line.split(',')[1])
                    markerTime = int(line.split(',')[2])
                    markerChapter = int(line.split(',')[4])
                    if currentChapter is None or currentChapter.index != markerChapter:
                        currentChapter = Chapter(markerChapter)
                        chapters.append(currentChapter)
                    else:
                        deltaTime = markerTime - currentTime
                        
                        currentChapter.time += deltaTime
                        totalTime += deltaTime
                        
                        if currentType == 1:
                            totalTimeType1 += deltaTime
                            currentChapter.timeType1 += deltaTime
                        elif currentType == 2:
                            totalTimeType2 += deltaTime
                            currentChapter.timeType2 += deltaTime
                        elif currentType == 3:
                            totalTimeType3 += deltaTime
                            currentChapter.timeType3 += deltaTime
                        elif currentType == 4:
                            totalTimeType4 += deltaTime
                            currentChapter.timeType4 += deltaTime
                        elif currentType == 5:
                            totalTimeType5 += deltaTime
                            currentChapter.timeType5 += deltaTime
                        
                        if markerType == 0:
                            currentTime = 0
                            currentType = 0
                        else:
                            currentTime = markerTime
                            currentType = markerType

for chapter in chapters:
    outputChapter(chapter)


print('')
print('--------------------------------------------------------')
print('')
print('Total (' + formatTime(totalTime) + '):')
print('    Type 1 :: ' + formatTime(totalTimeType1) + ' :: ' + formatPercent(totalTimeType1, totalTime))
print('    Type 2 :: ' + formatTime(totalTimeType2) + ' :: ' + formatPercent(totalTimeType2, totalTime))
print('    Type 3 :: ' + formatTime(totalTimeType3) + ' :: ' + formatPercent(totalTimeType3, totalTime))
print('    Type 4 :: ' + formatTime(totalTimeType4) + ' :: ' + formatPercent(totalTimeType4, totalTime))
print('    Type 5 :: ' + formatTime(totalTimeType5) + ' :: ' + formatPercent(totalTimeType5, totalTime))