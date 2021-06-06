import cv2
import random
import numpy as np
import master_share_generator as master
import utils

def wm_gen(PATH, owner):
    random.seed(a=utils.KEY)
    random_points = random.sample(range(utils.IMG_SIZE), utils.WATERMARK_SIZE)
    owner_img = cv2.imread(owner, 0)
    master_img = master.gen(PATH)
    watermark_img = np.zeros((utils.WATERMARK_WIDTH, utils.WATERMARK_HEIGHT, 1), np.uint8)

    i = 0
    j = 0

    for i in range(0, utils.WATERMARK_HEIGHT):
        for j in range(0, utils.WATERMARK_WIDTH):
            watermark_img[i, j] = utils.xor(master_img[i, j], owner_img[i, j])

    watermark_img = (255-watermark_img)
    kernel = np.ones((4,4),np.uint8)
    watermark_img = cv2.medianBlur(watermark_img, 3)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_OPEN, kernel)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_CLOSE, kernel)
    watermark_img = (255-watermark_img)

    cv2.imshow("Extracted Watermark", watermark_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return watermark_img
