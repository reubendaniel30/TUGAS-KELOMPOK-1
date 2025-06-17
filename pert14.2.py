import tkinter as tk

def gambar():
    # Buat jendela utama
    root = tk.Tk()
    root.title("Aplikasi Komputer Grafik")

    # Buat canvas dengan ukuran dan warna background
    canvas = tk.Canvas(root, width=300, height=250, bg="white")
    canvas.pack()

    # Gambar polygon (bentuk tidak beraturan)
    points = [
        10, 10,
        200, 10,
        200, 110,
        30, 110,
        10, 125,
        20, 110,
        10, 110
    ]
    canvas.create_polygon(points, fill="yellow", outline="black")

    # Gambar teks
    canvas.create_text(50, 50, text="Komputer Grafik 1", anchor="nw", font=("Arial", 12), fill="black")

    # Jalankan GUI
    root.mainloop()

# Panggil fungsi utama
gambar()
