import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from blur import ImageProcessor  # Supponendo che il tuo codice sia in un file chiamato "image_processor.py"

class Gui:

    def __init__(self, root):
        self.root = root
        self.root.title("PkLot")
        self.root.attributes("-fullscreen", True)  # Imposta il full screen
        root.configure(bg="white")

        self.model_path = 'best.pt'
        self.image_path = None
        self.processor = None

        # Creazione del frame principale
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Creazione della sidebar sulla destra
        self.sidebar_frame = tk.Frame(main_frame, bg="lightgray", width=150)
        self.sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.select_image_button = tk.Button(self.sidebar_frame, text="Seleziona immagine", command=self.load_image)
        self.select_image_button.pack(pady=10)

        self.button1 = tk.Button(self.sidebar_frame, text="blur car", command=self.blur_car)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.sidebar_frame, text="draw boxes", command=self.draw_bboxes)
        self.button2.pack(pady=10)

        self.quit_button = tk.Button(self.sidebar_frame, text="Chiudi", command=self.root.quit, bg="red", fg="white")  # Aggiunto il tasto di chiusura
        self.quit_button.pack(side=tk.BOTTOM, pady=10)

        # Etichetta per il testo sopra al riquadro
        self.title_label = tk.Label(main_frame, text="pk_lot v1.0 - by gyanma e FValerio96", font=("Helvetica", 12, "bold"))
        self.title_label.pack(side=tk.TOP, pady=10, padx=20, anchor="w")

        # Creazione del riquadro immagine
        self.image_frame = tk.Frame(main_frame, bg="white", highlightbackground="black", highlightthickness=1)  # Riquadro elegante
        self.image_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)  # Centra l'immagine

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            image = Image.open(self.image_path)
            image = image.resize((300, 300))
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)

    def blur_car(self):
        if self.image_path:
            self.processor = ImageProcessor(self.model_path, self.image_path)
            self.processor.pklot_busy()
            result_image = Image.open("example_with_blur.jpg")
            result_image = result_image.resize((300, 300))
            self.result_photo = ImageTk.PhotoImage(result_image)
            self.image_label.config(image=self.result_photo)

    def draw_bboxes(self):
        if self.image_path:
            self.processor = ImageProcessor(self.model_path, self.image_path)
            self.processor.pklot_free()
            result_image = Image.open("example_with_blur.jpg")
            result_image = result_image.resize((300, 300))
            self.result_photo = ImageTk.PhotoImage(result_image)
            self.image_label.config(image=self.result_photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    root.lift()  # Solleva la finestra all'avvio
    root.mainloop()
