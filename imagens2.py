from PIL import ImageFilter, Image


imagem = Image.open(r'imagens\Borat!.jpg')
imagem.show()
imagem = imagem.filter(ImageFilter.CONTOUR)
imagem.show()