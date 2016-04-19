from PIL import Image
import utils

def iterate(p):
    z = 0
    iteration = 0
    z = z**level + p
    while abs(z) < 2 and iteration < max_iteration:
        z = z**level + p
        iteration += 1
    return iteration

def render_fractal():
    for i in xrange(size):
        for j in xrange(size):
            p = complex(x_center + 2.5 * (float(i - size / 2) / size),
                        y_center + 2.5 * (float(j - size / 2) / size))
            iteration = iterate(p)
            if iteration == max_iteration:
                color_value = 255
            else:
                color_value = iteration * 10 % 255
            im.paste((color_value, color_value, color_value), (i, j, i + 1 , j + 1))

max_iteration = 1000
level = utils.get_level_input()
x_center = -0.75 if level == 2 else 0.0
y_center = 0.0
size = 400
im = Image.new("RGB", (size, size))

render_fractal()
im.save("mandelbrot.png", "PNG")
