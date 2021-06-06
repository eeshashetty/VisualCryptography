import cv2
import random
import numpy as np
import utils

def gen(path):
    random.seed(a=utils.KEY)
    random_points = random.sample(range(utils.IMG_SIZE), utils.WATERMARK_SIZE)
    og_img = cv2.imread(path,0)

    master_img = np.zeros((utils.WATERMARK_WIDTH, utils.WATERMARK_HEIGHT, 1), np.uint8)

    i = 0
    j = 0

    for k in random_points:
        x = k // utils.IMG_WIDTH
        y = k % utils.IMG_WIDTH
        if utils.mean_neighbour(og_img, x, y) > utils.THRESH:
            master_img[i,j] = 255
        j += 1
        if j == 256:
            j = 0
            i += 1

    return master_img
