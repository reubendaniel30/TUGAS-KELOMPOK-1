import cv2
import matplotlib.pyplot as plt

# Load classifier untuk wajah
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Baca gambar
img = cv2.imread('nba.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

# Deteksi wajah
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Gambar bounding box di sekitar wajah
for (x, y, w, h) in faces:
    cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (255, 0, 0), 3)  # Kotak biru
    cv2.putText(img_rgb, 'Wajah', (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

plt.figure(figsize=(12, 8))
plt.imshow(img_rgb)
plt.axis('off')
plt.title(f'Deteksi Wajah: {len(faces)} ditemukan')
plt.show()

print("\nHasil Deteksi:")
print(f"Jumlah wajah terdeteksi: {len(faces)}")
for i, (x, y, w, h) in enumerate(faces, 1):
    print(f"Wajah {i}: Posisi (X:{x}, Y:{y}), Ukuran {w}x{h} piksel")