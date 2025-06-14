import cv2
import matplotlib.pyplot as plt

# Load gambar
img = cv2.imread('gtr.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Konversi ke RGB

# Buat pyramid
pyramid = [img]
for i in range(3):  # Buat 3 level (Half, Quarter, Eighth)
    img = cv2.pyrDown(img)
    pyramid.append(img)

# Tampilkan hasil
titles = ['Full Resolution', 'Half', 'Quarter', 'Eighth']
plt.figure(figsize=(12, 4))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(pyramid[i])
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
