import cv2
import os
import matplotlib.pyplot as plt

img = cv2.imread('rubik.jpg')

# Kompres gambar menjadi JPEG dengan kualitas rendah
compressed_path = 'compressed_image.jpg'
cv2.imwrite(compressed_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])  # Kualitas 0-100

# Tampilkan ukuran file sebelum dan sesudah kompresi
original_size = os.path.getsize('rubik.jpg')
compressed_size = os.path.getsize(compressed_path)

print(f"Ukuran asli       : {original_size / 1024:.2f} KB")
print(f"Ukuran terkompres : {compressed_size / 1024:.2f} KB")

# Tampilkan gambar hasil kompresi menggunakan matplotlib
compressed_img = cv2.imread(compressed_path)
compressed_img = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB

plt.imshow(compressed_img)
plt.title("Compressed Image")
plt.axis('off')
plt.show()
