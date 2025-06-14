import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar dalam grayscale
img = cv2.imread('sidik jari.jpg', 0)

# Threshold untuk membuat gambar biner
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Kernel morfologi (struktur persegi 3x3)
kernel = np.ones((3, 3), np.uint8)

# Operasi morfologi
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Tampilkan hasil
titles = ['Original Binary', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [binary, erosion, dilation, opening, closing]

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
