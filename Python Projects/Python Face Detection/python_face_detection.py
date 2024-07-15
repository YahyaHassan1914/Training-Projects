import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

def detect_faces(image_path, output_path=None):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image file.")
        return

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Resize image for display if too large
    screen_res = 1280, 720
    scale_width = screen_res[0] / image.shape[1]
    scale_height = screen_res[1] / image.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(image.shape[1] * scale)
    window_height = int(image.shape[0] * scale)

    resized_image = cv2.resize(image, (window_width, window_height))

    # Display the result
    cv2.imshow('Detected Faces', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image with detected faces if output path is provided
    if output_path:
        cv2.imwrite(output_path, image)
        print(f"Image saved to {output_path}")

def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Ask the user if they want to save the output image
        save_output = messagebox.askyesno("Save Output", "Do you want to save the output image?")
        if save_output:
            output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
            if output_path:
                detect_faces(file_path, output_path)
            else:
                detect_faces(file_path)
        else:
            detect_faces(file_path)

def process_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select a directory
    directory_path = filedialog.askdirectory()
    if directory_path:
        for filename in os.listdir(directory_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(directory_path, filename)
                output_path = os.path.join(directory_path, "output_" + filename)
                detect_faces(image_path, output_path)

def main():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to choose between "Image" and "Directory"
    choice = simpledialog.askstring("Choose Task", "Type 'Image' to process a single image or 'Directory' to process a directory:")

    if choice is not None:
        choice = choice.lower()
        if choice == 'image':
            select_image()
        elif choice == 'directory':
            process_directory()
        else:
            messagebox.showerror("Invalid Choice", "Please type 'Image' or 'Directory'.")

if __name__ == '__main__':
    main()
