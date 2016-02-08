#!/usr/bin/env sh

TSNE_ROOT='/YOUR/PATH/HERE'

resize_images () {
	mkdir $TSNE_ROOT/ILSVRC2012_img_val_small
	python resize_imagenet_small.py
	touch $TSNE_ROOT/resize_done
}

set_paths () {
	sed 's/\/data\/ILSVRC2012\/val/.\/ILSVRC2012_img_val_small/g' $TSNE_ROOT/val_imgs_med.txt > $TSNE_ROOT/val_imgs_med2.txt
	sed -i 's/.JPEG/.JPEG.small.jpeg/g' $TSNE_ROOT/val_imgs_med2.txt
	touch paths_set
}

if [ -f $TSNE_ROOT/resize_done ]
then 
	echo $TSNE_ROOT/resize_done exists, skipping resizing
else
	resize_images
fi

if [ -f $TSNE_ROOT/paths_set ]
then
	echo $TSNE_ROOT/paths_set exists, skipping setting paths_set
else
	set_paths
fi

python tsne.py