import sys

from PIL import Image

image = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif",save_
)
