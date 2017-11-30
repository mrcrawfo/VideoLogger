# python scripts/scrape.py data

import locale
locale.setlocale(locale.LC_ALL, '')

import os
import sys

chapters = []

class Chapter:
    index = None
    
    def __init__(self, index):
        self.index = index

fd = sys.argv[1]
files = [f for f in os.listdir(fd) if os.path.isfile(os.path.join(fd, f))]
currentChapter = None
for fn in files:
    if os.path.exists(os.path.join(fd, fn)) and fn != '.DS_Store':
        print(fn)
        with open(os.path.join(fd, fn)) as file:
            e = None
            for line in file:
                if not line.startswith('index'):
                    chapterIndex = int(line.split(',')[4])
                    if currentChapter is None or currentChapter.index != chapterIndex:
                        currentChapter = Chapter(chapterIndex)
                        chapters.append(currentChapter)
                        print(currentChapter.index)

print(len(chapters))