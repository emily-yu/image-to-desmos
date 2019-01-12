# import cv2;
# import numpy as np;
from PIL import Image
 
import cv2
import numpy as np
from matplotlib import pyplot as plt

# turn main parts of images into blobs
def blobify(file_path, new_file_name):
	# im_in = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE);
	# th, im_th = cv2.threshold(im_in, 120, 255, cv2.THRESH_BINARY_INV);
	# im_floodfill = im_th.copy()
	 
	# # fill
	# h, w = im_th.shape[:2]
	# mask = np.zeros((h+2, w+2), np.uint8)
	# cv2.floodFill(im_floodfill, mask, (0,0), 255);
	# im_floodfill_inv = cv2.bitwise_not(im_floodfill)
	# im_out = im_th | im_floodfill_inv
	 

	# im2 = Image.fromarray(im_out)
	# im2 = im2.convert("RGB")

	# im2.save(new_file_name)

	# img = cv2.imread(file_path,0)
	# edges = cv2.Canny(img,100,200)
	# edges = cv2.dilate(edges, None, iterations=10)
	# edges = cv2.erode(edges, None, iterations=1)

	# plt.subplot(121),plt.imshow(img,cmap = 'gray')
	# plt.title('Original Image'), plt.xticks([]), plt.yticks([])


	dpi = 80
	# im_data = img
	im_data = cv2.imread(file_path,0)
	edges = cv2.Canny(im_data,100,200)
	edges = cv2.dilate(edges, None, iterations=5)
	edges = cv2.erode(edges, None, iterations=4)
	edges = cv2.bitwise_not(edges)

	height, width = im_data.shape

	# What size does the figure need to be in inches to fit the image?
	figsize = width / float(dpi), height / float(dpi)

	# Create a figure of the right size with one axes that takes up the full figure
	fig = plt.figure(figsize=figsize)
	ax = fig.add_axes([0, 0, 1, 1])

	# Hide spines, ticks, etc.
	ax.axis('off')

	# Display the image.
	ax.imshow(edges, cmap='gray')

	# plt.show()

	# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	# plt.title(''), plt.xticks([]), plt.yticks([])

	# fig, ax = plt.subplots(1)
	# # plt.figure(figsize=(12, 9))
	# for ind in df.index:
	#     ax.scatter(df.loc[ind, 'wt'], df.loc[ind, 'mpg'], label=ind)
	# ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
	# fig.tight_layout()
	# plt.show()
	fig.savefig('lol3.jpg')
	#----------------------END MAKING THE EDGES LOOK NICER
	print('done')


blobify('leaf-identification.jpg', 'lol3.jpg')
