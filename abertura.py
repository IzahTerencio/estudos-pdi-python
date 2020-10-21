from PIL import Image #importando o módulo Image da biblioteca PIL
                      #esse módulo permite realizar várias operações com imagens, neste exemplo focaremos em estudar pixels
import os             #o módulo os utiliza as funcionalidades do sistema operacional, para entrada, manipulação de path...

INPUT_FOLDER = "input"   #recebe a pasta input criada no projeto
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.open(in_path("imagem01.jpg"))
print(image.getpixel((100,100)))

#image = Image.open("imagem01.jpg")
#image.show() #exibe a imagem
#print(image.getpixel((200,200)))