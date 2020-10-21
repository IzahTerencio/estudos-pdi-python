from PIL import Image #importando o módulo Image da biblioteca PIL
                      #esse módulo permite realizar várias operações com imagens, neste exemplo focaremos em estudar pixels
image = Image.open("imagem01.jpg")
#image.show() #exibe a imagem
print(image.getpixel((200,200)))