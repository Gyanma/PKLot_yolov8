import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from blur import ImageProcessor  # Supponendo che il tuo codice sia in un file chiamato "image_processor.py"


class Gui:

    def __init__(self, root):

        self.root = root
        self.root.title("PkLot")
        self.root.geometry("800x600")
        root.configure(bg="white")


        self.model_path = 'best.pt'
        self.image_path = None
        self.processor = None

        self.select_image_button = tk.Button(self.root, text="Seleziona immagine", command=self.load_image)
        self.select_image_button.pack()


        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            image = Image.open(self.image_path)
            image = image.resize((300, 300))
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
            if self.image_path:
                self.processor = ImageProcessor(self.model_path, self.image_path)
                self.processor.process()
                result_image = Image.open("example_with_blur.jpg")
                result_image = result_image.resize((300, 300))
                self.result_photo = ImageTk.PhotoImage(result_image)
                self.image_label.config(image=self.result_photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()
