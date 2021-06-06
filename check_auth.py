import cv2
import numpy as np
from watermark_generator import wm_gen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image')
parser.add_argument('--watermark')
parser.add_argument('--owner')

args = parser.parse_args()

template = cv2.imread(args.watermark,0)
PATH = args.image
owner = args.owner

final = wm_gen(PATH, owner)

res = cv2.matchTemplate(final,template,cv2.TM_CCOEFF_NORMED)

if(res[0] > 0.8):
    print("The Picture is Authentic! [%0.2f Percent Similar]"%(res[0]*100))
else:
    print("The Picture is Fake! [%0.2f Percent Similar]"%(res[0]*100))
