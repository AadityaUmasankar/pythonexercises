import  tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("gimg01.jpg")
image = image.resize((224,224))
image = np.array(image)


model = tf.keras.applications.mobilenet_v2.MobileNetV2(include_top = True, weights = 'imagenet')

