import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("gray.jpeg")
im_rgb = im.convert('RGB')
arr_rgb = np.asarray(im_rgb)

rows, columns, _ = np.shape(arr_rgb)

plt.figure()
plt.imshow(im)
plt.gray()

# User selects the initial seed point
print('Please select the initial seed point')

pseed = plt.ginput(1)
x = int(pseed[0][0])
y = int(pseed[0][1])
seed_pixel = [x, y]

print('You clicked:', seed_pixel)

plt.close()

img_rg = np.zeros((rows + 1, columns + 1))
img_rg[seed_pixel[0], seed_pixel[1]] = 255.0  # Modified indexing to use comma instead of square brackets
region_points = [[x, y]]


def find_region():
    print('\nLoop runs until region growing is complete')
    count = 0
    x_offsets = [-1, 0, 1, -1, 1, -1, 0, 1]
    y_offsets = [-1, -1, -1, 0, 0, 1, 1, 1]

    while len(region_points) > 0:
        if count == 0:
            point = region_points.pop(0)
            i, j = point
        val = arr_rgb[i, j, 0]  # Modified indexing to use comma instead of square brackets
        lt = val - 8
        ht = val + 8
        for k in range(8):
            if img_rg[i + x_offsets[k], j + y_offsets[k]] != 1:  # Modified indexing to use comma instead of square brackets
                try:
                    if lt < arr_rgb[i + x_offsets[k], j + y_offsets[k], 0] < ht:  # Modified indexing to use comma instead of square brackets
                        img_rg[i + x_offsets[k], j + y_offsets[k]] = 1  # Modified indexing to use comma instead of square brackets
                        p = [i + x_offsets[k], j + y_offsets[k]]
                        if p not in region_points and 0 < p[0] < rows and 0 < p[1] < columns:
                            region_points.append(p)
                except IndexError:
                    continue
        point = region_points.pop(0)
        i, j = point
        count += 1


find_region()

plt.figure()
plt.imshow(img_rg, cmap="Greys_r")
plt.colorbar()
plt.show()