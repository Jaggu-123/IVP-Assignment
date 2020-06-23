from PIL import Image
img = Image.open('Lenna.png').convert('LA')
img.show()