import cv2
import numpy as np
import matplotlib.pyplot as plt

# Buat gambar kosong (hitam)
img = np.zeros((300, 300, 3), dtype=np.uint8)

# Gambar poligon melengkung (distorsi) - simulasi distorsi
pts_src = np.array([[60, 80], [240, 60], [220, 240], [80, 220]], np.int32)
pts_src = pts_src.reshape((-1, 1, 2))
cv2.fillPoly(img, [pts_src], (180, 180, 180))

# Simulasi image restoration dengan perspektif transform
src = np.float32([[60, 80], [240, 60], [220, 240], [80, 220]])
dst = np.float32([[60, 60], [240, 60], [240, 240], [60, 240]])

# Hitung transformasi & terapkan
M = cv2.getPerspectiveTransform(src, dst)
restored = cv2.warpPerspective(img, M, (300, 300))

# Tampilkan hasil
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Gambar Ter-distorsi")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(restored, cv2.COLOR_BGR2RGB))
plt.title("Hasil Restorasi")
plt.axis('off')

plt.tight_layout()
plt.show()
