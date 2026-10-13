from PIL import Image, ImageDraw, ImageFont
import os

PATH = r'C:\Users\86297\Desktop\RPA\RPA\imagens'

fonte = ImageFont.load_default()

for arquivo in os.listdir(PATH):
    imagem = Image.open(rf'{PATH}/{arquivo}')
    imagem = imagem.convert(mode='L')
    imagem = imagem.rotate(90, expand=True)

    draw = ImageDraw.Draw(imagem)

    draw.text((15, 15), arquivo, fill=0, font=fonte)

    imagem.save(rf'{PATH}/CONVERTIDO {arquivo}')


    # print(arquivo)

# imagem = Image.open(r'imagens\borat!.jpg')

# imagem = imagem.resize((1400,1400))

# imagem.show()