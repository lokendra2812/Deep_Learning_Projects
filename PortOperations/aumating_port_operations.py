# -*- coding: utf-8 -*-
"""Aumating Port Operations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VkC2xLKpD33gBLWeN5vsxK5SAYhQuos
"""

import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D
from tensorflow.keras import Sequential
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data_dir = pathlib.Path('/content/drive/MyDrive/Data_for_Streamlit/boat_type_classification_dataset')
data_dir_path = pathlib.Path(data_dir)
print(f"Dataset directory: {data_dir_path}")

data_dir_path

len(list(data_dir.glob('*/*.jpg')))

(list(data_dir.glob('*/*.jpg')))

sailboats = list(data_dir.glob('sailboat/*'))
sailboats[:5]

import PIL
PIL.Image.open(sailboats[0])

ferry_boats = list(data_dir.glob('ferry_boat/*'))
PIL.Image.open(ferry_boats[0])

kayaks = list(data_dir.glob('kayak/*'))
PIL.Image.open(kayaks[0])

batch_size=32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

train_ds.class_names

class_names = train_ds.class_names
class_names

train_ds

train_ds.take(1) #  32 images

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# AUTOTUNE
# cache() method
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

from tensorflow.keras.layers import Rescaling

normalization_layer = Rescaling(1/256)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixels values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))

"""# Data Augmentation"""

from tensorflow.keras.layers import RandomFlip, RandomRotation, RandomZoom,MaxPooling2D, Flatten,Dropout

model = Sequential()
model.add(RandomFlip("horizontal", input_shape=(img_height, img_width, 3)))
model.add(RandomRotation(0.1))
model.add(RandomZoom(0.1))
model.add(Rescaling(1/255))
model.add(Conv2D(16, 3, padding='same', activation='relu')) # yes padding
model.add(MaxPooling2D())
model.add(Conv2D(32, 3, padding='same', activation='relu')) #  yes padding
model.add(MaxPooling2D())
model.add(Conv2D(64, 3, padding='same', activation='relu')) # yes padding
model.add(MaxPooling2D())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(5, activation='softmax'))

model.summary()

labels_batch

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_ds, validation_data=val_ds, epochs=10)

epochs = 10
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

import PIL
img = PIL.Image.open(sailboats[0])
new_size = (img_width, img_height)  # Set your desired width and height
img_resized = img.resize(new_size)
img_array = tf.keras.utils.img_to_array(img_resized) # convert the PIL format to array
img_array.shape

img_array = tf.expand_dims(img_array, 0) # Create a batch
img_array.shape

predictions = model.predict(img_array)
predictions

np.argmax(predictions)

class_names[np.argmax(predictions)]