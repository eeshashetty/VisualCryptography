import cv2
import random
import numpy as np
import argparse
from master_share_generator import gen
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--image')
parser.add_argument('--watermark')

args = parser.parse_args()

PATH = args.image
WM_PATH = args.watermark

watermark_img = cv2.imread(WM_PATH, 0)
ret,watermark_img = cv2.threshold(watermark_img,127,255,cv2.THRESH_BINARY)

master_img = gen(PATH)
owner_img = np.zeros((utils.WATERMARK_WIDTH, utils.WATERMARK_HEIGHT, 1), np.uint8)

random.seed(a=utils.KEY)
random_points = random.sample(range(utils.IMG_SIZE), utils.WATERMARK_SIZE)

i = 0
j = 0


for i in range(0, utils.WATERMARK_HEIGHT):
    for j in range(0, utils.WATERMARK_WIDTH):
        owner_img[i, j] = utils.xor(master_img[i, j], watermark_img[i, j])

cv2.imshow('Master Image', master_img)
cv2.imshow('Owner Image', owner_img)

cv2.imwrite('images/owner_img.jpg', owner_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
