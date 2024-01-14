import numpy as np
import matplotlib.pyplot as plt

# Add a mask to the image and display it
img1 = plt.imread('Images/DSCN0453_e.JPG')
nrows, ncols, channels = img1.shape
row, col = np.ogrid[:nrows, :ncols]
center_row, center_col = nrows/2, ncols/2
outer_disk_mask = ((row - center_row) ** 2 +
                   (col - center_col) ** 2) > (ncols/2)**2
img1.setflags(write=True)
img1[outer_disk_mask] = 128
plt.imshow(img1)
plt.axis('off')
plt.title('Masked Image')
plt.show()
