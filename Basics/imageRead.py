import numpy as np
import matplotlib.pyplot as plt


# Get image and display it
img1 = plt.imread('Images/DSCN0453_e.JPG')
plt.imshow(img1)
plt.axis('off')
plt.show()

# Print ndarray properties
print(type(img1))
print(img1.shape)
print(img1.ndim)
print(img1.size)
print(img1.dtype)
print(img1.nbytes)

print(img1.min())
print(img1.max())
print(img1.mean())
