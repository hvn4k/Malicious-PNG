from PIL import Image
import random

img = Image.new("RGB", (100, 100))
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

img.save("1image.png")

