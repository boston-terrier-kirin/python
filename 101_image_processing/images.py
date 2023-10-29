# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageFilter

import os
if not os.path.exists("test"):
    os.mkdir("test")

# pikachu
img = Image.open("./pokedex/pikachu.jpg")

# blur
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./test/blur.png", "png")

# grey
filtered_img = img.convert("L")

# rotate
crocked = filtered_img.rotate(90)
crocked.save("./test/grey.png", "png")

# resize
resized = filtered_img.resize((300, 300))
resized.save("./test/grey_300x300.png", "png")

# crop
box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
cropped.save("./test/grey_cropped.png", "png")

# astro
img = Image.open("./pokedex/astro.jpg")
img.thumbnail((400, 400))
img.save("./test/thumbnail.jpg")
