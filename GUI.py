import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import os

class ImageProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tugas 1")
        self.root.geometry("400x540")

        # Create buttons

        grayscale_button = tk.Button(self.root, text="Grayscale", command=self.grayscale)
        grayscale_button.pack(pady=10)

        crop_button = tk.Button(self.root, text="Crop", command=self.crop)
        crop_button.pack(pady=10)

        flip_button = tk.Button(self.root, text="Flip", command=self.flip)
        flip_button.pack(pady=10)

        resize_button_30 = tk.Button(self.root, text="Resize", command=lambda: self.resize((30, 30),(90, 90),(120, 120)))
        resize_button_30.pack(pady=10)

        rotate_button = tk.Button(self.root, text="Rotation", command=self.rotation)
        rotate_button.pack(pady=10)

        translate_button = tk.Button(self.root, text="Translate", command=self.translation)
        translate_button.pack(pady=10)

        affine_transform_button = tk.Button(self.root, text="Affine Transform", command=self.affine)
        affine_transform_button.pack(pady=10)

        perspective_transform_button = tk.Button(self.root, text="Perspective Transform", command=self.perspective)
        perspective_transform_button.pack(pady=10)

        padding_button = tk.Button(self.root, text="Padding", command=self.padding)
        padding_button.pack(pady=10)

        split_color_channel_button = tk.Button(self.root, text="Split Color Channel", command=self.split_color_channel)
        split_color_channel_button.pack(pady=10)

        to_rgb_button = tk.Button(self.root, text="To RGB", command=self.toRGB)
        to_rgb_button.pack(pady=10)

        self.image_path = None

        self.image_path = None

    def grayscale(self):
        # Call grayscale.py program using os.system()
        if self.image_path is not None:
            os.system("python grayscale.py " + self.image_path)

    def crop(self):
        # Call cropping.py program using os.system()
        if self.image_path is not None:
            os.system("python cropping.py " + self.image_path)

    def flip(self):
        # Call flipping.py program using os.system()
        if self.image_path is not None:
            os.system("python flipping.py " + self.image_path)
    
    def affine(self):
        # Call grayscale.py program using os.system()
        if self.image_path is not None:
            os.system("python affine_transform.py " + self.image_path)

    def padding(self):
        # Call cropping.py program using os.system()
        if self.image_path is not None:
            os.system("python padding.py " + self.image_path)

    def perspective(self):
        # Call flipping.py program using os.system()
        if self.image_path is not None:
            os.system("python perspective_transform.py " + self.image_path)

    def resize(self):
        # Call grayscale.py program using os.system()
        if self.image_path is not None:
            os.system("python resize.py " + self.image_path)

    def rotation(self):
        # Call cropping.py program using os.system()
        if self.image_path is not None:
            os.system("python rotation.py " + self.image_path)

    def split_color_channel(self):
        # Call flipping.py program using os.system()
        if self.image_path is not None:
            os.system("python split_color_channel.py " + self.image_path)

    def toRGB(self):
        # Call cropping.py program using os.system()
        if self.image_path is not None:
            os.system("python toRGB.py " + self.image_path)

    def translation(self):
        # Call flipping.py program using os.system()
        if self.image_path is not None:
            os.system("python translation.py " + self.image_path)

# Create Tkinter window
root = tk.Tk()

# Create ImageProcessorGUI object
app = ImageProcessorGUI(root)

# Run the main event loop
root.mainloop()