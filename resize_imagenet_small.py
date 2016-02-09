#!/usr/bin/env/python

# resize imagenet 2012 val images

import os
import glob
import cv2

# path to imagenet validation data (50k images, original size)
IMAGE_ROOT = '/YOUR/PATH/HERE'
IMAGE_DEST = './ILSVRC2012_img_val_small/'

ims = glob.glob(os.path.join(IMAGE_ROOT, '*.JPEG'))

counter = 0.
for filename in ims:
	im = cv2.imread(filename)
	small = cv2.resize(im, (50,50))
	im_name = str.split(filename, '/')[5]
	cv2.imwrite(os.path.join(IMAGE_DEST, im_name + '-small.JPEG'), small)
	counter += 1
	if counter % 100 == 0:
		print '%d images done...' % counter
