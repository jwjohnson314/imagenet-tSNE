# imagenet-tSNE
python port of karpathy t-SNE code for visualization of Imagenet
See http://cs.stanford.edu/people/karpathy/cnnembed/

To run, download the scripts here, the files imagenet_val_embed.mat, val_imgs_med.txt from above, and the imagenet 2012 validation data from www.image-net.org. 

In resize_imagenet_small.py, set IMAGE_ROOT to path to imagenet validation data

put all other files in one directory. Set TSNE_ROOT to that directory path in resize_imagenet_small.py and in run.sh

./run.sh

