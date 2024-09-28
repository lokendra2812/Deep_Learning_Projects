import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D
from tensorflow.keras import Sequential
import numpy as np
import matplotlib.pyplot as plt
import pathlib

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

# Perform the following steps:
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)

data_dir

len(list(data_dir.glob('*/*.jpg')))


