def getDirectory():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    return file_path
print("Este software agrupa las imagenes y videos de la carpeta seleccionada en retrato, paisaje, videos y imagenes animadas")
print("This software sorts images and videos of the selected folder in portrait, landscape, video files and animated gif")
print("[ES] Selecciona la carpeta a sortear\\[EN] Select the folder you desire to sort")
try:
    workingDirectory = getDirectory()+"//"
    from PIL import Image
    import os
    from pathlib import Path

    print("Sorting images in "+workingDirectory+'...')
    for individualFile in os.listdir(workingDirectory):
        try:
            filePath = workingDirectory + individualFile
            if individualFile.endswith(('.jpg', '.png', '.jpeg', '.bmp', '.webp', '.png', '.JPG', '.PNG', '.JPEG', '.BMP', '.WEBP', '.PNG')): #accepted file extensions
                portrait = True
                square = False
                print('Processing\\Procesando: ' + str(individualFile))
                with Image.open(filePath) as imageObject:
                    if imageObject.size[0] == imageObject.size[1]:
                        square = True
                    else:
                        if imageObject.size[0] > imageObject.size[1]:
                            portrait = False
                if square:
                    Path(workingDirectory + 'SORTED MEDIA\\' + 'square\\').mkdir(parents=True, exist_ok=True)
                    os.rename(filePath, workingDirectory + 'SORTED MEDIA\\'+'square\\' + individualFile)
                else:
                    if portrait:
                        Path(workingDirectory + 'SORTED MEDIA\\' + 'portrait\\').mkdir(parents=True, exist_ok=True)
                        os.rename(filePath, workingDirectory + 'SORTED MEDIA\\'+'portrait\\' + individualFile)
                    else:
                        Path(workingDirectory + 'SORTED MEDIA\\' + 'landscape\\').mkdir(parents=True, exist_ok=True)
                        os.rename(filePath, workingDirectory + 'SORTED MEDIA\\'+'landscape\\' + individualFile)
            elif individualFile.endswith(('.gif','.GIF')):
                print('Processing: ' + str(individualFile))
                Path(workingDirectory + 'SORTED MEDIA\\' + 'animated gif\\').mkdir(parents=True, exist_ok=True)
                os.rename(filePath, workingDirectory + 'SORTED MEDIA\\'+'animated gif\\' + individualFile)
            elif individualFile.endswith(('.webm', '.mp4', '.mkv', '.avi', '.WEBM', '.MP4', '.MKV', '.AVI')):
                print('Processing: ' + str(individualFile))
                Path(workingDirectory + 'SORTED MEDIA\\' + 'video\\').mkdir(parents=True, exist_ok=True)
                os.rename(filePath, workingDirectory + 'SORTED MEDIA\\'+'video\\' + individualFile)
        except:
            print("Last imaged failed to process")
            print("La ultima imagen no fue procesada debido a un error")
    print("\nEl procesado finalizo con exito")
    print("Processing finished successfully")
except:
    print("Error selecciona una ruta correcta//Error desconocido")
    print("Error, select a correct folder path//Unknown error")
input("Presione cualquier tecla para salir/Press any key to exit")