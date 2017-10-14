import numpy as np
import matplotlib
from PIL import Image
import math
from functions import *

x = 0
y = 0
nb_pixels_noirs_i1 = 0
nb_pixels_noirs_i2 = 0
nb_pixels_noirs_i = 0
nb_pixels_cercle = 0
i_inconnue = Image.open('images/image1.jpg')
i_ar = np.asarray(i_inconnue)
x_max_i = len(i_ar)
y_max_i = len(i_ar[0])

# pointsCercle = cercle(x_max_i, y_max_i, 1.* y_max_i/2, [0,0], 1000)


for x in range(x_max_i):
    for y in range(y_max_i):
        if (x - 1.* x_max_i / 2)*(x - 1.* x_max_i / 2) + (y - 1.*y_max_i/2)*(y - 1.*y_max_i/2) <= np.min([y_max_i, x_max_i])*np.min([y_max_i, x_max_i]):
            nb_pixels_cercle += 1
            if i_ar[x][y][0] <= 50 and i_ar[x][y][1] <= 50  and i_ar[x][y][2] <= 50:
                nb_pixels_noirs_i += 1

            # print "les coordonnes des points en noir sont: ", x, y

rapport_inc = 1.* nb_pixels_noirs_i / nb_pixels_cercle * 100

print rapport_inc
if rapport_inc > 5 and rapport_inc < 8:
    print 'Cette image est stylee'
