#!/usr/bin/env sh

resize_images () {
	if [ ! -d './ILSVRC2012_img_val_small/' ]
	then
		echo 'creating directory for resized images'
		mkdir ./ILSVRC2012_img_val_small/
	fi
	echo 'resizing images'
	python resize_imagenet_small.py
	touch resize_done
}

set_paths () {
	sed 's/\/data\/ILSVRC2012\/val/.\/ILSVRC2012_img_val_small/g' val_imgs_med.txt > val_imgs_med2.txt
	touch paths_set
}

if [ -f resize_done ]
then 
	echo 'resize_done exists, skipping resizing'
else
	resize_images
fi

if [ -f paths_set ]
then
	echo 'paths_set exists, skipping setting paths_set'
else
	set_paths
fi

echo 'creating image'
python tsne.py