from PIL import Image #importando o módulo Image da biblioteca PIL
                      #esse módulo permite realizar várias operações com imagens, neste exemplo focaremos em estudar pixels
import os             #o módulo os utiliza as funcionalidades do sistema operacional, para entrada, manipulação de path...

INPUT_FOLDER = "input"   #recebe a pasta input criada no projeto
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

#image = Image.new("RGB",(500,500),(255,255,0))
#image.show()

#FUNÇÃO PARA PINTAR UM TRIÂNGULO NA PARTE DE BAIXO DA IMAGEM
def triangulo(size):
    branco = (255,255,255)
    preto  = (0,0,0)

    image = Image.new("RGB", (size,size), branco)

    for x in range(size):
        for y in range(size):
            if (x<y):
                image.putpixel((x,y), preto)
    return image

#para desenhar figura semelhante à bandeira da França: retângulo com três listras
def bandeira_franca(altura):
    azul = (0,85,164)
    branco = (255,255,255)
    vermelho = (239,65,53)
    largura = 3*altura//2 #// é operação de divisão inteira

    image = Image.new("RGB",(largura,altura),branco) #a imagem inicia toda branca
    intervalo = largura//3

    for x in range(intervalo):
        for y in range(altura):
            image.putpixel((x,y),azul)
            image.putpixel((x+2*intervalo,y),vermelho)
    return image

#para ser executado como main
if __name__ == "__main__":
    t = bandeira_franca(700)
    t.show()