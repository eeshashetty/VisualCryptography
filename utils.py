IMG_WIDTH = 1180
IMG_HEIGHT = 799
WATERMARK_WIDTH = 256
WATERMARK_HEIGHT = 256

IMG_SIZE = IMG_HEIGHT * IMG_WIDTH
WATERMARK_SIZE = WATERMARK_HEIGHT * WATERMARK_WIDTH

KEY = 1001
THRESH = 75

def xor(x ,y):
     if x == 0 and y == 0:
         return 0
     elif x == 0 and y != 0:
         return 255
     elif x != 0 and y == 0:
         return 255
     elif x !=0 and y != 0:
         return 0
def mean_neighbour(img, x, y):
     val = 0
     num = 0
     i = x
     j = y
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x + 1
     j = y + 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x - 1
     j = y - 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x + 1
     j = y
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x
     j = y + 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x + 1
     j = y - 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x - 1
     j = y + 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1
     i = x - 1
     j = y
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val = val + img[i, j]
         num += 1
     i = x
     j = y - 1
     if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
         val += img[i, j]
         num += 1

     return val/float(num)

