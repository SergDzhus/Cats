from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():


window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataaas.com/cat"
img = load_image(url)

if img:
    label.config(image=img) #установка картинки на метку
    label.image = img

window.mainloop()
