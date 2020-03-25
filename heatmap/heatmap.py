import cv2
import numpy as np


def generate_heatmap(original_image, heat_map_2d_array, kernel_size=11, opacity=0.3, cmap=cv2.COLORMAP_TURBO, save_path=None):

    # get height and width of the image
    height, width = original_image.shape[0], original_image.shape[1]

    # resize heat map to make sure it is equal to the size of image
    heat_map = cv2.GaussianBlur(heat_map_2d_array, (kernel_size, kernel_size), 0)
    heat_map = cv2.resize(heat_map, (width, height))

    # normalize heat map values from 0 to 255
    max_value = np.max(heat_map)
    min_value = np.min(heat_map)
    heat_map = (heat_map - min_value) / (max_value - min_value)
    heat_map = np.array(heat_map * 255, dtype=np.uint8)

    # apply color map to convert heat map into RGB values
    heat_map = cv2.applyColorMap(heat_map, cmap)

    # merge heat map and background image
    outImage = cv2.addWeighted(heat_map, opacity, original_image, 1 - opacity, 0)

    if save_path is not None:
        cv2.imwrite(save_path + 'heatmap.jpg', outImage)

    return cv2.cvtColor(outImage, cv2.COLOR_BGR2RGB)
