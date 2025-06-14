import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('rubik.jpg')  
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Segmentasi Thresholding
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 2. Segmentasi K-Means
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  # Jumlah cluster
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
kmeans_segmented = centers[labels.flatten()]
kmeans_segmented = kmeans_segmented.reshape(image.shape)

# 3. Segmentasi Watershed
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(image, markers)
image[markers == -1] = [255,0,0]

# Menampilkan hasil
plt.figure(figsize=(20, 10))

plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title('rubik asli (dengan watershed)')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(thresh, cmap='gray')
plt.title('Thresholding')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(kmeans_segmented)
plt.title('K-Means (k=3)')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(markers, cmap='jet')
plt.title('Watershed')
plt.axis('off')

plt.tight_layout()
plt.show()