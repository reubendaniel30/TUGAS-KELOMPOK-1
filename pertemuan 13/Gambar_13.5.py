import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load gambar 
image = cv2.imread('rubik.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Konversi ke HSV
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Equalize hanya channel V (brightness)
h, s, v = cv2.split(hsv)
v_eq = cv2.equalizeHist(v)
hsv_eq = cv2.merge((h, s, v_eq))

# Konversi kembali ke RGB
enhanced = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2RGB)

# Tampilkan hasil
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Sebelum Enhancement")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(enhanced)
plt.title("Setelah Enhancement")
plt.axis('off')

plt.tight_layout()
plt.show()
