import cv2
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

img_path = 'gtr.jpg' 
image = Image.open(img_path)

# Brightness & Contrast
enhancer_bright = ImageEnhance.Brightness(image)
bright_image = enhancer_bright.enhance(1.5)  # 1.0 = normal

enhancer_contrast = ImageEnhance.Contrast(bright_image)
contrast_image = enhancer_contrast.enhance(1.5)  # 1.0 = normal

# Grayscale
gray_image = image.convert("L")

# Sharpness
enhancer_sharp = ImageEnhance.Sharpness(image)
sharp_image = enhancer_sharp.enhance(3.0)  # 1.0 = normal

# Tampilkan hasil
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].imshow(image)
axs[0].set_title("Original")
axs[1].imshow(contrast_image)
axs[1].set_title("Brightness & Contrast")
axs[2].imshow(gray_image, cmap='gray')
axs[2].set_title("Grayscale")
axs[3].imshow(sharp_image)
axs[3].set_title("Sharpness")

for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()
