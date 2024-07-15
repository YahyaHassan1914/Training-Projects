import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, StringVar
from PIL import Image

"""
- Remember to add more immage types (only .png for now)
"""

class ImageResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Image Resizer")
        self.root.geometry("400x350")

        self.image_path = StringVar()

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Select an image to resize:").pack(pady=10)

        Entry(self.root, textvariable=self.image_path, width=50).pack(pady=5)

        Button(self.root, text="Browse", command=self.browse_image).pack(pady=5)

        Label(self.root, text="Enter new width:").pack(pady=10)
        self.width_entry = Entry(self.root)
        self.width_entry.pack(pady=5)

        Label(self.root, text="Enter new height:").pack(pady=10)
        self.height_entry = Entry(self.root)
        self.height_entry.pack(pady=5)

        Button(self.root, text="Resize Image", command=self.resize_image).pack(pady=20)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        self.image_path.set(file_path)

    def resize_image(self):
        img_path = self.image_path.get()
        if not os.path.isfile(img_path):
            messagebox.showerror("Error", "Invalid image file path.")
            return

        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Width and height must be integers.")
            return

        try:
            img = Image.open(img_path)
            resized_img = img.resize((width, height), Image.LANCZOS)

            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("PNG", "*.png")])
            if save_path:
                resized_img.save(save_path)
                messagebox.showinfo("Success", f"Image resized and saved to {save_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = Tk()
    app = ImageResizer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
