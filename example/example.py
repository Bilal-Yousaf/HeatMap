import cv2
import numpy as np
import heatmap

image_path = '../samples/interior-top-view.jpg'
image = cv2.imread(image_path)

x = np.zeros((100, 100))
x[50, 50] = 70
x[25, 25] = 100

output = heatmap.generate_heatmap(image, x, save_path='../samples/')
