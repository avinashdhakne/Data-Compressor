import os
import PIL
from PIL import Image

def compressMe(file, name): 
    print('Name: ' + file)
    Image = PIL.Image.open(file)
    height, width = Image.size
    Img = Image.resize((int(height/2),int(width/2)))
    Img.save(f'{name}.jpeg')

dir = os.getcwd()
verbose = False

for a,b,c in os.walk(dir):
    for files in c:
        
        # print(a,b)
        dirname = a.split('\\')
        # print(dirname[-1:])

        # print(files)
        name = files.split('.')
        # print(name[1])

        path = os.path.join(a, files)
        try:
            compressMe(path, name)
            print('[Success]:', path , '\n\n')
        except Exception as e:
            print("[ERROR]: ", path)
            print(e, end='\n\n')

    print("---------------------")
