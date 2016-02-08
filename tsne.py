#!/usr/bin/env python
# -*- coding: utf-8 -*-

# port to python of @karpathy's matlab code for t-SNE
# visualization of Imagenet
# see http://cs.stanford.edu/people/karpathy/cnnembed/
# download imagenet_val_embed.mat, val_imgs_med.txt there

# prerequisites: imagenet 2012 validation images
# get here: www.image-net.org
# resize images to 50x50
# set your paths appropriately in val_imgs_med.txt
# see included scripts

from __future__ import division

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# load the tsne points
data = sio.loadmat('imagenet_val_embed.mat')

# set min point to 0 and scale
x = data['x'] - np.min(data['x'])
x = x / np.max(x)

# create embedding image
S = 2000  # size of full embedding image
G = np.zeros((S, S, 3), dtype=np.uint8)
s = 50  # size of single image


with open('val_imgs_med2.txt') as f:
	for i, fs in enumerate(f):
		if np.mod(i, 100) == 0:
			print('%d/%s...\n') % (i, str.split(fs, '/')[2])

		# set location
		a = np.ceil(x[i, 0] * (S-s-1)+1)
		b = np.ceil(x[i, 1] * (S-s-1)+1)
		a = a - np.mod(a-1,s) + 1
		b = b - np.mod(b-1,s) + 1
		if G[a,b,0] != 0:
		    continue

		I = plt.imread(fs.rstrip())

		G[a:a+s, b:b+s,:] = I
	    
plt.imshow(G)
plt.show()