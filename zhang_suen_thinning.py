import matplotlib
import matplotlib.pyplot as plt
import skimage.io as io
from PIL import Image
"load image data"
img = Image.open('subpixel5.png')
file_out = "test1.png"
img.save(file_out)

Img_Original =  io.imread( 'test1.png', as_grey=True)      # Gray image, rgb images need pre-conversion

"Convert gray images to binary images using Otsu's method"
from skimage.filter import threshold_otsu
Otsu_Threshold = threshold_otsu(Img_Original)   
BW_Original = Img_Original < Otsu_Threshold    # must set object region as 1, background region as 0 !

def neighbours(x,y,image):
    "Return 8-neighbours of image point P1(x,y), in a clockwise order"
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],     # P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]    # P6,P7,P8,P9

def transitions(neighbours):
    "No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence"
    n = neighbours + neighbours[0:1]      # P2, P3, ... , P8, P9, P2
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

coords = []
def zhangSuen(image):
    "the Zhang-Suen Thinning Algorithm"
    Image_Thinned = image.copy()  # deepcopy to protect the original image
    changing1 = changing2 = 1        #  the points to be removed (set as 0)
    while changing1 or changing2:   #  iterates until no further changes occur in the image
        # Step 1
        changing1 = []
        print(Image_Thinned.shape)
        rows, columns = Image_Thinned.shape               # x for rows, y for columns
        for x in range(1, rows - 1):                     # No. of  rows
            for y in range(1, columns - 1):            # No. of columns
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1     and    # Condition 0: Point P1 in the object regions 
                    2 <= sum(n) <= 6   and    # Condition 1: 2<= N(P1) <= 6
                    transitions(n) == 1 and    # Condition 2: S(P1)=1  
                    P2 * P4 * P6 == 0  and    # Condition 3   
                    P4 * P6 * P8 == 0):         # Condition 4
                    changing1.append((x,y))
                    coords.append((x, y))

        # print('lol')
        # print(changing1)
        for x, y in changing1: 
            Image_Thinned[x][y] = 0

        # Step 2
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                # 1 is black, 0 is white
                if (Image_Thinned[x][y] == 1   and # Condition 0 - is black pixel
                    2 <= sum(n) <= 6  and  # Condition 1 - 2 to 6 black neighbor
                    transitions(n) == 1 and  # Condition 2 - only 1 neighbor to transition to *******
                    P2 * P4 * P8 == 0 and       # Condition 3 - TOP HALF... either 2, 4, or 8 is white
                    P2 * P6 * P8 == 0):            # Condition 4: BOTTOM HALF... either 2, 6, or 8 is white
                    coords.append((x, y))   
        for x, y in changing2: 
            Image_Thinned[x][y] = 0 # the 0 pixels are the white ones

    return Image_Thinned
 

"Apply the algorithm on images"
BW_Skeleton = zhangSuen(BW_Original)

# -------------------------------------------------------------
print(type(BW_Skeleton))
print('yahaoalalallalalao')
# coords = BW_Skeleton.tolist()
print(coords) # array containing coordinates of points

set_coords = set(coords)

height, width = BW_Skeleton.shape
dpi = 80
# What size does the figure need to be in inches to fit the image?
figsize = width / float(dpi), height / float(dpi)

# Create a figure of the right size with one axes that takes up the full figure
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

# Display the image.
ax.imshow(BW_Skeleton, cmap='gray')
print(type(ax))

fig.savefig('asdf.png')