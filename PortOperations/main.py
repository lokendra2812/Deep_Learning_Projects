import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D
from tensorflow.keras import Sequential
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from PIL import Image


# Project Details
st.title("Automating Port Operations using Deep Learning")
st.title("Company Name : Marina Pier Inc.")
st.write("## Developed by : Mr. Lokendra Kumar Agrawal")

# Information providing user : why this solution required and what its doing
st.write("""
## The company’s management has set out to build a bias-free/ corruption-free automatic system that reports & avoids faulty situations caused by human error. Examples of human error include miss classifying the correct type of boat. The type of boat that enters the port region is as follows.
    • Buoy
    • Cruise_ship
    • Ferry_boat
    • Freight_boar
    • Gondola
    • Inflatable_boat
    • Kayak
    • Paper_boat
""")


def load_image(image_file):
    img = Image.open(image_file)
    return img

if st.button("Add Image to Classify "):
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])
    if uploadFile is not None:
        img = load_image(uploadFile)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Image Uploaded Successfully")
    else:
        st.write("Make sure your image is in JPG/PNG format.")




