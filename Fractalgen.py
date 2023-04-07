from PIL import Image
import random

# image size
width = 1920
height = 1080

# create image
image = Image.new("RGB", (width, height), (255, 255, 255))

# fractal parameters
scale = 0.005
xoffset = random.uniform(-1, 1)
yoffset = random.uniform(-1, 1)
iterations = 500

# fractal function
def fractal(x, y):
    zx = 0
    zy = 0
    for i in range(iterations):
        xt = zx * zx - zy * zy + x
        yt = 2 * zx * zy + y
        if xt * xt + yt * yt > 4:
            return i
        zx, zy = xt, yt
    return iterations

# draw fractal
for x in range(width):
    for y in range(height):
        color = fractal(x * scale + xoffset, y * scale + yoffset) * 255 // iterations
        image.putpixel((x, y), (color, color, color))

# save image
image.save("fractal.png", dpi=(300, 300))
