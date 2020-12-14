from PIL import Image
import os
from pathlib import Path
def getDirectory():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path
workingDirectory = getDirectory() + '//'
print("Sorting images in "+workingDirectory+'...')
Path(workingDirectory+'badRatio').mkdir(parents=True, exist_ok=True)
Path(workingDirectory+'goodRatio').mkdir(parents=True, exist_ok=True)
for individualFile in os.listdir(workingDirectory):
    if individualFile.endswith(('.jpg','.png','.jpeg','.bmp')): #accepted file extensions
        print('Processing: '+str(individualFile))
        badRatio = True
        filePath = workingDirectory+individualFile
        #print(filePath)
        with Image.open(filePath) as imageObject:
            if ((imageObject.size[0] / imageObject.size[1]) > 1.3) and ((imageObject.size[0] / imageObject.size[1]) < 2) and imageObject.size[0]>999:
                badRatio = False
        if badRatio:
            os.rename(filePath, workingDirectory + 'badRatio\\' + individualFile)
        else:
            os.rename(filePath, workingDirectory + 'goodRatio\\' + individualFile)
print("\nProcessing finished successfully")